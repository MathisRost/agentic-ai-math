"""Build the talk's native, editable draw.io multi-agent diagram."""
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

def rich(value,x,y,w,h,size=27,bold=False,color=INK):
 ident=d.text(value,x,y,w,h,size,bold,color)
 cell=d.root.find("mxCell[@id='"+ident+"']")
 cell.set('style',cell.get('style').replace('html=0','html=1'))

d=Diagram('multi_agent_contexts',820,365)
d.box('',15,5,785,100,'#BDDAD6')
d.text('Instructions (system harness)',25,12,765,44,35,True,TEAL)
d.text('assign tasks / select context / share findings',25,59,765,35,28)
for x,idx in [(15,1),(280,2),(545,3)]:
 d.arrow([(x+170,112),(x+170,169)])
 d.arrow([(x+70,169),(x+70,112)],TEAL)
 d.vertex('',x,175,245,180,'rounded=1;arcSize=9;fillColor=none;strokeColor=#B8C8C5;strokeWidth=1.5;dashed=1;dashPattern=3 5;sketch=1;jiggle=0.5;')
 rich('Agent<sub>'+str(idx)+'</sub>',x+5,183,235,38,32,True,TEAL)
 d.box('',x+12,233,221,65,'#D2E6E2')
 rich('Context C<sub>'+str(idx)+'</sub>',x+18,233,209,65,29,True)
 rich('LLM<sub>'+str(idx)+'</sub> + tools',x+5,310,235,36,29,True)
d.save()
