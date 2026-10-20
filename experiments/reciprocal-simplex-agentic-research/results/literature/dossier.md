# Literature dossier: exact reciprocal-simplex product densities

Date of check: 19 October 2026.  This dossier uses the frozen common snapshot for
run `20261019T114252Z_cox_rerun`.  It is a source-and-comparison record, not an
additional proof track.

## Outcome and scope

**Overall literature-check status: E.**  No source establishing the governing
target was located in the supplied collection or in the bounded wider search
described below.  Here E means only *no supporting result located within this
documented search*.  It does not mean that the statement is novel, that no proof
exists, or that the problem is known to be open.

The target checked is existence, for every prescribed admissible
`(lambda_0,M,h_3,h_4)`, of one stationary simple locally finite point process in
`R^3`, with intensity exactly `lambda_0`, finite local moments through order four
and absolutely continuous factorial moment measures through order four, whose
**full normalized factorial/product densities** obey

\[
g_2=C_2/D,\qquad g_3=C_3/A,\qquad g_4=C_4/V
\]

almost everywhere on the three finite physical domains in the frozen problem
statement.  In particular, the pair domain contains every `0<D<=M`; there is no
positive lower distance cutoff.  The triangle and tetrahedron domains impose
the stated absolute altitude cutoffs.  The constants `C_2,C_3,C_4` may depend on
the prescribed parameters but must be positive.  Approximation, connected
densities, equality only for same-cluster terms, a selected intensity, or a
strictly smaller domain does not settle this target.

The closest supplied results are both **D (partial)**:

- the local spherical Cox construction gives uniform relative approximation on
  the target-shaped finite domains at independently prescribed intensity, but
  not exact identities at any finite parameter choice;
- the local finite-cluster construction gives exact full identities, but has a
  positive pair cutoff and chooses a small intensity together with its
  amplitudes.  It is not presented as a Cox process.

The basic Cox moment identity, the Poisson-cluster partition formula and the
Hawkes cumulant formulas are **A** for the structural statements they actually
make; none is an existence theorem for the reciprocal-simplex target.  Two
restricted model classes can be excluded by short consequences of primary
formulas: ordinary log-Gaussian Cox processes and Hermitian determinantal point
processes are **C** class-specific nonmatches.  These exclusions do not apply to
general Cox processes or to general point processes.

## 1. Definitions and what the historical sources claim

### 1.1 Product densities are not factorial cumulants

For a simple point process `Phi`, the order-`n` factorial moment measure is

\[
\alpha^{(n)}(B_1\times\cdots\times B_n)
=\mathbb E\!\sum_{x_1,\ldots,x_n\in\Phi}^{\ne}
  \prod_{i=1}^n {\bf1}_{B_i}(x_i).
\]

When it is absolutely continuous its density is written `rho_n` here.  For a
stationary process of positive constant intensity `lambda`, the normalized full
product density is `g_n=rho_n/lambda^n`.  It includes tuples assembled from all
possible parents or clusters.  Factorial cumulant densities `c_n` are the
connected terms.  They are related by set partitions, not by equality.

For a stationary scalar-intensity process, with `c_1=lambda`, the formulas
through order four are

\[
\begin{aligned}
\rho_2(1,2)
 &=\lambda^2+c_2(1,2),\\
\rho_3(1,2,3)
 &=\lambda^3+\lambda\sum_{\{i,j\}\subset[3]}c_2(i,j)+c_3(1,2,3),\\
\rho_4(1,2,3,4)
 &=\lambda^4
   +\lambda^2\sum_{\{i,j\}\subset[4]}c_2(i,j)
   +\sum_{\{ij\}\mid\{k\ell\}}c_2(i,j)c_2(k,\ell)\\
 &\quad+\lambda\sum_{\{i,j,k\}\subset[4]}c_3(i,j,k)
   +c_4(1,2,3,4).
\end{aligned}
\]

