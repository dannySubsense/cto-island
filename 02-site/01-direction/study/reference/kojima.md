# Kojima: reading

- **Source:** https://kojima-san.vercel.app/ by Marc Andrew (creator of HeroKit). Measured at
  `#s=736651081`, the seed in Danny's screenshot `_references/design/inspo/kojima-inspo.png`.
- **Measured on:** 2026-09-26, with `tools/measure_reference.py`
- **Files:** `kojima-measurements.json`, `kojima-viewport-1440.png`, `kojima-fullpage-1440.png`,
  `kojima-viewport-390.png`
- **Caveats:**
  - The graphic in the centre changes with the seed and the locked traits. This run drew layout
    OFFSET; Danny's screenshot has CENTERED. The interface around it is the same.
  - The screenshots show DejaVu Sans Mono, this VM's fallback font, not what Danny saw (see Type).

## Type

- **One family:** `ui-monospace, "SF Mono", Menlo, Consolas, monospace`. The site downloads no font
  files, so each visitor sees their own system monospace: SF Mono on a Mac, Consolas in Chrome on
  Windows, and something else on Linux.
- **One weight:** 400 everywhere. No bold anywhere.
- **Capitals throughout,** tracked wide:

  | Role | Size | Letter-spacing | Ratio |
  |---|---|---|---|
  | Site title (h1) | 14px | 3.5px | 0.25em |
  | Section labels (h2) | 10px | 2.5px | 0.25em |
  | Buttons | 10–13px | 1.5–1.95px | 0.15em |
  | Small labels | 8–10px | 1–2px | 0.1–0.2em |
  | Graphic title (`STRATA—55`) | 26px | 4px | 0.15em |

- **Most text is 10px.** Sizes used, by count: 10px ×40, 12px ×14, 11px ×7, 9px ×6, 8px ×4, 13px ×2,
  14px ×1, 26px ×1.

## Colour (the site's own CSS variables)

| Variable | Value | Role | Contrast on `--bg` |
|---|---|---|---|
| `--bg` | `#141310` | page, a warm near-black | — |
| `--panel` | `#1C1B17` | the stage behind the frame | — |
| `--ink` | `#EFEBE0` | main text and line art, a warm off-white | 15.6:1 |
| `--dim` | `#8A867A` | secondary labels | 5.1:1 |
| `--line` | `#33312A` | borders and rules | 1.4:1 (decorative only) |
| `--acc` | `#FF4D00` | the one accent: CTA frame, active lock, the dot, the square | 5.6:1 |

Six colours in total, all warm-tinted, with no pure black or white. The accent appears in only a
handful of places per screen.

## Lines and shapes

- **Borders:** all 1px solid. `--line` for the quiet frames (135 edges), `--ink` for the main frame
  and active inputs (40), `--acc` for the call-to-action (4).
- **No rounded corners** (radius 0 on every box; only the round swatches are circles). **No
  shadows.**
- **Line art in the graphic:** 1.5px strokes mostly, 1px for fine work, 0.75px dashed for the dotted
  orbit rings, and 2.25px accent strokes.
- **The frame device:** a 1px `--ink` rectangle with `+` crosshairs at the four corners. A header row
  (`N°1081 / KOJIMA — SERIES A / FIG.07`) sits over a rule, and a footer row with a large title and
  a small code line sits under another rule.

## Layout at 1440 wide

- The page has 28px padding, and a header row with a 1px rule under it.
- Below it are three columns in a flex row with a 24px gap:
  - **left rail:** 196px (its content starts 53px in from the page edge);
  - **centre stage:** 710px;
  - **right panel:** 324px, a stack of 1px-bordered cards.
- **At 390 wide** everything stacks into one column in this order: header, rail, stage, panel.
- **Spacing is small and not strictly on a grid.** By count: 8px ×40, 16px ×20, 6px ×19, 9px ×18,
  10px ×12, 7px ×12, 12px ×10. Mostly multiples of 4 and 8, with odd values mixed in.

## What this means for our site (observations for Danny to decide on)

- **The character comes from treatment, not an exotic font:** one monospace, one weight, capitals,
  wide tracking, small sizes, 1px lines, no radius, no shadow, one accent. That treatment carries
  over to any colour field, including a blue or magenta one.
- **We need a real, self-hosted monospace.** "Whatever the visitor has" would make the site look
  different on every machine. Which one to use depends on what Danny saw: SF Mono or Consolas.
- **This type is for labels, not reading.** Articles need body text at a reading size, either the
  same mono set larger or a second face.
- **The accent is used sparingly on purpose.** In our palette, magenta could play the role of
  `--acc` on a blue field, or the reverse.
