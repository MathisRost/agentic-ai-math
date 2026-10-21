# Editing in Overleaf

The existing `agentic-ai-math` Overleaf project is linked to this GitHub repository. The current canonical manuscript is:

`experiments/reciprocal-simplex-astra6/00_main_draft/reciprocal_simplex.tex`

Select the main document according to what you want to compile:

| Document | Overleaf main document |
|---|---|
| Astra paper | `01_papers/astra_main.tex` |
| Presentation | `agentic_ai_math_talk.tex` |
| Research setup tutorial | `02_tutorial/codex_research_setup_guide.tex` |

The paper entry point supplies figure paths relative to the project root and inputs the canonical manuscript. All required figures and the embedded bibliography are committed. Use pdfLaTeX. Edit the manuscript in its canonical file; the entry point contains no duplicate paper text.

Use the project's GitHub integration to pull repository changes before editing and push your Overleaf edits back when ready. GitHub and Overleaf synchronise through those explicit actions; a GitHub push alone does not certify that the Overleaf copy has updated. Preserve and merge edits from both sides when the integration reports divergence. Generated PDF previews in Overleaf do not automatically refresh the committed PDF: rebuild and commit that PDF when publishing a new draft.

Full raw simulation arrays are downloadable from the [Astra paper release](https://github.com/MathisRost/agentic-ai-math/releases/tag/astra-paper-2026-10-21). They are separate from the editable Overleaf project; all code, seeds, results, figures and array hashes remain in the repository.

For a separate paper-only Overleaf project, upload `astra_overleaf.zip` from the same release and select `reciprocal_simplex.tex`. This optional snapshot is not a second automatically synchronised manuscript.
