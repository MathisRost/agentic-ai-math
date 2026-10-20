# Approach 2 — submission v02

- Run / model / reasoning: `20261019T114252Z_cox_rerun` / `gpt-5.6-sol` / `xhigh`.
- Problem snapshot SHA-256: `4c7a8b0ec361395179d7c6131e53b61bd312e028e552baa1a98fe6dc16eea84a`.
- Context packet and source dossier version: `context_packets/proof_2_v02.md`, SHA-256 `3a59b82b784e74a9b8455a82349a471186bce0f9dd023bfd560821c3cc5af50d`; `shared_literature/dossier.md`, SHA-256 `5d42ad11b6b55246e6a0eb098b3f09c1bf3751cd3add4a819f5e427017b659f5`.
- Claim status: **scoped obstruction and explicit unresolved directing-measure moment problem**. The exact target for general Cox processes remains unresolved.

## Claim and scope

Fix an admissible tuple

\[
(\lambda _0,M,h_3,h_4),\qquad \lambda _0,M,h_3,h_4>0,
\]

with the triangle and tetrahedron domains in the frozen problem statement of positive Lebesgue measure. This submission proves the following restricted results.

1. Within the class of Cox processes, the governing problem is equivalent to a truncated moment problem for one stationary diffuse random measure. Once a witness exists at any positive intensity for the fixed physical domains, deterministic scaling of its directing measure gives every prescribed intensity \(\lambda _0\) without changing \(g_2,g_3,g_4\).
2. No Cox process directed by a Poisson population of uniformly weighted spheres, with a nonnegative radius density and nonnegative radius-dependent surface weight in the class below, can satisfy even the pair and triangle identities simultaneously. The proof allows arbitrary radial mixing. It therefore includes, but is not limited to, the spherical construction in the first local manuscript.
3. An absolutely continuous directing measure \(\Lambda(dx)=Z(x)dx\) with a stationary random intensity field satisfying \(\mathbb E Z(0)^2<\infty\) cannot satisfy the pair law without a positive lower distance cutoff. Ordinary log-Gaussian Cox processes are excluded as a consequence and also have a separate third-order shape obstruction.
4. The exact dependent finite-cluster process in the second local manuscript is not a Cox process. Thus it cannot be combined with Cox intensity scaling merely by reinterpreting its law as Cox.

These are reductions and class-specific exclusions, not a solution of the governing arbitrary-Cox problem. In particular, this submission neither constructs nor rules out a sufficiently irregular absolutely continuous directing field, a singular non-spherical directing measure, dependent carriers, or a general stationary diffuse random measure.

## Relation to prior work

The frozen spherical manuscript, `common/prior_work/reciprocal-simplex/`, uses the directing measure

\[
\Xi=\sum_{(c,r)}\frac{\beta}{r}\mathcal H^2\!\restriction S(c,r)
\]

with Poisson sphere parameters of intensity \(\tau r\,dc\,dr\), \(0<r<L\). Its Sections 3--5 derive

\[
q_2=\pi\tau\beta^2\frac{L^2-D^2/4}{D},\qquad
q_3=\tau\beta^3\frac{\sqrt{L^2-R_3^2}}{A},\qquad
q_4=\frac{\tau\beta^4}{6V}
\]

on their supports, followed by every set-partition term. Its Theorem 5.3 is an approximation theorem at independently prescribed intensity, not an equality theorem. I reuse its incidence geometry and give the measurable-weight coarea statement needed for the larger radial class below. The new obstruction is that no choice of positive radius mixing and uniform radius-dependent surface weight in this class can make the full pair and triangle targets exact simultaneously.

The frozen finite-cluster manuscript, `common/prior_work/finite-cluster-reciprocal-laws/`, proves exact full identities on smaller domains with a positive pair cutoff and an intensity chosen jointly with the construction. Its Sections 3--4 and appendices construct positive exact-size cluster kernels and retain all parent partitions. Proposition 5 below does not use that construction as a Cox witness; it gives a direct bounded-window count obstruction to doing so.

For external structure, Last and Penrose, equation (13.10), identify Cox factorial moment measures with \(\mathbb E\Lambda^{\otimes n}\). Møller, Syversveen and Waagepetersen, Theorem 1, equation (2), give the log-Gaussian product identity used below. The frozen dossier records the full-text checks and exact locations.

## Process and existence

### 1. Cox processes and directing-measure moments

