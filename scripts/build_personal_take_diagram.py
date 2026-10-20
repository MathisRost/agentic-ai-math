"""Editable research paths for the final personal-take slide."""
from pathlib import Path
import xml.etree.ElementTree as E

OUT = Path(__file__).resolve().parents[1] / "assets" / "personal_research_paths.drawio"
TEAL, ORANGE, INK = "#21736F", "#B16B24", "#252A2D"
doc = E.Element("mxfile", host="app.diagrams.net")
diagram = E.SubElement(doc, "diagram", name="Research paths", id="research-paths")
model = E.SubElement(
    diagram, "mxGraphModel", grid="0", page="0", pageWidth="1180",
    pageHeight="320", background="#FFFFFF",
    extFonts="Kalam^https://fonts.googleapis.com/css?family=Kalam:400,700",
)
root = E.SubElement(model, "root")
E.SubElement(root, "mxCell", id="0")
E.SubElement(root, "mxCell", id="1", parent="0")
serial = 1


def vertex(value, x, y, w, h, style):
    global serial
    serial += 1
    c = E.SubElement(root, "mxCell", id=str(serial), parent="1",
                     vertex="1", value=value, style=style)
    E.SubElement(c, "mxGeometry", x=str(x), y=str(y),
                 width=str(w), height=str(h), **{"as": "geometry"})


def text(value, x, y, w, h, size=27, color=INK):
    vertex(value, x, y, w, h,
           f"text;html=0;whiteSpace=wrap;align=center;verticalAlign=middle;"
           f"fontFamily=Kalam;fontSize={size};fontColor={color};"
           "strokeColor=none;fillColor=none;")


def arrow(points, color=TEAL, dashed=False):
    global serial
    serial += 1
    c = E.SubElement(
        root, "mxCell", id=str(serial), parent="1", edge="1",
        style=f"edgeStyle=none;curved=1;rounded=1;sketch=1;comic=0;jiggle=0.6;"
              f"strokeWidth=2.6;strokeColor={color};dashed={int(dashed)};"
              "endArrow=open;endFill=0;endSize=13;",
    )
    g = E.SubElement(c, "mxGeometry", relative="1", **{"as": "geometry"})
    for p, role in [(points[0], "sourcePoint"), (points[-1], "targetPoint")]:
        E.SubElement(g, "mxPoint", x=str(p[0]), y=str(p[1]), **{"as": role})
    a = E.SubElement(g, "Array", **{"as": "points"})
    for p in points[1:-1]:
        E.SubElement(a, "mxPoint", x=str(p[0]), y=str(p[1]))


vertex("", 0, 0, 1180, 320, "fillColor=none;strokeColor=none;")
# Alternative routes to the proof; the loop revisits the original question.
arrow([(120, 110), (220, 55), (370, 55), (470, 110)])
arrow([(122, 130), (255, 115), (365, 140), (468, 130)])
arrow([(120, 148), (225, 212), (370, 212), (470, 148)])
arrow([(500, 213), (500, 267), (90, 267), (90, 213)], ORANGE)
# Solving a problem also reveals new directions.
arrow([(532, 125), (660, 78), (768, 125)], ORANGE)
arrow([(832, 130), (940, 166), (1068, 130)], ORANGE)
for letter, x, label in [
    ("A", 90, "Question"),
    ("B", 500, "Proof"),
    ("C", 800, "New question"),
    ("D", 1100, "Further ideas"),
]:
    vertex(letter, x-31, 99, 62, 62,
           f"ellipse;sketch=1;comic=0;jiggle=1.2;strokeWidth=2;"
           f"strokeColor={TEAL};fillColor=#D2E6E2;fillStyle=hachure;"
           "hachureGap=7;fillWeight=0.8;fontFamily=Kalam;"
           f"fontSize=36;fontStyle=1;fontColor={TEAL};")
    text(label, x-80, 167, 160, 36, 27)
text("Vary the starting conditions", 145, 0, 310, 42, 27, TEAL)
text("Discover what to ask next", 545, 18, 255, 62, 26, ORANGE)
text("Was A the question I meant?", 80, 278, 435, 36, 25, ORANGE)
E.indent(doc)
E.ElementTree(doc).write(OUT, encoding="utf-8", xml_declaration=True)
print(OUT)
