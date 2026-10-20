"""Build the editable sketch for the paper-writing stage of the talk."""

from pathlib import Path
import base64
import xml.etree.ElementTree as ET


ASSETS = Path(__file__).resolve().parents[1] / "assets"
INK, TEAL, ORANGE, PURPLE = "#252A2D", "#21736F", "#B16B24", "#8B5A8B"
WIDTH, HEIGHT = 760, 650
doc = ET.Element("mxfile", host="app.diagrams.net")
diagram = ET.SubElement(doc, "diagram", name="Writing the paper", id="writing-workflow")
model = ET.SubElement(
    diagram, "mxGraphModel", dx=str(WIDTH), dy=str(HEIGHT), grid="0", page="0",
    pageWidth=str(WIDTH), pageHeight=str(HEIGHT), background="#FFFFFF",
    extFonts="Kalam^https://fonts.googleapis.com/css?family=Kalam:400,700",
)
root = ET.SubElement(model, "root")
ET.SubElement(root, "mxCell", id="0")
ET.SubElement(root, "mxCell", id="1", parent="0")
serial = 1


def cell(value, x, y, width, height, style):
    global serial
    serial += 1
    element = ET.SubElement(root, "mxCell", id=str(serial), value=value,
                            style=style, vertex="1", parent="1")
    ET.SubElement(element, "mxGeometry", x=str(x), y=str(y), width=str(width),
                  height=str(height), **{"as": "geometry"})


def text(value, x, y, width, height, size=30, bold=False, color=INK, align="left"):
    cell(value, x, y, width, height,
         f"text;html=0;whiteSpace=wrap;align={align};verticalAlign=middle;"
         f"fontFamily=Kalam;fontSize={size};fontStyle={int(bold)};fontColor={color};"
         "strokeColor=none;fillColor=none;spacing=0;")


def box(value, x, y, width, height, color=TEAL, tint="#D2E6E2", size=33, shape="rounded=1;arcSize=12;"):
    cell(value, x, y, width, height,
         f"{shape}html=0;whiteSpace=wrap;align=center;verticalAlign=middle;"
         "sketch=1;comic=0;jiggle=1.2;strokeWidth=2;"
         "fillStyle=hachure;hachureGap=7;fillWeight=0.8;"
         f"fillColor={tint};strokeColor={color};fontFamily=Kalam;"
         f"fontSize={size};fontStyle=1;fontColor={INK};spacing=12;")


def arrow(points, color=TEAL, dashed=False):
    global serial
    serial += 1
    element = ET.SubElement(root, "mxCell", id=str(serial), value="", edge="1", parent="1",
                            style="edgeStyle=none;rounded=1;html=0;sketch=1;comic=0;jiggle=0.6;"
                            f"strokeColor={color};strokeWidth=2.5;endArrow=open;endFill=0;endSize=12;"
                            f"dashed={int(dashed)};dashPattern=5 5;")
    geometry = ET.SubElement(element, "mxGeometry", relative="1", **{"as": "geometry"})
    for point, role in [(points[0], "sourcePoint"), (points[-1], "targetPoint")]:
        ET.SubElement(geometry, "mxPoint", x=str(point[0]), y=str(point[1]), **{"as": role})
    if len(points) > 2:
        middle = ET.SubElement(geometry, "Array", **{"as": "points"})
        for point in points[1:-1]:
            ET.SubElement(middle, "mxPoint", x=str(point[0]), y=str(point[1]))


def icon(filename, x, y, size=43):
    path = ASSETS / "icons" / filename
    mime = "svg+xml" if path.suffix == ".svg" else "png"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    cell("", x, y, size, size,
         f"shape=image;imageAspect=1;aspect=fixed;image=data:image/{mime},{data};")


# Inputs feed one persistent writer. The two agents exchange different artifacts.
box("", 12, 10, 452, 124, PURPLE, "#EEE4EF")
text("Me", 28, 13, 420, 39, 35, True, PURPLE, "center")
text("Read report;\nchoose structure + audience", 28, 53, 420, 73, 30, align="center")
box("Results +\nchecked citations", 522, 10, 226, 124,
    ORANGE, "#F1E3D2", 30, "shape=note;size=20;")
arrow([(235, 142), (235, 181)], PURPLE)
arrow([(635, 142), (635, 181)], ORANGE)

box("", 80, 190, 600, 240)
text("Writer", 100, 202, 560, 49, 41, True, TEAL, "center")
text("Draft + integrate citations\nRevise + check changes + compile", 100, 265, 560, 81, 31, align="center")
text("Tools used:", 106, 365, 132, 43, 27, color=ORANGE)
icon("zotero.png", 248, 365)
text("Zotero", 301, 365, 104, 43, 28)
icon("undermind.svg", 425, 365)
text("Undermind", 478, 365, 178, 43, 28)

# Draft and feedback go in opposite directions between the same two boxes.
arrow([(225, 438), (225, 489)], TEAL)
text("draft", 95, 442, 112, 41, 32, color=TEAL, align="right")
arrow([(535, 489), (535, 438)], ORANGE)
text("feedback", 552, 442, 177, 41, 32, color=ORANGE)

box("", 80, 500, 600, 132)
text("Reader", 100, 510, 560, 49, 41, True, TEAL, "center")
text("Fresh context\nIdentify specific difficulties", 100, 561, 560, 62, 31, align="center")

ET.indent(doc)
ET.ElementTree(doc).write(ASSETS / "writing_workflow.drawio", encoding="utf-8", xml_declaration=True)
