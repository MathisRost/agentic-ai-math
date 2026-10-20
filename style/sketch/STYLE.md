# Mathis turquoise and orange sketch

Approved reference: the five levels of AI use illustration, 18 October 2026.

Use a white background, charcoal text, turquoise outlines and pale turquoise
diagonal hatching. Reserve muted orange for one directional cue or emphasis.
Kalam Regular supplies handwritten labels; Kalam Bold supplies category names
and prominent numerals. Keep the presentation title in its existing sans serif.
The exact palette, sizes and draw.io properties are in `style.json`.

Keep outlines gently uneven (`sketch=1`, `comic=0`, `jiggle=1.2`), hatching
light and open, and labels short. Use generous whitespace and faint dashed
guide lines. Do not add shadows, gradients, decorative icons or heavy fills.
The pyramid belongs to this example; reuse the style with other appropriate
layouts. Preserve meanings rather than forcing every concept into levels.

Author editable `.drawio` XML directly. The approved example is
`../../assets/ai_usage_levels.drawio`; `reference.drawio` is a retained copy.
The local TTF fonts and their licence are in `fonts/`.

Export from the project root:

```sh
python3 talk/scripts/export_drawio.py talk/assets/ai_usage_levels.drawio
```

The exporter uses draw.io Desktop, writes PDF and SVG beside the XML, and uses
installed Kalam fonts for offline rendering. It does not edit the XML source.
The first setup installs the fonts under the current user's `~/Library/Fonts`.
Future runs use the saved local renderer and fonts.

For LaTeX use `\includegraphics[clip,width=\textwidth]{diagram.pdf}`. Compile
the presentation and inspect the slide at its intended size; XML validity alone
does not establish that text fits. Keep concise source attribution outside the
illustration when the content is adapted from a paper.

Sources: [Kalam](https://fonts.google.com/specimen/Kalam),
[draw.io sketch settings](https://www.drawio.com/docs/manual/styles/rough-style/),
[official local export workflow](https://github.com/jgraph/drawio-mcp).
