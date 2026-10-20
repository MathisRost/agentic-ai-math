"""Editable Poisson samples and a pair-counting illustration for the talk."""
from pathlib import Path
import math
import random
import json
import xml.etree.ElementTree as E

ASSETS = Path(__file__).resolve().parents[1] / "assets"
TEAL, ORANGE, INK = "#21736F", "#B16B24", "#252A2D"


class Diagram:
    def __init__(self, name, width, height):
        self.name = name
        self.doc = E.Element("mxfile", host="app.diagrams.net")
        diagram = E.SubElement(self.doc, "diagram", name=name, id=name)
        model = E.SubElement(
            diagram, "mxGraphModel", dx=str(width), dy=str(height), grid="0",
            page="0", pageWidth=str(width), pageHeight=str(height),
            background="#FFFFFF",
            extFonts="Kalam^https://fonts.googleapis.com/css?family=Kalam:400,700",
        )
        self.root = E.SubElement(model, "root")
        E.SubElement(self.root, "mxCell", id="0")
        E.SubElement(self.root, "mxCell", id="1", parent="0")
        self.serial = 1

    def vertex(self, value, x, y, width, height, style):
        self.serial += 1
        cell = E.SubElement(
            self.root, "mxCell", id=str(self.serial), value=value,
            style=style, vertex="1", parent="1",
        )
        E.SubElement(cell, "mxGeometry", x=str(x), y=str(y),
                     width=str(width), height=str(height), **{"as": "geometry"})

    def text(self, value, x, y, width, height, size=29, color=INK, bold=False, html=False):
        self.vertex(value, x, y, width, height,
                    f"text;html={int(html)};whiteSpace=wrap;align=center;verticalAlign=middle;"
                    f"fontFamily=Kalam;fontSize={size};fontColor={color};"
                    f"fontStyle={int(bold)};strokeColor=none;fillColor=none;spacing=0;")

    def box(self, x, y, width, height, color=TEAL, fill="#FFFFFF", hatch=False):
        self.vertex("", x, y, width, height,
                    "rounded=1;arcSize=5;sketch=1;comic=0;jiggle=1.2;"
                    f"strokeWidth=2;strokeColor={color};fillColor={fill};"
                    + ("fillStyle=hachure;hachureGap=7;fillWeight=0.8;" if hatch else ""))

    def dot(self, x, y, color=TEAL, radius=5):
        self.vertex("", x-radius, y-radius, 2*radius, 2*radius,
                    f"ellipse;fillColor={color};strokeColor={color};strokeWidth=1;")

    def line(self, a, b):
        self.serial += 1
        cell = E.SubElement(
            self.root, "mxCell", id=str(self.serial), edge="1", parent="1",
            style="edgeStyle=none;endArrow=none;strokeColor=#B8C8C5;"
                  "strokeWidth=2;dashed=1;dashPattern=4 4;",
        )
        geometry = E.SubElement(cell, "mxGeometry", relative="1", **{"as": "geometry"})
        for point, role in [(a, "sourcePoint"), (b, "targetPoint")]:
            E.SubElement(geometry, "mxPoint", x=str(point[0]), y=str(point[1]),
                         **{"as": role})

    def save(self):
        E.indent(self.doc)
        E.ElementTree(self.doc).write(
            ASSETS / f"{self.name}.drawio", encoding="utf-8", xml_declaration=True)


def poisson_count(rng, mean):
    product, count = 1.0, -1
    while product > math.exp(-mean):
        product *= rng.random()
        count += 1
    return count


def poisson_rectangle(rng, intensity, bounds):
    x0, x1, y0, y1 = bounds
    count = poisson_count(rng, intensity * (x1-x0) * (y1-y0))
    return [(rng.uniform(x0, x1), rng.uniform(y0, y1)) for _ in range(count)]


def contains(bounds, point):
    x0, x1, y0, y1 = bounds
    x, y = point
    return x0 <= x < x1 and y0 <= y < y1


def main():
    # Retain the two original independent Poisson realisations.
    rng = random.Random(20261020)
    samples = [poisson_rectangle(rng, 20, (0, 1, 0, 1)) for _ in range(2)]
    d = Diagram("poisson_teaching", 620, 680)
    for i, (left, points) in enumerate(zip((15, 335), samples), start=1):
        d.text(f"Realisation {i}", left, 0, 270, 46, 36, TEAL, True)
        d.box(left+10, 57, 250, 250)
        for x, y in points:
            d.dot(left+10+250*x, 57+250*y, radius=4.5)
        d.text(f"{len(points)} points", left, 315, 270, 40, 33, ORANGE)
    bounds = (0, 1.6, 0, 0.65)
    b1, b2 = (0.10, 0.68, 0.10, 0.55), (0.92, 1.50, 0.10, 0.55)
    points = poisson_rectangle(random.Random(20261025), 20, bounds)
    left, top, scale = 20, 390, 360
    d.box(left, top, 1.6*scale, 0.65*scale)
    for box, color, fill in [(b1, TEAL, "#D2E6E2"), (b2, ORANGE, "#F1E3D2")]:
        x0, x1, y0, y1 = box
        d.box(left+x0*scale, top+y0*scale, (x1-x0)*scale,
              (y1-y0)*scale, color, fill, True)
    for x, y in points:
        color = TEAL if contains(b1, (x, y)) else ORANGE if contains(b2, (x, y)) else "#626A70"
        d.dot(left+x*scale, top+y*scale, color=color, radius=5)
    counts = [sum(contains(b, p) for p in points) for b in (b1, b2)]
    for i, (x, color, count) in enumerate(zip((15, 335), (TEAL, ORANGE), counts), start=1):
        d.text(f"X(B<sub>{i}</sub>) = {count}", x, 632, 270, 42,
               35, color, True, html=True)
    d.save()
    (ASSETS / "poisson_teaching_samples.json").write_text(json.dumps({
        "intensity": 20, "top_seed": 20261020,
        "top_window": [0, 1, 0, 1], "top_samples": samples,
        "counting_seed": 20261025, "counting_window": bounds,
        "counting_points": points, "subwindows": [b1, b2], "counts": counts,
        "method": "Poisson count, then independent uniform locations; no conditioning on the count",
    }, indent=2)+"\n")
    print(f"Poisson examples: {[len(p) for p in samples]}; subwindow counts: {counts}")


if __name__ == "__main__":
    main()
