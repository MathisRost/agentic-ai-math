"""Build editable file sketches for Step 3 of the agentic mathematics talk."""

from pathlib import Path
import xml.etree.ElementTree as ET


ASSETS = Path(__file__).resolve().parents[1] / "assets"
INK = "#252A2D"
TEAL = "#21736F"
ORANGE = "#B16B24"
MUTED = "#626A70"
WIDTH, HEIGHT = 1320, 470

doc = ET.Element("mxfile", host="app.diagrams.net")
diagram = ET.SubElement(doc, "diagram", name="Skills and agent files", id="skills-agent-files")
model = ET.SubElement(
    diagram,
    "mxGraphModel",
    dx=str(WIDTH), dy=str(HEIGHT), grid="0", page="0",
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
    element = ET.SubElement(
        root, "mxCell", id=str(serial), value=value, style=style,
        vertex="1", parent="1",
    )
    ET.SubElement(
        element, "mxGeometry", x=str(x), y=str(y), width=str(width),
        height=str(height), **{"as": "geometry"},
    )


def text(value, x, y, width, height, size=29, bold=False, color=INK):
    cell(
        value, x, y, width, height,
        "text;html=0;whiteSpace=wrap;align=left;verticalAlign=middle;"
        f"fontFamily=Kalam;fontSize={size};fontStyle={int(bold)};fontColor={color};"
        "strokeColor=none;fillColor=none;spacing=0;",
    )


def file_sketch(x, filename, subtitle, bullets, color=TEAL, tint="#D2E6E2"):
    y, w, h = 12, 410, 438
    cell(
        "", x, y, w, h,
        "shape=note;size=28;whiteSpace=wrap;html=0;sketch=1;comic=0;"
        "jiggle=1.2;strokeWidth=2;fillColor=#FFFFFF;"
        f"strokeColor={color};",
    )
    cell(
        "", x + 16, y + 17, w - 55, 52,
        "rounded=1;arcSize=7;sketch=1;comic=0;jiggle=0.7;strokeWidth=1;"
        "fillStyle=hachure;hachureGap=7;fillWeight=0.8;"
        f"fillColor={tint};strokeColor=none;",
    )
    text(filename, x + 27, y + 20, w - 66, 44, size=27, bold=True, color=color)
    text(subtitle, x + 27, y + 83, w - 50, 32, size=25, color=MUTED)
    for n, bullet in enumerate(bullets):
        by = y + 132 + n * 73
        cell(
            "", x + 29, by + 27, 6, 6,
            f"ellipse;fillColor={color};strokeColor=none;sketch=0;",
        )
        text(bullet, x + 48, by, w - 72, 64, size=27)


file_sketch(
    8, "literature_agent.md", "Used: literature role",
    ["Read supplied papers\nand earlier manuscripts",
     "Extract theorems, conditions\nand page references",
     "Separate exact results\nfrom approximations",
     "Share references and\nunresolved questions"],
)
file_sketch(
    455, "proof_agent.md", "Used: proof role",
    ["Keep prescribed intensity\nand geometric cutoffs",
     "Construct a stationary,\nsimple point process",
     "Derive full densities\nat orders 2, 3 and 4",
     "Prove the exact laws\nor report a precise gap"],
)
file_sketch(
    902, "SKILL.md", "Available: math-literature-check",
    ["Specify the claim\nand search scope",
     "Read the source theorem\nand its assumptions",
     "Show the implication\nor identify the mismatch",
     "Record evidence; no match\ndoes not mean novelty"],
    color=ORANGE, tint="#F1E3D2",
)

ET.indent(doc)
ET.ElementTree(doc).write(
    ASSETS / "skills_agent_files.drawio", encoding="utf-8", xml_declaration=True,
)
