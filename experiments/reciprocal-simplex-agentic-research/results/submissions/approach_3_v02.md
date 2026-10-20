# Approach 3 — submission v02

- Run / model / reasoning: `20261019T114252Z_cox_rerun` / `gpt-5.6-sol` / `xhigh`.
- Problem snapshot SHA-256: `4c7a8b0ec361395179d7c6131e53b61bd312e028e552baa1a98fe6dc16eea84a`.
- Context packet and source dossier version: `context_packets/proof_3_v02.md`, SHA-256 `7173641df170328470650ab5ed5bcd8a9359aff21c94c58da42f1d0cb33694d3`; `shared_literature/dossier.md`, SHA-256 `5d42ad11b6b55246e6a0eb098b3f09c1bf3751cd3add4a819f5e427017b659f5`.
- Claim status: **scoped obstruction for regular scalar linear Hawkes processes; exact target unresolved outside that class**.

## Claim and scope

The governing question quantifies over every prescribed admissible tuple

\[
(\lambda _0,M,h_3,h_4),\qquad \lambda _0,M,h_3,h_4>0,
\]

with nonempty triangle and tetrahedron domains of positive Lebesgue measure. It
asks for one stationary simple point process on all of \(\mathbb R^3\), of
intensity exactly \(\lambda _0\), with finite local count moments and absolutely
continuous factorial moment measures through order four, and positive constants
\(C_2,C_3,C_4\) such that the full normalised densities satisfy

\[
g_2=\frac{C_2}{D},\qquad g_3=\frac{C_3}{A},\qquad
g_4=\frac{C_4}{V}
\]

almost everywhere on the complete domains \(\mathcal D_2,\mathcal D_3,
\mathcal D_4\) in the frozen problem. In particular, \(\mathcal D_2\) contains
every \(0<D\le M\); there is no positive lower pair-distance cutoff.

This submission proves only the following restricted negative theorem.

**Theorem 1 (bounded-kernel Hawkes obstruction).** Fix any \(T>0\),
\(\lambda _0>0\) and \(M>0\). Let \(N\) be a stationary scalar linear Hawkes
process on space--time \(E=\mathbb R\times\mathbb R^3\), with a homogeneous
immigrant rate and a nonnegative causal triggering density

\[
\phi\in L^1(E)\cap L^\infty(E),\qquad
\eta:=\int_E\phi(z)\,dz<1.
\]

Project the events in a finite time interval \(I\) of length \(T\) to
\(\mathbb R^3\), and choose the immigrant rate so that the projected process
has the prescribed intensity \(\lambda _0\). Its spatial pair correlation is
uniformly bounded off the diagonal. Consequently it cannot satisfy

\[
g_2(x_1,x_2)=C_2/\|x_2-x_1\|
\]

almost everywhere for all \(0<\|x_2-x_1\|\le M\), for any \(C_2>0\). It
therefore cannot satisfy the three governing identities simultaneously.

The theorem applies at every prescribed \(\lambda _0,M,h_3,h_4\), but only to
the stated scalar, linear, subcritical, \(L^1\cap L^\infty\) Hawkes subclass.
Singular kernels, marked or multitype Hawkes processes, random-carrier
triggering, nonlinear Hawkes processes, critical no-ancestor models, and
arbitrary point processes remain unresolved. Nothing below is a non-existence
theorem for those classes.

Before imposing \(L^\infty\), I derive the exact factorial-cumulant measures and
the **full product-density** hierarchy through order four for a subcritical
scalar space--time Hawkes process and its finite-time spatial projection. This
also gives necessary residual inequalities for any singular scalar linear
Hawkes candidate.

## Relation to prior work

1. The frozen spherical Cox manuscript,
   `common/prior_work/reciprocal-simplex/`, constructs a stationary process at
   an independently prescribed intensity and derives all parent partitions.
   Its Sections 3--5 give exact formulas but only uniform relative
   approximation to the reciprocal laws. Its common-sphere terms have
   curvature factors at orders two and three, and its full densities retain
   the positive disconnected partitions. It does not give exact equality at a
   finite parameter choice.

2. The frozen finite-cluster manuscript,
   `common/prior_work/finite-cluster-reciprocal-laws/`, gives exact full
   identities by a triangular residual-kernel construction. Its theorem has a
   positive lower pair cutoff and selects a small intensity jointly with the
   amplitudes. It is therefore an exact benchmark on a smaller domain, not a
   solution of the prescribed-intensity, no-pair-cutoff target.

