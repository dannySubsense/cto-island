# awesome-design-skills

- **Repo:** https://github.com/bergside/awesome-design-skills
- **Commit read:** `f631a09b4fcc0166f2e2c1a8c81906ef680c57e8` (2026-06-28)
- **Read on:** 2026-09-26, from the raw files at that commit
- **Read in full:** `README.md`; `skills/minimal/SKILL.md` and `skills/minimal/DESIGN.md`; the
  per-skill content (Brand, Style Foundations, accessibility and tone lines, Do/Don't rules) of
  all 67 `SKILL.md` files
- **Checked by comparison, not read one by one:** the rest of each `SKILL.md` (the instruction
  body) and the other 66 `DESIGN.md` files
- **Not read:** `registry-examples/*.png` (preview images); the TypeUI CLI (`typeui.sh`), which
  does the installing and lives in a separate repo, https://github.com/bergside/typeui.sh
- **License:** MIT
- **Status:** not installed

## What it is

A catalog of 67 named styles (Minimal, Brutalism, Editorial, Glassmorphism, Terracotta, and so on).
Each has a `SKILL.md` for an agent and a `DESIGN.md` for people. You install one with
`npx typeui.sh pull <slug>`, which writes the `SKILL.md` into the agent's folders
(`.claude/`, `.cursor/skills/` and others) (`README.md:455`).

## What it would install or touch

- The `SKILL.md` for one style, written into the agent config folders by the TypeUI CLI.
- Running the CLI through `npx` fetches and executes the `typeui.sh` package, which was not read.

## Notable findings

1. **The skills are generated boilerplate.**
   - The instruction body from `## Expected Behavior` onward is identical in 62 of the 67 files.
     The other 5 differ only by blank lines.
   - What differs per style is a one-line brand description, a font trio, about seven hex
     values, and a spacing scale.
   - The files are marked `TYPEUI_SH_MANAGED`, output of the `typeui.sh generate` command
     (`README.md:486`).
2. **Many are unfilled.**
   - 16 skills carry the same default palette: primary `#3B82F6`, secondary `#8B5CF6`
     (Tailwind's blue-500 and violet-500). Examples: "Premium" (brand line: "Apple design
     style"), "Refined", "Retro", "Futuristic".
   - 10 have an empty Brand section.
   - Some brand lines are placeholders: "the best game in the world" (fantasy), "Electronics
     shop" (professional).
   - `mono` and `neumorphism` share the same brand line ("Join the private club…") and nearly
     identical foundations.
3. **The DESIGN.md files have no rationale.** All 67 are generated from the tokens. The only
   explanation given for each colour is "Token from style foundations." The README promises
   "Rationale and references" (`README.md:440`).
4. **Some claims contradict their own values.**
   - Every skill claims WCAG 2.2 AA.
   - `pulse`'s text colour on its own surface colour (`#EA580C` on `#FDBA74`) is 2.1:1, below
     the 4.5:1 AA minimum.
   - `mono`'s text on surface (`#78716B` on `#E7E5E4`) is 3.8:1.
   - `matrix` describes itself as "dark-only", but its tokens set a white surface.
   - Nearly every skill lists weights 100–900, including single-weight display fonts such as
     Bangers and Audiowide.
5. **Several copy named brands**: `claude` (Anthropic's fonts), `premium` ("Apple design style"),
   `lingo` ("duolingo inspired"), `sega`, `pacman`, `tetris`.
6. **The instructions are aimed at the wrong job.** The mission line in every file is "You are an
   expert design-system guideline author": it tells the agent to write guidelines, not to build UI
   to them.
7. **It is the opposite of building our own design.** Pulling one means adopting a stock style.

## Worth keeping

- One pattern, not the content: design values as named tokens, with do/don't rules written
  against those tokens. This is the single-source-of-values idea we need anyway.

## Open questions

- None that would change the outcome. The catalog adds nothing that writing our own token file
  wouldn't do better.
