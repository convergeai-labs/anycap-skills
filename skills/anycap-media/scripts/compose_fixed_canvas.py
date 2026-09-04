#!/usr/bin/env python3
"""Fit a raster visual onto an exact delivery canvas without cropping."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path

try:
    from PIL import Image, ImageColor, ImageOps
except ImportError as exc:
    raise SystemExit(
        "Pillow is required for fixed-canvas composition; do not install it silently"
    ) from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Contain a raster image on an exact PNG canvas."
    )
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--width", type=int, default=3200)
    parser.add_argument("--height", type=int, default=1800)
    parser.add_argument("--margin", type=int, default=96)
    parser.add_argument("--background", default="#FFFFFF")
    parser.add_argument(
        "--no-upscale",
        action="store_true",
        help="Keep source pixels at 1:1 when they already fit.",
    )
    parser.add_argument(
        "--force", action="store_true", help="Replace an existing output file."
    )
    return parser.parse_args()


def compose_image(
    input_path: Path,
    output_path: Path,
    *,
    width: int,
    height: int,
    margin: int,
    background: str,
    allow_upscale: bool,
    force: bool,
) -> dict[str, object]:
    if not input_path.is_file():
        raise ValueError(f"input not found: {input_path}")
    if output_path.suffix.lower() != ".png":
        raise ValueError("fixed-canvas output must use the .png extension")
    if output_path.exists() and not force:
        raise ValueError(
            "output already exists; choose a versioned path or use "
            f"--force: {output_path}"
        )
    if width <= 0 or height <= 0:
        raise ValueError("canvas width and height must be positive")
    if margin < 0 or margin * 2 >= min(width, height):
        raise ValueError("margin must be non-negative and leave positive content space")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        fill = ImageColor.getrgb(background)[:3]
    except ValueError as exc:
        raise ValueError(f"invalid background color: {background}") from exc

    with Image.open(input_path) as opened:
        opened.load()
        source = ImageOps.exif_transpose(opened).convert("RGBA")
        source_width, source_height = source.size
        available_width = width - 2 * margin
        available_height = height - 2 * margin
        scale = min(
            available_width / source_width,
            available_height / source_height,
        )
        if not allow_upscale:
            scale = min(scale, 1.0)
        fitted_width = max(1, round(source_width * scale))
        fitted_height = max(1, round(source_height * scale))
        if (fitted_width, fitted_height) != source.size:
            source = source.resize(
                (fitted_width, fitted_height), Image.Resampling.LANCZOS
            )

        canvas = Image.new("RGBA", (width, height), (*fill, 255))
        x = (width - fitted_width) // 2
        y = (height - fitted_height) // 2
        canvas.alpha_composite(source, (x, y))

        descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{output_path.name}.",
            suffix=".tmp",
            dir=output_path.parent,
        )
        os.close(descriptor)
        temporary_path = Path(temporary_name)
        try:
            canvas.convert("RGB").save(temporary_path, format="PNG", optimize=True)
            os.chmod(temporary_path, 0o644)
            with temporary_path.open("rb") as handle:
                os.fsync(handle.fileno())
            if force:
                os.replace(temporary_path, output_path)
            else:
                try:
                    os.link(temporary_path, output_path)
                except FileExistsError as exc:
                    raise ValueError(
                        "output already exists; choose a versioned path or use "
                        f"--force: {output_path}"
                    ) from exc
        finally:
            temporary_path.unlink(missing_ok=True)

    return {
        "ok": True,
        "input": str(input_path.resolve()),
        "output": str(output_path.resolve()),
        "source_dimensions": [source_width, source_height],
        "output_dimensions": [width, height],
        "content_box": [x, y, fitted_width, fitted_height],
        "scale": round(scale, 6),
        "margin": margin,
        "background": background,
        "cropped": False,
    }


def main() -> int:
    args = parse_args()
    try:
        result = compose_image(
            args.input,
            args.output,
            width=args.width,
            height=args.height,
            margin=args.margin,
            background=args.background,
            allow_upscale=not args.no_upscale,
            force=args.force,
        )
    except (OSError, ValueError) as exc:
        raise SystemExit(str(exc)) from exc
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