The second sum in the last line has six pair terms, the pair-pair sum has three
pairings, and the third-order sum has four triples.  Thus the term counts are
`2,5,15` at orders `2,3,4`.  Jovanovic, Hertz and Rotter give the general
moment-cumulant partition identity in their equation (18) and then derive
Hawkes **cumulants**; Clark and Houssineau give the corresponding factorial
moment partition formula for cluster processes in Theorem 4.2, equation (21)
[@jovanovicHertzRotter2015; @clarkHoussineau2013].  Any proposed construction
must still include every displayed term.

### 1.2 The earthquake papers use conditional/full moments, not cumulants

The locally archived primary PDFs support the following narrower historical
claims.

- Kagan and Knopoff (1980) define and estimate a conditional two-point moment
  and normalize it by a Poisson catalogue; the source is explicitly
  three-dimensional as well as two-dimensional (printed p. 308, zero-based PDF
  index 5).  Their empirical discussion is compatible with a finite scaling
  range and does not assert a process-existence theorem (printed pp. 317--318,
  PDF indices 14--15) [@kaganKnopoff1980].
- Kagan (1981a) describes the empirical three-point ratio as approximately
  reciprocal to triangle area over a finite range (printed p. 697, PDF index
  0).  Equation (1) is a catalogue-to-Poisson-reference ratio (printed p. 699,
  PDF index 2).  The appendix explicitly distinguishes moments from cumulants:
  it writes the second- and third-order cumulant relations, notes that a Poisson
  process has vanishing higher cumulants but nonzero product moments, and says
  that the empirical analysis uses moments/conditional moments (printed
  pp. 715--717, PDF indices 18--20) [@kagan1981three].
- Kagan (1981b) reports an approximate reciprocal-volume four-point law
  (printed pp. 723 and 729, PDF indices 4 and 10).  It also observes that an
  unrestricted `1/H` height singularity is nonintegrable and introduces a
  positive height regularization (printed p. 730, PDF index 11)
  [@kagan1981four].
- Kagan's 2014 monograph again presents catalogue/reference `Q_k` statistics,
  separates measurement, scaling and boundary regimes, and summarizes the
  relations as approximate `1/D`, `1/S`, `1/V` laws (printed pp. 125--127,
  PDF indices 148--150) [@kagan2014].
- Daley and Vere-Jones, Volume II, Exercise 12.6.11, records the proposed
  second-, third- and fourth-order factorial moment density forms and asks about
  their compatibility with stationarity and approximate random-fault models
  (printed p. 249, PDF index 265) [@daleyVereJones2008].  An exercise posing a
  compatibility question is not a construction or nonexistence theorem, and
  its 2008 wording cannot establish present-day status.

These source readings support **A** for the historical occurrence and meaning
of the empirical reciprocal laws.  They do not support an exact continuum
existence result.

The corresponding frozen local files are
`common/papers/kagan_knopoff_1980_two_point.pdf`,
`common/papers/kagan_1981_three_point.pdf`,
`common/papers/kagan_1981_four_point.pdf`,
`common/papers/kagan_2014_earthquakes.pdf`, and
`common/papers/daley_vere_jones_2008_volume_ii.pdf`.

## 2. Poisson clusters

### 2.1 General existence and intensity

A stationary Poisson cluster process can be formed by a stationary Poisson
process of parents and translated iid finite cluster marks.  Last and Penrose,
Exercise 8.2, give the stationary construction and the intensity

\[
\lambda=\gamma\int \mu(\mathbb R^d)\,Q(d\mu)
\]

under the corresponding finite-mean assumption (author PDF p. 91, printed p.
80) [@lastPenrose2017].  For a bounded observation set `B`, finite local moments
through order four follow, for example, from integrability of the first four
cluster-count moments after accounting for all parents capable of reaching
`B`.  Bounded cluster size and bounded offsets are a simple sufficient regime.
Simplicity additionally requires that collisions have probability zero; this
must be checked from the mark law, not inferred from stationarity alone.

