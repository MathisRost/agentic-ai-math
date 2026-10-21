# Final independent synthesis — S0, S1 and all frozen submissions

- **Verdict:** S0 is impossible at every positive prescribed intensity. The actual law in proof_4 v04 establishes S1 for every independently prescribed pair \((\lambda_0,M)\in(0,\infty)^2\). Its full factorial measures of orders 2–4 are globally Lebesgue absolutely continuous with finite-almost-everywhere densities. The exact reciprocal identities hold on the entire nondegenerate diameter-below-\(M\) domains. No blocking mathematical gap was found in the consequential dependencies reconstructed below.
- **Reviewer:** `/root/final_synthesis`, fresh independent cross-track synthesis, actual runtime `gpt-6-astra`, effort `xhigh`; no delegation or new construction submission.
- **Own runtime:** session `session-25`, turn `turn-37`; turn-context timestamp `2026-10-20T19:25:01.188Z`. Preflight boundary `2026-10-20T19:25:43.236749+00:00`; evidence in `runtime_preflight.json`. Final freeze time and latest exposed counters are in the separate freeze/accounting artifacts.
- **Original packet:** `packets/final_synthesis.json`, SHA-256 `f925bb7962b0ce75a1158cd3654971cab27e8fc5004f04aeb948c2f8742b102d`; all 109 allowed-file hashes verified before mathematical work.
- **Sole later input:** administrative addendum `packets/final_synthesis_administrative_01.json`, SHA-256 `a0af789139ac8568f3947e9d106f5a742f95ff124d2e258d92131bb3c8b83183`; all 52 allowed-file hashes verified. Its historical packet references did not expand mathematical reading permission.
- **Context:** frozen statements, submissions, reviews, specified source dossier, governing instructions, and administrative snapshots. Excluded: author/coordinator conversations, private work, unassigned seeds/sources, old runs and other chats. Earlier review labels and the coordinator's outcome summary were claims to audit, not premises. The frozen proof-reviser skill and its required proof/writing references were applied.

All paths below are relative to `runs/20261020T164437Z_astra6/` unless indicated otherwise. This is an informal mathematical audit with explicit proofs and scope limits, not formal machine certification or a novelty assessment.

## Correctness verdict and scope

Write \(D=|x_1-x_2|\), \(A\) for triangle area, \(V\) for tetrahedron volume, and \(E_n(M)\) for ordered nondegenerate \(n\)-tuples of diameter strictly below \(M\). Factorial measures count ordered distinct points. Full densities include every allocation of the points; connected or same-parent contributions alone are insufficient.

S0, SHA-256 `3b5b5ad81bf56136bd79f0fde2d4aa39e3bed32aaf37511460007dfb0fc656f0`, requires the three reciprocal identities without a diameter cap. It is false even without a finite-fourth-moment assumption. The pair law alone contradicts large-volume count inequalities; independent triangle and fourth-tail arguments reinforce this conclusion.

S1, SHA-256 `1075eb6bd3d54d5e0ddec1a1adee1fd30e474accb715304f42c46f21176226e8`, retains every positive prescribed intensity and every independently prescribed finite positive diameter cap. It requires one stationary simple locally finite process, positive finite process-dependent constants \(a_2,a_3,a_4\), and full globally absolutely continuous factorial measures through order four, with densities finite almost everywhere. Only the reciprocal identities are restricted to \(E_n(M)\). There is no lower distance, area, volume or shape cutoff, no finite-fourth-moment assumption, and no required ergodicity, mixing or isotropy. The constants are not independently prescribed by the owner.

The successful proof is `tracks/proof_4/submissions/v04.md`, SHA-256 `e3f403b4c55b69845e83ea74d7348026a86cd9b36691b1a4cdc9a6983ac3df5f`. I independently reconstructed its probability law, parameter choices, normalization, local coarea identities, all-allocation global absolute continuity, and finite-a.e. fourth density. The earlier review, SHA-256 `680b32c05642871d0207ffe59e4bc04d65d6a3bca26a06d61d96e60a2d031e7c`, is consistent with this audit but is not its justification.

Every S1 process has finite third moments on bounded sets and infinite fourth moments on every nonempty ball. These facts are compatible with almost-sure local finiteness and with a finite-a.e. fourth density. The successful law is necessarily outside the Cox class by the independently reconstructed Cox obstruction. The Poisson-cluster and Hawkes/branching tracks retain substantial partial results and scoped negative theorems; their unsuccessful attempts do not imply general impossibility.

## Reconstruction and detailed audit

### 1. S0 and the local moment distinction

For \(N_R=X(B_R)\), the global pair identity yields
\[
\mathbb E(N_R)_2=a_2\int_{B_R^2}|x-y|^{-1}\,dx\,dy=O(R^5),
\qquad \mathbb EN_R=\lambda_0|B_R|=\Theta(R^3).
\]
The integral is finite, so the second moment is derived, not assumed. Variance nonnegativity would require \(\mathbb E N_R^2\geq(\mathbb EN_R)^2=\Theta(R^6)\), a contradiction for large \(R\). The same reasoning independently works at order three: the reciprocal-area integral is finite and scales as \(R^7\), whereas \((N-2)_+^3\leq(N)_3\) and Jensen require growth of order \(R^9\). Cylindrical coordinates perpendicular to a fixed pair give the needed local integrability of \(1/A\). No fourth-moment hypothesis enters either argument.

The strengthened fourth-tail theorem in nonexistence_1 v02 is stronger than a finite-moment exclusion. It excludes any stationary positive-intensity process whose fourth factorial measure, on all sufficiently large-diameter noncoplanar tuples, is bounded by \(a/V\). A concise reconstruction is as follows. Let \(p>0\) be the probability that a unit cube is occupied, and let \(Y_m\in[0,1]\) be the average of the occupancy indicators of the \(m^3\) unit cubes in a large cube. Then \(\mathbb EY_m=p\) and \(\mathbb EY_m^4\geq p^4\), without any count-moment assumption. Express this fourth power as an integral over four points of the unit cube, mapped to their grid cells. The set on which their tetrahedron volume is at most \(\varepsilon\) has measure \(b_\varepsilon\to0\). On its complement, replacing those scaled positions by any four points in their cells changes normalized volume by at most \(3\sqrt3/m\). For sufficiently large \(m\), these are distinct cells and every such quadruple has volume at least \(\varepsilon m^3/2\) and diameter tending to infinity. The probability that all four cells are occupied is bounded by the expected ordered count of quadruples, hence by \(2a/(\varepsilon m^3)\). Thus
\[
p^4\leq b_\varepsilon+\frac{2a}{\varepsilon m^3},
\]
which is impossible after first choosing \(\varepsilon\) and then \(m\). Stationarity supplies the common occupancy probability; ergodicity and mixing are unused. This proves an obstruction for the broad S0 class, including infinite local fourth moments.

The separate local obstruction is different. For a base triangle of area bounded away from zero and a fourth point at normal height \(h\),
\[
V=\frac{A|h|}{3},\qquad \int_{-\delta}^{\delta}\frac{dh}{|h|}=\infty.
\]
This divergence can occur near an ordinary planar square while all six edges and all four face areas stay bounded away from zero. Thus reciprocal fourth density on \(E_4(M)\) gives \(\mathbb E(X(B))_4=\infty\) for every nonempty ball. This does not prove that \(X(B)=\infty\) with positive probability. Conversely, pair and triangle integrability gives finite third moments for sufficiently small balls; a finite covering and \((\sum_{i=1}^k N_i)^3\leq k^2\sum_iN_i^3\) gives finite third moments on all bounded sets.

The nonexistence_2 counterexample correctly separates these notions: Poisson clusters with population distribution proportional to \(n^{-5}\) and iid uniform offsets in a ball of radius \(1/(10n)\) have finite intensity and third local moments, infinite fourth local moments, and finite-a.e. full densities. For a fixed distinct tuple in a common-parent block, the shrinking diameter allows only finitely many population sizes. All parent partitions are then controlled. This is a counterexample to an invalid moment inference, not a reciprocal-density construction.

