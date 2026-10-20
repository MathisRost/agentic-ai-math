"""Editable AlphaProof architecture, adapted from Hubert et al., Figures 1-2."""
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

d=Drawing('alphaproof_architecture',1130,420)
d.box('Problem\nformalized\nin Lean',10,90,180,125,ORANGE,'#F1E3D2',size=27)
# The network supplies policy/value predictions; search chooses and tests tactics.
d.box('',270,65,280,170,MUTED,'#FFFFFF',size=26)
d.box('LLM proof network\npolicy + value',285,80,250,76,size=24)
d.line([(410,162),(410,181)],TEAL)
d.text('Tree search',285,186,250,37,28,MUTED,True)
d.line([(197,150),(263,150)],ORANGE)
d.text('start',196,111,70,28,23,ORANGE)
d.box('',675,90,245,125,MUTED,'#E7EAEC',size=26)
lean_logo=base64.b64encode((ASSETS/'icons'/'lean.svg').read_bytes()).decode('ascii')
d.cell('',691,104,78,29,f'shape=image;imageAspect=1;aspect=fixed;image=data:image/svg+xml,{lean_logo};')
d.text('environment',775,103,133,32,23,MUTED,True)
d.text('executes tactics\nchecks proofs',687,144,220,62,26,INK,True)
d.line([(557,150),(668,150)],TEAL)
d.text('tactic',560,112,106,30,25,TEAL)
d.box('Verified\nproof',1010,90,140,125,MUTED,'#FFFFFF',shape='shape=note;size=18;',size=29)
d.line([(927,150),(1003,150)],MUTED)
d.text('success',925,113,80,28,21,MUTED)
d.line([(795,221),(795,270),(480,270),(480,242)],PURPLE)
d.text('new goals / errors',595,279,330,35,25,PURPLE)
d.box('RL training\non formal problems',270,345,280,74,MUTED,'#E7EAEC',size=26)
d.line([(380,338),(380,242)],TEAL)
d.text('updates\nnetwork',270,265,105,64,23,TEAL)
d.box('Verified outcomes\nfrom training attempts',675,345,330,74,PURPLE,'#EEE4EF',size=25)
d.line([(880,221),(880,338)],MUTED)
d.line([(668,382),(557,382)],PURPLE)
d.text('experience',551,340,120,30,20,PURPLE)
d.save()