Last and Penrose, Exercises 9.10--9.12 (author PDF p. 102, printed pp. 91--92),
give the Poisson baseline plus a same-cluster contribution at second order.  In
particular the normalized pair density of an absolutely continuous Poisson
cluster model is at least one where the same-cluster term is nonnegative.  This
is a second-order fact only.  For the target pair law it would require
`C_2>=M` within the Poisson-cluster class.  Since `C_2` is not prescribed, that
is a constraint rather than an obstruction.

### 2.2 Complete factorial moment formulas, including dependent clusters

Clark and Houssineau do not assume iid daughters inside a cluster.  Their
Theorem 4.1, equation (19), composes the parent and conditional daughter
probability-generating functionals.  Theorem 4.2, equations (20)--(22), takes
the higher variations and sums over set partitions.  Equation (21) is the
factorial moment formula (publisher PDF p. 6, lines 591--645 in the checked text)
[@clarkHoussineau2013].  Consequently, internally dependent finite clusters are
legitimate, but full product densities still receive every multi-parent
partition.

For Poisson parents, let `q_r(x_1,...,x_r)` denote the integrated same-parent
ordered `r`-tuple density, equivalently the factorial cumulant density under the
usual integrability assumptions.  Then the formulas in section 1.1 apply.
Specifying `q_2=C_2/D`, `q_3=C_3/A`, or `q_4=C_4/V` does **not** specify the
required `rho_r`; the positive lower-order partitions remain.  Conversely, an
exact finite-cluster construction may solve the triangular inverse problem by
choosing same-parent kernels so that the complete sums, not just their leading
terms, equal the desired product densities.  The local finite-cluster
manuscript does exactly that on a restricted domain; see section 6.2.

### 2.3 What remains for the exact target

The structural literature reduces a Poisson-cluster attempt to a concrete
inverse problem: construct nonnegative cluster laws whose integrated
same-parent densities cancel or complement the partition contributions on all
three target domains, while retaining consistency under marginalization,
normalization, prescribed intensity, simplicity and finite local fourth
moments.  None of the checked general theorems supplies those nonnegative
kernels for the no-lower-cutoff pair domain and arbitrary prescribed intensity.

## 3. Cox processes

### 3.1 Directing-measure identity

Let `Lambda` be a locally finite random measure and, conditionally on `Lambda`,
let `Phi` be Poisson with intensity measure `Lambda`.  Last and Penrose equation
(13.10) states, for every `m`,

\[
\alpha_\Phi^{(m)}=\mathbb E\,\Lambda^{\otimes m}
\]

(author PDF p. 142, printed p. 131) [@lastPenrose2017].  Proposition 13.6,
equation (13.8), supplies the corresponding variance decomposition (author PDF
p. 141, printed p. 130).  Thus a Cox solution is precisely a random-measure
moment problem through order four, plus the required process properties.

The directing measure need not possess a Lebesgue density in each realization.
Random surfaces, lines or other singular carriers can average to absolutely
continuous `E Lambda^{\otimes m}`.  The spherical local construction is an
example.  What must be shown separately is:

1. `Lambda` is stationary and locally finite almost surely;
2. `Lambda` is diffuse almost surely, to make the conditional Poisson process
   simple;
3. `E Lambda(B)^4<infinity` for every bounded `B`;
4. `E Lambda^{\otimes m}` is absolutely continuous for `m=2,3,4`; and
5. its full densities, not one-carrier terms alone, equal the targets.

### 3.2 Prescribed intensity is removable inside the Cox class

**New short consequence of equation (13.10), not an explicit statement in the
source.**  Suppose a stationary Cox process directed by `Lambda` has positive
intensity `lambda` and already has the required normalized `g_2,g_3,g_4` on the
fixed physical domains.  For any prescribed `lambda_0>0`, set

\[
\Lambda'=(\lambda_0/\lambda)\Lambda.
\]

Then `E (Lambda')^{\otimes n}=(lambda_0/lambda)^n E Lambda^{\otimes n}`.
The intensity becomes `lambda_0`, while each normalized product density is
unchanged.  Stationarity, diffuseness and finite fourth local moments are
preserved.  Therefore, for the Cox approach specifically, finding one exact
positive-intensity directing measure for the given `(M,h_3,h_4)` automatically
solves every prescribed intensity.  This does not help a non-Cox construction,
and it does not construct the missing directing measure.

