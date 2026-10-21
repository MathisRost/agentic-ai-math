# What is sampled and what is estimated

This note derives the simulation estimator from the accepted v04 process law.
The computation is an importance-sampled factorial-tuple experiment. Its rows
are **not iid realisations of the whole-space process**, or points extracted
from one stationary realisation. They contain sampled point coordinates from
the conditional sphere Poisson factorial law and from the correction-cluster
mark law. Poisson count randomness is integrated out using its factorial
moment identity. No reciprocal-simplex density is evaluated to generate the
process observations. The reciprocal formula is used only in the independent
comparison calculation.

## Parameters and measurable bins

We take the accepted explicit parameter choice with M=1 and lambda=0.000006.
Thus lambda_C=lambda_Y=lambda, K=10^8 lambda^3/C_0^3 and L=1. All remaining
parameters follow equations (2)--(5), (30)--(35), (43) and (56) of v04.
The full-precision numerical parameters are in `data/results.json`.

For order n, anchor x_1=0 and write y=(x_2,...,x_n). Let H_{nj}(y) be the
indicator that every pair distance is below 1 and the simplex size Delta_n
is in the specified half-open bin. For n=4 also require the unique
circumsphere radius to be at most R_* = 2. The measured bins have strictly
positive lower edges. These are bounded, integrable **observables**, not
additional hypotheses or cutoffs on the constructed process. No small-radius
or large-radius modification is made to its law. For n=2,3 the sampled latent
sphere radius retains its full support (0,infinity).

The estimand is the uniform Lebesgue bin average

    gbar_nj = integral H_nj(y) rho_X^(n)(0,y) dy
              / [lambda^n integral H_nj(y) dy].

The reference prediction is (a_n/lambda^n) times the bin average of 1/Delta_n,
not the value at the bin midpoint. Isotropy of these local densities permits
geometric binning, but an isotropic whole-process law is not assumed.

This anchored reduced-coordinate estimand follows from stationarity: the
expected number of ordered tuples with x_1 in a set W, others unrestricted,
and relative geometry H equals |W| times the numerator. Consequently there
is no finite-window boundary correction to estimate. Sampling anchors from
a spatial window and silently discarding outside vertices would give a
different estimator; the code does not do that.

## Sphere factorial-tuple sampler

Put b(R)=a(R)/(2R), gamma(R)=2FR exp(-4R^2/L^2)/L^4, and

    S(R) = pi min(1,4R^2).

For a sphere through the origin, S(R) is the area of its cap inside B(0,1).
The first point integration in the sphere factorial measure gives

    integral H r_n
      = integral_0^infinity 4 pi R^2 gamma(R) b(R)^n S(R)^(n-1)
          E[H(0,X_2,...,X_n) | R] dR.                       (A)

Here the centre is R e with e uniform on S^2 and X_2,...,X_n are independent
uniform points in that cap. The factor 4 pi R^2 comes from integrating the
first point's surface measure over the centre: with x_1 fixed, centres lie
on a sphere of radius R about x_1. Equation (A) follows from Tonelli applied
to v04 equation (27), followed by this change of variables. It does not use
the evaluated reciprocal-simplex identities. Separation ensures these are
the full local factorial measures, including all eligible allocations.

The conditional Poisson identity E[(N)_n]=m^n says that directions of selected
ordered distinct Poisson points have precisely this product surface law.
Thus the generated tuples are samples of the actual conditional factorial
point law. The count N and unused Poisson points need not be generated.
This integration is the variance reduction in the experiment; it must not
be described as observed ordinary Poisson configurations. Equivalently, one
could add the independent Poisson background to the forced factorial-Palm
points and then discard it. We do not perform or count those unused draws.

To sample each cap point stably, draw d^2 uniform on (0,min(1,4R^2)), and an
independent uniform azimuth phi. In a tangent basis (e_1,e_2) orthogonal to e,

    X = [d^2/(2R)] e
        + sqrt(d^2-d^4/(4R^2)) (cos(phi)e_1+sin(phi)e_2).

The uniform-area law follows since the spherical area element is pi d(d^2).
The code samples and saves these Cartesian point coordinates; measured bins
are computed from their Euclidean distances, cross products and determinants.

The proposal densities for the latent radius are

    h_2(R) = (4R/L^2) exp(-2R^2/L^2),
    h_3(R) = 2/(L sqrt(pi)) exp(-R^2/L^2).

