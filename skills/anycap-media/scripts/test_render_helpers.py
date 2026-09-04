#!/usr/bin/env python3
"""Regression tests for deterministic Mermaid and fixed-canvas delivery."""

from __future__ import annotations

import json
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import unittest

from PIL import Image


SCRIPT_DIR = Path(__file__).resolve().parent
COMPOSE = SCRIPT_DIR / "compose_fixed_canvas.py"
RENDER = SCRIPT_DIR / "render_mermaid_d1.py"
sys.path.insert(0, str(SCRIPT_DIR))

from compose_fixed_canvas import compose_image  # noqa: E402


class FixedCanvasTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="visual-helper-test-")
        self.root = Path(self.temp.name)
        self.source = self.root / "source.png"
        Image.new("RGB", (200, 100), "#336699").save(self.source)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_exact_contain_dimensions_without_crop(self) -> None:
        output = self.root / "canvas.png"
        result = compose_image(
            self.source,
            output,
            width=320,
            height=180,
            margin=20,
            background="#FFFFFF",
            allow_upscale=True,
            force=False,
        )
        self.assertEqual([320, 180], result["output_dimensions"])
        self.assertEqual([20, 20, 280, 140], result["content_box"])
        self.assertFalse(result["cropped"])
        with Image.open(output) as image:
            self.assertEqual((320, 180), image.size)

    def test_exif_orientation_is_normalized_before_fit(self) -> None:
        source = self.root / "rotated.jpg"
        exif = Image.Exif()
        exif[274] = 6
        Image.new("RGB", (20, 10), "#884422").save(source, exif=exif)
        result = compose_image(
            source,
            self.root / "rotated.png",
            width=100,
            height=100,
            margin=10,
            background="#FFFFFF",
            allow_upscale=False,
            force=False,
        )
        self.assertEqual([10, 20], result["source_dimensions"])
        self.assertEqual([45, 40, 10, 20], result["content_box"])

    def test_invalid_extension_and_force_replace(self) -> None:
        with self.assertRaisesRegex(ValueError, "must use the .png extension"):
            compose_image(
                self.source,
                self.root / "canvas.jpg",
                width=100,
                height=80,
                margin=10,
                background="#FFFFFF",
                allow_upscale=True,
                force=False,
            )
        output = self.root / "existing.png"
        output.write_bytes(b"old")
        compose_image(
            self.source,
            output,
            width=120,
            height=80,
            margin=8,
            background="#FFFFFF",
            allow_upscale=True,
            force=True,
        )
        with Image.open(output) as image:
            self.assertEqual((120, 80), image.size)

    def test_two_no_force_writers_yield_exactly_one_success(self) -> None:
        output = self.root / "race.png"
        command = [
            sys.executable,
            str(COMPOSE),
            "--input",
            str(self.source),
            "--output",
            str(output),
            "--width",
            "160",
            "--height",
            "90",
            "--margin",
            "10",
        ]
        writers = [
            subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for _ in range(2)
        ]
        results = [writer.communicate(timeout=20) + (writer.returncode,) for writer in writers]
        self.assertEqual(1, sum(returncode == 0 for _, _, returncode in results), results)
        self.assertEqual(1, sum(returncode != 0 for _, _, returncode in results), results)
        with Image.open(output) as image:
            self.assertEqual((160, 90), image.size)


class MermaidWrapperTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="mermaid-wrapper-test-")
        self.root = Path(self.temp.name)
        self.fake_mmdc = self.root / "fake-mmdc"
        self.fake_mmdc.write_text(
            """#!/usr/bin/env python3
from pathlib import Path
import sys
from PIL import Image

if "--version" in sys.argv:
    print("11.16.0")
    raise SystemExit(0)
args = sys.argv[1:]
source = Path(args[args.index("--input") + 1]).read_text(encoding="utf-8")
output = Path(args[args.index("--output") + 1])
output.parent.mkdir(parents=True, exist_ok=True)
if "FAIL_RENDER" in source:
    output.write_bytes(b"partial")
    print("simulated renderer failure", file=sys.stderr)
    raise SystemExit(17)
if "INVALID_BYTES" in source:
    output.write_bytes(b"not a png")
    raise SystemExit(0)
Image.new("RGB", (80, 40), "#FFFFFF").save(output, format="PNG")
""",
            encoding="utf-8",
        )
        self.fake_mmdc.chmod(self.fake_mmdc.stat().st_mode | stat.S_IXUSR)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_render(self, source_text: str, output: Path, *extra: str) -> subprocess.CompletedProcess[str]:
        source = self.root / f"{output.stem}.mmd"
        source.write_text(source_text, encoding="utf-8")
        return subprocess.run(
            [
                sys.executable,
                str(RENDER),
                "--input",
                str(source),
                "--output",
                str(output),
                "--mmdc",
                str(self.fake_mmdc),
                *extra,
            ],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_valid_render_and_exact_canvas(self) -> None:
        output = self.root / "rendered.png"
        result = self.run_render(
            "flowchart LR\nA --> B\n",
            output,
            "--canvas",
            "160x90",
            "--canvas-margin",
            "10",
        )
        self.assertEqual(0, result.returncode, result.stderr)
        receipt = json.loads(result.stdout)
        self.assertEqual([160, 90], receipt["output_dimensions"])
        self.assertFalse(receipt["cropped"])
        with Image.open(output) as image:
            self.assertEqual((160, 90), image.size)

    def test_invalid_renderer_bytes_are_not_promoted(self) -> None:
        output = self.root / "invalid.png"
        result = self.run_render("flowchart LR\nINVALID_BYTES\n", output)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("does not match requested format", result.stderr)
        self.assertFalse(output.exists())

    def test_renderer_failure_preserves_existing_force_target(self) -> None:
        output = self.root / "preserved.png"
        original = b"known-good-existing-output"
        output.write_bytes(original)
        result = self.run_render("flowchart LR\nFAIL_RENDER\n", output, "--force")
        self.assertEqual(17, result.returncode)
        self.assertEqual(original, output.read_bytes())


if __name__ == "__main__":
    unittest.main(verbosity=2)