### 3.3 Necessary positivity and moment tests

For bounded `B`, put `L_B=Lambda(B)` and `mu_k=E L_B^k`.  Cox identities imply
`mu_k=alpha^{(k)}(B^k)`.  Since `L_B>=0`, the truncated Stieltjes moment matrices

\[
\begin{pmatrix}1&\mu_1&\mu_2\\
\mu_1&\mu_2&\mu_3\\
\mu_2&\mu_3&\mu_4\end{pmatrix}\succeq0,
\qquad
\begin{pmatrix}\mu_1&\mu_2\\\mu_2&\mu_3\end{pmatrix}\succeq0
\]

are necessary.  In particular `mu_2>=mu_1^2`,
`mu_1 mu_3>=mu_2^2`, and `mu_2 mu_4>=mu_3^2`.  More generally the covariance
kernel `rho_2-lambda^2` must be positive semidefinite as a bilinear form:

\[
\iint f(x)f(y)[\rho_2(x,y)-\lambda^2],dx,dy\ge0
\]

for bounded compactly supported real `f`.  These are elementary consequences
of nonnegative random variables and covariance, using the verified Cox moment
identity.  They are diagnostic necessary conditions, not sufficient ones.

There is one target-specific consequence.  If `B=B_R` is a ball with
`2R<=M`, the pair law fixes every off-diagonal pair in `B^2` and

\[
\mathbb E L_B^2
=\lambda^2 C_2\iint_{B_R^2}\frac{dx,dy}{|x-y|}.
\]

The elementary ball integral is
`32 pi^2 R^5/15`, while `|B_R|^2=16 pi^2 R^6/9`.  Jensen's inequality therefore
requires

\[
C_2\ge 5R/6,
\]

and choosing `R=M/2` gives `C_2>=5M/12` for any Cox solution.  Since `C_2` is
free and positive, this is not a contradiction.  Higher window-moment tests do
not close without knowing the densities on triangle and tetrahedron
configurations excluded by the altitude conditions.

### 3.4 Log-Gaussian Cox processes are too rigid

Møller, Syversveen and Waagepetersen Theorem 1 gives, for a stationary
log-Gaussian Cox process,

\[
\rho_n(x_1,\ldots,x_n)
=\lambda^n\prod_{i<j}g_2(x_i-x_j)
\]

(publisher/author PDF p. 7, equation (2)); the paper first identifies general
Cox product densities as moments of the random intensity on p. 6
[@mollerSyversveenWaagepetersen1998].

**New short consequence.**  On any target triangle with side lengths `a,b,c`,
the pair target forces

\[
g_3=\frac{C_2^3}{abc}=\frac{C_2^3}{4AR},
\]

where `R` is the circumradius and `abc=4AR`.  Equality with `C_3/A` would make
`R=C_2^3/(4C_3)` constant almost everywhere on the triangle domain.  Whenever
that domain has positive Lebesgue measure it contains shape families with
varying circumradius, so the simultaneous pair/triangle identities are
incompatible.  Independently, an ordinary finite-variance Gaussian field has
`|c(h)|<=c(0)=sigma^2`, hence its LGCP pair density
`g_2(h)=exp(c(h))` is bounded, whereas `C_2/D` diverges as `D` decreases to
zero.  Thus the no-lower-cutoff pair target alone excludes ordinary LGCPs,
including cases in which the triangle domain is vacuous.  This is status **C
for the LGCP subclass**, not for arbitrary Cox processes.

### 3.5 Shot-noise and random-carrier Cox models

Shot-noise Cox models are promising because one random carrier can produce
reciprocal Jacobians: intersections of spheres give `1/D`, `1/A`, `1/V`
factors in the local spherical manuscript.  But equation (13.10) expands the
entire random intensity moment.  With a Poisson population of carriers, tuples
may use one, two, three or four carriers, reproducing the complete partition
structure.  All terms are nonnegative before any specially designed dependence
is introduced.  Exactness therefore requires either carrier kernels whose full
moments already have the desired form, or a more structured dependent random
measure; isolating the common-carrier Jacobian is insufficient.

