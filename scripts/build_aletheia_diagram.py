"""Editable Aletheia architecture, adapted from Feng et al. (2026), Figure 1."""
from pathlib import Path
import base64
import xml.etree.ElementTree as ET

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
TEAL, ORANGE, INK, MUTED = '#21736F', '#B16B24', '#252A2D', '#626A70'
PURPLE = '#8B5A8B'
SKETCH = 'sketch=1;comic=0;jiggle=1.2;strokeWidth=2;fillStyle=hachure;hachureGap=7;fillWeight=0.8;'

class Drawing:
    def __init__(self, name, w, h):
        self.name = name
        self.doc = ET.Element('mxfile', host='app.diagrams.net')
        d = ET.SubElement(self.doc, 'diagram', name=name, id=name)
        m = ET.SubElement(d, 'mxGraphModel', grid='0', page='0', pageWidth=str(w), pageHeight=str(h), background='#FFFFFF', extFonts='Kalam^https://fonts.googleapis.com/css?family=Kalam:400,700')
        self.root = ET.SubElement(m, 'root')
        ET.SubElement(self.root, 'mxCell', id='0')
        ET.SubElement(self.root, 'mxCell', id='1', parent='0')
        self.n = 1
    def cell(self, value, x, y, w, h, style):
        self.n += 1
        c = ET.SubElement(self.root, 'mxCell', id=str(self.n), parent='1', vertex='1', value=value, style=style)
        ET.SubElement(c, 'mxGeometry', x=str(x), y=str(y), width=str(w), height=str(h), **{'as':'geometry'})
    def text(self, value, x, y, w, h, size=26, color=INK, bold=False):
        self.cell(value,x,y,w,h,f'text;html=0;whiteSpace=wrap;align=center;verticalAlign=middle;spacing=0;strokeColor=none;fillColor=none;fontFamily=Kalam;fontSize={size};fontColor={color};fontStyle={int(bold)};')
    def box(self, value, x, y, w, h, color=TEAL, fill='#D2E6E2', shape='rounded=1;arcSize=12;', size=28):
        self.cell(value,x,y,w,h,shape+SKETCH+f'html=0;whiteSpace=wrap;align=center;verticalAlign=middle;spacing=6;strokeColor={color};fillColor={fill};fontFamily=Kalam;fontSize={size};fontColor={INK};fontStyle=1;')
    def line(self, pts, color=TEAL, arrow=True, dashed=False):
        self.n += 1
        c=ET.SubElement(self.root,'mxCell',id=str(self.n),parent='1',edge='1',style=f'edgeStyle=none;rounded=1;sketch=1;comic=0;jiggle=0.5;strokeWidth=2.5;strokeColor={color};endArrow={"open" if arrow else "none"};endSize=12;endFill=0;dashed={int(dashed)};')
        g=ET.SubElement(c,'mxGeometry',relative='1',**{'as':'geometry'})
        for p,role in [(pts[0],'sourcePoint'),(pts[-1],'targetPoint')]:
            ET.SubElement(g,'mxPoint',x=str(p[0]),y=str(p[1]),**{'as':role})
        if len(pts)>2:
            a=ET.SubElement(g,'Array',**{'as':'points'})
            for p in pts[1:-1]: ET.SubElement(a,'mxPoint',x=str(p[0]),y=str(p[1]))
    def save(self):
        ET.indent(self.doc)
        ET.ElementTree(self.doc).write(ASSETS/(self.name+'.drawio'),encoding='utf-8',xml_declaration=True)

d=Drawing('aletheia_architecture',680,300)
# All three coloured boxes are LLM roles; arrows distinguish proposals from critique.
d.box('Generator\nLLM',10,85,180,80,size=29)
d.box('Verifier\nLLM',290,85,180,80,size=29)
d.box('Reviser\nLLM',290,225,180,75,size=29)
d.box('Accepted\nsolution',555,85,125,80,MUTED,'#FFFFFF',size=25)
d.line([(197,125),(283,125)],TEAL)
d.text('draft',195,87,88,30,25,TEAL)
d.line([(477,125),(548,125)],TEAL)
d.text('accept',475,87,80,30,23,TEAL)
d.line([(380,78),(380,32),(100,32),(100,78)],ORANGE)
d.text('major flaws: retry',120,0,245,30,25,ORANGE)
d.line([(380,172),(380,218)],ORANGE)
d.text('minor fixes',415,180,165,32,25,ORANGE)
d.line([(283,262),(235,262),(235,150),(283,150)],TEAL)
d.text('revised\ndraft',95,210,125,65,24,TEAL)
d.save()
