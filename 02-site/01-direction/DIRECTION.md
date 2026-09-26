# Direction

Each decision is stated once, as it currently stands. **Status: in progress, not yet approved.**

## Decided by Danny

- **Boxes, layout and type come from Kojima** (`study/reference/kojima.md`):
  - **Boxes:** square 1px frames, crosshair corners, header and footer rows over thin rules; no
    radius, no shadow.
  - **Layout:** a top horizontal menu bar; a left vertical rail; a right vertical column of stacked
    cards against the right edge; between them, a centre stage, a large framed rectangle centred in
    the space, with a big shape in the middle and shapes around its edge, where articles, metrics
    and other content appear. On a phone everything stacks in one column.
  - **Spacing:** generous. The top bar and the left rail both have more room than Kojima, and the
    right column fills top to bottom with cards.
  - **The centre square** fits the space, up to 690px at most.
  - **Reading:** clicking the square fades it out and shows the piece as a text block in the same
    frame. Only that block scrolls; the page itself (bar, rail, column, background) stays still on
    desktop. `← BACK` in the frame's header row returns to the square. On a phone the page scrolls
    normally.
  - **Type:** Kojima's treatment: monospace, one weight, capitals, wide letter-spacing, small sizes.
- **Background and grid come from Formas** (`study/reference/formas.md`): a deep colour field with
  large blurred shapes, under a two-level square grid (fine and major) whose lines are tinted from
  the field colour.
- **Colours: blue field, magenta accent.** Danny approved the blue-field study
  (`study/shots/blue-1440.png`, `study/shots/blue-390.png`). Its values are the current picks:
  - field `oklch(0.24 0.09 244)`;
  - accent `oklch(0.66 0.25 340)`;
  - grid 28px fine / 140px major at strength ×1;
  - live link: `study/colour.html#f=blue&bh=244&mh=340&fl=0.24&fc=0.09&cell=28&gs=1`.
  Magenta as the field (`study/shots/mag-1440.png`) is liked, but as a transition colour, not the
  base.

## Open

- **Fine-tuning the exact blue and magenta,** if Danny wants to move them from the current picks.
- **Background morph on a content change.** Danny likes it, but it still needs refining. When content
  changes (a new section, opening a piece, going back), the soft shapes travel across the page to a
  new arrangement (about 5s, slow in and slow out) while their colour swings to pink (about 0.9s)
  and settles back to blue (about 2.2s). The shapes are soft gradients that move without being
  re-blurred each frame, which is what removes the stutter. The clouds stay blue to
  violet, with no green. Demo in the study page: click any menu or rail item
  (`study/shots/morph-400ms.png`, `study/shots/morph-3000ms.png`).
- **The monospace font.** Target: **Consolas**, which is what Danny's Kojima screenshot shows (taken
  on Windows; Kojima uses the visitor's system monospace). Consolas is licensed with Windows, not
  for serving on a website, so the site needs a free, self-hostable font that matches it.
- **Reading text:** the size and face for article body text. Kojima's sizes are for labels.
- **The reader may need to be unframed.** Danny's direction: keeping a box around the text may be
  too restrictive to read comfortably. The frame may need to fade away so the text block stands as
  its own element, the way Medium and Substack present writing. Still to be worked out.
- **The centre stage with a long article:** how it behaves.
- **Stack.**