The generalised shot-noise Cox article by Møller (2003) was located only through
metadata/abstract in the archived dossier during this check; no theorem from it
is relied upon here [@moller2003].  Likewise the line-based Cox citation of
Gloaguen, Voss and Schmidt is useful model context, but it was not inspected as
a decisive full-text theorem and is not used to infer exact higher moments
[@vossGloaguenSchmidt2013].

## 4. Hawkes and ETAS processes

### 4.1 Stationarity and the branching representation

A linear Hawkes process can be represented as a Poisson cluster process of
immigrants and descendants.  The stability hypothesis in the checked
multivariate source is that the spectral radius of the matrix of kernel masses
is less than one.  Jovanovic, Hertz and Rotter equations (13)--(15) give the
stationary mean rate under that condition; equations (37) and (39) give the
second- and third-order cumulant densities, and the fourth order requires 26
family-tree terms (arXiv:1409.5353, pp. 3, 6--7) [@jovanovicHertzRotter2015].
Their equation (18) is the set-partition conversion from cumulants to full
moments.  Thus Hawkes tree diagrams cannot be substituted directly for `g_n`.

Hawkes and Oakes (1974) was accessible here only at abstract/metadata level;
its Poisson-cluster attribution is recorded but no delicate hypothesis is taken
from uninspected full text [@hawkesOakes1974].  Ogata's 1998 space-time ETAS
paper gives primary model and observation context (opening and model pages of
the official full PDF were checked), but it does not establish the spatial
reciprocal-simplex identities [@ogata1998].

### 4.2 Space-time versus the required spatial process

The common Hawkes/ETAS sources concern time or space-time event processes.  A
spatial catalogue obtained by retaining events in a time window, projecting
away time, or taking a stationary temporal limit has spatial factorial moment
measures obtained by integrating the **full space-time** product densities over
all time coordinates.  The operation depends on observation-window and
boundary conventions.  No checked source shows that these integrals are
exactly reciprocal distance, area and volume simultaneously on the prescribed
three-dimensional domains.  Branching subcriticality alone also does not prove
the required spatial absolute continuity or the fourth local moment after
projection.  The Hawkes approach is therefore **D (structurally relevant but
not a target result)** in this search.

## 5. Other constructions, realizability and obstructions

### 5.1 Pair and low-order realizability theorems

Kuna, Lebowitz and Speer (2007), Theorem 3.1, gives a low-density sufficient
condition for realizing a specified pair function under integrability and a
stability condition; section 4 discusses adding a specified triplet modifier
(arXiv:math-ph/0612075, pp. 7 and 12--15) [@kunaLebowitzSpeer2007].  It does not
construct simultaneous prescribed full correlations through order four.

Kuna, Lebowitz and Speer (2011) gives necessary and sufficient realizability
conditions for prescribed first and second moment measures, with additional
moment-control results including finite local third moments; see Theorem 3.20
and the stationary discussion (arXiv:0910.1710) [@kunaLebowitzSpeer2011].  This
does not provide a ready four-order extension for the current target.
Caglioti, Kuna, Lebowitz and Speer (2006) explicitly frames specified low-order
correlations and gives partial results, again without the present exact
four-order theorem [@cagliotiEtAl2006].  All three are **D** for this target.

### 5.2 Gibbs processes

Dereudre, Drouilhet and Georgii prove existence of stationary Gibbs point
processes for broad geometry-dependent hyperedge interactions under their
finite-horizon, stability and confinement hypotheses; the paper includes
Delaunay edges and triangles (arXiv:1003.2875, abstract and Theorems 3.2--3.3)
[@dereudreDrouilhetGeorgii2012].  Jansen develops convergent activity expansions
for factorial moment and factorial cumulant densities of repulsive pairwise
Gibbs processes under a small-activity criterion (arXiv:1807.10725, Theorems
2.3--2.6) [@jansen2019].  These results show that geometric interactions can be
made into processes and that their correlations can be expanded.  They do not
identify a Boltzmann factor with a correlation function, nor do they invert the
correlation hierarchy to give exact `1/D,1/A,1/V` full densities.  Gibbs methods
are **D**, not a solved approach.

