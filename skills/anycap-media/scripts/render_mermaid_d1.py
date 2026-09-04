#!/usr/bin/env python3
"""Render Mermaid through the local CLI with the bundled D1 technical theme."""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = SKILL_DIR / "assets" / "mermaid-d1-config.json"
COMPACT_SEQUENCE_CONFIG = SKILL_DIR / "assets" / "mermaid-d1-compact-sequence.json"
DEFAULT_CSS = SKILL_DIR / "assets" / "mermaid-d1.css"
VERSION_GATES = {
    "ishikawa": (11, 12, 3),
    "eventmodel": (11, 15, 0),
    "cynefin": (11, 16, 0),
}


def canvas_dimensions(raw: str) -> tuple[int, int]:
    match = re.fullmatch(r"(\d+)[xX](\d+)", raw.strip())
    if not match:
        raise argparse.ArgumentTypeError(
            "canvas must be WIDTHxHEIGHT, for example 3200x1800"
        )
    width, height = (int(part) for part in match.groups())
    if width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError("canvas dimensions must be positive")
    return width, height


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render .mmd source with the bundled D1 Mermaid theme."
    )
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--width", type=int, default=1600, help="Browser viewport width")
    parser.add_argument("--height", type=int, default=900, help="Browser viewport height")
    parser.add_argument(
        "--scale",
        type=float,
        default=None,
        help="Raster scale; defaults to 2 for PNG and 1 otherwise",
    )
    parser.add_argument("--background", default="white")
    parser.add_argument(
        "--canvas",
        type=canvas_dimensions,
        help="Compose PNG onto an exact WIDTHxHEIGHT canvas after Mermaid rendering.",
    )
    parser.add_argument(
        "--canvas-margin",
        type=int,
        default=96,
        help="Outer margin in pixels for --canvas output.",
    )
    parser.add_argument(
        "--no-upscale",
        action="store_true",
        help="Do not upscale rendered content when composing a fixed canvas.",
    )
    parser.add_argument(
        "--force", action="store_true", help="Replace an existing output file."
    )
    parser.add_argument("--mmdc", default="", help="Optional explicit mmdc path")
    parser.add_argument(
        "--config",
        type=Path,
        help="Optional config override; fixed-canvas sequences use the compact D1 profile by default.",
    )
    parser.add_argument("--css", type=Path, default=DEFAULT_CSS)
    return parser.parse_args()


def version_tuple(raw: str) -> tuple[int, int, int]:
    match = re.search(r"(\d+)\.(\d+)\.(\d+)", raw)
    if not match:
        raise ValueError(f"cannot parse mmdc version: {raw!r}")
    return tuple(int(part) for part in match.groups())


def first_directive(source: str) -> str:
    lines = source.splitlines()
    index = 0
    if lines and lines[0].strip() == "---":
        index = 1
        while index < len(lines) and lines[index].strip() != "---":
            index += 1
        index += 1
    for line in lines[index:]:
        stripped = line.strip()
        if stripped and not stripped.startswith("%%"):
            return re.split(r"\s+", stripped, maxsplit=1)[0].lower()
    return ""


def enforce_version_gate(directive: str, current: tuple[int, int, int]) -> None:
    required = VERSION_GATES.get(directive)
    if required and current < required:
        need = ".".join(map(str, required))
        have = ".".join(map(str, current))
        raise SystemExit(
            f"{directive} requires Mermaid CLI {need}+; local version is {have}. "
            "Use a flowchart causal DAG or deterministic HTML/SVG fallback."
        )


def output_dimensions(path: Path) -> tuple[int | None, int | None]:
    if path.suffix.lower() == ".png":
        data = path.read_bytes()[:24]
        if data[:8] == b"\x89PNG\r\n\x1a\n" and len(data) >= 24:
            return struct.unpack(">II", data[16:24])
    if path.suffix.lower() == ".svg":
        try:
            root = ET.parse(path).getroot()
        except (ET.ParseError, OSError):
            return None, None
        if root.tag.rsplit("}", 1)[-1].lower() != "svg":
            return None, None
        view_box = root.attrib.get("viewBox", "").replace(",", " ").split()
        if len(view_box) == 4:
            try:
                return round(float(view_box[2])), round(float(view_box[3]))
            except ValueError:
                return None, None
        values = []
        for name in ("width", "height"):
            match = re.match(r"\s*([0-9]+(?:\.[0-9]+)?)", root.attrib.get(name, ""))
            if not match:
                return None, None
            values.append(round(float(match.group(1))))
        return values[0], values[1]
    return None, None


def validate_output_format(path: Path, requested_suffix: str) -> None:
    prefix = path.read_bytes()[:8]
    width, height = output_dimensions(path)
    if requested_suffix == ".png":
        valid = prefix == b"\x89PNG\r\n\x1a\n" and bool(width and height)
    elif requested_suffix == ".svg":
        valid = bool(width and height)
    elif requested_suffix == ".pdf":
        valid = prefix.startswith(b"%PDF-")
    else:
        valid = False
    if not valid:
        raise ValueError(
            f"renderer output does not match requested format {requested_suffix}: {path}"
        )


def promote_output(candidate: Path, output: Path, *, force: bool) -> None:
    with candidate.open("rb") as handle:
        os.fsync(handle.fileno())
    if force:
        os.replace(candidate, output)
        return
    try:
        os.link(candidate, output)
    except FileExistsError as exc:
        raise ValueError(
            f"output already exists; choose a versioned path or use --force: {output}"
        ) from exc