### 2. The final sphere component is an actual stationary law

Fix arbitrary \(\lambda=\lambda_0>0\) and \(M>0\). Define
\[
\kappa=\frac1{36e\pi M^3},\quad
\lambda_C=\min(\lambda,\kappa/2),\quad
\lambda_Y=2\lambda-\lambda_C>0,\quad
C_0=\frac{\pi^{3/2}}{3\sqrt3}.
\]
Choose a finite sufficiently large \(K\) and put
\[
c=\sqrt{C_0K^3/\lambda_Y},\qquad
F=K^4/c^3=\frac{\lambda_Y^{3/2}}{C_0^{3/2}\sqrt K}
\leq\frac1{10000M}.
\]
A later choice of \(L\geq M\) does not disturb this inequality. Set
\[
f(q)=\frac K L e^{-q/L^2},\qquad
a(R)=\frac c{f(R^2)},\qquad
\gamma(R)=\frac{2R f(R^2)^4}{c^3}.
\]
The law does not postulate a Poisson process of mutually separated spheres. It constructs a separated random family with the required first sphere intensity. Let \(H=2M\), \(b_k=2^kM\), \(P_k=4b_k+2M\), with radius bands \(I_0=(0,M]\) and \(I_k=(b_k/2,b_k]\) for \(k\geq1\). Give band \(k\) probability
\[
p_k=HP_k^3\sup_{R\in I_k}\gamma(R),
\]
and use the remaining probability for no spheres. Conditional on the band, take a uniform lattice shift \(Z\in[0,P_k)^3\), a uniform radial phase \(U\in[0,H)\), and candidates with centres \(Z+P_km\) and radii \(U+jH\in I_k\). Independently retain each candidate with probability \(\gamma(R)HP_k^3/p_k\leq1\). This countable construction is measurable and yields the exact first sphere intensity \(\gamma(R)\,dz\,dR\).

The probability budget is uniform in the subsequent \(L\). For \(t_k=b_k/L\),
\[
p_0\leq864FM(M/L)^4,\qquad
p_k\leq864FM t_k^4e^{-t_k^2}.
\]
Splitting the dyadic sum at \(t_k=1\) bounds it by \(16/15+8\), so \(\sum p_k<9000FM\leq0.9\). There is therefore a genuine nonnegative empty-band probability. Neither a limiting probability measure nor a signed measure is being used.

On each retained sphere put an independent Poisson process with intensity measure \(a(R)\sigma_{z,R}/(2R)\), where \(\sigma_{z,R}\) is surface area. At a fixed band, a bounded region meets finitely many candidates. The realized directing measure is locally finite and nonatomic; the conditional Poisson law is simple and locally finite. The uniform shift makes the process stationary under arbitrary translations; relabelling the iid retention marks causes no problem. Isotropy and ergodicity are unnecessary and are not asserted.

Surfaces at the same centre are at least \(H=2M\) apart. At distinct centres their separation is at least \(P_k-2b_k=2b_k+2M>M\). Consequently every tuple of diameter below \(M\) lies on a single sphere. This is the reason its local full factorial density can be calculated from one-sphere contributions without omitted cross-sphere terms.

Translation integration gives \(\int\sigma_{z,R}(B)\,dz=4\pi R^2|B|\). Thus the mean intensity is exactly
\[
2\pi\int_0^\infty\gamma(R)a(R)R\,dR
=\frac{2\pi}{c^2}\int_0^\infty\sqrt q\,f(q)^3\,dq
=\frac{\pi^{3/2}K^3}{3\sqrt3c^2}=\lambda_Y.
\]
The apparent dependence on the later scale \(L\) cancels. This cancellation is essential to the all-parameter conclusion.

### 3. Coarea constants and the three local densities

Use the nonnegative surface-measure identity
\[
\delta(|x-z|^2-q)\,dx=\frac{\sigma_{z,\sqrt q}(dx)}{2\sqrt q}.
\]
It is shorthand for integration in regular coordinates, not an unsupported multiplication of distributions. After \(q=R^2\), the scalar weights are
\[
w_n(q)=\frac{\gamma(\sqrt q)a(\sqrt q)^n}{2\sqrt q},
\qquad w_4=c,\quad w_3=f,\quad w_2=f^2/c,\quad w_1=f^3/c^2.
\]
For a pair at distance \(D\), the difference of squared-distance constraints has Jacobian \(2D\); integration over the perpendicular centre plane contributes \(\pi\). For a triangle, the two linear constraints give Jacobian \(4|u\times v|=8A\); the remaining centre coordinate is the normal height. For a noncoplanar quadruple, the four constraints in \((z,q)\) have absolute determinant \(8|\det(u_2,u_3,u_4)|=48V\), with a unique circumsphere. These calculations give, on the full domains \(E_n(M)\),
\[
r_2=\frac{A_2}{D}e^{-D^2/(2L^2)},\qquad
r_3=\frac{A_3}{A}e^{-R_\triangle^2/L^2},\qquad
r_4=\frac c{48V},
\]
where \(A_2=\pi K^2/(4c)\), \(A_3=K\sqrt\pi/8\), and \(R_\triangle\) is the triangle circumradius. There is no extra \(n!\): the Poisson factorial measure already counts ordered tuples. Large circumradii of nearly collinear or coplanar configurations are included, not cut off.

### 4. Global absolute continuity and finite-a.e. density

The local formulas do not by themselves prove S1's global requirement. The following two separate arguments close it.

At a fixed band, expand the conditional factorial measure \(\Lambda^{\otimes n}\), \(n\leq4\), over **all** choices of sphere indices. For one such allocation,
\[
x_i=Z+P_km_i+(U+j_iH)\omega_i,\qquad \omega_i\in S^2.
\]
The angular derivatives span each sphere's tangent plane. After quotienting those tangent directions, derivatives in \((Z,U)\) have rows \((\omega_i^T,1)\). These rows have rank \(n\) for almost every collection of directions when \(n\leq4\): for four directions, the last one would otherwise lie in the affine plane of the first three, whose intersection with the sphere has surface measure zero. The lower-order cases follow similarly. Positive radii fail only on phase-null boundaries. Local coordinate charts, the ordinary change-of-variables/submersion argument and Fubini therefore make every allocation absolutely continuous. Measurable retention and amplitude weights preserve this conclusion, and there are only countably many allocations and bands. This argument includes repeated sphere indices and different-centre allocations; it is not restricted to eligible short tuples.

At a fixed band the directing mass on a bounded set has a deterministic finite bound, so its fourth moments are locally finite and its densities finite a.e. A countable mixture of such densities could nevertheless be infinite on a positive-measure set. Two further estimates are needed.

First, for a bounded set inside a ball of radius \(r\), the number \(J_B\) of candidate spheres meeting it is bounded uniformly over bands: centre spacing is proportional to \(b_k\), and the radial grid spacing is \(H\). Sphere intersection area is at most \(C_B=4\pi r^2\). Writing the mass of one sphere in \(B\) as \(m\), the inequality \((\sum m)^3\leq J_B^2\sum m^3\), followed by translation integration, bounds \(\mathbb E\Lambda(B)^3\) by a finite multiple of
\[
\int_0^\infty\frac{\gamma(R)a(R)^3}{R}\,dR
=2\int_0^\infty f(R^2)\,dR=K\sqrt\pi.
\]
The area integration controls the small-radius endpoint. Conditional Poisson moments then give finite local third moments, and hence finite-a.e. global densities through order three.

