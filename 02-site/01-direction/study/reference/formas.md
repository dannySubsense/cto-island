# Formas: reading

- **Source:** https://formas.ai/ (home page) and https://formas.ai/founding-studios (the card grid in
  `_references/design/inspo/formas-inspo.png`)
- **Measured on:** 2026-09-26, with `tools/measure_reference.py`
- **Files:** `formas-home-*` and `formas-founding-*` (measurements JSON; 1440 viewport, full-page
  and 390 phone screenshots)
- **Not measured:** the wine/magenta "Have a referral?" page in
  `_references/design/inspo/formas-taste-layout-inspo.png`. It is step 3 of 3 of the signup setup
  in `/studio`, not a public page. What we know about its blurred colour field comes from the image
  alone.

## The grid background (the part Danny wants)

The same grid is on every Formas page: `.global-crosses-pattern::before`, a full-screen layer. It is
two square grids drawn with CSS gradients:

| Layer | Cell | Line width | Line colour |
|---|---|---|---|
| Fine | 28 × 28px | 1px | `rgba(160,130,100,0.06)`, warm beige at 6% |
| Major | 140 × 140px (5 fine cells) | 1.25px | `rgba(180,150,120,0.10)`, warm beige at 10% |

- **It is pure CSS:** four `linear-gradient` layers with `background-size: 28px 28px, 28px 28px,
  140px 140px, 140px 140px`. No image file.
- **The lines are tinted toward the page colour,** not grey. On a blue or magenta field the same
  construction would use a tint of that field.
- **The Founding Studios page adds soft light on top of the grid:** a faint gold radial glow at the
  top (`radial-gradient(at 50% 0%, rgba(212,175,55,0.1), transparent 52%)`) and a darkening wash
  over the whole page.
- **The magenta page** (from the image only) layers large, heavily blurred colour shapes under the
  same grid. That blur is what gives it depth.

## The card grid (formas-inspo)

- **Layout:** 3 columns × 2 rows, each column about 347px, gap 20px, the whole grid 1080px wide and
  centred.
- **Card:**
  - 24px corner radius;
  - 1px border in `rgba(255,235,210,0.06)`, nearly invisible;
  - translucent warm-dark fill `rgba(28,22,18,0.7)` with `backdrop-filter: blur(10px)`, so the grid
    shows through softly;
  - 30px padding; no shadow.
- **Card type:** titles in the system sans at 16.8px, weight 600, `#E8E0D8`; body at 14px with
  22.5px line-height, `#A89888`.
- **Headings:** Georgia serif at 64px (h1) and 48px (h2), weight 400, slightly negative tracking.

## Colours (the site's own CSS variables, abridged)

- Backgrounds: `#0a0a0a`, `#141414`, `#1a1a1a`
- Text: `#ffffff`, `#a0a0a0`, `#666666`
- Borders: `#2a2a2a`
- Accent: gold (`#B8860B`, `#D4AF37`, `#DAA520`) and orange (`#E8903C`, `#F5A623`)
- Also defined: `--formas-magenta: #FF00FF` and `--formas-cyan: #00E5FF`. Neither is prominent on the
  pages measured.

## What we take from Formas

Danny's call: from Formas we take **the background and the grid only.** The boxes, layout and type
come from Kojima (see `kojima.md` and `../../DIRECTION.md`).

- **The grid:** two layered square grids, fine and major, with lines tinted from the field colour at
  very low opacity. It carries over to a blue or magenta field directly; the study page varies cell
  size and line strength.
- **The background:** a deep colour field with large, heavily blurred shapes under the grid (from
  the magenta page), plus soft light washes like the Founding Studios page.
- **Not taken:** Formas cards (rounded, translucent), its type (system sans plus Georgia) and its
  gold/orange palette.