Dividing the integrand coefficient in (A) by these proposals gives

    W_2(R)=2 A_2 S(R),    W_3(R)=4 pi A_3 S(R)^2.            (B)

These weights are bounded, although the original fourth count moment is
infinite. Both proposals have infinite support; no Gaussian tail is cut off.

For four points the unique generating sphere is the circumsphere of the
sampled noncoplanar tuple. The observable's radius guard therefore allows
the exact restriction 0<R<=2 in (A), without omitting any mass of the
observable. Set Z=1/6+log(2R_*) and use

    h_4(R)=S(R)^3/[pi^3 Z R],  0<R<R_*.

It is a mixture: with probability (1/6)/Z take R=U^(1/6)/2; otherwise take
R=exp(U log(2R_*))/2. The importance weight is constant,

    W_4 = (pi^4 c/2) Z.                                    (C)

For n=2,3,4, a sphere row contributes W_n H_nj to its component's integral.
In particular the tetrahedral reciprocal volume is not inserted into this
empirical numerator. Four random point coordinates determine whether a row
contributes to a volume bin.

## Exact correction-cluster sampling without a numerical marginal

All formulas in this section are for M=1. Set epsilon=1/(2L) and

    J=integral_0^1 min(1,epsilon^2/r^2) dr=2epsilon-epsilon^2.

For u=d e with 0<d<1 and v=t e+r(cos(phi)e_1+sin(phi)e_2), define

    E(0,u,v) = 2A_3/(d r) min(1,epsilon^2/r^2)
                1{|t|<1,0<r<1,0<d<1}.

The proof's triangle bound gives q_3<=E everywhere: on the eligible domain
R_triangle<=1/(2r), and outside it q_3=0. Its exact mass is

    T=16 pi^2 A_3 J.

To sample E/T: draw d with density 2d on (0,1), e uniform on S^2, t uniform
on (-1,1), phi uniform on (0,2pi), and r with density
min(1,epsilon^2/r^2)/J. The last distribution is sampled by an explicit
uniform/inverse-power mixture. Accept with probability q_3/E, calculated as

    1{diam(0,u,v)<1}
       [1-exp(-|v|^2 |v-u|^2/(4r^2L^2))]
       /min(1,epsilon^2/r^2).

The accepted triples therefore have density q_3/Q_3, exactly the actual
three-point cluster mark law. The acceptance probability is Q_3/T; Q_3 is
not needed to execute the sampler. An accepted row contributes T H_3j to
the third-order integral. For the second-order integral, it contributes
T/3 times the sum of the three pair-bin indicators. Re-rooting symmetry
of q_3 shows each edge has the same integrated distribution, so this gives
the integral of (M q_3)H_2j. Keep the three terms in a single row when
computing its variance; they are not independent observations.

For pairs the exact anchored mass is

    Q_2=4pi{delta/2+A_2[1/2-L^2(1-exp(-1/(2L^2)))]}.

We first sample u from q_2/Q_2. This is elementary rejection from density
1/(2pi |u|) in B(0,1); the remaining radial factor has a finite known
upper bound. Given u, sample v from the cylindrical density h(v|u) above,
and accept the pair with probability

    1 - q_3(0,u,v)/[q_2(0,u)h(v|u)].                       (D)

The rejected probability is at most 1/2 because

    q_3/(q_2 h)
      <= 8pi A_3 J/[delta+A_2(1-exp(-d^2/(2L^2)))]
      <= JL/2 <=1/2.

Integration of the auxiliary v in (D) proves that the accepted u has
unnormalised density (q_2-Mq_3)/Q_2=F_2/Q_2. It is therefore the actual
two-point cluster mark law after conditioning on acceptance. An accepted
row contributes Q_2 H_2j. The auxiliary v is saved for audit; it is not
an emitted point of the accepted two-point cluster.

The local retained-parent intensity kappa and size-mark probabilities
Z_2/(2kappa),Q_3/(6kappa) cancel the ordered factors 2 and 6 to give F_2
and q_3. This is why the tuple estimator need not instantiate the dependent
Matérn parent process. It is not replacing those parents by independent
ones. Different clusters cannot contribute eligible tuples.

## Exact full-window algorithm, and its relation to this computation

For completeness the accepted model also gives an exact mathematical
algorithm for any bounded observation window W.

1. Flip the whole-law fair coin once. Never superpose both alternatives or
   flip a new coin for each point.