For order four take a noncoplanar tuple, anchor \(x_1=0\), and let \(W\) have rows \(u_i^T=(x_i-x_1)^T\), \(i=2,3,4\). In sufficiently large bands the surface separation prevents different centres from contributing to this fixed bounded-diameter tuple. For concentric radii \(R+Hm_i\), reverse triangle inequality gives \(|Hm_i|\leq D\), leaving finitely many integers in a bounded neighbourhood of the tuple. With \(n=z/R\) and \(b_i=|u_i|^2-H^2m_i^2\), subtraction of the squared-distance equations yields
\[
Wn=-Hm+\frac b{2R},\quad |n|=1,
\qquad
R\big|1-H|W^{-1}m|\big|\leq\tfrac12|W^{-1}b|.
\]
For nonzero \(m\), the exceptional equality \(H|W^{-1}m|=1\) is the zero set of the nonzero polynomial
\[
H^2|\operatorname{adj}(W)m|^2-\det(W)^2.
\]
It is not identically zero, as evaluation at \(W=tI\) shows. For \(m=0\) the equality is impossible. Away from the countable union of these null sets and the coplanar set, a sufficiently small neighbourhood has bounded \(W^{-1}\), only finitely many relevant \(m\), and a positive minimum gap from the exceptional equalities. The displayed inequality bounds \(R\) uniformly there. Thus only finitely many bands contribute on this neighbourhood. Their fourth measures are locally finite, so the density is finite a.e. A countable cover proves the desired global statement. The earlier absolute-continuity argument already excludes any singular mass on the exceptional sets.

This is the strongest technical dependency of the final proof. It is valid and cannot be replaced by merely checking \(r_4=c/(48V)\) on \(E_4(M)\). At degenerate tuples one may assign arbitrary finite values to a density version; these sets carry no factorial mass. Infinite integrals in neighbourhoods of coplanarity are permitted and required.

### 5. Positive residuals, a genuine correction law, and joint feasibility

Define, with zero values outside the eligible domains,
\[
q_3=\mathbf1_{E_3(M)}\frac{A_3}{A}
       (1-e^{-R_\triangle^2/L^2}),
\qquad
q_2=\frac{\mathbf1_{E_2(M)}}D
       [\delta+A_2(1-e^{-D^2/(2L^2)})],
\]
where \(B_L=8\pi A_3M^3/L\) and \(\delta=2B_L\). Let \(\mathcal Mq_3(x_1,x_2)=\int q_3(x_1,x_2,z)\,dz\). If the pair length is \(d\) and the third point is at distance \(r\) from its line, then \(A=dr/2\) and \(R_\triangle\leq M^2/(2r)\). Using \(1-e^{-t}\leq\min(1,t)\), cylindrical coordinates yield
\[
d\,\mathcal Mq_3\leq8\pi A_3M
 \int_0^M\min\{1,M^4/(4L^2r^2)\}\,dr\leq B_L.
\]
This is uniform even near pair coalescence and triangle degeneracy. Therefore
\[
F_3=q_3,\qquad F_2=q_2-\mathcal Mq_3\geq B_L\mathbf1_{E_2(M)}/D>0.
\]
Both kernels are symmetric, translation invariant and have finite anchored integrals. Set \(Q_j=\int q_j(0,\cdot)\), \(Z_3=Q_3\), \(Z_2=Q_2-Q_3\). In particular \(Z_2,Z_3>0\). The bound
\[
Q_2\leq\frac{32\pi^2 A_3M^5}{L}
            +\frac{\pi A_2M^4}{2L^2}
\]
allows the explicit finite choice
\[
L=\max\left\{M,\frac{128\pi^2A_3M^5}{\lambda_C},
                  M^2\sqrt{\frac{2\pi A_2}{\lambda_C}}\right\},
\]
which gives \(Q_2\leq\lambda_C/2\). The choice occurs after \(K,c\); the sphere probability budget was uniform in \(L\). There is no circular parameter requirement and no upper bound on \(\lambda M^3\).

For the correction law take Poisson centres of intensity \(\eta=1/(36\pi M^3)\), retaining only centres with no other centre within distance \(3M\). The exclusion ball has volume \(36\pi M^3\), so the retained intensity is \(\eta e^{-1}=\kappa\). Retained centres are dependent; only their first intensity is used in the local calculation. At each retained centre emit an empty, singleton, two-point or three-point cluster. For sizes two and three use the anchored offset probability densities \(F_j/Z_j\). Define
\[
\beta=\lambda_C-Q_2+Q_3/2=\lambda_C-Z_2-Z_3/2,
\quad
\pi_1=\beta/\kappa,\quad
\pi_2=Z_2/(2\kappa),\quad
\pi_3=Z_3/(6\kappa).
\]
Here \(\beta\geq\lambda_C/2>0\), and
\[
\kappa(\pi_1+\pi_2+\pi_3)
=\lambda_C-Q_2/2+Q_3/6\leq\lambda_C\leq\kappa.
\]
Thus \(\pi_0=1-\pi_1-\pi_2-\pi_3\geq0\). The expected cluster size times \(\kappa\) is exactly \(\lambda_C\).

Every cluster has diameter below \(M\), and its points lie within \(M\) of its centre. Different retained centres are more than \(3M\) apart, so their emitted points are more than \(M\) apart. Every eligible tuple therefore lies in one cluster. Reanchoring a symmetric translation-invariant \(F_j\) has Jacobian one. The ordered selection coefficients \(j!/(j-n)!\), together with the probabilities above, give
\[
\rho_C^{(2)}=F_2+\mathcal MF_3=q_2,\qquad
\rho_C^{(3)}=F_3=q_3,\qquad
\rho_C^{(4)}=0\quad\hbox{on }E_4(M).
\]
This checks all local allocations and the factors \(2\) and \(6\).

Global regularity of \(C\) is obtained by placing the same marks on every centre before thinning. The resulting unthinned Poisson cluster process \(C^\sharp\) dominates \(C\). Its bounded counts are at most three times the number of original centres in the \(M\)-enlargement, so it has moments of every order. Its anchored offset kernels are ordinary Lebesgue densities, and its full factorial measures are sums over all parent partitions, hence globally absolutely continuous. Measure domination transfers global absolute continuity and local finiteness of these factorial measures to \(C\). This step does not pretend that the retained centres are Poisson.

### 6. Final mixture and reconciliation with the negative theorems

Choose a fair coin once for the entire process and use the law of \(Y\) or the law of \(C\) accordingly. This is a mixture of whole probability laws. Its intensity is
\[
(\lambda_Y+\lambda_C)/2=\lambda,
\]
and for every nonnegative factorial test, including tests with infinite integral,
\[
\alpha_X^{(n)}=\tfrac12\alpha_Y^{(n)}+\tfrac12\alpha_C^{(n)}.
\]
There are no cross-alternative tuples. The local identities are exactly
\[
\rho_X^{(2)}=\frac{A_2+\delta}{2D},\qquad
\rho_X^{(3)}=\frac{A_3}{2A},\qquad
\rho_X^{(4)}=\frac c{96V}.
\]
All three constants are positive and finite. The global regularity just established is preserved by the finite mixture. Stationarity, simplicity, almost-sure local finiteness and prescribed intensity are preserved as well. This proves every S1 requirement for every \(\lambda,M>0\), using finite parameters and an actual probability law.

The intermediate law \(Y\) is Cox. Its third density contains the circumradius attenuation, so it does not satisfy the exact reciprocal-area premise of the Cox exclusion. The final law \(X\) does satisfy that premise and a positive reciprocal fourth law, and therefore is **not** Cox. A mixture involving a non-Cox component would not alone prove this assertion; the exclusion theorem does. Likewise, independent-superposition obstructions do not apply to this whole-law mixture. Earlier slab-plus-finite-fourth-correction intensity ceilings assume the specific slab component, whose coalescing lower contributions vanish; the new sphere component has different pair behaviour. They impose no ceiling on this construction.

### 7. Cox exclusion: the exact scope and proof mechanism

Proof_2 v01, SHA-256 `4e2b6a17c32546ab2a6b4be629027e3b2618336753c805bf5bbf212f9cd89e7f`, excludes **all Cox processes** from S1, including those with singular random directing measures. The proof does not merely exclude random intensity functions or a selected covariance family. No stationarity, pair identity or finite fourth moment is needed for its core contradiction.

