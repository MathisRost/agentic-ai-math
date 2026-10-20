"""Editable schematic of the paper's rooted finite Poisson clusters."""
from pathlib import Path
import xml.etree.ElementTree as E

OUT = Path(__file__).resolve().parents[1] / 'assets' / 'final_poisson_cluster.drawio'
TEAL, ORANGE, INK, GREY = '#21736F', '#B16B24', '#252A2D', '#BAC9C7'
doc = E.Element('mxfile', host='app.diagrams.net')
diagram = E.SubElement(doc, 'diagram', name='Rooted Poisson clusters', id='final-poisson-cluster')
model = E.SubElement(diagram, 'mxGraphModel', grid='0', page='0', pageWidth='760', pageHeight='350', background='#FFFFFF', extFonts='Kalam^https://fonts.googleapis.com/css?family=Kalam:400,700')
root = E.SubElement(model, 'root')
E.SubElement(root, 'mxCell', id='0')
E.SubElement(root, 'mxCell', id='1', parent='0')
serial = 1

def vertex(value, x, y, w, h, style):
    global serial
    serial += 1
    c = E.SubElement(root, 'mxCell', id=str(serial), parent='1', vertex='1', value=value, style=style)
    E.SubElement(c, 'mxGeometry', x=str(x), y=str(y), width=str(w), height=str(h), **{'as':'geometry'})

def text(value, x, y, w, h, size=26, color=INK):
    vertex(value,x,y,w,h,f'text;html=0;whiteSpace=wrap;align=center;verticalAlign=middle;fontFamily=Kalam;fontSize={size};fontColor={color};strokeColor=none;fillColor=none;')

def line(a,b,color=GREY,arrow=False,dashed=True):
    global serial
    serial += 1
    c = E.SubElement(root,'mxCell',id=str(serial),parent='1',edge='1',style=f'edgeStyle=none;sketch=1;comic=0;jiggle=0.6;strokeWidth=2;strokeColor={color};dashed={int(dashed)};endArrow={"open" if arrow else "none"};endSize=12;endFill=0;')
    g=E.SubElement(c,'mxGeometry',relative='1',**{'as':'geometry'})
    for p,role in [(a,'sourcePoint'),(b,'targetPoint')]:
        E.SubElement(g,'mxPoint',x=str(p[0]),y=str(p[1]),**{'as':role})

def dot(x,y,parent=False):
    color = ORANGE if parent else TEAL
    radius = 8 if parent else 6
    vertex('',x-radius,y-radius,2*radius,2*radius,
           f'ellipse;strokeWidth=1.5;strokeColor={color};fillColor={color};')

# A rectangular schematic point pattern; positions are illustrative, not sampled
# from the manuscript's cluster density. Every cluster has one retained parent.
vertex('',5,5,750,340,f'rounded=0;sketch=1;comic=0;jiggle=1.2;strokeWidth=1.5;strokeColor={GREY};fillColor=none;')
clusters=[
    ((90,90),[(60,40)]),                         # highlighted pair
    ((280,248),[(70,-40),(95,32)]),              # highlighted triangle
    ((610,70),[(-60,85),(70,95),(-5,135)]),      # projected tetrahedron
    ((210,47),[(18,17),(-20,28)]),
    ((430,100),[]),
    ((65,260),[]),
    ((170,215),[(15,35)]),
    ((470,270),[(-30,30),(20,40),(34,-20)]),
    ((695,285),[]),
    ((320,65),[(20,25)]),
    ((700,50),[(25,25)]),
]
# Geometric guides connect actual points, not extra nodes or all parent-child pairs.
for cluster_index in (0,1,2):
    (x,y), offsets = clusters[cluster_index]
    points=[(x,y)]+[(x+dx,y+dy) for dx,dy in offsets]
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            hidden = cluster_index==2 and (i,j)==(1,2)
            line(points[i],points[j],color='#6D9E98',dashed=hidden)
for (x,y), offsets in clusters:
    dot(x,y,True)
    for dx,dy in offsets:
        dot(x+dx,y+dy)
E.indent(doc)
E.ElementTree(doc).write(OUT,encoding='utf-8',xml_declaration=True)
print(OUT)