3. Jovanović, Hertz and Rotter derive Hawkes cumulant tree formulas and the
   moment--cumulant partition identity. Their equation (37) is the second
   cumulant formula, equation (39) gives the four third-order rooted
   topologies, and their fourth-order construction has 26 rooted tree terms.
   Those connected terms are not the requested \(\rho^{(n)}\); the
   set-partition conversion in their equation (18) is essential.

4. The local Kagan fault-model PDF was inspected at printed pp. 659--665. It
   proposes a critical or slightly subcritical branching simulation in time,
   space and orientation. Each event has Poisson offspring, and spatial and
   orientational increments are attached along the family tree. It does not
   provide a homogeneous immigrant construction on all space--time, a
   stationary finite-intensity spatial projection, or exact full factorial
   densities through order four.

5. The frozen geometry-alternatives note reports an approximate
   sphere-triggered Hawkes candidate on a six-year projection. The result is
   approximate and does not resolve the exact inverse problem considered here.

The contribution here is the self-contained finite-window construction, the
measure-to-density justification, the full hierarchy, and the bounded-kernel
obstruction. I do not claim that the Hawkes cluster recursion itself is new.

## Process and existence

### 1. Stationary space--time process and total progeny

Write a space--time location as \(z=(t,x)\in E\), with Lebesgue measure
\(dz=dt\,dx\). Let \(\phi:E\to[0,\infty)\) be measurable, supported on
\(\{t>0\}\), and satisfy

\[
\eta=\int_E\phi(z)\,dz<1.
\]

Immigrants form a homogeneous Poisson process on \(E\) of rate \(\mu>0\).
Every event at \(u\) independently produces a Poisson process of children with
intensity \(\phi(v-u)\,dv\); children reproduce by the same rule. Thus each
immigrant generates a Poisson Galton--Watson cluster with mean offspring number
\(\eta\). The total progeny \(S\), including the immigrant, is finite almost
surely.

We need more than almost-sure finiteness. Let \(F(s)=\mathbb E[s^S]\). Its
branching equation is

\[
F(s)=s\exp\{\eta(F(s)-1)\}.                                  \tag{1}
\]

For \(0<\eta<1\), Lagrange inversion gives the Borel probabilities

\[
\mathbb P(S=n)=\frac{e^{-\eta n}(\eta n)^{n-1}}{n!},
\qquad n\ge1.                                                  \tag{2}
\]

Stirling's formula shows that the power series in (1) has radius

\[
R=\frac{e^{\eta-1}}{\eta}>1,
\]

because \(\log R=\eta-1-\log\eta>0\) for \(0<\eta<1\). Hence
\(\mathbb E e^{\theta S}<\infty\) whenever \(1<e^\theta<R\). If \(\eta=0\),
then \(S=1\). In either case

\[
\mathbb E S^r<\infty\quad\hbox{for every fixed }r,
\qquad\text{in particular }\mathbb E S^4<\infty.              \tag{3}
\]

Superposing the translated clusters gives the stationary causal Hawkes process
\(N\), whose space--time intensity is

\[
\nu=\frac{\mu}{1-\eta}.                                      \tag{4}
\]

The construction is simple because immigrant locations and every offspring
displacement have densities. We next verify the required local fourth moment.
For a bounded Borel set \(W\subset E\), write one relative cluster as
\(C=\{Y_1,\ldots,Y_S\}\) and put

\[
C_u(W)=\sum_{j=1}^{S}\mathbf 1\{u+Y_j\in W\}.
\]

For every integer \(r\ge1\), pathwise expansion gives

\[
\begin{aligned}
\int_E C_u(W)^r\,du
&=\sum_{j_1,\ldots,j_r=1}^{S}
  \left|\bigcap_{\ell=1}^r(W-Y_{j_\ell})\right|\\
&\le |W|S^r.                                                   \tag{5}
\end{aligned}
\]

This also justifies the Poisson-cluster cumulant calculation rather than merely
asserting it. For sufficiently small \(\theta>0\),

\[
\int_E\mathbb E\!\left[e^{\theta C_u(W)}-1\right]du
\le \theta |W|\,\mathbb E\!\left[S e^{\theta S}\right]<\infty,
\]

where we used \(e^{\theta k}-1\le\theta k e^{\theta k}\), (5) with
\(r=1\), and the exponential moment above. The exponential formula for the
marked Poisson immigrant process therefore gives

\[
\log\mathbb E e^{\theta N(W)}
=\mu\int_E\left(\mathbb E e^{\theta C_u(W)}-1\right)du.
\]