For a locally finite nonnegative random measure \(\Lambda\), the Cox factorial measures are \(\Gamma_n=\mathbb E\Lambda^{\otimes n}\). Assume the full third measure on diameter-below-\(M\) tuples is exactly \(a_3/A\) with no singular part. For \(R=M/4\), a smooth compactly supported test \(\varphi\) in \(B_R\), and
\[
L\varphi(w)=w\cdot\nabla\varphi(w)+2\varphi(w),\qquad
F_\varphi(x)=\int L\varphi(y-x)\,\Lambda(dy),
\]
the third identity computes \(\mathbb E\int_W F_\varphi(x)^2\Lambda(dx)\). In polar coordinates \(w=ru,w'=sv\),
\[
\frac{dw\,dw'}{A(0,w,w')}=
\frac{2rs\,dr\,ds\,d\sigma(u)\,d\sigma(v)}{|u\times v|}.
\]
The angular integral of \(|u\times v|^{-1}\) is \(8\pi^3\); the full integral over \(B_R^2\) is \(4\pi^3R^4\). This proves absolute integrability of the signed expansion. The radial identity
\(\int_0^R rL\varphi(ru)\,dr=[r^2\varphi(ru)]_0^R=0\)
then makes the expected square zero. A countable dense family of tests, followed by local-finiteness continuity in the test norm, gives the dilation identities simultaneously for all tests at \(\Lambda\)-almost every centre.

In a sufficiently small open ball \(U\), if the full-measure set of such centres contains four affinely independent points, subtracting their dilation identities gives \(\int\partial_j\psi\,d\Lambda=0\) for all tests supported in \(U\) and all three directions. Mollification implies \(\Lambda|_U=c\,dx\). The original dilation identity has coefficient 2 in ambient dimension 3 and forces \(c=0\). Hence any nonzero restriction is supported in an affine plane. Its fourth product gives zero mass to noncoplanar quadruples, contradicting the positive density \(a_4/V\) there. With global fourth absolute continuity one can also note that a nonzero planar restriction would concentrate \(\Lambda(U)^4\) on a Lebesgue-null set, so it must vanish. The argument accounts for random planes and singular directing measures; they are not loopholes.

### 8. Poisson-cluster track: retained progress and failures

All four submissions of proof_1 fail exact S1. Their strongest retained results have different scopes.

**v01.** Algebraic residual cumulant kernels can be made pointwise positive for any \(\lambda,M\). This is not a realizing process. Actual clusters with bounded population, or finite fourth population moment, have finite fourth local moments and cannot meet S1. If population is independent of iid displacement geometry and its fourth factorial moment is infinite, the same-parent fourth measure is infinite on every set of positive common-parent kernel mass. That non-sigma-finite behaviour is incompatible with a finite-a.e. full density, which is sigma-finite. The scope is count-independent iid geometry. Population-dependent geometry, as used later, is not excluded. A further necessary observation is that infinite fourth mass near separated planar squares cannot be supplied solely by clusters whose diameters shrink to zero; large-diameter cluster contributions must carry infinite fourth weight at each relevant fixed scale. The actual small-intensity size-at-most-three construction realizes the lower pair and triangle laws, not the fourth law.

**v02.** A finite-radius cylinder family couples cluster population to thickness. Its type measure contains \(d\varepsilon/\varepsilon\), divided by the fourth population factorial, so first-to-third contributions are finite and can be made small while fourth weight survives. The inverse-width angular identity and the height integral
\[
\int_0^\infty\frac{(2\varepsilon-w)_+}{(2\varepsilon)^4}
 \frac{d\varepsilon}{\varepsilon}=\frac1{12w^3}
\]
produce a reciprocal-volume term multiplied by a finite-disc intersection factor \(F_R\), with \((1-M/R)^2\leq F_R\leq1\) on the target domain. Nonnegative two- and three-point cluster corrections give exact lower densities in the stated small-intensity range, and a uniform relative fourth approximation. Finite \(R\) leaves genuine shape dependence; choosing \(R\) large is not exact equality.

**v03.** The non-existence results are within specified cylinder families. A positive mixture of fixed finite radii cannot turn the intersection factor into a constant: shrinking configurations determine the total coefficient, while a planar square of positive side has strictly smaller disc intersection. For the stated expanding-radius inverse-width family, \(Vk_4\) tends to one universal coefficient along every bounded-diameter approach to degeneracy. A full fourth residual after exact lower laws instead requires different coefficients at an ordinary planar square and at a face-collapse with fixed opposite altitude. These are incompatible. Neither argument excludes all Poisson clusters.

The limit warning is substantial: a sequence of increasingly large cylinders can have rare heavy clusters whose intensities vanish, while its fourth factorial measures retain a nonzero reciprocal contribution. The actual laws converge locally even in total variation to a size-at-most-three cluster law, but fourth factorial integrals do not converge to those of the limit. The lower-order corrections converge through their integrable kernels; unbounded fourth observables lack uniform integrability. Taking a process limit therefore does not complete an exact construction.

**v04.** A radius-mixture of finite spherical clusters gives an exact same-parent density \(k_4=a/V\) globally on noncoplanar quadruples, with arbitrarily small intensity and lower contributions. Its population
\(N_T(R)=4+\lceil T(R/\ell+\ell/R)^8\rceil\)
and radius rate \(cR^5/(N_T(R))_4\) are genuine finite-cluster parameters; \(c=1536\pi^4a\). The common-sphere pair and triangle kernels and the fourth-radius evaluation give the stated coarea normalization. The radius density is crucial at fourth order; conditioning on a fixed radius alone would give a singular fourth measure. Bounds of order \(T^{-3},T^{-2},T^{-1}\) make the intensity, pair and triangle contributions small, respectively. This is a valid exact same-parent theorem with finite third and infinite fourth local moments.

After exact lower correction at small intensity, the **full** fourth density is \(a/V+B_4\), where all fourteen other parent partitions are present and \(B_4\geq\lambda^4\). Near an ordinary planar square the extra terms remain bounded, fixing the reciprocal coefficient at \(a\); their positivity then prevents exact fourth equality. They cannot be silently called connected-density errors or discarded.

The v04 cap construction adds a separate all-intensity partial theorem. Spherical caps with a radius uniform on \([M,2M]\), random direction and threshold have pair-inclusion probability \(1/2-D/(8R)\). Appropriate positive cap intensity and amplitude give a same-parent pair term \(A_{\rm cap}/D-\lambda^2\), with \(A_{\rm cap}=56\lambda^2M/9\), so the full pair background can be cancelled by an actual nonnegative cluster law. Combining caps, spheres, a pair correction and singleton fill yields the exact pair law at every \(\lambda,M\) and a uniform relative fourth approximation. It still fails the triangle law: near distinct collinear triples the cap contribution vanishes once their circumradius exceeds \(2M\); the sphere contribution times area tends to zero, as do the lower partitions times area. It cannot equal a positive constant \(a_3\). The fourth approximation's adjustable amplitude is not a prescribed-amplitude theorem.

### 9. Hawkes/branching track: retained progress and failures

All four proof_3 submissions fail exact S1. The later one-generation spherical examples are broader marked cluster constructions, not proofs for an arbitrary conventional Hawkes model.

**v01.** In the specified count-independent iid-displacement branching model with homogeneous Poisson immigrants and all generations observed, finite intensity forces mean offspring \(m<1\): expected generation size is \(m^j\). If the offspring fourth moment is finite, the recursive moment bounds give finite fourth total-progeny moment and hence finite fourth local count moments. If it is infinite, the four-direct-children term is infinite on a positive-Lebesgue-measure set: its integrated nonzero displacement kernel on a bounded product ball is \(\int q_B(z)^4\,dz\in(0,|B|]\). It therefore cannot have a finite-a.e. full fourth density. This covers the stated ordinary spatial branching/linear-Poisson-offspring cases, not count-dependent geometry or arbitrary marks. The source also treats a finite-window space-time projection under its stated assumptions. I checked the moment mechanism and the projection scope, but did not reconstruct every ancillary genealogy formula in that first manuscript. Infinite expected count in an all-time projection is not by itself an almost-sure non-local-finiteness proof.

