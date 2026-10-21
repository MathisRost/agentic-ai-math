"""Editable Poisson samples with fixed disjoint regions for factorial moments."""
import json
import random

from build_point_process_teaching import (
    ASSETS, Diagram, TEAL, ORANGE, contains, poisson_rectangle,
)


def main():
    bounds = (0, 1.6, 0, 1.0)
    intensity = 35
    pairs = [(0.46, 0.74, 0.35, 0.63), (0.79, 1.07, 0.35, 0.63)]
    six = [(x, x+0.30, y, y+0.25)
           for y in (0.12, 0.62) for x in (0.12, 0.65, 1.18)]
    d = Diagram('factorial_moment_regions', 540, 860)
    records = []
    for top, title, regions, seed in [
        (0, 'Two nearby regions', pairs, 2026102101),
        (435, 'Six disjoint regions', six, 2026102102),
    ]:
        # Set regions before sampling; no conditioning on their point counts.
        for i, a in enumerate(regions):
            for b in regions[i+1:]:
                assert a[1] <= b[0] or b[1] <= a[0] or a[3] <= b[2] or b[3] <= a[2]
        points = poisson_rectangle(random.Random(seed), intensity, bounds)
        left, y0, scale = 30, top+58, 300
        d.text(title, 0, top, 540, 45, 34, TEAL, True)
        d.box(left, y0, 480, 300)
        for i, (x0, x1, bottom, upper) in enumerate(regions):
            color = TEAL if i % 2 == 0 else ORANGE
            fill = '#D2E6E2' if i % 2 == 0 else '#F1E3D2'
            d.box(left+x0*scale, y0+bottom*scale,
                  (x1-x0)*scale, (upper-bottom)*scale, color, fill, True)
        for x, y in points:
            index = next((i for i, b in enumerate(regions) if contains(b, (x, y))), None)
            color = '#626A70' if index is None else TEAL if index % 2 == 0 else ORANGE
            d.dot(left+scale*x, y0+scale*y, color, radius=4.5)
        for i, (x0, x1, bottom, upper) in enumerate(regions):
            color = TEAL if i % 2 == 0 else ORANGE
            # Place each label inside its region without obscuring sampled points.
            positions = [(x, y) for y in (bottom+.065, bottom+.125, upper-.065)
                         for x in ((x0+x1)/2, x0+.105, x1-.105)]
            label_x, label_y = next((x, y) for x, y in positions
                                   if not any(abs(x-px) < .105 and abs(y-py) < .065
                                              for px, py in points))
            d.vertex(f'B<sub>{i+1}</sub>', left+label_x*scale-27,
                     y0+label_y*scale-17.5, 54, 35,
                     'text;html=1;whiteSpace=wrap;align=center;verticalAlign=middle;'
                     f'fontFamily=Kalam;fontSize=30;fontStyle=1;fontColor={color};'
                     'strokeColor=none;fillColor=#FFFFFF;spacing=0;')
        records.append({'seed': seed, 'regions': regions, 'points': points,
                        'counts': [sum(contains(b, p) for p in points) for b in regions]})
    d.save()
    (ASSETS/'factorial_moment_regions_samples.json').write_text(json.dumps({
        'window': bounds, 'intensity': intensity,
        'method': 'Poisson count followed by independent uniform locations; fixed regions',
        'samples': records,
    }, indent=2)+'\n')
    print('Factorial moment regions:', [(len(r['points']), r['counts']) for r in records])


if __name__ == '__main__':
    main()
