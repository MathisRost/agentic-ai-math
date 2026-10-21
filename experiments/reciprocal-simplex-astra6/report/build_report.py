"""Rebuild the PDF offline: Python 3 + reportlab + DejaVu Sans fonts.

Set RESEARCH_REPORT_FONT_DIR if the fonts are not installed in a standard path.
The source data are report.json and ../accounting/turns.json.
"""
from pathlib import Path
import os, json, html, re
from datetime import datetime, timezone
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Flowable
from reportlab.graphics.shapes import Drawing, Rect, Line, String, Polygon, Group
from reportlab.graphics import renderPDF, renderSVG

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
font_candidates=[Path(os.environ.get('RESEARCH_REPORT_FONT_DIR','.')),Path('/usr/share/fonts/truetype/dejavu'),Path('/usr/share/fonts/dejavu')]
FONT=next((p for p in font_candidates if (p/'DejaVuSans.ttf').is_file() and (p/'DejaVuSans-Bold.ttf').is_file()),None)
if FONT is None:raise SystemExit('Install DejaVu Sans or set RESEARCH_REPORT_FONT_DIR to its font directory.')
for name,file in [('Body','DejaVuSans.ttf'),('Strong','DejaVuSans-Bold.ttf')]:pdfmetrics.registerFont(TTFont(name,str(FONT/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Strong',italic='Body',boldItalic='Strong')
INK=colors.HexColor('#17383E');TEAL=colors.HexColor('#087F8C');ORANGE=colors.HexColor('#D77733')
PALE=colors.HexColor('#EDF5F4');GREY=colors.HexColor('#5B6B70');LINE=colors.HexColor('#D5E2E2')
W,H=A4;M=44;CONTENT=W-2*M
S={
 'body':ParagraphStyle('body',fontName='Body',fontSize=9.5,leading=14,spaceAfter=9,textColor=INK),
 'title':ParagraphStyle('title',fontName='Strong',fontSize=23,leading=28,spaceAfter=15,textColor=INK),
 'kicker':ParagraphStyle('kicker',fontName='Strong',fontSize=8,leading=11,spaceAfter=8,textColor=TEAL),
 'sub':ParagraphStyle('sub',fontName='Strong',fontSize=11.3,leading=15,spaceBefore=5,spaceAfter=7,textColor=INK),
 'note':ParagraphStyle('note',fontName='Body',fontSize=8,leading=11.5,textColor=GREY,spaceBefore=3,spaceAfter=8),
 'equation':ParagraphStyle('equation',fontName='Body',fontSize=10.1,leading=15,textColor=TEAL,spaceBefore=4,spaceAfter=11,leftIndent=10),
 'cell':ParagraphStyle('cell',fontName='Body',fontSize=8.05,leading=11.4,textColor=INK),
 'head':ParagraphStyle('head',fontName='Strong',fontSize=8,leading=11.4,textColor=colors.white),
 'small':ParagraphStyle('small',fontName='Body',fontSize=7.35,leading=10.2,textColor=INK),
}
def esc(s):return html.escape(str(s)).replace('\n','<br/>')
def par(s,style='body'):return Paragraph(esc(s),S[style])
def arrow(d,x1,y1,x2,y2,color=TEAL):
    import math
    d.add(Line(x1,y1,x2,y2,strokeColor=color,strokeWidth=1.1))
    a=math.atan2(y2-y1,x2-x1);r=5
    d.add(Polygon([x2,y2,x2-r*math.cos(a-.5),y2-r*math.sin(a-.5),x2-r*math.cos(a+.5),y2-r*math.sin(a+.5)],fillColor=color,strokeColor=color))
def box(d,x,y,w,h,title,subtitle='',fill=PALE):
    d.add(Rect(x,y,w,h,rx=5,ry=5,fillColor=fill,strokeColor=LINE,strokeWidth=.6))
    d.add(String(x+w/2,y+h-16,title,fontName='Strong',fontSize=9,textAnchor='middle',fillColor=INK))
    if subtitle:d.add(String(x+w/2,y+10,subtitle,fontName='Body',fontSize=7.1,textAnchor='middle',fillColor=GREY))
def architecture():
    d=Drawing(CONTENT,226)
    box(d,134,182,240,39,'Coordinator','model + accounting gate / frozen S0')
    box(d,4,121,156,40,'N1: global obstruction','independent fresh context')
    box(d,172,121,156,40,'N2: local geometry','independent fresh context')
    box(d,340,121,163,40,'Fresh reviewers','audit before target revision')
    arrow(d,220,182,82,163);arrow(d,277,182,250,163)
    # Parallel investigation outputs both feed the review stage.
    arrow(d,82,121,82,111);arrow(d,82,111,422,111);arrow(d,422,111,422,121)
    arrow(d,328,141,338,141)
    box(d,135,65,240,39,'S1: common upper diameter bound','broadcast target + evidence; no lower cutoffs')
    arrow(d,422,121,422,85);arrow(d,422,85,377,85)
    for i,title in enumerate(['P1: clusters','P2: Cox','P3: branching','P4: choice']):
        x=3+i*127;box(d,x,3,119,40,title,'≤ 4 submissions each')
        arrow(d,254,65,x+59.5,45)
    full=Drawing(CONTENT,288)
    g=Group(*d.contents);g.translate(0,62);full.add(g)
    box(full,3,18,CONTENT-6,36,'Per track: submission → fresh review → own feedback','Repeat within the original four-submission allowance; no reset')
    for i in range(4):arrow(full,62+i*127,65,62+i*127,56)
    full.add(String(CONTENT/2,3,'Shared literature on request  •  Fresh final synthesis after all individual reviews',fontName='Body',fontSize=7.1,textAnchor='middle',fillColor=GREY))
    return full
class ArchFlow(Flowable):
    def __init__(self):super().__init__();self.width=CONTENT;self.height=297
    def draw(self):renderPDF.draw(architecture(),self.canv,0,6)

def parse(s):return datetime.fromisoformat(s.replace('Z','+00:00'))
class Timeline(Flowable):
    def __init__(self):super().__init__();self.width=CONTENT;self.height=236
    def draw(self):
        c=self.canv;rows=json.loads((ROOT/'accounting/turns.json').read_text())
        lanes=[('N1','nonexistence_1'),('R-N1','review_nonexistence_1'),('N2','nonexistence_2'),('R-N2','review_nonexistence_2')]
        for i in range(1,5):lanes += [(f'P{i}',f'proof_{i}'),(f'R-P{i}',f'review_proof_{i}')]
        lanes += [('Literature','literature'),('Final review','final_synthesis')]
        start=parse('2026-10-20T16:42:00Z');duration=186*60;left=68;right=CONTENT-7;plot=right-left
        for minute in [0,30,60,90,120,150,180]:
            x=left+minute*60/duration*plot;c.setStrokeColor(LINE);c.line(x,29,x,220)
            c.setFillColor(GREY);c.setFont('Body',6.9);t=start.timestamp()+minute*60
            c.drawCentredString(x,225,datetime.fromtimestamp(t,timezone.utc).strftime('%H:%M'))
        for j,(name,role) in enumerate(lanes):
            y=207-j*13;c.setFont('Body',7.7);c.setFillColor(INK);c.drawRightString(left-6,y-2,name)
            for t in rows:
                if not t['ended_at_utc']:continue
                if (role.startswith('review_') and t['role'].startswith(role+'_')) or t['role']==role:
                    x=left+(parse(t['started_at_utc'])-start).total_seconds()/duration*plot
                    w=(parse(t['ended_at_utc'])-parse(t['started_at_utc'])).total_seconds()/duration*plot
                    c.setFillColor(ORANGE if role.startswith('review_') or role=='final_synthesis' else TEAL)
                    c.roundRect(x,y-3,max(w,1),7,2,fill=1,stroke=0)
        c.setFont('Body',7.5);c.setFillColor(TEAL);c.drawString(left,10,'Investigation / source work')
        c.setFillColor(ORANGE);c.drawString(left+175,10,'Independent review')

class Hero(Flowable):
    def __init__(self,items):super().__init__();self.items=items;self.height=100;self.width=CONTENT
    def draw(self):
        c=self.canv;w=(CONTENT-10)/2
        for i,(big,small) in enumerate(self.items):
            x=(i%2)*(w+10);y=53-(i//2)*50
            c.setFillColor(PALE);c.roundRect(x,y,w,44,4,fill=1,stroke=0)
            c.setFillColor(TEAL);c.setFont('Strong',14);c.drawString(x+12,y+24,big)
            c.setFont('Body',8);c.setFillColor(GREY);c.drawString(x+12,y+10,small)

def make_table(z):
    n=len(z['headers']);ratios=z.get('widths') or [1/n]*n
    widths=[CONTENT*r/sum(ratios) for r in ratios]
    small=n>=7
    data=[[par(x,'head') for x in z['headers']]]+[[par(x,'small' if small else 'cell') for x in row] for row in z['rows']]
    t=Table(data,colWidths=widths,hAlign='LEFT',repeatRows=1)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),TEAL),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),3.2 if len(data)>20 else 5),('BOTTOMPADDING',(0,0),(-1,-1),3.2 if len(data)>20 else 5),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),('LINEBELOW',(0,-1),(-1,-1),.5,LINE)]))
    return t