**v02.** The marked one-generation Gaussian law is actual, simple, stationary and locally finite. Conditional mark \(v\) gives precision \(I+vv^T\), child mean \(1+|v|^2\), and parent mark rate \(c(1+|v|^2)^{-11/2}dv\), with observed roots and sterile children. Direct beta-integral normalization gives total intensity \(32\pi c/63\), so \(c=63\lambda/(32\pi)\). Roots and children contribute \(2\lambda/5\) and \(3\lambda/5\); neither is missing. The cubic family moment is integrable. Gaussian completion gives the four-children term
\[
\frac{c}{24\pi^3L^6}\frac{e^{-\operatorname{tr}(S_4)/L^2}}V.
\]
Root-containing terms and every immigrant partition are included in the full density. Near ordinary planar squares their remainder is bounded, leaving a size-dependent leading coefficient from the exponential. Thus the full fourth law fails; the concrete pair density also fails. In the stated broader radial-productivity family, the pair integral is either infinite at every separation or has \(d\rho^{(2)}(d)\to0\), depending on the specified integrability condition. This remains a family-specific obstruction.

**v03.** The one-generation common-sphere law has infinitely many latent tiny-radius parents but a finite intensity of nonempty families, since \(\int q(R)(1-e^{-m(R)})dR\leq\int q(R)m(R)dR=\lambda\). Removing empty families does not change offspring factorial weights. Translation integration includes distant parents and gives the exact whole-space intensity. Its same-parent pair term is \(3\lambda^2L/D-\lambda^2\) for \(D<2L\), hence the full pair law is exact on that domain. Its same-parent fourth term is \(8\lambda^4L^3/(3\pi V)\). It has global density regularity, finite third local moments and infinite fourth ones. The full triangle law fails near distinct collinear triples; the full fourth law has the positive lower-partition remainder.

There is also a broader obstruction for iid points on a common sphere with Poisson parents and arbitrary count/radius mixing. The same-parent triple term has the form \(F(R_\triangle)/A\). If full pair and triangle laws held, the required \(F(r)\) at fixed circumradius would equal
\(a_3-\lambda a_2 A\sum D^{-1}+2\lambda^3A\).
Using right triangles with hypotenuse \(2r\) and legs \(2rs,2rt\), \(s^2+t^2=1\), gives a polynomial in \(p=s+t\) with nonzero linear coefficient \(-\lambda a_2r\). It cannot be constant on \((1,\sqrt2)\). Fubini in smooth radius/shape coordinates followed by continuity justifies this specialization of a.e. identities. The theorem does not cover dependent angular offspring or non-Poisson parent laws. At fourth order the weighted radius measure must be absolutely continuous: an atom carrying positive fourth factorial weight would produce a singular component on a fixed-circumradius hypersurface. The v04 clarification states this correctly; absolute continuity of the entire radius law is stronger than necessary.

**v04.** For \(\lambda M^3\leq1/(64\pi)\), a sphere stream of intensity \(\lambda/2\), dependent three-point and two-point offset laws, and singleton fill give exact full pair and triangle identities with
\[
a_2=2\lambda^2M,\qquad a_3=4\lambda^3M^2.
\]
The residual kernels are nonnegative before normalization; the third residual's pair marginal is bounded by \(40\pi\lambda^3M^4/D\), leaving a positive pair kernel. Their anchored integrals and singleton budget give an actual process. It retains global absolute continuity, finite-a.e. densities, finite third moments and infinite fourth moments. Its fourth cumulant is \(b_4/V\), \(b_4=\lambda^4M^3/(48\pi)\), but the full fourth density is
\[
\frac{b_4}V+\lambda a_3\sum_{|I|=3}\frac1{A_I}
+a_2^2\sum_{ij\mid kl}\frac1{D_{ij}D_{kl}}
-2\lambda^2a_2\sum_{i<j}\frac1{D_{ij}}+6\lambda^4.
\]
The general positive parent-partition representation shows the nonzero remainder; the negative terms in this expanded expression do not represent signed cluster probabilities.

The frozen display (26) omits two plus signs. Read literally it is incorrect. The correct fourth partition identity is
\[
c_4+\lambda\sum_{|I|=3}c_3(I)
+\sum_{ij\mid kl}c_2(ij)c_2(kl)
+\lambda^2\sum_{i<j}c_2(ij)+\lambda^4.
\]
There are one, four, three, six and one terms, respectively. The manuscript's general partition formula (24), prose and expanded formula (28) use this correct identity. This is a recoverable display defect, already recorded by the individual review, not a fifth substantive submission or a reason to upgrade the partial theorem to exact S1.

### 10. Investigator-selected track before the successful fourth submission

**v01.** A randomized periodic slab Cox intensity is a genuine stationary locally finite law. Its phase and orientation/tilt distribution give an exact full local reciprocal fourth density. A global allocation/resonance argument controls its fourth density outside the local domain, and a third-moment estimate gives the correct moment class. Its lower densities have nonconstant attenuation factors; in particular \(d\rho^{(2)}(d)\to0\) as \(d\downarrow0\). The broader finite-thickness radial slab pair obstruction uses the canonical expected-product density and dominated convergence; it cannot be asserted for an arbitrary density version on a single ray. The later clarification replaces an endpoint strict inequality by the correct weak inequality. These precision corrections do not make v01 exact S1.

**v02.** The slab law mixed with a separated process of clusters of size at most three gives all three exact identities in a strictly positive small-intensity range. With \(J=\pi^2/4\) and \(Z_0=\pi^2/4+2\pi/3\), the supplied sufficient bound is
\[
\lambda M^3\leq\tau=\min\left\{\frac1{36e\pi},
\frac{J^2}{8\pi^2Z_0},
\sqrt{\frac{J^3}{32\pi^4Z_0^2}}\right\}.
\]
Its residual positivity, probability normalization and global domination argument reconstruct. Spatial dilation preserves \(\lambda M^3\), so it cannot extend this result to arbitrary independent intensity and cap.

The separate v02 obstruction assumes precisely this slab component and a correction process partitioned into diameter-below-\(M\) clusters of size at most three, with different clusters separated by at least \(M\). For every eligible ordered pair of correction points there is at most one eligible third point. After eliminating correction densities and coalescing the pair, the slab terms vanish in the appropriate weighted limit, giving \(a_2\geq2\pi^2M^2a_3\). Count inequalities on balls of radius below \(M/2\) imply \(\lambda M^3\leq18/\pi\). This theorem uses only the two lower identities, not the fourth identity. It is not a general S1 intensity bound.

**v03.** For any process with the lower reciprocal laws, a separate general necessary inequality is
\[
\frac{\lambda\pi M^3}{6}
\leq 2+\frac{a_3}{a_2}\frac{\pi^2M^2}{2}.
\]
For a ball of radius \(r<M/2\), integrating reciprocal distance to a line gives \(F_3\leq(a_3/a_2)2\pi^2r^2 F_2\). Cauchy–Schwarz gives \(F_2^2\leq\mu(F_3+F_2)\), and variance gives \(\mu\leq2+(a_3/a_2)2\pi^2r^2\). Letting \(r\uparrow M/2\) yields the displayed inequality. Since the ratio is free, this imposes no universal upper intensity on S1.

Independent union with a positive-intensity finite-fourth-moment process cannot preserve an exact reciprocal fourth law of a finite-third-moment base. All mixed fourth terms have finite mass on bounded products. A nonzero change in the \(1/V\) coefficient would have infinite mass there, forcing the coefficient change to be zero; the positive mixed \(3+1\) contribution then gives a contradiction. The analogous stated two-base case is covered. This is an independent-union obstruction, not a convex-mixture obstruction.

The v03 slab mixture theorem permits an arbitrary finite-fourth-moment correction, but now assumes all three reciprocal identities. Integrability forces the correction's local fourth measure to vanish. Global absolute continuity eliminates hidden coplanar quadruples, hence there are almost surely no four correction points in a set of diameter below \(M\). For an eligible pair, at most one additional point can lie in a sufficiently small ball. Coalescence gives \(a_2\geq(\pi^2M^2/2)a_3\), which combined with the general inequality again yields \(\lambda M^3\leq18/\pi\). This broadens the correction class but adds a fourth-law premise; it is not an unconditional strengthening of the lower-law theorem in v02.