For \(1\le r\le4\), after reducing \(\theta\) if necessary,

\[
\int_E C_u(W)^r e^{\theta C_u(W)}\,du
\le |W|S^r e^{\theta S},
\qquad
\mathbb E[S^r e^{\theta S}]<\infty.
\]

Differentiating at zero under this integrable domination,
the ordinary cumulants satisfy

\[
\kappa_r(N(W))=\mu\int_E\mathbb E[C_u(W)^r]\,du
\le \mu|W|\mathbb E S^r,
\qquad 1\le r\le4.                                            \tag{6}
\]

Thus \(N(W)\) has a finite fourth moment; explicitly,

\[
\mathbb E N(W)^4
=\kappa_4+4\kappa_3\kappa_1+3\kappa_2^2
 +6\kappa_2\kappa_1^2+\kappa_1^4<\infty.                     \tag{7}
\]

In particular, \(N\) is locally finite.

### 2. Finite-time spatial projection and prescribed intensity

Fix a bounded interval \(I\subset\mathbb R\) of length \(T>0\), and define

\[
X_I(B):=N(I\times B),\qquad B\subset\mathbb R^3.
\]

This is the spatial catalogue of events occurring during \(I\), with their
times discarded. It is a point process on all of \(\mathbb R^3\), not a
finite-window spatial simulation. Spatial translation invariance of \(N\)
makes \(X_I\) stationary. If \(B\) is bounded, then \(I\times B\) is bounded,
so (7) gives \(\mathbb E X_I(B)^4<\infty\).

Two distinct space--time events have the same spatial coordinate with
probability zero. Indeed, conditional on a finite genealogy, immigrant
locations and edge displacements have densities; the equality of two spatial
coordinates is a Lebesgue-null constraint. Local finiteness and a countable
exhaustion then reduce all possible collisions to a countable union of null
events. Hence \(X_I\) is simple.

Its spatial intensity is

\[
\lambda_I=\nu T.
\]

For the independently prescribed \(\lambda _0>0\), choose

\[
\boxed{\ \mu=\frac{\lambda _0(1-\eta)}{T}.\ }                 \tag{8}
\]

Then \(X_I\) has intensity exactly \(\lambda _0\). Projection over all time
would give infinitely many points in each positive-volume spatial set, whereas
a deterministic time slice of this diffuse continuous-time process contains no
events. The finite interval is therefore part of the construction.

If length and time have units \(L\) and \(\Theta\), then \(\phi,\mu,\nu\) have
units \(L^{-3}\Theta^{-1}\), \(\eta\) is dimensionless, and
\(\lambda _0=\nu T\) has units \(L^{-3}\). The target constants
\(C_2,C_3,C_4\) consequently have units \(L,L^2,L^3\).

## Full product-density calculation

I first work with measures. This avoids treating the fixed immigrant's Dirac
mass as though it were a density. Only after integrating over the immigrant
location do I pass to Radon--Nikodym densities.

### 1. Fixed-root cluster recursion as a measure identity

Let \(C_u\) be the cluster whose immigrant is fixed at \(u\). For a nonempty
label set \(A\), let \(\mathsf M_A^u\) be its ordered factorial moment measure
on \(E^A\). Define the measure

\[
\mathsf H_A^u:=\int_E\phi(v-u)\mathsf M_A^v\,dv.              \tag{9}
\]

If measures indexed by disjoint label sets are juxtaposed below, the product is
their tensor product placed in the labelled coordinates. Write
\(\delta_u^{(i)}\) for a Dirac mass in coordinate \(i\). The cluster generating
functional obeys

\[
G_u[f]=f(u)\exp\left\{\int_E\phi(v-u)(G_v[f]-1)\,dv\right\}.
\]

Functional differentiation at \(f\equiv1\) gives the following identity of
nonnegative measures for \(A=[n]\):

\[
\mathsf M_A^u
=\sum_{i\in A}\delta_u^{(i)}
  \sum_{\pi\in\mathcal P(A\setminus\{i\})}
  \prod_{B\in\pi}\mathsf H_B^u
 +\sum_{\pi\in\mathcal P(A)}\prod_{B\in\pi}\mathsf H_B^u.   \tag{10}
\]

The empty-partition product in (10) is one. Separating the one-block term in
the second sum gives

\[
\mathsf M_A^u=\mathsf H_A^u+\mathsf b_A^u.                   \tag{11}
\]

Set

\[
\Psi=\sum_{m\ge1}\phi^{*m},\qquad
\mathsf R=\delta_0+\Psi(z)\,dz.
\]