2. In the sphere alternative, draw the specified categorical band or empty
   alternative, then its uniform lattice shift and radial phase. Only
   lattice centres within distance b_k of W and candidate radii meeting W
   matter. Retain with t_k(R). For a ball W, each intersection is a spherical
   cap or a whole sphere; draw its Poisson count of mean b(R) times its area
   and independent uniform cap points. This requires only finitely many
   candidates for each realised finite band.
3. In the correction alternative, sample Poisson parents on W^{+4M}. Only
   parents in W^{+M} can emit a point into W; their full 3M neighbour test is
   visible in this halo. Retain them by the Matérn I empty-ball rule, sample
   their marks, emit offsets and finally restrict points to W.

Even the mark probabilities can be sampled without numerical Q_3 or F_2
normalisations. At a retained centre use the following disjoint candidate
categories, assigning all remaining probability and rejected candidates to
the empty mark:

* probability (lambda_C-Q_2)/kappa: emit the singleton;
* probability Q_2/(2kappa): propose a q_2/Q_2 pair and accept by (D);
* probability T/(6kappa): propose E/T and accept q_3/E; emit its triple;
* probability T/(2kappa): make the same kind of accepted proposal, but emit
  just the singleton.

These masses sum to at most one, because T<=2pi B_L<=Q_2/2 and lambda_C<=kappa.
Their accepted singleton, pair and triple probabilities are exactly
beta/kappa, Z_2/(2kappa), Q_3/(6kappa). This theoretical algorithm clarifies
what the variance-reduced cluster observations represent. The delivered
experiment does **not** claim to have run this full-window algorithm.

If W is a ball of radius below M/2, at most one retained sphere and at most
one correction cluster can meet it. Its mean point count is lambda|W|.
For radius 0.45 and the chosen lambda this is about 2.29e-6: ordinary empty
windows would dominate even an ensemble of hundreds of thousands. High-order
counts also have poor or infinite moments. This is the practical reason for
the explicitly weighted tuple experiment.

## Mixture, normalisation and uncertainty

Sphere, pair and triple proposal streams are independent. Let their sample
means be Y_nj, P_j and T_nj. The empirical full factorial integrals are

    I_2j=(Y_2j+P_j+T_2j)/2,
    I_3j=(Y_3j+T_3j)/2,
    I_4j=Y_4j/2.

These equal weights implement the whole-law mixture at the expectation
level, including both actual alternatives. There are no cross-component
tuples. The known prescribed lambda, not an estimated conditional
intensity from one nonergodic sample, is used in every denominator.

Independent reference streams draw each relative point uniformly in B(0,1).
Their row contributions to bin volume and reciprocal-simplex integral are
|B|^(n-1) H and |B|^(n-1) H/Delta. These are numerical integration samples,
not simulated process observations, and are labelled separately. The
numerator I is divided by the estimated bin volume to obtain gbar. The
theoretical bin average uses the same reference volume. The ratio of
empirical to theoretical bin averages consequently equals I divided by
a_n times the reference reciprocal-simplex integral; the common volume
cancels. The code propagates both process Monte Carlo variance and
independent reference integration variance. For the theoretical bin-average
error, it also includes the reference numerator/denominator covariance.

All process row contributions are bounded by (B), (C), Q_2 or T, and the
reference rows are bounded because each measured simplex bin has a positive
lower edge. Thus the independent-row CLT and ordinary delta-method standard
errors apply to this particular importance experiment despite the original
process's infinite fourth count moment. Error bars use +/-1.96 estimated
standard errors; they are approximate Monte Carlo intervals, not a claim
of exact finite-sample coverage, simultaneous coverage or theorem validation.
They quantify only the stated experiment and numerical integration.

## Checks and scope

Checks validate the accepted parameter inequalities and probability budget,
the spherical cap support, recovered four-point circumradii, and rejection
probability bounds. The independent reference integral is compared with
known one-dimensional pair integrals as a separate check. A short pilot
tested feasibility; the final fourth-order upper bin edge was set to 0.075
because near-maximal-volume tetrahedra were rare. Pilot observations are
not added to the final estimates. The final stream seeds and counts are
recorded explicitly. Re-running a seed is reproducibility, not replication.

Agreement in these finite bins does not establish the exact identities,
global absolute continuity, all intensity/diameter quantifiers, or the
divergence of the unguarded fourth integral. Those are mathematical results
of the proof. This experiment tests the implementation of the construction
and its local measure calculation. It does not compare with earthquake
catalogues and supports no ergodic or mixing claim.
