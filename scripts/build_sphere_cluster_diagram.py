"""Editable schematic of the two alternative laws in proof_4, submission v04.

The sphere shows a selected tetrahedron among Poisson surface points. The
correction shows separated clusters of size at most three. Positions are
illustrative, not simulation output. A global coin chooses one whole law.
"""
from pathlib import Path
from math import cos, sin, pi, sqrt
import xml.etree.ElementTree as E

OUT = Path(__file__).resolve().parents[1] / 'assets' / 'sphere_cluster_mixture.drawio'
TEAL, ORANGE, INK, GREY = '#21736F', '#B16B24', '#252A2D', '#A7BFBC'
doc = E.Element('mxfile', host='app.diagrams.net')
diagram = E.SubElement(doc, 'diagram', name='Sphere and correction laws', id='sphere-cluster-mixture')
model = E.SubElement(diagram, 'mxGraphModel', grid='0', page='0',
                     pageWidth='760', pageHeight='320', background='#FFFFFF',
                     extFonts='Kalam^https://fonts.googleapis.com/css?family=Kalam:400,700')
root = E.SubElement(model, 'root')
E.SubElement(root, 'mxCell', id='0')
E.SubElement(root, 'mxCell', id='1', parent='0')
serial = 1


def vertex(value, x, y, w, h, style):
    global serial
    serial += 1
    cell = E.SubElement(root, 'mxCell', id=str(serial), parent='1', vertex='1', value=value, style=style)
    E.SubElement(cell, 'mxGeometry', x=str(x), y=str(y), width=str(w), height=str(h), **{'as': 'geometry'})


def text(value, x, y, w, h, size=27):
    vertex(value, x, y, w, h,
           f'text;html=0;whiteSpace=wrap;align=center;verticalAlign=middle;'
           f'fontFamily=Kalam;fontSize={size};fontColor={INK};strokeColor=none;fillColor=none;')


def path(points, color=TEAL, dashed=False, width=2.5, sketch=True):
    global serial
    serial += 1
    cell = E.SubElement(root, 'mxCell', id=str(serial), parent='1', edge='1',
                        style=f'edgeStyle=none;rounded=0;endArrow=none;'
                        f'sketch={int(sketch)};comic=0;jiggle=0.35;'
                        f'strokeWidth={width};strokeColor={color};dashed={int(dashed)};')
    geom = E.SubElement(cell, 'mxGeometry', relative='1', **{'as': 'geometry'})
    for p, role in [(points[0], 'sourcePoint'), (points[-1], 'targetPoint')]:
        E.SubElement(geom, 'mxPoint', x=str(p[0]), y=str(p[1]), **{'as': role})
    if len(points) > 2:
        array = E.SubElement(geom, 'Array', **{'as': 'points'})
        for x, y in points[1:-1]:
            E.SubElement(array, 'mxPoint', x=str(x), y=str(y))


def dot(x, y, color=TEAL, radius=5):
    vertex('', x-radius, y-radius, 2*radius, 2*radius,
           f'ellipse;strokeWidth=1;strokeColor={color};fillColor={color};')


# Invisible extent keeps labels and both examples on the same baseline.
vertex('', 0, 0, 760, 320, 'strokeColor=none;fillColor=none;')
cx, cy, radius = 185, 143, 118
vertex('', cx-radius, cy-radius, 2*radius, 2*radius,
       f'ellipse;sketch=1;comic=0;jiggle=0.5;strokeWidth=2.3;strokeColor={TEAL};fillColor=none;')

# Projected great circles, with the rear half of the equator dashed.
for start, stop, dashed in [(0, pi, False), (pi, 2*pi, True)]:
    path([(cx+radius*cos(start+(stop-start)*i/48),
           cy+0.29*radius*sin(start+(stop-start)*i/48)) for i in range(49)],
         GREY, dashed, 1.6, False)
path([(cx+0.34*radius*cos(2*pi*i/96), cy+radius*sin(2*pi*i/96)) for i in range(97)],
     GREY, True, 1.3, False)

# Every vertex is normalised in R^3 before orthographic projection. Orange
# points select one noncoplanar quadruple, not an imposed sphere population.
raw_vertices = [(0.03, 0.97, 0.24), (-0.92, -0.20, 0.34),
                (0.86, -0.27, 0.43), (0.05, -0.72, -0.69)]
unit_vertices = [tuple(t/sqrt(sum(v*v for v in p)) for t in p) for p in raw_vertices]
projected = [(cx+radius*x, cy-radius*y) for x, y, z in unit_vertices]
for i in range(3):
    path([projected[i], projected[3]], TEAL, True, 2.4)
for i, j in [(0, 1), (1, 2), (2, 0)]:
    path([projected[i], projected[j]], TEAL, False, 3)
for x, y in [(-0.47, 0.51), (0.46, 0.59), (-0.62, -0.55),
             (0.56, -0.61), (-0.17, 0.19), (0.39, -0.06)]:
    dot(cx+radius*x, cy-radius*y, radius=4)
for x, y in projected:
    dot(x, y, ORANGE, 6.5)
text('Process A', 25, 277, 320, 38)

# Distinct clusters are shown far apart; each orange point is its retained
# centre. Cluster sizes 0 and 1 are permitted as well as pairs and triangles.
clusters = [[(438, 66), (510, 98)],
            [(581, 187), (667, 140), (715, 222)],
            [(443, 213), (482, 244)],
            [(689, 54)]]
for points in clusters:
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            path([points[i], points[j]], '#6D9E98', False, 2.6)
    for i, (x, y) in enumerate(points):
        dot(x, y, ORANGE if i == 0 else TEAL, 6.5 if i == 0 else 5)
text('Process B', 410, 277, 330, 38)

E.indent(doc)
E.ElementTree(doc).write(OUT, encoding='utf-8', xml_declaration=True)
print(OUT)