Since \(\eta<1\), \(\mathsf R(E)=(1-\eta)^{-1}\). Nonnegative
Neumann iteration of (11), equivalently iteration by genealogy depth, gives

\[
\mathsf M_A^u
=\int_E \mathsf R(dw)\,\mathsf b_A^{u+w}.                    \tag{12}
\]

At first order,

\[
\mathsf M_{\{i\}}^u=\delta_u^{(i)}+\Psi(z_i-u)\,dz_i,
\qquad
\mathsf H_{\{i\}}^u=\Psi(z_i-u)\,dz_i.
\]

For compactness write the latter measure as \(\psi_i^u\). Equations
(10)--(11) now give, as measure identities,

\[
\mathsf b_2^u
=\delta_u^{(1)}\psi_2^u+\delta_u^{(2)}\psi_1^u
 +\psi_1^u\psi_2^u,                                          \tag{13}
\]

\[
\begin{aligned}
\mathsf b_3^u
&=\sum_{i=1}^3\delta_u^{(i)}
  \bigl(\mathsf H_{\{j,k\}}^u+\psi_j^u\psi_k^u\bigr)\\
&\quad+\sum_{\{i,j\}\sqcup\{k\}=[3]}
  \mathsf H_{\{i,j\}}^u\psi_k^u
  +\psi_1^u\psi_2^u\psi_3^u,                                \tag{14}
\end{aligned}
\]

where \(\{i,j,k\}=[3]\), and

\[
\begin{aligned}
\mathsf b_4^u
&=\sum_{i=1}^4\delta_u^{(i)}\left[
 \mathsf H_{[4]\setminus\{i\}}^u
 +\sum_{\{a,b\}\sqcup\{c\}=[4]\setminus\{i\}}
      \mathsf H_{\{a,b\}}^u\psi_c^u
 +\prod_{j\ne i}\psi_j^u\right]\\
&\quad+\sum_{|A|=3}\mathsf H_A^u\psi_{A^c}^u
 +\sum_{A\mid A^c,\ |A|=2}^{\text{three pairings}}
       \mathsf H_A^u\mathsf H_{A^c}^u\\
&\quad+\sum_{|A|=2}\mathsf H_A^u\prod_{j\notin A}\psi_j^u
 +\prod_{i=1}^4\psi_i^u.                                    \tag{15}
\end{aligned}
\]

The non-root terms in (15) have respectively four \(3+1\), three \(2+2\),
six \(2+1+1\), and one \(1+1+1+1\) partitions. Expanding the lower-order
\(\mathsf H_A^u\) recovers the usual four third-order and 26 fourth-order
rooted topologies.

### 2. Immigrant integration and absolute continuity

For a Poisson process of immigrants, the order-\(n\) factorial cumulant measure
of the full space--time process is

\[
\mathsf Q_n^{\mathrm{ST}}
=\mu\int_E\mathsf M_{[n]}^u\,du.                              \tag{16}
\]

It is important to justify that this measure has a density. For each fixed
\(u\), I claim inductively that \(\mathsf M_A^u\) is a sum of:

1. measures of the form
   \(\delta_u^{(i)}m_{A,i}^u(z_{A\setminus\{i\}})
   \,dz_{A\setminus\{i\}}\), with at most one root Dirac mass; and
2. a measure absolutely continuous in all coordinates of \(E^A\).

The assertion is explicit at order one. Suppose it holds for every proper
nonempty subset of \(A\). Integrating a root-Dirac term in
\(\mathsf M_B^v\) against \(\phi(v-u)\,dv\) identifies \(v\) with its root
coordinate and produces an ordinary density there; integrating an absolutely
continuous term preserves absolute continuity by Tonelli. Hence every
\(\mathsf H_B^u\) with \(B\subsetneq A\) is absolutely continuous in all of
its labelled coordinates. Formula (10), with its one-block term removed, then
shows that \(\mathsf b_A^u\) has precisely the asserted form. Finally, (12)
preserves the root-Dirac term only through the \(\delta_0\) part of
\(\mathsf R\); its \(\Psi\)-part turns that term into a density. This completes
the induction for \(|A|\le4\).

Now integrate over the immigrant location in (16). For a root term,

\[
\int_E\!\left[
 \delta_u(dz_i)\,
 m_{A,i}^u(z_{A\setminus\{i\}})
 \,dz_{A\setminus\{i\}}\right]du
=m_{A,i}^{z_i}(z_{A\setminus\{i\}})
 \,dz_1\cdots dz_n,
\]