### 5.3 Determinantal processes

For a Hermitian determinantal process,
`rho_n(x_1,...,x_n)=det[K(x_i,x_j)]`.  Soshnikov writes the determinant formula
in equations (1.4) and (1.11) and states the operator existence condition in
Remark 4 (publisher PDF pp. 1--2 and 7) [@soshnikov2000].  At second order,

\[
\rho_2(x,y)=K(x,x)K(y,y)-|K(x,y)|^2\le K(x,x)K(y,y).
\]

For a stationary process of intensity `lambda`, this gives `g_2<=1` almost
everywhere.  Since `C_2/D` exceeds one for all sufficiently small positive `D`
and the target pair domain has no lower cutoff, no Hermitian determinantal point
process can meet the target.  This is a direct **C** class exclusion; it says
nothing about permanental or general point processes.

### 5.4 Geometric integrability and finite-range qualifications

- The singularity `1/D` is locally integrable in three dimensions near the pair
  diagonal: the radial volume element contributes `D^2 dD`.  The absence of a
  lower pair cutoff is therefore not by itself inconsistent with finite second
  local moments.
- An unrestricted `1/V` lower bound on all bounded-diameter tetrahedra is not
  locally integrable near a full-dimensional family of flat configurations.
  Writing the fourth vertex height as `t` gives `V` proportional to `|t|` and an
  integral containing `int dt/|t|`.  The current target explicitly assumes a
  positive absolute tetrahedral altitude cutoff `h_4`, so that obstruction does
  not apply.
- Decay like `1/D`, `1/A` or `1/V` on all sufficiently large separated shapes
  can conflict with occupancy/variance inequalities.  The current laws are
  required only up to finite diameter `M`, so infinite-range obstructions do not
  apply.
- Correlations outside the specified domains are free.  Spectral, variance or
  truncated-moment arguments must not silently extend the target formulas to
  excluded configurations.

These points are proved in detail in the frozen local finite-cluster manuscript
and its mathematical audit.  They delimit nonexistence arguments but do not
settle the current finite, altitude-truncated problem.

## 6. Prior local work

### 6.1 Spherical Cox manuscript: prescribed intensity, approximate laws

The complete frozen source tree at
`common/prior_work/reciprocal-simplex/` was inspected, including `main.tex`, all
eight included section files, the bibliography, source notes, mathematical
check, writing state and simulation reports.  The construction uses Poisson
sphere parents `(c,r)` of intensity `tau r dc dr`, `0<r<L`, and conditional
Poisson offspring on each sphere with surface intensity `(beta/r) H^2`.  It is a
stationary isotropic Cox process with

\[
\rho=(4\pi/3)\tau\beta L^3.
\]

Its integrated common-sphere terms are

\[
\begin{aligned}
q_2&=\pi\tau\beta^2\frac{L^2-D^2/4}{D}{\bf1}_{D<2L},\\
q_3&=\tau\beta^3\frac{\sqrt{L^2-R_3^2}}{A}{\bf1}_{R_3<L},\\
q_4&=\frac{\tau\beta^4}{6V}{\bf1}_{R_4<L}.
\end{aligned}
\]

Here `R_3,R_4` are the relevant circumsphere radii.  The full product densities
are exactly the partition sums in section 1.1: `rho^2+q_2` at order two;
`rho^3+rho sum q_2+q_3` at order three; and all 15 terms at order four.
Thus even the exact `q_4` carrier term is not the full `rho_4`.

The manuscript's Theorem 5.3 says that for every finite geometry domain,
prescribed `rho_0>0` and every `epsilon>0`, parameters can be chosen so that all
three full normalized product densities are uniformly relatively close to
reciprocal laws.  Large `L`, small `zeta=tau L^4 M` and `beta` restoring `rho_0`
control curvature and multi-parent terms.  The theorem does not give equality
for `epsilon=0`, and no finite parameter choice removes the `D^2/(4L^2)` and
`R_j^2/L^2` curvature while also eliminating every lower partition.  No proved
weak-limit passage produces a nondegenerate locally finite exact process.

