"""Editable FunSearch workflow and illustrative result diagrams."""
from pathlib import Path
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
    def line(self, pts, color=TEAL, arrow=True, dashed=False, width=2.5):
        self.n += 1
        c=ET.SubElement(self.root,'mxCell',id=str(self.n),parent='1',edge='1',style=f'edgeStyle=none;rounded=1;sketch=1;comic=0;jiggle=0.5;strokeWidth={width};strokeColor={color};endArrow={"open" if arrow else "none"};endSize=12;endFill=0;dashed={int(dashed)};')
        g=ET.SubElement(c,'mxGeometry',relative='1',**{'as':'geometry'})
        for p,role in [(pts[0],'sourcePoint'),(pts[-1],'targetPoint')]:
            ET.SubElement(g,'mxPoint',x=str(p[0]),y=str(p[1]),**{'as':role})
        if len(pts)>2:
            a=ET.SubElement(g,'Array',**{'as':'points'})
            for p in pts[1:-1]: ET.SubElement(a,'mxPoint',x=str(p[0]),y=str(p[1]))
    def save(self):
        ET.indent(self.doc)
        ET.ElementTree(self.doc).write(ASSETS/(self.name+'.drawio'),encoding='utf-8',xml_declaration=True)

d=Drawing('funsearch_workflow',1120,280)
d.box('Human supplies\ninitial program',10,38,205,110,ORANGE,'#F1E3D2',size=27)
d.box('LLM\nproposes code\nchanges',310,38,200,110,size=27)
d.box('Evaluator\nfixed program\nruns + scores',620,38,200,110,MUTED,'#E7EAEC',size=26)
d.box('Best program\nfound so far',925,38,185,110,MUTED,'#FFFFFF',shape='shape=note;size=18;',size=27)
d.line([(220,93),(303,93)],ORANGE)
d.text('specification',217,57,90,27,16,ORANGE)
d.line([(516,93),(613,93)])
d.text('candidate',515,57,100,27,22,TEAL)
d.line([(827,93),(918,93)],MUTED)
d.text('improvement',821,57,104,27,19,MUTED)
d.box('Program database',600,192,240,46,PURPLE,'#EEE4EF',shape='rounded=1;arcSize=12;',size=24)
d.line([(720,154),(720,186)],MUTED)
d.text('valid code + scores',748,155,212,30,22,MUTED)
d.line([(594,215),(410,215),(410,155)],PURPLE)
d.text('reuse promising examples',291,244,382,32,24,PURPLE)
d.save()

d=Drawing('funsearch_cap_set',340,165)
for offset,forbidden in [(0,False),(175,True)]:
    for i in range(3):
        d.line([(offset+16,15+53*i),(offset+122,15+53*i)],'#CAD7D4',False,True)
        d.line([(offset+16+53*i,15),(offset+16+53*i,121)],'#CAD7D4',False,True)
    if forbidden:
        # Three selected points on one affine line in F_3^2.
        d.line([(offset+16,68),(offset+122,68)],TEAL,False)
    for x in range(3):
        for y in range(3):
            selected=(y==1) if forbidden else (x<2 and y<2)
            d.box('',offset+10+53*x,9+53*y,12,12,TEAL if selected else '#ADBDBA',TEAL if selected else '#FFFFFF',shape='ellipse;',size=10)
    if forbidden:
        d.line([(offset+18,130),(offset+153,4)],'#C34343',False,width=5)
    d.text('Forbidden' if forbidden else 'Allowed',offset-3,139,145,28,25,MUTED)
d.save()

d=Drawing('funsearch_bin_packing',500,165)
# Same four items: 0.4, 0.4, 0.6, 0.6; capacity one per bin.
for x,items in [(10,[.4,.4]),(80,[.6]),(150,[.6]),(330,[.4,.6]),(400,[.4,.6])]:
    d.box('',x,22,48,100,TEAL,'#FFFFFF',shape='rounded=0;')
    bottom=122
    for item in items:
        height=item*100
        d.box('',x+2,bottom-height,44,height,TEAL if item==.4 else ORANGE,'#A6CEC9' if item==.4 else '#F1D4AF',shape='rounded=0;')
        bottom-=height
d.line([(225,74),(302,74)],ORANGE)
d.text('3 bins',10,134,190,30,27,TEAL,True)
d.text('2 bins',318,134,145,30,27,TEAL,True)
d.save()