so immigrant integration removes the only possible Dirac coordinate. The
non-root terms were already absolutely continuous. Moreover, for bounded
\(W\subset E\) and \(2\le n\le4\),

\[
\mathsf Q_n^{\mathrm{ST}}(W^n)
=\mu\int_E\mathbb E[(C_u(W))_n]\,du
\le \mu|W|\mathbb E S^n<\infty,                               \tag{16a}
\]

where \((k)_n=k(k-1)\cdots(k-n+1)\). Thus the resulting densities
are locally integrable. Therefore
\(\mathsf Q_n^{\mathrm{ST}}\ll dz_1\cdots dz_n\) for \(n=2,3,4\). Denote
compatible nonnegative Radon--Nikodym versions by
\(q_n^{\mathrm{ST}}(z_{1:n})\).

Using (12), Tonelli, and \(\mathsf R(E)=(1-\eta)^{-1}\), we also have the
measure identity

\[
\mathsf Q_n^{\mathrm{ST}}
=\nu\int_E\mathsf b_n^u\,du,
\qquad n=2,3,4,                                              \tag{17}
\]

and \(q_1^{\mathrm{ST}}=\nu\). At order two, (13) yields, for almost every
pair of distinct space--time points,

\[
\boxed{\quad
q_2^{\mathrm{ST}}(z_1,z_2)
=\nu\left[
\Psi(z_2-z_1)+\Psi(z_1-z_2)
 +\int_E\Psi(z_1-u)\Psi(z_2-u)\,du
\right].\quad}                                               \tag{18}
\]

All these factorial cumulant densities have nonnegative versions because the
measures in (16) are nonnegative.

### 3. Full space--time product densities

The factorial moment--cumulant identity is an identity of measures. Since all
cumulant measures through order four are absolutely continuous, it gives the
following density identities almost everywhere:

\[
\rho^{(2)}_{\mathrm{ST}}(1,2)
=\nu^2+q_2^{\mathrm{ST}}(1,2),                                \tag{19}
\]

\[
\rho^{(3)}_{\mathrm{ST}}(1,2,3)
=\nu^3+\nu\sum_{1\le i<j\le3}q_2^{\mathrm{ST}}(i,j)
 +q_3^{\mathrm{ST}}(1,2,3),                                  \tag{20}
\]

and

\[
\begin{aligned}
\rho^{(4)}_{\mathrm{ST}}(1,2,3,4)
&=\nu^4+\nu^2\sum_{1\le i<j\le4}q_2^{\mathrm{ST}}(i,j)\\
&\quad+q_2^{\mathrm{ST}}(1,2)q_2^{\mathrm{ST}}(3,4)
 +q_2^{\mathrm{ST}}(1,3)q_2^{\mathrm{ST}}(2,4)
 +q_2^{\mathrm{ST}}(1,4)q_2^{\mathrm{ST}}(2,3)\\
&\quad+\nu\sum_{|A|=3}q_3^{\mathrm{ST}}(A)
 +q_4^{\mathrm{ST}}(1,2,3,4).                                \tag{21}
\end{aligned}
\]

Thus the complete term counts are \(2,5,15\). These are the requested full
product densities, including observations from different immigrant clusters,
not merely the connected tree terms.

### 4. Finite-time spatial pushforward

Restrict (16) to \((I\times\mathbb R^3)^n\) and push it forward by discarding
the time coordinates. Since \(q_n^{\mathrm{ST}}\ge0\), Tonelli's theorem shows
that this spatial factorial cumulant measure is absolutely continuous, with
locally integrable density

\[
Q_n^I(x_{1:n})
:=\int_{I^n}q_n^{\mathrm{ST}}
 ((t_1,x_1),\ldots,(t_n,x_n))\,dt_1\cdots dt_n,
\quad n=2,3,4.                                                \tag{22}
\]

The same argument applies to the factorial moment measures, so the projected
process has absolutely continuous factorial moment measures through order
four. Integrating (19)--(21), with the singleton time integrals equal to
\(\nu T=\lambda _0\), gives the full ordered spatial densities

\[
\boxed{\rho_I^{(2)}(1,2)=\lambda _0^2+Q_2^I(1,2),}            \tag{23}
\]

\[
\boxed{\rho_I^{(3)}(1,2,3)
=\lambda _0^3+\lambda _0\sum_{i<j}Q_2^I(i,j)
 +Q_3^I(1,2,3),}                                             \tag{24}
\]

and

