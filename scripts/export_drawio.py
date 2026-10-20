#!/usr/bin/env python3
"""Export native draw.io XML locally with installed fonts, without browser UI."""
import argparse
import base64
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET


def renderer_path():
    candidates = [os.environ.get("DRAWIO_BIN"), shutil.which("drawio"),
                  str(Path.home() / "Applications/draw.io.app/Contents/MacOS/draw.io"),
                  "/Applications/draw.io.app/Contents/MacOS/draw.io"]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return candidate
    raise SystemExit("Install draw.io Desktop or set DRAWIO_BIN to its executable.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--formats", nargs="+", choices=["pdf", "svg", "png"], default=["pdf", "svg"])
    parser.add_argument("--border", type=int, default=12)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    source = args.source.resolve()
    tree = ET.parse(source)
    models = list(tree.getroot().iter("mxGraphModel"))
    if not models:
        raise SystemExit("Use uncompressed draw.io XML (mxGraphModel) for this exporter.")
    # Fonts are installed locally: omit web font CSS requests from the export copy.
    for model in models:
        model.attrib.pop("extFonts", None)
        model.set("background", "#FFFFFF")
    for cell in tree.getroot().iter("mxCell"):
        if "style" in cell.attrib:
            cell.set("style", ";".join(part for part in cell.get("style", "").split(";")
                                      if not part.startswith("fontSource=")))
    destination = (args.output_dir or source.parent).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    renderer = renderer_path()
    with tempfile.TemporaryDirectory(prefix="mathis-drawio-") as temporary:
        local = Path(temporary) / source.name
        tree.write(local, encoding="utf-8", xml_declaration=True)
        for fmt in args.formats:
            staged = Path(temporary) / f"{source.stem}.{fmt}"
            command = [renderer, "--disable-update", "--export", "--theme", "light", "--timeout", "60",
                       "--format", fmt, "--border", str(args.border),
                       "--embed-diagram", "--output", str(staged)]
            if fmt == "pdf":
                command.append("--crop")
            if fmt == "png":
                command.extend(["--scale", "2"])
            subprocess.run(command + [str(local)], check=True, timeout=90)
            if not staged.is_file() or staged.stat().st_size == 0:
                raise SystemExit(f"draw.io did not produce {fmt} output.")
            if fmt == "svg":
                # Keep the vector export portable without any font service request.
                base = Path(__file__).resolve().parent.parent
                font_roots = [base / "style/sketch/fonts", base / "assets/fonts"]
                fonts = next((p for p in font_roots if (p / "Kalam-Regular.ttf").is_file()), None)
                if fonts:
                    css = []
                    for weight, name in [(400, "Regular"), (700, "Bold")]:
                        encoded = base64.b64encode((fonts / f"Kalam-{name}.ttf").read_bytes()).decode("ascii")
                        css.append("@font-face{font-family:'Kalam';font-style:normal;"
                                   f"font-weight:{weight};src:url(data:font/ttf;base64,{encoded}) format('truetype');}}")
                    svg = staged.read_text()
                    opening = svg.index(">", svg.index("<svg")) + 1
                    svg = svg[:opening] + '<style type="text/css">' + "".join(css) + "</style>" + svg[opening:]
                    staged.write_text(svg)
            output = destination / staged.name
            shutil.copy2(staged, output)
            print(output)


if __name__ == "__main__":
    main()