def footer(c,doc):
    c.saveState();c.setStrokeColor(LINE);c.line(M,36,W-M,36)
    c.setFillColor(GREY);c.setFont('Body',7);c.drawString(M,24,'RECIPROCAL SIMPLEX  /  GPT-6-ASTRA  /  20 OCT 2026')
    c.drawRightString(W-M,24,str(doc.page));c.restoreState()
def main():
    data=json.loads((HERE/'report.json').read_text())
    # Fail early if the selected font cannot display any report character.
    missing=set()
    for p in data['pages']:
        s=json.dumps(p,ensure_ascii=False)
        missing|={c for c in s if ord(c)>32 and ord(c) not in pdfmetrics.getFont('Body').face.charToGlyph}
    if missing:raise ValueError('Unsupported glyphs: '+repr(missing))
    story=[]
    for i,p in enumerate(data['pages']):
        if i:story.append(PageBreak())
        story += [par(p['kicker'],'kicker'),par(p['title'],'title')]
        for z in p['blocks']:
            kind=z['kind']
            if kind in ['p','h','note','equation']:story.append(par(z['text'],{'p':'body','h':'sub'}.get(kind,kind)))
            elif kind=='table':story += [make_table(z),Spacer(1,10)]
            elif kind=='architecture':story.append(ArchFlow())
            elif kind=='timeline':story.append(Timeline())
            elif kind=='hero':story.append(Hero(z['items']))
    out=HERE/'astra6_experiment_report.pdf'
    doc=SimpleDocTemplate(str(out),pagesize=A4,rightMargin=M,leftMargin=M,topMargin=43,bottomMargin=49,title=data['title'],author='Mathis Rost — research experiment documentation',subject='Architecture, explicit reasoning summaries, proofs, reviews, token and runtime accounting',pageCompression=1)
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    renderSVG.drawToFile(architecture(),str(HERE/'architecture.svg'))
    print(out)
if __name__=='__main__':main()