\[
\boxed{\begin{aligned}
\rho_I^{(4)}(1,2,3,4)
&=\lambda _0^4+\lambda _0^2\sum_{i<j}Q_2^I(i,j)\\
&\quad+Q_2^I(1,2)Q_2^I(3,4)
 +Q_2^I(1,3)Q_2^I(2,4)
 +Q_2^I(1,4)Q_2^I(2,3)\\
&\quad+\lambda _0\sum_{|A|=3}Q_3^I(A)+Q_4^I(1,2,3,4).
\end{aligned}}                                               \tag{25}
\]

These identities hold almost everywhere for compatible Radon--Nikodym
versions. Division by \(\lambda _0^n\) gives \(g_n\).

## Proof or obstruction

### 1. Proof of Theorem 1

Assume now that \(\phi\in L^1(E)\cap L^\infty(E)\). Young's convolution
inequality gives, for \(m\ge1\),

\[
\|\phi^{*m}\|_\infty
\le \|\phi\|_\infty\eta^{m-1}.
\]

Consequently

\[
\|\Psi\|_\infty\le\frac{\|\phi\|_\infty}{1-\eta},
\qquad
\|\Psi\|_1=\frac{\eta}{1-\eta}.                             \tag{26}
\]

Equation (18) and Young's inequality imply the almost-everywhere uniform
off-diagonal bound

\[
q_2^{\mathrm{ST}}(z_1,z_2)
\le \nu\|\Psi\|_\infty\left(2+\|\Psi\|_1\right)
=:K_{\mathrm{ST}}<\infty.                                    \tag{27}
\]

Integrating over \(I^2\) gives

\[
0\le Q_2^I(x_1,x_2)\le T^2K_{\mathrm{ST}}
\]

for almost every pair. By (23),

\[
g_2^I(x_1,x_2)
=1+\frac{Q_2^I(x_1,x_2)}{\lambda _0^2}
\le 1+\frac{T^2K_{\mathrm{ST}}}{\lambda _0^2}
=:G_*<\infty                                                  \tag{28}
\]

almost everywhere off the diagonal. If \(g_2^I=C_2/D\) almost everywhere on
\(0<D\le M\), choose

\[
0<d_*<\min\{M,C_2/(2G_*)\}.
\]

Pairs with \(x_1\) in a fixed unit cube and
\(0<\|x_2-x_1\|<d_*\) form a set of positive Lebesgue measure. Outside the
union of the null sets in the target identity and (28), both statements hold,
but \(C_2/D>2G_*\), a contradiction. This proves Theorem 1. The proof uses only
the absence of a positive pair-distance cutoff; the altitude restrictions at
orders three and four cannot repair the contradiction.

### 2. Necessary residual identities and their almost-everywhere scope

The boundedness obstruction need not survive an integrable singular kernel.
Nevertheless, every subcritical scalar linear Poisson-cluster Hawkes process
has nonnegative factorial cumulants. Choose compatible nonnegative versions and
write

\[
c_n^I:=Q_n^I/\lambda _0^n\ge0,
\qquad n=2,3,4.                                               \tag{29}
\]

All identities in this subsection are almost-everywhere statements for these
versions. If the pair target holds, (23) gives, almost everywhere on
\(\mathcal D_2\),

\[
c_2^I(i,j)=\frac{C_2}{D_{ij}}-1.                              \tag{30}
\]

Nonnegativity forces \(C_2\ge M\): otherwise the right-hand side is negative
on the positive-measure set \(C_2<D_{ij}\le M\).

Let the triangle target also hold. The pullback to triple space of the null set
where (30) fails is null by Fubini. Hence, on the common full-measure subset of
\(\mathcal D_3\), (24) gives

\[
\boxed{\quad
c_3^I(1,2,3)
=\frac{C_3}{A}+2-C_2
 \left(\frac1{D_{12}}+\frac1{D_{13}}+\frac1{D_{23}}\right)
\ge0.\quad}                                                   \tag{31}
\]

At order four, (25) gives, almost everywhere on \(\mathcal D_4\),

\[
\boxed{\quad
c_4^I
=\frac{C_4}{V}-1-\sum_{i<j}c_2^I(i,j)
 -\sum_{ij\mid k\ell}c_2^I(i,j)c_2^I(k,\ell)
 -\sum_{|A|=3}c_3^I(A)\ge0.\quad}                            \tag{32}
\]

Every edge of a target tetrahedron lies in \(\mathcal D_2\), so the pair
formula (30) may be substituted in (32) outside a null set. The triangle
formula requires more care. For a face label set \(A\), define