Comparison with the governing target:

| Aspect | Governing target | Spherical Cox manuscript | Status |
|---|---|---|---|
| Intensity | arbitrary prescribed `lambda_0` | independently prescribed | match |
| Pair domain | all `0<D<=M` | uniform approximation includes this range | domain match, equality mismatch |
| Orders 2--4 | exact full `g_n` | exact formulas, reciprocal only within positive relative error | mismatch |
| One process | yes | yes | match |
| Moments/simplicity/AC | required through 4 | established, in fact stronger local exponential control | match |

The manuscript is therefore a strong **D**, not an exact construction.  Its
Monte Carlo studies check the stated spherical model and explicitly label the
reciprocal curves as approximations; they provide no continuum equality.

### 6.2 Finite-cluster manuscript: exact laws, smaller domain and selected intensity

The complete frozen source tree at
`common/prior_work/finite-cluster-reciprocal-laws/` was inspected, including
`main.tex`, every included section and appendix, bibliography, writing state,
literature check, mathematical audits and simulation report.  It constructs a
stationary isotropic simple Poisson superposition of dependent finite clusters
of sizes at most four.  Recursive residual kernels are chosen as

\[
F_4=q_4,\qquad F_3=q_3-\mathcal Mq_4,\qquad
F_2=q_2-\mathcal Mq_3+\tfrac12\mathcal M^2q_4,
\]

with quantitative bounds ensuring nonnegativity.  Full parent partitions then
cancel to the desired full densities.  This is genuinely exact and not merely
a same-parent statement.

Its compatible domains, however, require

\[
0<\delta\le h\le H<\sqrt{2/3}M,\qquad M\le P,
\]

and the pair law only on `delta<=D<=P`.  The construction selects amplitudes and
intensity jointly:

\[
a_2=a,\quad a_3=a/(4B),\quad a_4=a/(16BC),\quad
\rho=a I,\quad I=2\pi(P^2-\delta^2),
\]

with `a` sufficiently small for positivity.  Thus it neither covers arbitrarily
small positive pair distances nor realizes an independently prescribed
`lambda_0` over the whole positive range.  For fixed compatible domains it does
realize a geometry-dependent interval of sufficiently small positive
intensities; the explicit numerical witness is extremely sparse.  Spatial
rescaling would also rescale the physical domains.  Independent thinning
preserves normalized product densities but only lowers intensity; it cannot
reach arbitrary larger `lambda_0` or fill the missing range `0<D<delta`.
Neither operation supplies the missing bridge.  The manuscript does not
identify its process as Cox.

Comparison with the governing target:

| Aspect | Governing target | Finite-cluster manuscript | Status |
|---|---|---|---|
| Pair lower cutoff | none | `delta>0` | mismatch |
| Intensity | arbitrary prescribed `lambda_0` | selected small `rho=aI` | mismatch |
| Orders 2--4 | exact full `g_n` | exact full `g_n` on its supports | match on smaller domain |
| Process properties | stationary, simple, finite moments, AC | established | match |

This is **D**, and it is the closest exact local result.  The retained
simulation is only a sampler/count diagnostic; its superseded buggy pilot is
explicitly withdrawn and was not used as evidence.

## 7. Compact approach-to-source map

