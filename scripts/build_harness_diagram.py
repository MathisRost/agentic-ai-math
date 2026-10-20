"""Build the talk's native, editable draw.io harness diagram."""
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

d=Diagram('skills_and_harness',610,580)
d.box('Agent file A',20,10,180,70,'#D2E6E2',26)
d.box('Skill S\n(M, I, R)',220,10,180,70,'#BDDAD6',26)
d.box('Configuration\nfile',420,10,180,70,'#BDDAD6',26)
d.vertex('',15,165,580,285,'rounded=1;arcSize=9;fillColor=none;strokeColor=#B8C8C5;strokeWidth=1.5;dashed=1;dashPattern=3 5;sketch=1;jiggle=0.5;')
d.text('Harness H',300,177,275,40,32,True,TEAL)
d.box('Context',45,240,205,70)
d.box('LLM',400,240,150,70,'#A6CEC9')
d.box('Tool',400,370,150,60,'#BDDAD6')
d.arrow([(110,87),(110,233)],TEAL)
d.text('by scope',10,108,95,35,21,color=TEAL)
d.arrow([(310,87),(310,122),(235,122),(235,232)],TEAL)
d.arrow([(510,87),(510,158)])
d.text('settings',425,110,80,30,21,color=ORANGE)
d.text('I: on demand',265,130,140,30,22,color=TEAL)
d.arrow([(257,275),(393,275)])
d.text('input',275,235,95,32,24)
d.arrow([(475,317),(475,363)])
d.text('call',485,323,65,32,24)
d.arrow([(393,400),(145,400),(145,317)],TEAL)
d.text('tool result',172,360,180,32,24,color=TEAL)
d.box('Environment',300,520,290,60,'#D2E6E2',29)
d.arrow([(430,436),(430,513)])
d.text('read / act',280,465,145,32,24)
d.arrow([(530,513),(530,436)],TEAL)
d.text('result',535,466,78,32,23,color=TEAL)
d.text('R: read or run via tools',15,530,260,40,23,color=TEAL)
d.save()
