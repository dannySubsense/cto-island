# 01-direction

**Job:** turn the design references and Danny's intent into decisions the build can follow.

**Inputs:**

- `_references/design/inspo/`: the inspiration images
- `docs/NORTHSTAR.md`: who the site is for
- what Danny says he wants; his words decide

**Process:**

1. **Measure every reference that has a live site.** Don't ask first. Run:

   ```bash
   python3 tools/measure_reference.py "<url>" <name>
   ```

   It saves screenshots (1440 wide viewport and full page, 390 wide phone) and the computed values
   (fonts, sizes, letter-spacing, colours, CSS variables, spacing, borders, layout columns,
   background grids and patterns) to
   `study/reference/`. Screenshots use this machine's fonts, so a site that relies on a system
   font Danny has and this VM lacks will look different. The JSON records the font the site asks for.
2. **Write a reading** for each reference in `study/reference/<name>.md`: the measured values that
   matter, and the principles Danny wants to carry over. Principles only; never copy a reference's
   surface.
3. **Build a study page:** plain HTML in `study/`, not part of the site. It puts the options side by
   side so Danny can choose by eye, for example colour variants on the grid background.
4. **Settle each decision with Danny:** palette, type, grid, layout regions, and how the centre area
   behaves when it holds a long article.
5. **Choose the stack with Danny,** from what the pages actually need.

**Outputs:**

- `DIRECTION.md` in this folder: each decision, stated once, as it currently stands
- `study/reference/`: measurements and readings for each reference
- `study/`: the study pages used to make the decisions

**Viewing the study page:** `study/README.md`, which covers starting the server, the URL and the
controls.

**Tools:** `tools/measure_reference.py` runs `tools/extract.js`, which is vendored unmodified from
taste-skill (MIT). Its colour `areaPct` double-counts nested elements, so judge which colours
dominate from the screenshot. Details: `_references/tools/taste-skill.md`.

**Checkpoint:** Danny approves `DIRECTION.md`. Nothing moves to `02-system/` before that.
