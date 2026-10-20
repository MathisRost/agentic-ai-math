"""Exact finite-window simulations of three stationary point-process models."""
import json
import math
import random

from build_point_process_teaching import (
    ASSETS, Diagram, ORANGE, contains, poisson_count, poisson_rectangle,
)

WINDOW = (0.0, 1.6, 0.0, 0.65)
INTENSITY = 20.0
POISSON_SEED = 20261028
CLUSTER_RATE, MEAN_OFFSPRING, CLUSTER_RADIUS = 4.0, 5.0, 0.10
HARD_RADIUS = 0.11
PROPOSAL_RATE = -math.log1p(-INTENSITY*math.pi*HARD_RADIUS**2)/(math.pi*HARD_RADIUS**2)


def expanded(bounds, distance):
    x0, x1, y0, y1 = bounds
    return (x0-distance, x1+distance, y0-distance, y1+distance)


def cluster_sample(seed):
    rng = random.Random(seed)
    # Compact support makes this buffer exact: no more distant parent can
    # contribute an offspring to WINDOW. Retain offspring only, not parents.
    parents = poisson_rectangle(rng, CLUSTER_RATE, expanded(WINDOW, CLUSTER_RADIUS))
    points = []
    for x, y in parents:
        for _ in range(poisson_count(rng, MEAN_OFFSPRING)):
            radius = CLUSTER_RADIUS*math.sqrt(rng.random())
            angle = 2*math.pi*rng.random()
            p = (x+radius*math.cos(angle), y+radius*math.sin(angle))
            if contains(WINDOW, p):
                points.append(p)
    return points


def hardcore_sample(seed):
    rng = random.Random(seed)
    proposals = poisson_rectangle(rng, PROPOSAL_RATE, expanded(WINDOW, HARD_RADIUS))
    marks = [rng.random() for _ in proposals]
    # Compare with ALL proposals, including rejected ones and the outer buffer.
    # This is Matérn II thinning, not sequential inhibition.
    retained = [p for i, p in enumerate(proposals)
                if contains(WINDOW, p)
                and all(i == j or marks[i] < marks[j]
                        or math.dist(p, q) >= HARD_RADIUS
                        for j, q in enumerate(proposals))]
    assert all(math.dist(p, q) >= HARD_RADIUS
               for i, p in enumerate(retained) for q in retained[i+1:])
    return retained


def main():
    clustered = cluster_sample(20261023)
    poisson = poisson_rectangle(random.Random(POISSON_SEED), INTENSITY, WINDOW)
    hardcore = hardcore_sample(20261024)
    assert math.isclose(CLUSTER_RATE*MEAN_OFFSPRING, INTENSITY)
    assert math.isclose((1-math.exp(-PROPOSAL_RATE*math.pi*HARD_RADIUS**2))
                        /(math.pi*HARD_RADIUS**2), INTENSITY)
    d = Diagram('point_process_patterns', 540, 800)
    panels = [
        ('g<sub>2</sub>(r) &gt; 1 for 0 &lt; r &lt; 2a', clustered),
        ('g<sub>2</sub>(r) = 1', poisson),
        ('g<sub>2</sub>(r) = 0 &lt; 1 for 0 &lt; r &lt; h', hardcore),
    ]
    for top, (formula, points) in zip((0, 270, 540), panels):
        # Plot with the same scale along both axes and the same window in all panels.
        left, y0, scale = 30, top+12, 300
        d.box(left, y0, 480, 195)
        for x, y in points:
            d.dot(left+scale*x, y0+scale*y, radius=4.7)
        d.text(formula, 0, top+215, 540, 42, 35, ORANGE, True, html=True)
    d.save()
    record = {
        'window': WINDOW, 'common_intensity': INTENSITY,
        'cluster': {'name': 'Matern cluster', 'seed': 20261023,
                    'parent_intensity': CLUSTER_RATE, 'mean_offspring': MEAN_OFFSPRING,
                    'disc_radius_a': CLUSTER_RADIUS, 'points': clustered,
                    'construction': 'Poisson parents; independent Poisson(mu) offspring uniform in radius-a discs; retain offspring only',
                    'g2': '1 + overlap_area_of_radius_a_discs(r)/(kappa*(pi*a^2)^2)',
                    'strict_inequality': 'g2(r)>1 for 0<r<2a; g2(r)=1 for r>=2a'},
        'poisson': {'seed': POISSON_SEED, 'points': poisson, 'g2': '1',
                    'selection': 'Illustrative seed selected to show more points at the same intensity'},
        'hardcore': {'name': 'Matern II', 'seed': 20261024, 'proposal_intensity': PROPOSAL_RATE,
                     'hard_distance_h': HARD_RADIUS, 'points': hardcore,
                     'construction': 'Poisson proposals with independent uniform marks; retain a point iff no proposal within h has a smaller mark',
                     'g2': '0 for 0<r<h; no claim of g2<1 at all distances',
                     'intensity': '(1-exp(-proposal_intensity*pi*h^2))/(pi*h^2)'},
        'simulation': 'Exact window restriction using finite support buffers; Poisson illustration resampled at the same intensity',
        'sources': [
            'https://leman.stat.vt.edu/VTCourses/BaddeleyPointProcesses.pdf#page=35',
            'https://search.r-project.org/CRAN/refmans/spatstat.random/html/rMatClust.html',
            'https://search.r-project.org/CRAN/refmans/spatstat.random/html/rMaternII.html',
        ],
    }
    (ASSETS.parent/'sources'/'point_process_examples.json').write_text(json.dumps(record, indent=2)+'\n')
    (ASSETS/'point_process_poisson_sample.json').write_text(json.dumps({
        'seed': POISSON_SEED, 'intensity': INTENSITY, 'window': WINDOW,
        'count': len(poisson), 'points': poisson,
        'method': 'Poisson count followed by independent uniform locations',
        'selection': 'Illustrative seed selected to show more points at the same intensity',
    }, indent=2)+'\n')
    print('Counts:', [len(p) for p in (clustered, poisson, hardcore)])
    print('Matérn II minimum distance:', min(math.dist(p, q) for i,p in enumerate(hardcore) for q in hardcore[i+1:]))


if __name__ == '__main__':
    main()
