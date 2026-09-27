# Direction

Each decision is stated once, as it currently stands. **Status:** Danny called the layout done on
2026-09-27, with a later refinement round to come. The items under Open are still open, and
`DIRECTION.md` as a whole isn't approved yet (the stage checkpoint).

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
  - **Reading, unframed** (Danny approved it, asking only for more width; Substack is the reference,
    `study/reference/substack.md`):
    - Clicking the square (or a piece) dissolves the frame: the border and crosshairs fade out, and
      the Kojima header row (`← BACK · SECTION · FIG`) stays.
    - The text stands on the grid in one column, 19px with 1.6 line height: title, subtitle, then
      text, with thin rules between sections. The column is 1000px wide (about 103–105 characters
      per line; it narrows to fit smaller screens). Danny treats the width as a variable to tune
      later.
    - While reading, the side columns dim and tighten to make room; hovering brings a column back.
    - `← BACK` or Esc returns to the square. The background morph runs on open and on close.
    - On a phone the page scrolls normally and opening jumps to the article (17px).
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
- **Background morph on a content change.** Danny likes it; refine later. When content changes (a
  new section, opening a piece, going back), the soft shapes travel across the page to a new
  arrangement (about 5s, slow in and slow out). Their colour swings to pink (about 0.9s) and settles
  back to blue (about 2.2s). The shapes are soft gradients that move without being re-blurred each
  frame. The clouds stay blue to violet, with no green. Demo: click any menu or rail item in
  `study/colour.html` (`study/shots/morph-400ms.png`, `study/shots/morph-3000ms.png`).
- **The label monospace.** Target: **Consolas**, which is what Danny's Kojima screenshot shows (taken
  on Windows; Kojima uses the visitor's system monospace). Consolas is licensed with Windows, not for
  serving on a website, so the site needs a free, self-hostable font that matches it. Candidates in
  the study page: Inconsolata, Cascadia Mono, JetBrains Mono, IBM Plex Mono, Geist Mono.
- **Reading face:** mono, Source Serif 4 or IBM Plex Sans (study page). The size is settled at 19px,
  with 1.6 line height.
- **Scroll model while reading:** text only (the page stays still) or the whole page, as Substack
  does.
- **Side columns while reading:** they currently tighten to 140/200px, and their faint text wraps.
  The alternative is to fade them out completely.
- **Stack.**