\[
\mathcal E_A
:=\mathcal D_4\cap
  \{(x_1,x_2,x_3,x_4):x_A\in\mathcal D_3\}.
\]

Only when \(\mathcal E_A\) has positive measure does (31) give a nonvacuous
face constraint, and then its pullback is valid almost everywhere on
\(\mathcal E_A\). It must not be substituted on
\(\mathcal D_4\setminus\mathcal E_A\). In particular, the governing problem
does not impose the \(h_3\) triangle-altitude condition on every face in
\(\mathcal D_4\).

Dropping the nonnegative triple and fourth-cumulant terms yields the weaker
necessary condition, valid almost everywhere throughout \(\mathcal D_4\),

\[
\frac{C_4}{V}
\ge1+\sum_{i<j}c_2^I(i,j)
 +\sum_{ij\mid k\ell}c_2^I(i,j)c_2^I(k,\ell).                 \tag{33}
\]

The resolved triangle and tetrahedron domains keep the relevant simplex
contents away from the degeneracies that would force an immediate contradiction
from (31)--(33), while the constants remain free outputs. These are therefore
necessary obligations, not a general non-existence proof.

### 3. Remaining exact obligation

To solve the governing problem by Hawkes methods, one would have to exhibit,
for every prescribed \((\lambda _0,M,h_3,h_4)\), a nonnegative causal singular
kernel, marked law, or other precisely specified Hawkes mechanism whose
time-integrated cumulants equal the residuals (30)--(32) on their exact domains,
while preserving subcriticality, simplicity, the prescribed intensity, finite
local fourth moments, and absolute continuity. No supplied source or calculation
does this. Matching only the resolvent, one rooted tree, or the common-immigrant
contribution is insufficient because (23)--(25) retain every disconnected
partition. Nonlinear and critical variants would additionally require a new
existence and moment argument, not an unlabelled extension of the calculation
above.

## Reasoning summary and decision record

1. **Spatialisation choice.** A temporal Hawkes process alone does not define
   hypocentres in \(\mathbb R^3\). Projection over all time has infinite spatial
   intensity, while a deterministic slice is empty for a diffuse process. A
   stationary space--time process observed on a finite time interval gives a
   genuine stationary spatial process on all of \(\mathbb R^3\).

2. **Intensity choice.** Subcriticality gives intensity \(\mu/(1-\eta)\).
   Equation (8) meets the independently prescribed spatial intensity exactly
   without rescaling the physical geometric domains.

3. **Moment check.** The Borel total-progeny law has an exponential moment when
   \(\eta<1\). Equations (5)--(7) then give a direct Poisson-cluster proof of
   finite local fourth moments.

4. **Measure-first hierarchy.** Fixed-root clusters necessarily contain a root
   Dirac mass. I therefore kept the recursion as a measure identity, proved that
   integrating over the diffuse immigrant location removes that mass, and only
   then used densities and the finite-time spatial pushforward.

5. **Partition check.** The fixed-root recursion supplies connected
   factorial-cumulant measures. Applying every set partition afterwards gives
   exactly \(2,5,15\) full product-density terms at orders two, three and four.

6. **Critical alternative discarded for this theorem.** At \(\eta=1\), the
   Poisson-immigrant Galton--Watson cluster has infinite mean progeny, so (4)
   fails. Special critical no-ancestor models have different hypotheses and do
   not supply the required fourth moments or exact reciprocal-simplex densities.

7. **Decisive obstruction and its limit.** For
   \(\phi\in L^1\cap L^\infty\), the descendant resolvent and the projected pair
   correlation are bounded, contradicting the required \(1/D\) divergence.
   An integrable unbounded kernel or a marked carrier can evade this step, so
   those cases remain unresolved.

## Checks and limitations

- **Analytical checks.** The cluster source terms were enumerated by Bell
  partitions. The full fourth density contains six pair--singleton--singleton
  terms, three pair--pair terms, four triple--singleton terms, the all-singleton
  term, and the connected fourth term. The total-progeny radius satisfies
  \(R>1\) precisely in the subcritical regime.
- **Density check.** Root Dirac masses occur only before immigrant integration.
  The induction following (16) and Tonelli's theorem establish absolute
  continuity after immigrant integration and after spatial projection.
- **Almost-everywhere check.** Residual formulas use compatible
  Radon--Nikodym versions. Pair and triangle null sets are pulled into higher
  configuration spaces only through Fubini. Formula (31) is used on a
  tetrahedral face only on the relevant positive-measure intersection
  \(\mathcal E_A\).
