# Simulation decisions and outcomes

The packet and own gpt-6-astra/xhigh runtime metadata were verified before
mathematics; no child agent was launched. The accepted S1/v04 law was retained.
All work is confined to this coder output directory.

We chose M=1 and lambda=6e-6, for which the accepted explicit parameters give
L=1. Ordinary sampling is extremely sparse. Five million independent exact
small-ball restrictions produced seven singleton points, hence no usable
ordinary correlation estimates. All counts and nonempty coordinates are saved.

We therefore used a separate, fully labelled factorial-tuple importance
experiment. It samples actual surface point coordinates under the Poisson
factorial law and actual rejected correction-cluster marks. Conditional
Poisson counts are integrated out, not pretended to have been observed.
The construction's generating gamma and surface mass determine weights;
reciprocal-simplex densities are evaluated only in an independent reference
integration. Exact auxiliary rejection avoids numerical evaluation of Mq3.

The final study has 524,288 proposals per sphere order and per cluster-mark
proposal, with 2,097,152 reference configurations per order. It reports all
18 selected bins. The pilot motivated omitting near-maximal-volume bins;
its data are not included in final results. Every reported fourth-order bin
also has circumsphere radius at most two, explicitly as an observable guard.
Orders two and three retain all latent sphere radii, without tail truncation.

Estimated/theoretical bin-average ratios range from 0.9767 to 1.0043; the
largest standardised deviation is 1.8202. Separate analytic pair-integral
checks and a correction-mass cancellation check agree within 1.85 standard
errors. Standard errors propagate independent reference integration error
and retain the dependence of three edges drawn from one correction cluster.
Finite variance is justified for these bounded importance contributions;
the original infinite fourth count moment is not estimated away.

Code, all process proposal points and per-row contributions, machine-readable
results, full derivations, an executable exact small-ball sampler, PDF/PNG
figures, manuscript section and table are delivered. Matplotlib layout was
visually inspected; the configuration figure received a padding-only v02
revision on new paths, leaving the manuscript's first frozen version intact.

The results test this implementation and these finite-bin integrals. They
do not prove exact identities, global absolute continuity, the entire
parameter range, ergodicity, or earthquake-data fit. A separate conditional
sphere illustration is labelled and excluded from ordinary-window statistics.