| Approach | Load first | Exact source location | What it supplies / warning |
|---|---|---|---|
| 1. Poisson clusters | Clark--Houssineau; Last--Penrose | Thm. 4.1--4.2, eqs. (19)--(22); Ex. 8.2 and 9.10--9.12 | General dependent-cluster partition calculus, stationarity and intensity. Must solve nonnegative inverse kernels and keep all partitions. |
| 2. Cox | Last--Penrose; local spherical manuscript; LGCP paper | Eq. (13.10), Prop. 13.6; local Sections 3--5; LGCP Thm. 1 eq. (2) | Directing-measure moment problem; singular carriers allowed after averaging. Intensity rescaling is available. Ordinary LGCP subclass is excluded by its pair-product hierarchy. |
| 3. Hawkes | Jovanovic--Hertz--Rotter | eqs. (13)--(18), (37), (39), fourth-order discussion | Stationary branching and cumulant trees. Convert to full products and justify spatial projection. |
| 4. Agent-selected | KLS; Dereudre et al.; Jansen; Soshnikov | KLS Thm. 3.1/Prop. 4.1; Gibbs existence Thms. 3.2--3.3; Jansen Thms. 2.3--2.6; DPP determinant formula | Pair/triplet realizability and Gibbs expansions are partial. Hermitian DPPs fail already at `g_2`. |
| 5. Necessary conditions | Last--Penrose; KLS 2011; local obstruction appendix | Cox eq. (13.10); KLS Thm. 3.20; finite-cluster appendices | Window moment matrices, covariance positivity and general realizability tests. Do not assume target formulas outside their finite domains. |

## 8. Source status and search coverage

### Fully checked primary sources used for mathematical claims

- Last and Penrose, *Lectures on the Poisson Process* (2017 author PDF):
  Exercises 8.2 and 9.10--9.12; Proposition 13.6; equation (13.10).
- Clark and Houssineau, *Faà di Bruno's formula and spatial cluster
  modelling* (2013 publisher PDF): Theorems 4.1--4.2, equations (19)--(22).
- Møller, Syversveen and Waagepetersen, *Log Gaussian Cox Processes* (1998
  full PDF): Theorem 1, equations (1)--(4).
- Jovanovic, Hertz and Rotter, *Cumulants of Hawkes point processes* (2015
  arXiv/publisher text): stability and mean-rate equations, moment-cumulant
  conversion, and second- through fourth-order cumulant formulas.
- Kuna, Lebowitz and Speer (2007, 2011): relevant theorem statements and
  surrounding hypotheses in the full arXiv texts.
- Dereudre, Drouilhet and Georgii (2012) and Jansen (2019): full arXiv texts for
  the cited existence/expansion scope.
- Soshnikov (2000): full PDF for the determinant definition and operator
  condition.
- The archived Kagan, Kagan--Knopoff and Daley--Vere-Jones PDFs at the printed
  pages listed in section 1.2.

The theorem statements and relevant surrounding assumptions were checked; this
was not a line-by-line audit of every published proof.

### Metadata-only or incompletely checked sources

- Hawkes and Oakes (1974): abstract/metadata accessible; no uninspected theorem
  hypothesis is used.
- Møller (2003), *Shot noise Cox processes*: metadata/abstract-level relevance
  only in this check.
- Voss, Gloaguen and Schmidt (2013), line-based Cox chapter: bibliographic/model
  context only.
- Kagan and Vere-Jones (1996) was present in the local bibliography but was not
  needed for a decisive claim and was not rechecked in full.
- Permanental Cox processes and non-Gaussian transformed-intensity subclasses
  were not exhaustively surveyed.  No conclusion about them is drawn.

### Search procedure and limits

The controlled collection consisted of the frozen common literature dossiers,
definition audit, all five approach briefs, the primary PDFs indexed under
`common/papers/`, and both complete local manuscript source trees.  Wider search
used two targeted semantic-query batches (exact simultaneous reciprocal-simplex
correlations; Cox random-measure moment/realizability) and targeted primary-web
checks for the principal structural papers.  Search results recovered the KLS
realizability papers, Cox/LGCP identities, cluster partitions, Gibbs existence
and expansion papers, and determinantal formulas, but no exact theorem matching
all target quantifiers.  The search stopped after those relevant full-text
candidates were compared because further hits were generic point-process or
empirical-model papers.  The non-discovery verdict is therefore bounded, not a
global priority or openness claim.

All bibliographic entries cited here are in `references.bib`.  Remaining
mathematical/source questions that could change an approach are separated in
`open_questions.md`.
