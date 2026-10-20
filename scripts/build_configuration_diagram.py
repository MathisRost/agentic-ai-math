"""Build the talk's native, editable draw.io agent configuration diagram."""
from pathlib import Path
import xml.etree.ElementTree as E
import base64
ASSETS=Path(__file__).resolve().parents[1]/'assets'
INK='#252A2D';TEAL='#21736F';ORANGE='#B16B24'
class Diagram:
 def __init__(self,name,w,h):
  self.name=name;self.doc=E.Element('mxfile',host='app.diagrams.net');d=E.SubElement(self.doc,'diagram',name=name,id=name)
  m=E.SubElement(d,'mxGraphModel',dx=str(w),dy=str(h),grid='0',page='0',pageWidth=str(w),pageHeight=str(h),background='#FFFFFF',extFonts='Kalam^https://fonts.googleapis.com/css?family=Kalam:400,700')
  self.root=E.SubElement(m,'root');E.SubElement(self.root,'mxCell',id='0');E.SubElement(self.root,'mxCell',id='1',parent='0');self.n=1
 def vertex(self,value,x,y,w,h,style):
  self.n+=1;c=E.SubElement(self.root,'mxCell',id=str(self.n),value=value,style=style,vertex='1',parent='1');E.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),**{'as':'geometry'});return str(self.n)
 def text(self,value,x,y,w,h,size=27,bold=False,color=INK):
  return self.vertex(value,x,y,w,h,f'text;html=0;whiteSpace=wrap;align=center;verticalAlign=middle;fontFamily=Kalam;fontSize={size};fontStyle={1 if bold else 0};fontColor={color};strokeColor=none;fillColor=none;')
 def box(self,value,x,y,w,h,fill='#D2E6E2',size=29):
  return self.vertex(value,x,y,w,h,f'rounded=1;arcSize=12;whiteSpace=wrap;html=0;sketch=1;comic=0;jiggle=1.2;strokeWidth=2;fillStyle=hachure;hachureGap=7;fillWeight=0.8;fillColor={fill};strokeColor={TEAL};fontColor={INK};fontFamily=Kalam;fontSize={size};fontStyle=1;')
 def arrow(self,pts,color=ORANGE,dashed=False):
  self.n+=1;c=E.SubElement(self.root,'mxCell',id=str(self.n),value='',edge='1',parent='1',style=f'edgeStyle=none;rounded=1;curved=0;html=0;sketch=1;comic=0;jiggle=0.6;strokeColor={color};strokeWidth=2.5;endArrow=open;endSize=12;endFill=0;dashed={int(dashed)};')
  g=E.SubElement(c,'mxGeometry',relative='1',**{'as':'geometry'})
  for p,role in [(pts[0],'sourcePoint'),(pts[-1],'targetPoint')]: E.SubElement(g,'mxPoint',x=str(p[0]),y=str(p[1]),**{'as':role})
  if len(pts)>2:
   a=E.SubElement(g,'Array',**{'as':'points'})
   for p in pts[1:-1]:E.SubElement(a,'mxPoint',x=str(p[0]),y=str(p[1]))
 def icon(self,file,x,y,w=40,h=40):
  p=ASSETS/'icons'/file;mime='svg+xml' if p.suffix=='.svg' else 'png';data=base64.b64encode(p.read_bytes()).decode()
  self.vertex('',x,y,w,h,f'shape=image;imageAspect=1;aspect=fixed;image=data:image/{mime},{data};')
 def save(self):
  E.indent(self.doc);E.ElementTree(self.doc).write(ASSETS/(self.name+'.drawio'),encoding='utf-8',xml_declaration=True)


# Rounded turquoise boxes are agents; orange documents are context/output files.
GREY='#879695'
HUMAN='#8B5A8B'
d=Diagram('research_agent_configuration',1020,665)
def agent(label,x,y,w=170):
 d.box(label,x,y,w,78,'#BDDAD6',32)
def document(label,x,y,w=180,h=66,stroke=ORANGE,fill='#F1E3D2'):
 d.vertex(label,x,y,w,h,f'shape=document;whiteSpace=wrap;html=0;sketch=1;comic=0;jiggle=1.2;strokeWidth=2;fillStyle=hachure;hachureGap=7;fillWeight=0.8;fillColor={fill};strokeColor={stroke};fontColor={INK};fontFamily=Kalam;fontSize=30;fontStyle=1;spacingBottom=10;')
# Literature tools sit directly above the agent that uses them.
d.icon('undermind.svg',0,105,85,58)
d.icon('zotero.png',128,105,58,58)
d.text('Undermind',-15,166,120,30,23)
d.text('Zotero',115,166,85,30,23)
agent('Literature\nagent',5,210)
# Folded-corner file symbols: an instruction key, not an extra agent node.
d.text('Agent instructions',680,20,340,40,30,True,ORANGE)
for label,x in [('Agent.md',680),('skill.md',870)]:
 d.vertex(label,x,75,160,115,f'shape=note;size=22;whiteSpace=wrap;html=0;sketch=1;comic=0;jiggle=1.2;strokeWidth=2;fillStyle=hachure;hachureGap=7;fillWeight=0.8;fillColor=#F1E3D2;strokeColor={ORANGE};fontColor={INK};fontFamily=Kalam;fontSize=29;fontStyle=1;')
d.text('Loaded for each role',680,200,350,35,26,False,GREY)
document('',-15,330,230,175)
d.text('Common files',-7,338,214,39,30,True)
d.text('Precise problem\nstatement\n+ literature',-7,379,214,82,24)
d.arrow([(90,293),(90,325)],TEAL)
for y,idx in [(85,1),(295,2),(505,5)]:
 document('',330,y-90,180,75,stroke=HUMAN,fill='#E9DDE9')
 d.text('Approach '+str(idx),332,y-82,176,46,30,True,HUMAN)
 d.arrow([(420,y-16),(420,y-3)],GREY)
 agent('Agent '+str(idx),335,y)
 d.arrow([(220,370),(270,370),(270,y+39),(330,y+39)],GREY)
 d.arrow([(510,y+28),(565,y+28),(565,320),(669,320)],TEAL)
 d.arrow([(670,352),(620,352),(620,y+57),(511,y+57)],ORANGE,True)
d.text('...',390,381,60,28,32,True,TEAL)
agent('Critical\nreviewer',675,295,170)
# The reviewer reads the same precise problem and verified sources.
d.arrow([(100,510),(100,602),(650,602),(650,405),(710,405),(710,379)],GREY)
document('Extensive\nreport',670,470,180,90)
d.arrow([(760,378),(760,464)],TEAL)
agent('Coder',900,295,140)
d.arrow([(850,320),(894,320)],ORANGE,True)
d.arrow([(895,352),(851,352)],TEAL)
for x,color,label,dashed,w in [(0,GREY,'context',False,160),(315,TEAL,'results',False,160),(620,ORANGE,'tasks / feedback',True,300)]:
 d.arrow([(x,640),(x+57,640)],color,dashed)
 d.text(label,x+65,619,w,42,29,False,color)
d.save()
