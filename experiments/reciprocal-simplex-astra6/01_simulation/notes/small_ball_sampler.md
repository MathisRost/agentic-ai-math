# Exact law of the implemented independent small-ball samples

Let W=B(0,r), r=0.45, M=1. Distinct retained sphere surfaces are more than M
apart, and points in distinct correction clusters are more than M apart.
Since diam(W)<M, at most one retained sphere meets W, and at most one
correction cluster can emit points into W. The original whole-space process
can have many objects elsewhere; those are irrelevant to this restriction.

For any random object family with at most one member meeting W, its first
measure on meeting objects is a subprobability measure. The restricted law
is obtained by drawing this possible object with that measure, otherwise
using the empty object, and then drawing its conditional points. This follows
by applying the first-measure identity to any nonnegative test of one meeting
object: the sum has either zero or one term. It determines the full object
distribution, not merely the mean number of points in W.

## Sphere alternative

The first sphere measure is gamma(R) dz dR. A sphere of radius R meets W
precisely when max(0,R-r)<=|z|<=R+r (boundary cases have zero measure).
The code dominates this by the centre ball |z|<=R+r. Its total mass is

    p_* = (8pi F/(3L^4)) integral R(R+r)^3 exp(-4R^2/L^2) dR.

For each term c_j R^(j+1), j=0,1,2,3, in R(R+r)^3, set

    I_j=(1/2)(L^2/4)^((j+2)/2) Gamma((j+2)/2).

The radius proposal chooses j with probabilities proportional to c_j I_j,
then R^2~Gamma(shape=(j+2)/2,scale=L^2/4). The code uses c=(r^3,3r^2,3r,1).
Draw a candidate with probability p_* and its centre uniformly in B(0,R+r).
The resulting unnormalised joint measure is exactly gamma(R) dz dR on the
dominating centre domain. Rejecting |z|<R-r when R>r leaves exactly the
meeting-sphere subprobability measure. The empty alternative absorbs
enclosing/nonmeeting spheres. No sphere-band probability sum is truncated.

For d=|z|, a sphere wholly inside W has surface area 4pi R^2. A partial
intersection has area 2pi R^2(1-mu), where

    mu=(R^2+d^2-r^2)/(2Rd).

The cap points have direction cosine uniform in (mu,1) about -z/d and
uniform azimuth. Conditional on this sphere, the code samples the actual
Poisson count of mean a(R)/(2R) times this area, then all its points in W.

## Correction alternative

Only centres in D=B(0,r+1) can contribute. The original marked retained
centre process has first measure kappa dz times the mark law. Use the exact
augmented mark categories from the estimator derivation. Multiplying their
probabilities by kappa |D| gives candidate masses

    |D|(lambda_C-Q2), |D|Q2/2, |D|T/6, |D|T/2.

Their sum is less than one for the chosen parameters. Choose at most one
candidate category, its centre uniformly in D, and execute its mark
proposal/rejection. Restrict emitted points to W. The resulting measure on
nonempty cluster restrictions is exactly the first measure of original
clusters meeting W. By the at-most-one property this is the original
restricted law. It does not assume independent Matérn retained centres or
replace their spatial law outside W. Multiple nearby windows cannot be
sampled independently when a joint whole-space realisation is wanted.

Finally choose the sphere or correction alternative with one independent
fair coin for each of 5,000,000 realisations. All zero counts are saved.
The output contains seven singleton windows and no higher-order tuples.
Their lack of tuples motivates the separate weighted experiment, rather
than justifying a zero estimate of the nonzero theoretical correlations.

## Conditional illustration

The figure's sphere-cap illustration uses the regular conditional law given
a radius-2 sphere centred at (0,0,2), followed by conditioning its cap count
on N>=4. It is not included in the ordinary ensemble. Conditional Poisson
tail probabilities are computed by the recurrence p_(k+1)/p_k=m/(k+1),
normalised after a tail tolerance of 1e-16. This numerical truncation applies
only to the displayed conditional count draw, not to the ordinary process
law or to the quantitative tuple estimators. The actual draw has four points.
