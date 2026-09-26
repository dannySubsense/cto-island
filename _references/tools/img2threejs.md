# img2threejs

- **Repo:** https://github.com/img2threejs/img2threejs (the official org; several forks exist under
  other accounts)
- **Commit read:** `6e60b5e22419464b4853e01ddb6c0e6f6659a733` (2026-09-06), version 2.0.0
- **Read on:** 2026-09-26, from the raw files at that commit
- **Read in full:** `README.md`, `SKILL.md`, `CLAUDE.md`, `LAB-FINDINGS.md`
- **Searched, not read:** every Python file in `forge/` (about 90 modules, 3.4MB), parsed for imports
  outside the Python standard library and grepped for network and subprocess calls; the five
  subprocess sites were then read in context
- **Not read:** the `forge/` code logic, `grimoire/` (256KB of stage-by-stage reference prompts),
  `docs/` (522KB), `integrations/`, `ROADMAP.md`, `CHANGELOG.md`, the companion showcase repo, and
  the `img2` plugin harness (a separate repo)
- **License:** Apache 2.0
- **Status:** not installed. Danny decided on 2026-09-26 that we will use it later.

## What it is

A Claude Code skill that takes one reference image of an object or character and rebuilds it as a
procedural Three.js model written in TypeScript: a `createObjectNameModel()` factory returning a
`THREE.Group`, with no mesh files. It works in locked passes (blockout → structure → form → material
→ surface → lighting → interaction → optimization). Python scripts validate the spec and gate each
step; the agent judges each pass from a side-by-side comparison of reference and render
(`SKILL.md:99-251`). Its live demos are CS2 weapon skins, knives, earbuds, a bike and stylized
characters (`README.md:54-70`).

## What it would install or touch

- The whole repo, cloned into `~/.claude/skills/img2threejs` (`README.md:116`). No hooks and no
  settings changes; it is a skill with its own scripts.
- **The core scripts need only the standard library.** I checked this: no `forge/` module imports
  anything outside the Python standard library or its own package, and none makes a network call.
  The only subprocess uses are:
  - macOS `sips` for image conversion when its built-in decoders fail
    (`forge/stage1_intake/delight_albedo.py:173-181`). On this Linux VM, such images will error.
  - An optional vision adapter run in its own virtualenv
    (`forge/stage1_intake/run_vision_adapter.py`).
  - Commands from installed plugins, for export targets (`forge/stage3_build/emit_target.py:154-175`).
- **Project files it writes:** `.img2threejs/state.json`, an `object-sculpt-spec.json`, assessment
  and inventory JSON, renders, comparison sheets, and the generated `.ts` factory.
- **What it needs around it:**
  - A running Three.js page in a browser.
  - A screenshot tool (browser MCP or Playwright).
  - For some gates, a `runtime/scripts/export_mesh_geometry.mjs` that is not in this repo
    (`SKILL.md:222`).
  - For TypeScript checks, a checkout of the separate showcase repo (`CLAUDE.md:25`).
- **Optional extras bring real dependencies and network use:** SAM2, Depth Anything and MediaPipe
  through `integrations/vision` (`uv.lock`); plugins through the `img2` harness installed with
  `npx github:img2threejs/img2 install` (`README.md:132`); and `plugin-img2glb`, which uses a
  hosted TRELLIS service (`README.md:149`).

## Notable findings

1. **The best-engineered of the four, and the least intrusive.**
   - It is honest about its limits: "A single image cannot reveal hidden sides or guarantee exact
     geometry" (`README.md:361`).
   - It fails closed before generating code (`SKILL.md:202-205`).
   - Its own lab notes record a live defect in its harness rather than hiding it (`LAB-FINDINGS.md`).
   - Nothing runs unless the skill is invoked.
2. **It contradicts itself on cost.** The headline says "deliberately token-efficient"
   (`README.md:9`). The sponsor section says "the pipeline is token-hungry by design, because gating
   a spec before codegen means running the analysis more than once" (`README.md:444-445`). Expect a
   long, expensive loop per object.
3. **It is heavy for what it would give us.** Each object runs about a dozen gated stages, needs
   browser rendering and screenshots each pass, and caps corrections at 3 per pass and 6 in total
   (`SKILL.md:75`).
4. **It would add Three.js and TypeScript to the site.** The output is a TypeScript Three.js factory
   (`SKILL.md:414`). That pulls a WebGL library and a build step into a site we want to keep small
   and static.
5. **It does not address any of our five failure modes** (generic look, scattered CSS, grep misses,
   no mental model, backend sprawl). It makes 3D objects; it has nothing to do with the site's
   design system.
6. **Unsourced numbers drive its gates.**
   - PBR confidence below 0.7 is a stop (`SKILL.md:187-188`).
   - Triangle tiers: ≤6k, ≤60k, else hero (`SKILL.md:209-210`).
   - The Divine Eye reviewer compares on a 64×64 luma grid (`SKILL.md:329-330`).
   They are tool internals, but pass/fail depends on them.

## Worth keeping

- If the site ever wants one signature 3D object, this is the candidate to revisit. At that point,
  read the `grimoire/` files for the relevant stages and the generator, `forge/stage3_build/`.

## Open questions

- Does the site need a 3D object at all? That is a design decision, not a tool question.