- **Source-tree check.** Both complete frozen local manuscript source trees
  were inspected for v01, including their included sections, appendices,
  bibliographies and mathematical audit records. They remain frozen inputs to
  this repair.
- **No numerical evidence.** No grid, simulation or empirical approximation is
  used in Theorem 1. The archived approximate Hawkes experiment is not an
  acceptance criterion.
- **No general non-existence claim.** The theorem excludes only scalar linear
  subcritical Hawkes processes whose four-dimensional triggering density lies
  in \(L^1\cap L^\infty\). Singular, marked, multitype, random-carrier,
  nonlinear and critical models remain unresolved, as do non-Hawkes processes.
- **No exact construction outside the subclass.** Equations (30)--(33) are
  necessary conditions, not a solved inverse theorem. The exact target remains
  unresolved by this approach.
- **Domains.** The pair contradiction uses the entire required domain
  \(0<D\le M\), with no lower cutoff. No triangle condition was imposed on all
  tetrahedral faces, and no identity was used beyond diameter \(M\).

## References

1. Jovanović, S., Hertz, J. and Rotter, S. (2015), *Cumulants of Hawkes point
   processes*, Physical Review E 91, 042802, arXiv:1409.5353. Full text was
   verified in the frozen literature dossier; relevant locations are equations
   (13)--(18), (28), (37), (39), and the fourth-order tree algorithm on pp. 3
   and 6--7.

2. Hawkes, A. G. and Oakes, D. (1974), *A cluster process representation of a
   self-exciting process*, Journal of Applied Probability 11, 493--503. In the
   frozen source work this was available at abstract/metadata level only. No
   delicate theorem hypothesis from the unavailable body is used; the branching
   construction, progeny bound and density passage are given above.

3. Ogata, Y. (1998), *Space-Time Point-Process Models for Earthquake
   Occurrences*, Annals of the Institute of Statistical Mathematics 50,
   379--402. The official full PDF's opening and model pages were checked for
   ETAS context in the frozen dossier. It is not a reciprocal-simplex
   product-density theorem.

4. Kagan, Y. Y. (1982), *Stochastic model of earthquake fault geometry*,
   Geophysical Journal of the Royal Astronomical Society 71, 659--691. The
   local full PDF was inspected, especially printed pp. 659--665. Its Monte
   Carlo model is motivation, not a stationary all-space proof for the present
   target.

5. *Reciprocal simplex correlations from random spherical surfaces* (local
   unpublished manuscript, 2026), frozen at
   `common/prior_work/reciprocal-simplex/`; especially Sections 3--5 and
   `MATH_CHECK.md`. Full source tree inspected.

6. *Exact reciprocal simplex correlations on finite domains* (local
   unpublished manuscript, 2026), frozen at
   `common/prior_work/finite-cluster-reciprocal-laws/`; especially the
   construction, partition appendix and mathematical audits. Full source tree
   inspected.

## Response to review (v02 onward)

1. **H3-v01-F01 — unresolved governing scope.** Preserved. Theorem 1 is stated
   only for scalar linear subcritical Hawkes processes with
   \(\phi\in L^1\cap L^\infty\). The claim, remaining obligation, checks and
   limitations all state explicitly that singular, marked, carrier, nonlinear
   and critical models remain unresolved.

2. **H3-v01-F02 — fourth local moment.** Repaired in equations (1)--(7). The
   Borel total-progeny law has power-series radius
   \(e^{\eta-1}/\eta>1\), hence an exponential moment and
   \(\mathbb E S^4<\infty\). The marked-Poisson exponential formula now gives
   \(\kappa_r(N(W))=\mu\int\mathbb E C_u(W)^r\,du\), while (5) gives
   \(\int C_u(W)^r\,du\le |W|S^r\). The fourth moment follows from the ordinary
   moment--cumulant formula.

3. **H3-v01-F03 — measure to density.** Repaired in equations (9)--(18).
   Fixed-root recursions are kept as measure identities. The induction after
   (16) isolates the single possible root Dirac mass and proves that integrating
   over the immigrant location removes it. Only then are space--time densities
   introduced. Equation (22) uses Tonelli to prove absolute continuity of the
   finite-time spatial pushforwards.

4. **H3-v01-F04 — almost-everywhere versions.** Repaired in equations
   (29)--(33). The residuals are stated for compatible nonnegative
   Radon--Nikodym versions and only almost everywhere. Pair and triangle null
   sets are handled by Fubini. The triangle residual is substituted for a
   tetrahedral face only almost everywhere on the relevant intersection
   \(\mathcal E_A\), and only when that intersection has positive measure.
