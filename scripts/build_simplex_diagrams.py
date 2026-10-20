"""Build three editable simplex sketches: distance, area, volume."""
from pathlib import Path
import xml.etree.ElementTree as E
import base64
import zlib
from urllib.parse import quote
import sys
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

def line(d,a,b,dashed=False,color=TEAL):
 d.arrow([a,b],color,dashed)
 cell=d.root.find("mxCell[@id='"+str(d.n)+"']")
 cell.set('style',cell.get('style').replace('endArrow=open','endArrow=none'))
def point(d,x,y,label,dx=0,dy=8):
 d.vertex('',x-6,y-6,12,12,'ellipse;fillStyle=solid;fillColor='+TEAL+';strokeColor='+TEAL+';sketch=1;jiggle=0.4;')
 ident=d.text('x<sub>'+str(label)+'</sub>',x-22+dx,y+dy,44,30,24,True)
 cell=d.root.find("mxCell[@id='"+ident+"']")
 cell.set('style',cell.get('style').replace('html=0','html=1'))
def face(d):
 d.vertex('',50,20,280,160,'shape=triangle;direction=north;fillColor=#D2E6E2;strokeColor='+TEAL+';strokeWidth=2;sketch=1;comic=0;jiggle=1.2;fillStyle=hachure;hachureGap=8;fillWeight=0.7;')
def polygon(d,points,fill,angle,hachure_gap=6,fill_weight=1.2):
 x0=min(p[0] for p in points);y0=min(p[1] for p in points)
 w=max(p[0] for p in points)-x0;h=max(p[1] for p in points)-y0
 shape=E.Element('shape',name='simplex_face',w='100',h='100',aspect='variable',strokewidth='inherit')
 fg=E.SubElement(shape,'foreground');path=E.SubElement(fg,'path')
 for i,(x,y) in enumerate(points):
  E.SubElement(path,'move' if i==0 else 'line',x=str(100*(x-x0)/w),y=str(100*(y-y0)/h))
 E.SubElement(path,'close');E.SubElement(fg,'fillstroke')
 compressor=zlib.compressobj(wbits=-15)
 payload=quote(E.tostring(shape,encoding='unicode'),safe="~()*!.'-").encode()
 encoded=base64.b64encode(compressor.compress(payload)+compressor.flush()).decode()
 d.vertex('',x0,y0,w,h,f'shape=stencil({encoded});fillColor={fill};strokeColor={TEAL};strokeWidth=2;sketch=1;comic=0;jiggle=0.7;fillStyle=hachure;hachureGap={hachure_gap};hachureAngle={angle};fillWeight={fill_weight};')

def altitude(d,top,foot,index,label_position,plane_step):
 # A representative altitude; h_3 and h_4 bound every altitude from below.
 line(d,top,foot,True,ORANGE)
 # The tetrahedron marker is projected along with its base plane.
 dx=top[0]-foot[0];dy=top[1]-foot[1]
 length=(dx*dx+dy*dy)**0.5
 u=(14*dx/length,14*dy/length);v=plane_step
 a=(foot[0]+u[0],foot[1]+u[1])
 b=(a[0]+v[0],a[1]+v[1])
 c=(foot[0]+v[0],foot[1]+v[1])
 line(d,a,b,False,ORANGE);line(d,b,c,False,ORANGE)
 ident=d.text('≥ h<sub>'+str(index)+'</sub>',*label_position,78,34,27,True,ORANGE)
 cell=d.root.find("mxCell[@id='"+ident+"']")
 cell.set('style',cell.get('style').replace('html=0','html=1').replace('fillColor=none','fillColor=#FFFFFF'))

for name in (sys.argv[1:] or ['segment','triangle','tetrahedron']):
 d=Diagram('simplex_'+name,380,260)
 # Invisible frame keeps all three exports aligned and equally scaled.
 d.vertex('',0,0,380,260,'fillColor=none;strokeColor=none;')
 if name=='segment':
  line(d,(60,135),(320,70))
  point(d,60,135,1);point(d,320,70,2)
  d.text('D',165,82,50,40,33,True,ORANGE)
  caption='Distance D'
 elif name=='triangle':
  face(d)
  point(d,50,180,1,-7,5);point(d,330,180,2,7,5);point(d,190,20,3,30,-15)
  altitude(d,(190,20),(190,180),3,(105,116),(14,0))
  d.text('A',230,112,40,40,33,True,ORANGE)
  caption='Area A'
 else:
  # An oblique projection separates the vertical altitude from the front ridge.
  # Its foot lies inside the projected base triangle, away from every edge.
  top=(225,25);left=(30,170);front=(325,205);right=(340,120)
  polygon(d,[top,left,front],'#C7E1DE',35,12,0.5)
  polygon(d,[top,front,right],'#DDEDEB',125,10,0.6)
  # The rear edge passes behind the solid; all five visible edges are solid.
  line(d,left,right,True)
  for a,b in [(top,left),(left,front),(front,right),(right,top),(top,front)]:
   line(d,a,b)
  altitude(d,top,(225,167),4,(135,100),(14,-3))
  point(d,*left,1,-20,-2);point(d,*front,2,18,-3)
  point(d,*right,3,13,-10);point(d,*top,4,0,-28)
  caption='Volume V'
 d.text(caption,0,224,380,35,29,True,TEAL)
 d.save()
