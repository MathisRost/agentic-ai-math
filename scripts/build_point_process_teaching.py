"""Editable Poisson samples and a pair-counting illustration for the talk."""
from pathlib import Path
import math
import random
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

    def text(self, value, x, y, width, height, size=29, color=INK, bold=False):
        self.vertex(value, x, y, width, height,
                    "text;html=0;whiteSpace=wrap;align=center;verticalAlign=middle;"
                    f"fontFamily=Kalam;fontSize={size};fontColor={color};"
                    f"fontStyle={int(bold)};strokeColor=none;fillColor=none;spacing=0;")

    def box(self, x, y, width, height, color=TEAL):
        self.vertex("", x, y, width, height,
                    "rounded=1;arcSize=5;sketch=1;comic=0;jiggle=1.2;"
                    f"strokeWidth=2;strokeColor={color};fillColor=#FFFFFF;")

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


# Simulate Poisson counts, then iid uniform locations in equal unit-area windows.
# No rejection or minimum spacing: accidental close pairs are allowed.
rng = random.Random(20261020)
poisson = Diagram("poisson_teaching", 390, 720)
for index, top in enumerate((0, 350), start=1):
    product, count = 1.0, -1
    while product > math.exp(-20):
        product *= rng.random()
        count += 1
    poisson.text(f"Realisation {index}", 30, top, 330, 40, 31, TEAL, True)
    poisson.box(65, top + 50, 260, 260)
    for _ in range(count):
        poisson.dot(65 + 260*rng.random(), top + 50 + 260*rng.random(), radius=4)
    poisson.text(f"{count} points", 30, top + 315, 330, 32, 28, ORANGE)
poisson.save()

# These are illustrative counts, not a simulated Poisson sample.
pairs = Diagram("product_density_pairs", 1030, 300)
pairs.box(25, 50, 300, 185)
pairs.box(705, 50, 300, 185, ORANGE)
pairs.text("B1", 25, 0, 300, 42, 34, TEAL, True)
pairs.text("B2", 705, 0, 300, 42, 34, ORANGE, True)
left = [(100, 90), (240, 145), (115, 205)]
right = [(785, 100), (925, 190)]
for a in left:
    for b in right:
        pairs.line(a, b)
for a in left:
    pairs.dot(*a, radius=8)
for b in right:
    pairs.dot(*b, color=ORANGE, radius=8)
pairs.text("3 points", 25, 250, 300, 40, 31, TEAL)
pairs.text("3 x 2 = 6 pairs", 350, 250, 330, 40, 34, INK, True)
pairs.text("2 points", 705, 250, 300, 40, 31, ORANGE)
pairs.save()
