"""Build schematic clustered and repulsive point patterns in the talk style."""
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

import random
rng=random.Random(62)
d=Diagram('point_process_patterns',460,590)
for top,title,caption in [(0,'Clustered','many close pairs'),(295,'Repulsive','few close pairs')]:
 d.text(title,10,top,440,38,31,True,TEAL)
 d.vertex('',20,top+47,420,195,'rounded=1;arcSize=8;fillColor=#FFFFFF;strokeColor='+TEAL+';strokeWidth=2;sketch=1;comic=0;jiggle=1.2;')
 d.text(caption,20,top+249,420,32,25,color=ORANGE)
 if top==0:
  points=[]
  for cx,cy in [(98,104),(222,186),(354,112)]:
   for angle in range(8):
    import math
    theta=angle*math.pi/4+rng.uniform(-.18,.18)
    radius=rng.uniform(17,36)
    points.append((cx+radius*math.cos(theta),cy+radius*math.sin(theta)))
 else:
  points=[]
  while len(points)<24:
   p=(rng.uniform(40,420),rng.uniform(66,224))
   if all((p[0]-q[0])**2+(p[1]-q[1])**2>41**2 for q in points):points.append(p)
 for i,(x,y) in enumerate(points):
  color=TEAL
  d.vertex('',round(x-5,2),round(top+y-5,2),10,10,'ellipse;fillStyle=solid;fillColor='+color+';strokeColor='+color+';strokeWidth=1;sketch=1;jiggle=0.4;')
d.save()