Finally, v03's pointwise-positive formal residual hierarchy after subtracting a Poisson background is not a realization theorem. Positivity of finitely many densities does not establish consistency with a probability measure on configurations. The final v04 construction avoids that unresolved route through explicit sampling and nonnegative normalized kernels.

## Finding register

“Closed” below means that the cited issue is resolved by the reconstructed proof, or that a claimed result is correctly confined to its stated scope. It does not mean that an unsuccessful submission passed S1.

| ID | Location | Precise issue | Consequence | Repair/status |
|---|---|---|---|---|
| F01 | S0; nonexistence_1 v01 | Global pair mass grows as \(R^5\), below the required squared mean \(R^6\). | S0 impossible for every positive intensity, without a fourth-moment assumption. | Closed, general obstruction. |
| F02 | nonexistence_1 v01 | Global triangle mass grows as \(R^7\), below the required cubic mean \(R^9\). | Independent S0 obstruction. | Closed; local integrability checked. |
| F03 | nonexistence_1 v02 | Fourth-tail exclusion must survive infinite local fourth moments. | Occupancy-indicator argument proves the needed general tail obstruction. | Closed; no mixing/ergodicity assumption. |
| F04 | nonexistence_2 v01 | Divergence near coplanarity can be confused with infinitely many realized points. | S1 requires infinite fourth expectation, not failure of local finiteness. | Closed; explicit counterexample and local slicing. |
| F05 | S1 moment class | Pair/triangle laws and global fourth AC do not imply finite fourth moment. | Finite third and infinite fourth moments are the correct class. | Closed; retain extended factorial measures. |
| F06 | S0→S1 | A common finite diameter cap is one repair among many. | Reviewed obstruction authorizes removal of unrestricted tails; it does not uniquely prescribe S1. | Closed authority distinction. |
| F07 | proof_4 v04 parameters | \(\lambda,M\) independent; large \(L\) could invalidate probability budget. | Uniform-in-\(L\) band bound and intensity cancellation allow all parameters. | Closed, no hidden intensity restriction. |
| F08 | proof_4 v04 bands | Desired first sphere intensity alone is not a probability law. | Explicit band/shift/phase/retention sampling realizes it. | Closed; empty probability nonnegative. |
| F09 | proof_4 v04 spheres | Infinitely many spheres or small radii could violate local finiteness. | Fixed selected band gives finite local candidate count; nonatomic finite mass. | Closed. |
| F10 | proof_4 v04 stationarity | A lattice construction need not be stationary. | Uniform shift plus mark relabelling gives arbitrary translation invariance. | Closed; isotropy/ergodicity not claimed. |
| F11 | proof_4 v04 local allocation | Distinct spheres could contribute uncounted short tuples. | Surface separation exceeds \(M\). | Closed; all eligible tuples lie on one sphere. |
| F12 | proof_4 v04 coarea | Constants and ordered-tuple factors are consequential. | Jacobians \(2D,8A,48V\) give the stated densities; no extra factorial. | Closed. |
| F13 | proof_4 v04 global AC | Same-sphere formulas do not cover all global allocations. | Rank of \((\omega_i^T,1)\) proves AC for every allocation. | Closed, strongest global regularity dependency. |
| F14 | proof_4 v04 fourth density | A countable mixture of finite densities can be infinite on a positive-measure set. | Polynomial exceptional sets and a local radius bound reduce generic regions to finitely many bands. | Closed; finite-a.e. proved separately. |
| F15 | proof_4 v04 degeneracy | Infinite neighbourhood mass could conceal singular mass on coplanarity. | Global AC eliminates mass on null degeneracy/resonance sets. | Closed; density values there are irrelevant. |
| F16 | proof_4 v04 residuals | A large triangle deficit might have too large a pair marginal. | Circumradius/line-distance estimate gives \(\mathcal Mq_3\leq B_L/D\). | Closed uniformly through degeneracy. |
| F17 | proof_4 v04 correction | Positive kernels alone need not normalize to a process. | Explicit \(Z_2,Z_3,\beta,\pi_j\) and finite budgets yield genuine probabilities. | Closed. |
| F18 | proof_4 v04 hard-core centres | Retained centres are dependent. | First intensity suffices locally; unthinned Poisson domination supplies global regularity. | Closed; no false Poisson assumption. |
| F19 | proof_4 v04 final combination | Independent union would create mixed factorial terms. | A fair whole-law mixture gives linear factorial measures and exact intensity. | Closed; exact S1. |
| F20 | proof_2 v01 versus proof_4 v04 | Cox exclusion appears to conflict with a Cox sphere component. | The component has attenuated triangle density; the final law is non-Cox. | Closed; no contradiction or theorem extension. |
| F21 | proof_2 v01 | Signed squared-test calculation and random-plane loophole. | Absolute integrability, countable tests, distributional derivatives and local planarity close both. | Closed for all locally finite directing measures. |
| F22 | proof_1 v01 | Finite-population and count-independent iid obstructions could be overextended. | They exclude only those cluster subclasses. | Closed scope; general Poisson-cluster S1 realization unresolved here. |
| F23 | proof_1 v01/v04 | Pointwise-positive residuals and exact same-parent fourth laws are not full realization. | Actual law and every parent partition remain necessary. | Partial only; no retrospective pass. |
| F24 | proof_1 v02/v03 | Finite cylinder intersections retain shape dependence. | Relative approximation and restricted mixture exclusions do not yield exact S1. | Closed scoped failure. |
| F25 | proof_1 v03 | Fourth moments need not pass through local total-variation convergence. | Rare heavy clusters retain fourth mass after their law disappears in the limit. | Closed negative result; uniform-integrability gap cannot be ignored. |
| F26 | proof_1 v04 | Exact reciprocal same-parent fourth term has positive full-density remainder. | Low-intensity lower laws plus \(a/V\) cumulant do not solve S1. | Closed failure by planar-square coefficient and positive remainder. |
| F27 | proof_1 v04 caps | All-intensity pair repair does not repair the triangle law. | Distinct-collinear limit forces area times density to zero. | Closed failure; fourth statement remains approximation. |
| F28 | proof_3 v01 | Standard branching exclusion does not cover count/geometry coupling. | Scope is the stated iid count-independent model and specified projections. | Closed scope; ancillary genealogy formulas not all reconstructed. |
| F29 | proof_3 v02 | Observed roots and non-four-children allocations could be omitted. | They are included; the exponential coefficient still varies with square size. | Closed failure; actual intensity normalization rechecked. |
| F30 | proof_3 v03 | Fixed-circumradius shape identity used on measure-zero triangle families. | Smooth coordinates, Fubini and continuity justify the specialization. | Closed common-sphere iid obstruction. |
| F31 | proof_3 v03/v04 | Arbitrary radius mixing can create singular fourth mass. | Fourth-factorial-weighted radius AC is necessary in the stated disintegration. | Clarified in v04; no claim for atomic positive fourth weight. |
| F32 | proof_3 v04 (26) | Two missing plus signs make the literal display false. | General partition formula and expanded density remain correct. | Explicit corrected identity above; frozen source preserved. |
| F33 | proof_3 v04 | Exact lower laws and reciprocal fourth cumulant still leave full fourth remainder. | Small-intensity theorem is partial S1 progress. | Closed failure, fourth attempt exhausted. |
| F34 | proof_4 v01/v02 | Slab endpoint inequality and density-on-a-ray convention. | Weak endpoint inequality and canonical expected-product version are required. | Corrected in later frozen exposition; v01 remains partial. |
| F35 | proof_4 v02 | Small \(\lambda M^3\) theorem cannot meet independent all-parameter quantifiers. | Dilation leaves the dimensionless parameter unchanged. | Closed partial theorem, no implicit S2. |
| F36 | proof_4 v02/v03 | Representation-specific \(18/\pi\) ceiling could be misreported as general. | Different correction classes and fourth-law premises must be retained. | Closed scope; final law is outside their slab hypotheses. |
| F37 | proof_4 v03 | General count inequality contains the free ratio \(a_3/a_2\). | It gives no general upper bound on intensity. | Closed. |
| F38 | proof_4 v03 | Positive formal hierarchy lacks a realization theorem. | That alternative route remains unresolved, but is unused by v04. | Open subsidiary route, not an S1 gap. |
| F39 | source dossier | Standard Radon/finite-moment or stability hypotheses fail for direct fourth input. | Inspected theorems do not directly certify the formal residual hierarchy. | Source gap accurately bounded; explicit v04 law bypasses it. |
| F40 | attempts and owner response | Early Cox closure could be labelled four-attempt exhaustion. | Actual count is 1/4, owner ended, three unused. | Closed documentary correction in final status. |
| F41 | proposal S2 | A precise proposal after three unsuccessful reviews is not approval. | S1 stayed active for attempt four; no retry reset. | Closed; S2 unapproved/inactive. |
| F42 | original statement ledger | S1 remained labelled “existence unresolved” after accepted v04 evidence. | Original snapshot was stale, not a mathematical contradiction. | Preserved; `ledger_v02.json` reconciles outcome only. |
| F43 | broadcasts/dispatch | Queued delivery, notification and actual acknowledgement differ. | Packets and recorded receipts support only a bounded documentary audit. | No claim of private reading or universal acknowledged receipt. |
| F44 | accounting | Cumulative snapshots, repeated input and reasoning subsets can be double-counted. | Per-turn records and boundary differences must be used with stated coverage. | Arithmetic checks pass where numeric; unknown splits remain NR. |
| F45 | experiment outcome | A successful later track does not validate earlier weaker submissions. | Twelve construction submissions remain unsuccessful for S1; only proof_4 v04 succeeds. | Closed; no retrospective pass or extra attempt. |