def main() -> int:
    args = parse_args()
    if not args.input.is_file():
        raise SystemExit(f"input not found: {args.input}")
    if args.output.suffix.lower() not in {".png", ".svg", ".pdf"}:
        raise SystemExit("output extension must be .png, .svg, or .pdf")
    if args.canvas and args.output.suffix.lower() != ".png":
        raise SystemExit("--canvas requires a .png output")
    if args.output.exists() and not args.force:
        raise SystemExit(
            f"output already exists; choose a versioned path or use --force: {args.output}"
        )
    source_text = args.input.read_text(encoding="utf-8")
    directive = first_directive(source_text)
    if args.config:
        selected_config = args.config
        config_profile = "custom"
    elif args.canvas and directive == "sequencediagram":
        selected_config = COMPACT_SEQUENCE_CONFIG
        config_profile = "sequence-compact"
    else:
        selected_config = DEFAULT_CONFIG
        config_profile = "default"
    for required_file in (selected_config, args.css):
        if not required_file.is_file():
            raise SystemExit(f"render asset not found: {required_file}")

    executable = args.mmdc or shutil.which("mmdc")
    if not executable:
        raise SystemExit("mmdc is unavailable; do not silently install it")
    try:
        version_result = subprocess.run(
            [executable, "--version"], text=True, capture_output=True
        )
    except OSError as exc:
        raise SystemExit(f"cannot execute mmdc: {executable}: {exc}") from exc
    if version_result.returncode != 0:
        detail = (version_result.stderr or version_result.stdout).strip()
        raise SystemExit(
            f"mmdc version probe failed with exit {version_result.returncode}: "
            f"{detail or executable}"
        )
    version_raw = version_result.stdout.strip()
    try:
        current_version = version_tuple(version_raw)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    enforce_version_gate(directive, current_version)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    scale = (
        args.scale
        if args.scale is not None
        else (2 if args.output.suffix.lower() == ".png" else 1)
    )
    if args.width <= 0 or args.height <= 0:
        raise SystemExit("viewport width and height must be positive")
    if not math.isfinite(scale) or scale <= 0:
        raise SystemExit("scale must be a finite positive number")

    with tempfile.TemporaryDirectory(
        prefix=f".{args.output.name}.mermaid-", dir=args.output.parent
    ) as temp_dir:
        requested_suffix = args.output.suffix.lower()
        render_suffix = ".png" if args.canvas else requested_suffix
        render_output = Path(temp_dir) / f"content{render_suffix}"
        command = [
            executable,
            "--input",
            str(args.input),
            "--output",
            str(render_output),
            "--width",
            str(args.width),
            "--height",
            str(args.height),
            "--scale",
            str(scale),
            "--backgroundColor",
            args.background,
            "--configFile",
            str(selected_config),
            "--cssFile",
            str(args.css),
            "--quiet",
        ]
        result = subprocess.run(command, text=True, capture_output=True)
        if result.returncode != 0:
            sys.stderr.write(result.stderr or result.stdout)
            return result.returncode
        if not render_output.is_file() or render_output.stat().st_size == 0:
            raise SystemExit(f"renderer produced no output: {render_output}")

        try:
            validate_output_format(render_output, render_suffix)
        except (OSError, ValueError) as exc:
            raise SystemExit(str(exc)) from exc

        content_width, content_height = output_dimensions(render_output)
        canvas_result = None
        candidate_output = render_output
        if args.canvas:
            try:
                from compose_fixed_canvas import compose_image

                candidate_output = Path(temp_dir) / "canvas.png"
                canvas_result = compose_image(
                    render_output,
                    candidate_output,
                    width=args.canvas[0],
                    height=args.canvas[1],
                    margin=args.canvas_margin,
                    background=args.background,
                    allow_upscale=not args.no_upscale,
                    force=False,
                )
            except (OSError, ValueError) as exc:
                raise SystemExit(str(exc)) from exc

        try:
            validate_output_format(candidate_output, requested_suffix)
            promote_output(candidate_output, args.output, force=args.force)
        except (OSError, ValueError) as exc:
            raise SystemExit(str(exc)) from exc

    width, height = output_dimensions(args.output)
    content_fill = None
    layout_warning = None
    if args.canvas and canvas_result:
        content_box = canvas_result["content_box"]
        available_width = args.canvas[0] - 2 * args.canvas_margin
        available_height = args.canvas[1] - 2 * args.canvas_margin
        content_fill = [
            round(content_box[2] / available_width, 3),
            round(content_box[3] / available_height, 3),
        ]
        if directive == "sequencediagram" and content_fill[0] < 0.6:
            layout_warning = (
                "Sequence remains too tall for the fixed canvas; reduce non-essential "
                "messages, split the visual, or use a full-width/appendix surface."
            )
    print(
        json.dumps(
            {
                "ok": True,
                "input": str(args.input.resolve()),
                "output": str(args.output.resolve()),
                "diagram": directive,
                "mmdc_version": version_raw,
                "viewport": [args.width, args.height],
                "scale": scale,
                "config_profile": config_profile,
                "content_dimensions": [content_width, content_height],
                "output_dimensions": [width, height],
                "canvas": list(args.canvas) if args.canvas else None,
                "content_box": canvas_result["content_box"] if canvas_result else None,
                "content_fill": content_fill,
                "cropped": False if args.canvas else None,
                "layout_warning": layout_warning,
                "note": (
                    "Exact fixed canvas composed with contain fit and no cropping."
                    if args.canvas
                    else "Content-shaped output; viewport is not a fixed delivery canvas."
                ),
            },
            ensure_ascii=False,
            allow_nan=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
