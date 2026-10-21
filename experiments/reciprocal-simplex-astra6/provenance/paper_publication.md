# Publication of the main Astra manuscript

Authorised by the owner on 21 October 2026: publish the draft as the main Astra paper, the experiment with its documentation, an organised landing structure and Overleaf editing support.

The export starts from GitHub commit `332aa61`, including the existing Overleaf merge. Existing slide source, assets, original research archive and earlier-model experiment were preserved. The new paper is canonical in `00_main_draft/`; the root-relative Overleaf entry point is `01_papers/astra_main.tex`. The standalone paper-only ZIP contains the same source and figures.

The simulation code, full-precision results, all saved-coordinate and contribution arrays, estimator derivations, frozen drafts, dispatch packets, reader report, repairs, source verification and measured writing-token checkpoints are published. Large arrays are stored on the `astra-paper-data-2026-10-21` data branch, with file hashes in the repository. Source-PDF copies, extracted copyrighted source text, raw conversation records, personal skill bodies, transient build files and caches are not redistributed. Runtime identifiers and local home paths are redacted in public copies.

The original research release manifest is preserved as `release_manifest_20261021_original.json`. Its current copy updates only the hash of the expanded Astra landing README; the research evidence and numerical accounting are unchanged. The paper export manifest records original/public hashes, and `paper_release_manifest.json` freezes the current manuscript publication. Historical embedded hashes remain original-source hashes.

Validation: the Overleaf entry point compiles in two passes from the repository root without warnings; current navigation links resolve; all 11 NPZ archive payloads match their SHA256 hashes; original experiment and paper-release verification scripts pass. The paper itself is unchanged by this publication. GitHub and Overleaf synchronisation are checked separately from these local build results.

The writing token ledger remains its original frozen checkpoint, with its disclosed coordinator tail. Publication work is subsequent and excluded from that ledger.
