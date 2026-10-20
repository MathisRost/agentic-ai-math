# Approach 3 — Hawkes process

**Motivation supplied by the owner:** Hawkes/ETAS models are a natural earthquake
modelling family. This motivates the approach; it does not establish the exact
spatial reciprocal identities.

Specify the model before calculating: a stationary space-time branching/Hawkes
process with a spatial projection over a fixed finite observation interval, or
a precisely defined spatial branching process. An ordinary temporal Hawkes
model alone does not define a point process of hypocentres in R^3.

For a nonnegative linear space-time kernel \(\phi\), a standard starting regime
is \(\eta=\int_0^\infty\int_{\mathbb R^3}\phi(t,x)\,dx\,dt<1\).
Derive the relevant intensity and moment conditions. If the stationary
space-time intensity is \(\nu\), projection of events during an interval of
length \(T\) has spatial intensity \(\nu T\), subject to the model's assumptions.
Show how it equals the prescribed \(\lambda_0\). Do not project all time and
create an infinite spatial count. A stationary process observed after time zero
may have ancestors before zero; an empty-history simulation is a different law.

Derive spatial product densities through four by the appropriate time integrals
of the full space-time factorial densities. Justify Fubini, local finiteness,
spatial simplicity, density existence and fourth moments. Account for every
genealogy and cross-immigrant partition. The excitation kernel, a resolvent and
a connected cumulant are not interchangeable with \(\rho^{(n)}\).

Investigate whether geometric offspring laws or triggering along random carriers
can give all three **exact** identities with one model and fixed physical
domains. Clearly state if a construction leaves the standard Hawkes class.
Critical or heavy-tailed alternatives require separate existence and moment
proofs; subcritical results cannot be transferred without argument.

Give either a construction meeting the target or a precise scoped obstruction.
Earthquake plausibility and empirical fit are separate from the exact theorem.
Starting material: `common/literature/01_hawkes.md`, Kagan's fault-model paper,
the Ogata and Hawkes-cumulant references in the shared dossier, and the prior
geometry-alternatives notes.