Let \(\Lambda\) be a random locally finite Borel measure on \(\mathbb R^3\). Conditional on \(\Lambda\), let \(X\) be Poisson with intensity measure \(\Lambda\).

**Proposition 1 (equivalent Cox moment formulation).** The following two assertions are equivalent.

1. \(X\) is a stationary, simple, locally finite Cox process of intensity \(0<\lambda<\infty\), has finite local count moments through order four, and has absolutely continuous ordered factorial moment measures through order four.
2. Its directing measure, whose law is uniquely determined by the Cox law, has these properties:
   - the law of \(\Lambda\) is translation invariant;
   - \(\Lambda\) is diffuse and locally finite almost surely;
   - \(\mathbb E\Lambda(B)^4<\infty\) for every bounded Borel set \(B\);
   - \(M_n:=\mathbb E\Lambda^{\otimes n}\) is absolutely continuous for \(1\le n\le4\), with density \(m_n\);
   - \(M_1(dx)=\lambda\,dx\).

Under either assertion,

\[
\alpha_X^{(n)}=M_n,\qquad \rho_X^{(n)}=m_n,\qquad 1\le n\le4.
\tag{1.1}
\]

Consequently, this Cox process meets the exact target if and only if there are constants \(C_2,C_3,C_4>0\) for which

\[
m_2=\lambda^2\frac{C_2}{D},\qquad
m_3=\lambda^3\frac{C_3}{A},\qquad
m_4=\lambda^4\frac{C_4}{V}
\tag{1.2}
\]

almost everywhere on the three prescribed domains.

**Proof.** Suppose first that the properties of \(\Lambda\) hold. Conditional Poisson processes with locally finite directing measures are locally finite. A Poisson process with diffuse intensity measure is simple, so conditional and then unconditional simplicity follow. Translation invariance of the directing law passes to the mixture. For a bounded \(B\), conditional on \(\Lambda\), \(X(B)\) is Poisson with mean \(L_B=\Lambda(B)\). Its first four ordinary moments are the corresponding Touchard polynomials in \(L_B\), so the fourth-moment assumption gives finite local count moments through order four. Conditional factorial moment measures are \(\Lambda^{\otimes n}\); Tonelli's theorem therefore gives (1.1), and the assumed absolute continuity gives the densities.

Conversely, suppose that \(X\) has the process properties in assertion 1. The Cox probability generating functional satisfies

\[
\mathbb E\prod_{x\in X}(1-h(x))
=\mathbb E\exp\{-\textstyle\int h\,d\Lambda\},
\qquad 0\le h<1,
\tag{1.3}
\]

for compactly supported measurable \(h\). These restricted Laplace functionals determine the law of a locally finite random measure: on finite collections of bounded sets they give the joint Laplace transform on a neighbourhood of the origin, and a countable generating ring then determines the random measure. Stationarity of \(X\), applied to (1.3), therefore implies translation invariance in law of \(\Lambda\).

Identity (1.1) holds for every Cox process. Because \(X\) is simple, \(\alpha_X^{(2)}\) gives zero mass to the diagonal. Hence

\[
0=M_2\{(x,x):x\in B\}
=\mathbb E\sum_{x\in B}\Lambda\{x\}^2
\]

for every bounded \(B\). Exhausting \(\mathbb R^3\) by countably many bounded sets shows that \(\Lambda\) is diffuse almost surely. If \(N=X(B)\), then

\[
\mathbb E[N^4\mid\Lambda]
=L_B^4+6L_B^3+7L_B^2+L_B\ge L_B^4.
\]

Thus finite fourth count moments imply \(\mathbb E\Lambda(B)^4<\infty\). Finally, absolute continuity of the factorial moment measures and (1.1) give the required tensor-moment densities, while the first moment measure is \(\lambda\,dx\). This proves both directions and (1.2). \(\square\)

**Corollary 1 (prescribed intensity).** If a directing measure satisfying (1.2) exists at one intensity \(\lambda>0\) for fixed \((M,h_3,h_4)\), then

\[
\Lambda'=(\lambda _0/\lambda)\Lambda
\]

satisfies the same normalised identities at every prescribed \(\lambda _0>0\) on exactly the same physical domains.

