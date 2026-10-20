"""Build the editable launch-prompt bubble and results placeholder."""

from pathlib import Path
import xml.etree.ElementTree as ET

ASSETS = Path(__file__).resolve().parents[1] / "assets"
INK = "#252A2D"
TEAL = "#21736F"
ORANGE = "#B16B24"
MUTED = "#626A70"

doc = ET.Element("mxfile", host="app.diagrams.net")
diagram = ET.SubElement(doc, "diagram", name="Results", id="results-prompt")
model = ET.SubElement(
    diagram, "mxGraphModel", dx="1320", dy="565", grid="0", page="0",
    pageWidth="1320", pageHeight="565", background="#FFFFFF",
    extFonts="Kalam^https://fonts.googleapis.com/css?family=Kalam:400,700",
)
root = ET.SubElement(model, "root")
ET.SubElement(root, "mxCell", id="0")
ET.SubElement(root, "mxCell", id="1", parent="0")
serial = 1


def vertex(value, x, y, width, height, style):
    global serial
    serial += 1
    cell = ET.SubElement(root, "mxCell", id=str(serial), value=value,
                         style=style, vertex="1", parent="1")
    ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(width),
                  height=str(height), **{"as": "geometry"})


def label(value, x, y, width, height, size=29, bold=False, color=INK, align="left"):
    vertex(value, x, y, width, height,
           "text;html=0;whiteSpace=wrap;verticalAlign=middle;spacing=0;"
           f"align={align};fontFamily=Kalam;fontSize={size};fontStyle={int(bold)};"
           f"fontColor={color};strokeColor=none;fillColor=none;")


# A native editable stencil makes the speaker's tail part of the same outline.
stencil = ET.Element("shape", name="Prompt bubble", w="610", h="550", aspect="variable", strokewidth="inherit")
ET.SubElement(stencil, "connections")
bg = ET.SubElement(stencil, "background")
path = ET.SubElement(bg, "path")
ET.SubElement(path, "move", x="28", y="0")
ET.SubElement(path, "line", x="582", y="0")
ET.SubElement(path, "quad", x1="610", y1="0", x2="610", y2="28")
ET.SubElement(path, "line", x="610", y="462")
ET.SubElement(path, "quad", x1="610", y1="490", x2="582", y2="490")
ET.SubElement(path, "line", x="128", y="490")
ET.SubElement(path, "line", x="48", y="548")
ET.SubElement(path, "line", x="68", y="490")
ET.SubElement(path, "line", x="28", y="490")
ET.SubElement(path, "quad", x1="0", y1="490", x2="0", y2="462")
ET.SubElement(path, "line", x="0", y="28")
ET.SubElement(path, "quad", x1="0", y1="0", x2="28", y2="0")
ET.SubElement(path, "close")
fg = ET.SubElement(stencil, "foreground")
ET.SubElement(fg, "fillstroke")

import base64
import zlib

encoded = base64.b64encode(zlib.compress(ET.tostring(stencil, encoding="utf-8"))[2:-4]).decode()
vertex("", 8, 8, 610, 550,
       f"shape=stencil({encoded});sketch=1;comic=0;jiggle=1.2;strokeWidth=2;"
       f"strokeColor={TEAL};fillColor=#FFFFFF;")
vertex("", 31, 27, 551, 52,
       "rounded=1;arcSize=9;sketch=1;comic=0;jiggle=0.7;strokeColor=none;"
       "fillStyle=hachure;hachureGap=7;fillWeight=0.8;fillColor=#D2E6E2;")
label("Launch prompt (shortened)", 48, 31, 530, 43, 29, True, TEAL)

paragraphs = [
    ("Run the configured workflow.\nRead instruction.md and agent.md.", 96, 68),
    ("Use GPT-5.6 Sol with extra-high\nreasoning for every agent.", 174, 68),
    ("Use one literature agent, five proof\nagents, the reviewer and the coder.", 252, 68),
    ("Preserve the exact problem\nand separate agent contexts.", 330, 68),
    ("Complete the reviews. Report results\nand remaining proof gaps.", 408, 68),
]
for content, y, height in paragraphs:
    label(content, 42, y, 552, height, 28)

vertex("", 716, 8, 598, 490,
       "rounded=1;arcSize=8;sketch=1;comic=0;jiggle=0.6;strokeWidth=2;"
       f"strokeColor={ORANGE};fillColor=none;dashed=1;dashPattern=5 7;")
label("Results to be added", 766, 209, 498, 60, 33, False, MUTED, "center")

ET.indent(doc)
ET.ElementTree(doc).write(ASSETS / "results_prompt_placeholder.drawio",
                         encoding="utf-8", xml_declaration=True)