## Amendment implications and attempt protocol

The amendment `statements/S0_to_S1.md`, SHA-256 `b2534040520dfc63bf5c22ecc508257308e619a040a7c6c54ce44375742394de`, was adopted at `2026-10-20T17:16:19.553060+00:00` with authority `reviewed_general_obstruction`. The initial non-existence work and its fresh reviews preceded construction dispatch. In particular, the fourth-tail refinement was reviewed before the adopted three-order cap. The record does not use the finite-fourth-moment exclusion to remove the infinite-fourth class. The necessary conclusion is that the unrestricted reciprocal tails cannot persist at positive intensity; a common finite cap is the chosen operational target, not a uniquely forced maximal domain. Local divergence persists after this change and is retained deliberately.

The original statement ledger was stale: it recorded S1 as active with existence unresolved, while the later frozen status/manifest/history recorded the proof_4 v04 success pending synthesis. This defect was reported during this audit. The explicitly supplied `statements/ledger_v02.json`, SHA-256 `f537e64e209c54632a2d910c4464e33e584240dda2e2fc0a4735b0822296c037`, preserves the original ledger hash and updates only the outcome. S0/S1 statement hashes, amendment authority and attempt counts are unchanged. I did not treat either ledger's outcome label as mathematical evidence.

The owner response preserved in `proposals/proof_2_early_track_decision_owner_response.json` ends Cox at 1/4. It authorizes early administrative closure, not a theorem about all processes or a target amendment. The proof_4 proposal after its third unsuccessful reviewed submission requests the precise small-intensity S2 restriction. The request was recorded after the third review, but its owner-response field is null. No explicit approval appears in the assigned evidence. S2 remains unapproved and inactive, and the fourth proof_4 submission was dispatched against unchanged S1. The successful result makes that proposal unnecessary; it does not retrospectively approve it.

| Track/submission | Target at review | Strongest supported outcome | Exact-target status |
|---|---|---|---|
| nonexistence_1 v01 | S0 | General pair/triangle large-scale impossibility; weaker tail and moment distinctions. | Valid obstruction, not a construction attempt. |
| nonexistence_1 v02 | S0 | Fourth-tail obstruction with no finite-fourth assumption. | Valid general obstruction. |
| nonexistence_2 v01 | S0 | Local fourth divergence, lower integrability and moment-class counterexample. | Valid local/scoped result; no general S1 impossibility. |
| proof_1 v01 | S1 | Positive formal residuals, restricted exclusions, actual lower-order progress. | Unsuccessful 1/4. |
| proof_1 v02 | S1 | Finite-cylinder approximation and exact lower laws in stated range. | Unsuccessful 2/4. |
| proof_1 v03 | S1 | Restricted cylinder exclusions and fourth-moment limit failure. | Unsuccessful 3/4. |
| proof_1 v04 | S1 | Exact reciprocal same-parent fourth term; all-intensity pair/relative-fourth theorem. | Unsuccessful 4/4; exhausted. |
| proof_2 v01 | S1 | General Cox-class exclusion. | Unsuccessful construction 1/4; owner ended, not exhausted. |
| proof_3 v01 | S1 | Specified standard branching/Hawkes exclusions. | Unsuccessful 1/4. |
| proof_3 v02 | S1 | Actual marked Gaussian family in correct moment class, but wrong full laws. | Unsuccessful 2/4. |
| proof_3 v03 | S1 | Exact full pair and reciprocal same-parent fourth law; iid-sphere lower-law obstruction. | Unsuccessful 3/4. |
| proof_3 v04 | S1 | Exact full pair/triangle laws at small intensity, reciprocal fourth cumulant. | Unsuccessful 4/4; exhausted. |
| proof_4 v01 | S1 | Exact full fourth law via slabs, lower laws fail. | Unsuccessful 1/4. |
| proof_4 v02 | S1 | All three exact laws at small intensity; scoped mixture ceiling. | Unsuccessful 2/4. |
| proof_4 v03 | S1 | General lower-law inequality, scoped mixture/superposition obstructions, formal residuals. | Unsuccessful 3/4; S2 proposal only. |
| proof_4 v04 | S1 | Actual exact law for all independent positive intensity/cap parameters, global regularity. | Successful 4/4. |

There are 16 substantive submissions in this table, of which 13 are construction submissions: twelve unsuccessful for the active target and one successful. Administrative notes, source clarifications, the S2 proposal and this synthesis do not constitute additional construction submissions. No earlier result is relabelled an S0 or S1 success because it became useful later.

The later administrative packet permits a bounded dispatch audit. All 13 construction dispatches consistently identify S1 and its hash, retain increasing attempt numbers, and reference the same frozen common-seed manifest. Their explicit allowlists contain no other construction track's proof or review. The initial non-existence packets contain no `starting_information` files. The delivery snapshot has 38 entries; early S1 notifications to the non-existence roles and their reviewers have null acknowledgements, whereas later dispatch reconciliation records report hash-verification acknowledgements. The original S0/S1 broadcast objects also distinguish queued roles from delivered roles. These documents support correct target assignment and recorded notification, not independently observed reading behaviour. No coder was dispatched. Fresh-review packet boundaries are documentary evidence of the intended independence protocol, not an operating-system isolation certificate.

## Source and coding evidence

The final construction, S0 proofs and Cox exclusion are reconstructed from explicit elementary probability, integration, linear algebra and Euclidean geometry. They do not rely on a general point-process realization theorem. The supplied literature dossier addresses the separate question whether the formal nonnegative residual hierarchy can be realized by invoking existing theorems. I checked the decisive hypothesis passages in the frozen extracted primary texts; I did not re-prove all results in those papers or search the current literature independently.