Indeed, \(\mathbb E(\Lambda')^{\otimes n}=(\lambda _0/\lambda)^nM_n\). Stationarity, diffuseness, local finiteness, density existence and finite fourth local moments are preserved. Prescribed intensity is therefore not the remaining Cox obstruction; existence and positivity of the geometric moment system are.

### 2. A general Poisson-sphere directing class

Fix \(L<\infty\). Let \(\Pi\) be Poisson on \(\mathbb R^3\times(0,L)\) with intensity

\[
dc\,p(r)\,dr,
\]

where \(p\ge0\) is measurable and \(0<\int_0^Lp(r)\,dr<\infty\). Let \(b:(0,L)\to[0,\infty)\) be measurable and assume

\[
\kappa:=\sup_{0<r<L}4\pi r^2b(r)<\infty.
\tag{2.1}
\]

Fix finite Borel representatives of \(p\) and \(b\), and define

\[
\Lambda=\sum_{(c,r)\in\Pi}b(r)\mathcal H^2\!\restriction S(c,r).
\tag{2.2}
\]

For a bounded set \(B\), only parents with centres in its bounded \(L\)-enlargement can contribute. Their number is finite Poisson, and every whole carrier has mass at most \(\kappa\). It follows that \(\Lambda(B)<\infty\) almost surely and \(\mathbb E\Lambda(B)^k<\infty\) for every finite \(k\). Each surface measure is diffuse and only finitely many carriers meet a bounded set, so \(\Lambda\) is diffuse. Its law is stationary and isotropic, and its intensity is

\[
\lambda=4\pi\int_0^Lp(r)b(r)r^2\,dr.
\tag{2.3}
\]

We assume this number is positive. The spherical manuscript is the special case \(p(r)=\tau r\), \(b(r)=\beta/r\); condition (2.1) then follows from \(4\pi r^2b(r)=4\pi\beta r\).

The next lemma supplies the density-existence step for merely measurable radial weights.

**Lemma 2 (measurable-weight sphere incidence).** For \(2\le j\le4\), define the one-carrier tensor measure

\[
Q_j(H)=\int_{\mathbb R^3}\int_0^L p(r)
\bigl(b(r)\mathcal H^2\!\restriction S(c,r)\bigr)^{\otimes j}(H)\,dr\,dc.
\tag{2.4}
\]

This is a locally finite measure on \((\mathbb R^3)^j\), is absolutely continuous, and has the following density almost everywhere. For an affinely independent tuple \(x=(x_1,\ldots,x_j)\), let \(E=\operatorname{span}(x_2-x_1,\ldots,x_j-x_1)\), let \(c_0\) and \(R_j\) be its circumcentre and circumradius in its affine span, and let \(\Delta_{j-1}\) be its simplex volume. Put

\[
w_j(r)=p(r)b(r)^j\mathbf1_{(0,L)}(r),
\qquad r_z=\sqrt{R_j^2+|z|^2}.
\]

Then

\[
q_j(x)=\frac{1}{(j-1)!\Delta_{j-1}}
\int_{E^\perp}w_j(r_z)r_z^{j-1}\,d\mathcal H^{4-j}(z).
\tag{2.5}
\]

For \(j=4\), \(E^\perp=\{0\}\) and \(\mathcal H^0\) is counting measure. Thus, for the chosen Borel version \(w_4=p b^4\mathbf1_{(0,L)}\),

\[
q_4(x_1,x_2,x_3,x_4)
=\frac{w_4(R_4)R_4^3}{6V}
\quad\text{for almost every noncoplanar tuple.}
\tag{2.6}
\]

Changing \(w_4\) on a one-dimensional null set does not change \(Q_4\), and (2.5) then shows that the resulting displayed versions agree almost everywhere in tuple space.

**Proof.** If \(K\subset\mathbb R^3\) is bounded, (2.1) gives

\[
Q_j(K^j)\le |K^{+L}|\,\kappa^j\int_0^Lp(r)\,dr<\infty,
\tag{2.7}
\]

which proves local finiteness. For a fixed sphere, affine dependence of \(j\le4\) surface-sampled points has product surface measure zero: after fewer than four generic points have been selected, their affine span intersects the sphere in a surface-null subset. Thus it suffices to work on affinely independent tuples.

Every sphere through such a tuple has the orthogonal-fibre representation

\[
c=c_0+z,\qquad r=r_z=\sqrt{R_j^2+|z|^2},\qquad z\in E^\perp.
\tag{2.8}
\]

On the incidence manifold \(|x_i-c|^2-r^2=0\), \(1\le i\le j\), the normal Jacobian in the vertex variables is \(J_x=(2r)^j\). In the \((c,r)\) variables, subtracting the first constraint row from the other \(j-1\) rows gives a parallelepiped of volume \(2^{j-1}(j-1)!\Delta_{j-1}\) in \(E\times\{0\}\). Its remaining orthogonal component is \(2(z,-r)\). Hence

\[
J_{c,r}=2^j(j-1)!\Delta_{j-1}\sqrt{|z|^2+r^2}.
\]

The parametrisation in (2.8) has area Jacobian \(\sqrt{|z|^2+r^2}/r\). The ratio of the two normal Jacobians, multiplied by this fibre Jacobian, is therefore

\[
\frac{J_x}{J_{c,r}}\frac{\sqrt{|z|^2+r^2}}r
=\frac{r^{j-1}}{(j-1)!\Delta_{j-1}}.
\tag{2.9}
\]

The nonnegative area--coarea formula, applied first to sphere parameters and then to the vertex projection, now gives (2.5) against every nonnegative test function. It is valid for measurable \(w_j\), with infinite integrals allowed. Local finiteness (2.7) then makes the density locally integrable and finite almost everywhere. For \(j=4\), the fibre has dimension zero, so (2.6) follows by evaluation at \(z=0\). If two choices of \(w_4\) agree almost everywhere, their left-hand measures in (2.4) agree; applying the same coarea identity shows that their density versions agree almost everywhere. \(\square\)

Lemma 2 proves absolute continuity of every one-carrier contribution through order four. The Poisson-carrier partition expansion below is a finite sum of products of these densities, so \(\mathbb E\Lambda^{\otimes n}\) is absolutely continuous for \(n\le4\). The argument stops at four for a geometric reason: five points on one sphere lie on the Lebesgue-null cospherical set in \((\mathbb R^3)^5\).

## Full product-density calculation

### 3. All carrier partitions through order four

For an arbitrary Cox process, \(m_n=\mathbb E\Lambda^{\otimes n}\) is already the full observed factorial density. When \(\Lambda\) is the Poisson sum (2.2), its moments admit a carrier-partition expansion. Let \(q_j\) be the one-carrier density from Lemma 2 and write \(q_{ij}=q_2(x_i,x_j)\). Poisson factorial identities for distinct carriers give

\[
\begin{aligned}
m_2&=\lambda^2+q_{12},\\
m_3&=\lambda^3+\lambda(q_{12}+q_{13}+q_{23})+q_{123},\\
m_4&=\lambda^4+\lambda^2\sum_{i<j}q_{ij}
 +(q_{12}q_{34}+q_{13}q_{24}+q_{14}q_{23})\\
&\qquad+\lambda(q_{123}+q_{124}+q_{134}+q_{234})+q_{1234}.
\end{aligned}
\tag{3.1}
\]

These are respectively the \(2,5,15\) set partitions of the labelled tuple. No factorial multiplier is missing: the points are ordered already, while each set partition records which labels use the same carrier.

### 4. Explicit one-sphere densities

Polar integration in the orthogonal fibres of (2.5) gives, almost everywhere,

\[
q_2(D)=\frac{2\pi}{D}\int_{D/2}^{L}p(r)b(r)^2r^2\,dr,
\tag{4.1}
\]

\[
q_3(x_1,x_2,x_3)
=\frac1A\int_{R_3}^{L}
\frac{p(r)b(r)^3r^3}{\sqrt{r^2-R_3^2}}\,dr
=\frac{\Phi(R_3)}A,
\tag{4.2}
\]

and, using the chosen version \(w_4\),

\[
q_4(x_1,x_2,x_3,x_4)
=\frac{w_4(R_4)R_4^3}{6V}.
\tag{4.3}
\]

Here \(w_4(r)=0\) outside \((0,L)\), so (4.3) includes the support indicator. Nonnegative Tonelli integration justifies the polar changes of order. Equations (2.7) and (3.1) ensure local integrability of the full densities. Substitution of \(p(r)=\tau r\), \(b(r)=\beta/r\) recovers the spherical manuscript's three one-parent formulas and, through (3.1), all of its full product densities.

## Proof or obstruction

### 5. Arbitrary radial mixing of uniform spheres is impossible

**Proposition 3 (uniform Poisson-sphere Cox obstruction).** Assume that the prescribed triangle domain \(\mathcal D_3\) has positive Lebesgue measure. No process in the Poisson-sphere class (2.2) can satisfy simultaneously

\[
g_2(x_1,x_2)=\frac{C_2}{D}\quad\text{a.e. on }\mathcal D_2,
\qquad
g_3(x_1,x_2,x_3)=\frac{C_3}{A}\quad\text{a.e. on }\mathcal D_3
\]

for positive constants \(C_2,C_3\).

**Proof.** Every edge of a triangle in \(\mathcal D_3\) has length in \((0,M]\). The first two lines of (3.1), with the full target densities rather than connected densities, force

\[
q_2(ij)=\lambda^2\left(\frac{C_2}{d_{ij}}-1\right)
\tag{5.1}
\]

and

\[
q_3(123)=\lambda^3\left(
\frac{C_3}{A}+2-C_2\sum_{i<j}\frac1{d_{ij}}
\right)
\tag{5.2}
\]

almost everywhere on the relevant configurations. By (4.2), \(Aq_3\) is a measurable function only of the circumradius \(R_3\). Equation (5.2) would therefore make

\[
C_3+2A-C_2A\sum_{i<j}\frac1{d_{ij}}
\tag{5.3}
\]

constant in triangle shape at almost every fixed admissible circumradius.

Positive measure of \(\mathcal D_3\) implies \(h_3<\sqrt3M/2\). Choose an open interval \(I\) with

\[
\frac{2h_3}{3}<R<\frac{M}{\sqrt3}.
\]

For every \(R\in I\), the equilateral triangle of circumradius \(R\) has diameter strictly below \(M\) and altitude strictly above \(h_3\). After shrinking \(I\), one open neighbourhood \(U\) of its angle pair remains in \(\mathcal D_3\) for all \((R,\text{angles})\in I\times U\).

Translation, spatial orientation, circumradius and two angles form smooth local coordinates with nonzero Jacobian near these triangles. Fubini's theorem applied to the almost-everywhere identities implies that, for almost every \(R\in I\), (5.3) is constant for almost every angle pair in \(U\). Fix one such \(R\). The expression in (5.3) is continuous in the angles, so it is constant on all of \(U\).

Restrict now to the isosceles curve with angles

\[
\theta,\quad \frac{\pi-\theta}{2},\quad \frac{\pi-\theta}{2}
\]

near \(\theta=\pi/3\), and set \(x=\sin(\theta/2)\). Its side lengths are

\[
a=2R\sin\theta,\qquad b=c=2R\cos(\theta/2).
\]

Using \(A=abc/(4R)\), we obtain

\[
A=4R^2x(1-x^2)^{3/2},\qquad
A\left(\frac1a+\frac1b+\frac1c\right)
=R(1-x^2)(1+4x).
\tag{5.4}
\]

After removing the constant \(C_3\), expression (5.3) becomes

\[
F(x)=8R^2x(1-x^2)^{3/2}
-C_2R(1-x^2)(1+4x).
\tag{5.5}
\]

If (5.3) were shape-constant on \(U\), the real-analytic function \(F\) would be constant on an open subinterval of \((0,1)\), hence throughout \((0,1)\). This contradicts

\[
\lim_{x\uparrow1}F(x)=0,
\qquad
\lim_{x\downarrow0}F(x)=-C_2R<0.
\]

The pair and triangle identities therefore cannot hold simultaneously. \(\square\)

The finite-radius curvature of the original manuscript is not the decisive obstruction. A different nonnegative radial law can make the pair residual exact. Here is an explicit check. At unit intensity, put

\[
f(r)=p(r)b(r)^2r^2.
\]

Equations (3.1), (4.1) and the pair target require

\[
2\pi\int_{D/2}^{L}f(r)\,dr=C_2-D,
\qquad 0<D\le M.
\tag{5.6}
\]

Choose any \(C_2\ge M\). If \(C_2>M\), a strictly positive tail is required and we choose \(L>M/2\). The same choice of \(L>M/2\) is harmless when \(C_2=M\). Define explicitly

\[
f(r)=\frac1\pi\mathbf1_{(0,M/2)}(r)
+\frac{C_2-M}{2\pi(L-M/2)}\mathbf1_{(M/2,L)}(r).
\tag{5.7}
\]

This function is nonnegative and integrable, and its tail integral is exactly \((C_2-M)/(2\pi)\). Let

\[
a=4\pi\int_0^Lf(r)r\,dr>0,
\qquad b(r)=\frac ar,
\qquad p(r)=\frac{f(r)}{a^2}.
\tag{5.8}
\]

Then \(p\) is nonnegative and integrable, \(4\pi r^2b(r)=4\pi ar\) is bounded, (2.3) gives \(\lambda=1\), and (5.6) holds. Thus the full pair density is exactly \(m_2=C_2/D\) for \(0<D\le M\). Scaling the directing measure gives any prescribed intensity. Proposition 3 shows that the obstruction enters at the full third-order density.

### 6. Finite-pointwise-second-moment fields and LGCPs

**Proposition 4.** Let \(\Lambda(dx)=Z(x)dx\), where \(Z\ge0\) is a jointly measurable stationary random field, \(0<\mathbb EZ(0)=\lambda<\infty\), and \(\mathbb EZ(0)^2<\infty\). Its Cox process cannot satisfy \(g_2=C_2/D\) almost everywhere on \(\mathcal D_2\), with \(C_2>0\).

**Proof.** A version of the second moment density is

\[
m_2(x,y)=\mathbb E[Z(x)Z(y)].
\]

Stationarity and Cauchy--Schwarz give \(m_2(x,y)\le\mathbb EZ(0)^2<\infty\) almost everywhere. The required density \(\lambda^2C_2/|x-y|\) exceeds this bound on a positive-measure set of sufficiently close distinct pairs. \(\square\)

This proof does not cover an integrable spike field with infinite pointwise second moment, and finite fourth moments of \(\Lambda(B)\) do not imply \(\mathbb EZ(0)^2<\infty\).

For an ordinary log-Gaussian Cox process, the directing density is \(e^{Y(x)}\) for a finite-variance stationary Gaussian field. Møller, Syversveen and Waagepetersen give

\[
g_n(x_1,\ldots,x_n)=\prod_{i<j}g_2(x_i,x_j).
\tag{6.1}
\]

Such a process is already excluded by Proposition 4. Independently, if its pair law held, then for a triangle with sides \(a,b,c\),

\[
g_3=\frac{C_2^3}{abc}=\frac{C_2^3}{4AR_3}.
\]

Equality with \(C_3/A\) would force \(R_3=C_2^3/(4C_3)\) on a positive-measure triangle domain, which is impossible.

### 7. The exact finite-cluster witness is not Cox

**Proposition 5.** The finite dependent-cluster process constructed in `common/prior_work/finite-cluster-reciprocal-laws/` is not a Cox process.

**Proof.** Its type-four parent rate is \(Z_4/4!>0\), its cluster offsets are bounded, and its four-point mark density is positive on an open set. Choose as \(B\) a sufficiently large bounded positive-Lebesgue-measure Borel window, for example a large open ball. Then a positive finite intensity \(\nu_4(B)>0\) of parents has all four daughters in \(B\). This is the single nontrivial window used in the argument; no count-law assertion is needed for null windows or for every bounded set.

For every parent type, the number of daughters in this \(B\) belongs to \(\{0,1,2,3,4\}\). Only parents in a bounded enlargement of \(B\) can contribute. Poisson marking and superposition therefore give

\[
G_B(z)=\mathbb Ez^{X(B)}
=\exp\left\{\sum_{j=1}^4\nu_j(B)(z^j-1)\right\},
\tag{7.1}
\]

where every \(\nu_j(B)<\infty\) and \(\nu_4(B)>0\).

If the process were Cox, \(X(B)\) would be mixed Poisson: for the nonnegative variable \(L=\Lambda(B)\),

\[
G_B(1-s)=\mathbb Ee^{-sL},\qquad 0\le s\le1.
\tag{7.2}
\]

The right side is holomorphic on \(\{\operatorname{Re}s>0\}\), while the expression obtained from (7.1) is entire. Equality on \((0,1)\) and the identity theorem extend (7.2) to every real \(s>0\). Yet

\[
\exp\left\{\sum_{j=1}^4\nu_j(B)((1-s)^j-1)\right\}\longrightarrow\infty
\]

as \(s\to\infty\), because the exponent has leading term \(\nu_4(B)s^4\). A Laplace transform of a nonnegative random variable is at most one. This contradiction proves the proposition. \(\square\)

The conclusion concerns this particular process law. It does not exclude another Cox directing measure with the same restricted product densities.

### 8. Necessary conditions for a general Cox witness

The unresolved problem is a nonnegative random-measure moment problem. Two necessary checks illustrate what is known and what remains free.

For a ball \(B_R\) with \(2R\le M\), the pair target and diffuseness determine

\[
\mathbb E\Lambda(B_R)^2
=\lambda^2C_2\iint_{B_R^2}\frac{dx\,dy}{|x-y|}.
\]

The overlap-volume integral is

\[
\iint_{B_R^2}\frac{dx\,dy}{|x-y|}
=\frac{32\pi^2R^5}{15},
\qquad |B_R|^2=\frac{16\pi^2R^6}{9}.
\]

Jensen's inequality gives \(C_2\ge5R/6\). Taking \(R=M/2\) yields the general necessary condition

\[
C_2\ge\frac{5M}{12}.
\tag{8.1}
\]

Because \(C_2\) is a free positive constant, this is not a contradiction.

For a bounded \(B\), set \(\mu_k(B)=\mathbb E\Lambda(B)^k\) and \(\mu_0=1\). Nonnegativity of \(\Lambda(B)\) requires

\[
\begin{pmatrix}
1&\mu_1&\mu_2\\
\mu_1&\mu_2&\mu_3\\
\mu_2&\mu_3&\mu_4
\end{pmatrix}\succeq0,
\qquad
\begin{pmatrix}
\mu_1&\mu_2\\
\mu_2&\mu_3
\end{pmatrix}\succeq0,
\tag{8.2}
\]

with mixed analogues for several test functions. The pair covariance kernel \(m_2-\lambda^2\) must likewise be positive semidefinite as a bilinear form.

These conditions do not close the problem. Any bounded positive-measure window contains positive-measure families of triangles below the altitude cutoff and tetrahedra below the tetrahedral altitude cutoff. Their third and fourth densities are not prescribed. Hence the target identities do not determine \(\mu_3(B)\), \(\mu_4(B)\), or all repeated-region entries in mixed moment matrices. Extending the reciprocal formulas to those omitted configurations would change the problem and could manufacture a false contradiction.

## Reasoning summary and decision record

1. I formulated the Cox step in both directions. The forward direction lifts a stationary diffuse directing measure to a stationary simple point process with the required moments and densities. The converse uses uniqueness of the Cox directing law, the diagonal mass of \(\mathbb E\Lambda^{\otimes2}\), and the fourth mixed-Poisson moment. This justifies calling the remaining question a directing-measure moment problem rather than only a sufficient ansatz.
2. I made the sphere-incidence step measure-theoretic. The nonnegative coarea identity applies to the measurable weights \(p(r)b(r)^j\), the orthogonal fibre has dimension \(4-j\), and the normal-Jacobian ratio is \(r^{j-1}/((j-1)!\Delta_{j-1})\). Local finiteness converts the extended-valued coarea expression into a locally integrable density. At order four the formula uses one fixed Borel version of \(p b^4\), with version independence only asserted almost everywhere.
3. A finite-cutoff curvature argument would exclude the original sphere parameters but not the entire radial class. The explicit construction (5.7)--(5.8) confirms that radial mixing can repair the full pair law. The robust obstruction is instead that \(Aq_3\) depends only on circumradius. Combining this with every order-three partition forces a shape-constant expression that the fixed-radius isosceles family disproves.
4. I tested two possible bridges beyond the sphere class. Finite-pointwise-second-moment intensity fields cannot create the required pair singularity, and the specific exact finite-cluster witness has a non-mixed-Poisson count distribution in one large positive-measure window. Neither argument covers arbitrary diffuse random measures.
5. Window moment positivity yields (8.1) and (8.2), but the prescribed identities leave lower-altitude third- and fourth-order configurations free. I therefore retain the general Cox problem as unresolved rather than filling the omitted configurations by an unrequested formula.

## Checks and limitations

- **Analytical checks.** Proposition 1 proves both directions of the Cox reduction. Lemma 2 is an equality of locally finite measures against nonnegative test functions, not a formal pointwise change of variables. Equations (3.1) contain every carrier partition through order four. Proposition 3 uses the full \(g_3\), including lower-order carrier partitions. Proposition 5 uses an exact distribution in one explicitly nontrivial window.
- **Symbolic and numerical evidence.** No numerical result is used as proof. Formula (5.4) follows algebraically from \(A=abc/(4R)\); the two endpoint limits of (5.5) give the contradiction.
- **Empirical evidence.** None is used. Published earthquake summaries and the manuscripts' simulations do not decide the exact existence question.
- **Exact remaining gap.** For each admissible \((M,h_3,h_4)\), construct or rule out a stationary diffuse locally finite random measure \(\Lambda\) of one positive intensity, with \(\mathbb E\Lambda(B)^4<\infty\) for bounded \(B\), absolutely continuous \(\mathbb E\Lambda^{\otimes n}\) through order four, and the three prescribed moment densities. Corollary 1 would then supply every \(\lambda_0>0\).
- **Class limits.** Proposition 3 assumes Poisson centres and uniform surface weight on each sphere. Dependent carriers, nonuniform marked surfaces, non-spherical carriers and non-Poisson carrier populations may have further shape dependence. Proposition 4 assumes a finite pointwise second moment. Proposition 5 concerns one finite-cluster law only.
- **Domains.** No positive pair cutoff, extra face condition on \(\mathcal D_4\), tail identity beyond \(M\), mixing assumption or isotropy requirement has been added.

## References

1. G. Last and M. Penrose, *Lectures on the Poisson Process* (2017), Chapter 13, Proposition 13.6 and equations (13.8)--(13.10), author PDF pp. 141--142 / printed pp. 130--131. The frozen dossier records full-text verification. Equation (13.10) supplies \(\alpha_X^{(n)}=\mathbb E\Lambda^{\otimes n}\).
2. J. Møller, A. R. Syversveen and R. P. Waagepetersen, “Log Gaussian Cox Processes”, *Scandinavian Journal of Statistics* 25 (1998), Theorem 1, equation (2), printed pp. 455--456 / checked PDF pp. 7--8. The frozen dossier records full-text verification. It supplies (6.1).
3. L. Simon, *Introduction to Geometric Measure Theory* (2014 Tsinghua lectures), Chapter 2, Section 6, equation (6.3), printed p. 66, and Chapter 3, Section 2, equations (2.5), (2.9), printed p. 77. The frozen spherical manuscript's source audit records full-text verification of the smooth area--coarea interfaces; the normal-Jacobian calculation needed here is reproduced in Lemma 2.
4. *Reciprocal simplex correlations from random spherical surfaces*, frozen local unpublished manuscript at `common/prior_work/reciprocal-simplex/`, especially Sections 3--5 and `MATH_CHECK.md`. Complete source tree inspected. Its `main.tex` SHA-256 is `344c53bd4e9e1bbff7e95b138de68e21883ad0d683f56276d9e095ff22e5b8bd`.
5. *Exact reciprocal simplex correlations on finite domains*, frozen local unpublished manuscript at `common/prior_work/finite-cluster-reciprocal-laws/`, especially Section 4 and Appendices A--D. Complete source tree inspected. Its `main.tex` SHA-256 is `65255329d4f352f74603f1b846ab22416794d502ec75c508a2142ffd51df2fa2`.

## Response to review (v02 onward)

1. **R2-V01-01 — unresolved governing scope.** Preserved. The claim line, opening scope, Corollary 1, Section 8 and the limitations all state that arbitrary Cox existence is unresolved. The proved results remain reductions and subclass exclusions.
2. **R2-V01-03 — incidence/absolute continuity.** Repaired in Lemma 2. It treats measurable \(p(r)b(r)^j\), exhibits the orthogonal fibre \(E^\perp\), derives the factor \(((j-1)!\Delta_{j-1})^{-1}\), states the almost-everywhere density conclusion, proves local finiteness in (2.7), and fixes a Borel version of \(p b^4\) while explaining why another version changes the tuple density only on a null set.
3. **R2-V01-04 — equivalence wording.** Repaired by proving the converse in Proposition 1. Stationarity of the directing law follows from the determining Cox Laplace functional; simplicity forces almost-sure diffuseness through diagonal second-moment mass; finite fourth count moments force finite fourth directing-mass moments; and the Cox factorial identity supplies the tensor-moment densities.
4. **R2-V01-05 — pair-only repair choices.** Repaired in (5.7). The submission states \(L>M/2\) when \(C_2>M\) requires positive tail mass and chooses the tail explicitly as the constant \((C_2-M)/(2\pi(L-M/2))\), which is nonnegative and integrable. The zero-tail case \(C_2=M\) is also covered.
5. **R2-V01-08 — window qualification.** Repaired in Proposition 5. The non-Cox test now uses one sufficiently large bounded positive-measure Borel window, concretely a large open ball, and explicitly makes no claim for null windows or every bounded set.
6. **Validated subclass scopes.** Preserved separately: Proposition 3 concerns Poisson-centred, radius-only uniformly weighted sphere mixtures; Proposition 4 concerns finite-pointwise-second-moment intensity fields and ordinary LGCPs; Proposition 5 concerns only the specific finite-cluster witness. None is promoted to general Cox non-existence.