| Frozen primary source | Checked location/hypothesis | Consequence for this experiment |
|---|---|---|
| Kuna–Lebowitz–Speer, *Necessary and sufficient conditions for realizability of point processes* (2011), arXiv:0910.1710v2 | Definition 3.1 uses symmetric Radon measures through the prescribed order and realization with corresponding finite local moments. | Direct inclusion of \(a_4/V\) on small product balls violates bounded local fourth mass. The cited framework does not directly realize that fourth input. |
| Infusino–Kuna, *The full moment problem on subsets of probabilities and point configurations*, inspected arXiv:1802.03582v2 (2019; journal 2020) | Definition 3.1 and Theorems 3.9–3.10 require a full sequence, continuous local moments, determining/growth conditions and positivity conditions; simplicity also has its diagonal condition. | A four-term non-Radon fourth hierarchy does not satisfy the displayed input class or provide the required higher sequence. Positivity of the few supplied densities is insufficient. |
| Lachièze-Rey–Molchanov, *Regularity conditions in the realisability problem…* (2015), arXiv:1102.1950v5 | Assumption 2.4, regularity-modulus framework and Theorem 2.6 concern a finite real linear functional on the selected test space with a regularity bound. The stationary pair criterion in Theorem 3.10 has an additional near-zero integrability condition. | Quartic tests with infinite expectation cannot simply be inserted in that finite functional. A restricted integrable test space is a possible separate project, but its positivity/tightness/extension bridge is not supplied. The concrete pair criterion fails for the reciprocal pair singularity; this is failure of a sufficient criterion, not non-existence. |
| Kuna–Lebowitz–Speer, *Realizability of point processes* (2007), arXiv:math-ph/0612075v2 | Theorem 3.1 requires \(\int|g-1|<\infty\) and a uniform product stability bound; already the one-factor case bounds \(g\). | A no-lower-cutoff \(g(r)\propto1/r\) violates that bound. The low-density hierarchy or hard-core variants do not directly establish the present full reciprocal laws. |
| Daley–Vere-Jones, *An Introduction to the Theory of Point Processes*, vol. II (2008), frozen selected text, printed pp. 65–68 | Their discussion distinguishes potentially infinite expectations from a convention that a moment measure “exists” when boundedly finite. | S1 explicitly uses extended factorial measures. Importing a boundedly-finite convention would silently change the target. |

The source files, extraction record, inspected versions and bibliographic details are in `literature/realisability_v01/`; their hashes are included in the original assigned packet. This audit supports **no direct applicability of the inspected theorems under the stated inputs**. It does not prove that no theorem anywhere can realize an extended hierarchy, and it makes no novelty claim or claim about the present research status of a historical exercise. The unused formal-hierarchy source gap remains a subsidiary open route, while explicit proof_4 v04 closes S1 itself.

No numerical campaign, earthquake-data comparison, simulation, symbolic computation campaign or proof assistant was used. Code in this review verified hashes, parsed authorized JSON/JSONL records and checked accounting arithmetic. Mathematical constants and estimates above were checked analytically. No external source or computational request remained necessary.

## Measured-token accounting and audit limits

Runtime preflight read only allowlisted metadata fields from this reviewer's explicitly identified own rollout: session metadata, turn context and numeric token-count/task-completion metadata. It verified the actual model and effort before mathematics, rather than relying on a requested role label. The preflight file preserves the evidence and UTC boundary. The latest exposed preflight checkpoint was at `2026-10-20T19:25:31.156Z`: input 162347, cached input 142336, cache-write input 0, output 1003, reasoning output 61, total 163350. The subsequent preflight write and completion tail are not silently included in that checkpoint. The final `accounting.json` identifies its own latest observation, preflight/research split method and incomplete coverage; final completed-turn counters require post-completion reconciliation by the coordinator.

The frozen historical ledger contains 36 per-turn rows across 24 sessions: 35 completed rows and an active coordinator row. I checked uniqueness of session/turn pairs, numerical `input + output = total`, subset inequalities for cache/reasoning fields, and additive preflight/research splits when all entries are numeric. These checks found no discrepancy. Four construction turns have unavailable numeric boundary splits: proof_1 v02, v03 and v04, and proof_3 v03. Their split checks remain NR; numeric whole-turn totals do not make unavailable splits zero. Thirty-three referenced artifact entries fell within the original allowlist and their hashes matched; 31 other referenced artifact entries were not opened because they were not assigned.

The administrative addendum supplies a coordinator counter-consistency record reporting no numerical issues and a 33-completed-turn timestamp-correction verification reporting unchanged numeric usage. I inspected those JSON records as documentary evidence, not the other agents' raw rollouts. The correction addresses time representation/turn-start selection; it does not license invented counters. My independent audit of historical numeric usage is limited to the frozen ledger's internal arithmetic and the supplied verification records. Actual other-agent runtime metadata was not re-read outside the assigned evidence.

Cumulative token snapshots are not summed. Reasoning output is a subset of output, and cached input is a subset of input. Exposed input usage can include repeated context across requests and is not a measure of manuscript length. Parent/child aggregation semantics are NR; no cross-session billing grand total is asserted. Estimates, pricing/tier assumptions and actual monetary charges are NR. Artifact word counts are measured separately and are not token estimates. This review's completion tail and the coordinator's active tail are incomplete at its freeze. See `administrative_audit.json`, `administrative_addendum_audit.json`, `accounting.json` and the metadata-only accounting evidence for precise coverage.

## Presentation judgement and remaining obligations

The final proof is mathematically coherent but has several dependencies whose prominence should be preserved in any later exposition: the band probability budget uniform in \(L\); the exact first sphere intensity without a false Poisson assertion; the all-allocation submersion argument; the separate generic-radius argument for finite-a.e. fourth density; the uniform residual marginal estimate; and the distinction between whole-law mixture and independent union. Removing those details would reopen real proof obligations. The ordered coarea constants and explicit probability budgets should remain adjacent to the corresponding constructions.

Historical manuscripts should keep their target labels and explicit partial-status statements. In particular, correct proof_3 v04 display (26) in any future editorial edition while retaining the frozen original and the correction record. Preserve the separate assumptions of proof_4 v02 and v03's \(18/\pi\) statements. “Cox obstruction,” “iid common-sphere obstruction,” “finite-moment obstruction” and “general S0 obstruction” should never be conflated.

The main mathematical verdict has no unresolved dependency within the assigned S1 specification. General realization within all Poisson-cluster models, extra ergodicity/mixing requirements, independently prescribed constants \(a_n\), and a general extended-moment realization theorem are not settled by this experiment. They are not requirements of S1. The exact successful law supplies no claim about order five or higher.

The audit is extensive but not a re-certification of every historical subsidiary sentence. I reconstructed all dependencies of the S0/S1 verdicts and the all-Cox exclusion; the final actual laws, principal failure mechanisms and scoped obstructions described above were checked from their frozen proofs. Earlier detailed genealogy expansions, every optional side estimate in the first cluster/branching submissions, and full proofs of the external literature theorems were not reconstructed in full. Those historical details remain available with their individual reviews and are not used as premises for the exact S1 verdict. The source dossier's search completeness and other agents' private reading behaviour are outside this audit. No unresolved historical detail is being promoted into a general theorem here.

## Final synthesis

The experiment establishes a sharp distinction between targets. S0 is false because unrestricted reciprocal correlations conflict with positive-density large-scale counts; the fourth-tail argument reaches the infinite-fourth-moment class as well. The adopted S1 retains the near-degenerate singularity and prescribed positive intensity while restricting only the geometric domain of the identities. Its local singularity forces infinite fourth expectation but permits a locally finite process.

Proof_4 v04 supplies that process for every independent positive intensity and diameter cap. The final law uses separated spherical Poisson surfaces with carefully controlled radius mixing, an explicit nonnegative low-order correction process, and a whole-law mixture. Its local identities and global measure regularity have both been independently reconstructed. The Cox exclusion and other scoped obstructions remain valid because their premises do not describe this final law. The other tracks' exact lower-order, same-parent, approximation, small-intensity and non-existence results remain partial or scoped as recorded; none is upgraded by the final success.

The protocol outcome is one exact S1 success on proof_4's fourth and last submission, exhausted unsuccessful tracks proof_1 and proof_3, and owner-ended Cox at one of four. S2 was never adopted. The stale ledger was reconciled in a new preserved administrative version. Hashes, measured counters and their coverage limits accompany this report; no billing, novelty or formal-certification claim is made.
