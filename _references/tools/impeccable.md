# Impeccable

- **Repo:** https://github.com/pbakaus/impeccable
- **Commit read:** `9d715cc4f5564a990ca8345abfdd5df6dc9b41c8` (2026-09-25); npm package 4.1.0, skill 4.4.0,
  engine 0.1.6
- **Read on:** 2026-09-26, from the raw files at that commit
- **Read in full:** `README.md`, `package.json`, `cli/bin/cli.js`, and the Claude Code payload under
  `.claude/`: `settings.json`, `skills/impeccable/SKILL.md`, every file in
  `skills/impeccable/reference/` (including `degraded/`), `scripts/impeccable` (launcher),
  `scripts/command-metadata.json`, and the four agents in `.claude/agents/`
- **Searched, not read:** the Rust engine source (`crates/`, 300 `.rs` files) was grepped for
  network endpoints, API keys and telemetry only
- **Not read:** `scripts/live-browser.js` (547KB bundle), `scripts/modern-screenshot.umd.js`
  (third-party library), `scripts/data/font-index.json` (1.1MB data), `tests/`, the 17 other
  harness copies, `docs/`, `extension/`, `ui/`
- **Assumption:** the repo's own `.claude/` matches what the installer ships for Claude Code. The
  README's manual path copies `dist/claude-code/.claude`, which is a build output not in the repo.
- **License:** Apache 2.0
- **Status:** not installed

## What it is

A design skill plus a prebuilt engine binary. `/impeccable <command>` has 24 commands: `init`,
`shape`, `critique`, `audit`, `polish`, `bolder`, `quieter`, `distill`, `typeset`, `layout`,
`colorize`, `animate`, `live`, `generate` and others. The engine runs 61 deterministic detector
rules against HTML/CSS. For new visual work it runs its own full design process: an interview,
a randomized direction "roll" from a catalog of design worlds, optional AI image comps, measured
build gates, and a separate finish-reviewer subagent.

## What it would install or touch

- **Skill + agents:** `.claude/skills/impeccable/`, four agents in `.claude/agents/`.
- **Hooks** (`.claude/settings.json` in repo; installer writes `.claude/settings.local.json`,
  `README.md:402`): runs `scripts/impeccable hook` at **SessionStart**, after **every Edit/Write**,
  and on **Stop**.
- **Engine binary:** the launcher downloads a prebuilt binary from GitHub releases into
  `~/.impeccable/bin/<version>/` on first run (`README.md:99`, `scripts/impeccable:121-196`).
  It verifies against a `.sha256` file from the same release. That catches a corrupted download,
  not a compromised release.
- **Hooks bypass approval.** "installed command hooks run independently of model-tool approval.
  The first edit or Stop event can therefore download and cache the engine even if the session
  denies the model's launcher command" (`README.md:410`).
- **Project files it writes:** `PRODUCT.md` and `DESIGN.md` at the repo root, `.impeccable/`
  (config, critiques, screenshots, mocks, live-session state), and a `.gitignore` block
  (`README.md:356`).
- **Network:**
  - GitHub releases: engine download.
  - `https://impeccable.style/api/roll`: one GET per direction roll (scope, mode, seed key,
    re-roll counter; states no project content is sent) (`crates/context/src/seed_text.rs:24`).
  - Anonymous choice telemetry ping after each roll; off when `DO_NOT_TRACK` or
    `IMPECCABLE_NO_TELEMETRY` is set (`seed_text.rs:40`, `crates/context/src/concept_seed.rs:97`).
  - OpenAI image API, only if `OPENAI_API_KEY` is set (`crates/context/src/generate_image.rs:249`, `:303`).
  - Google Fonts, for font matching.
- **Live mode:** runs a localhost helper server (port 8400), injects a script into our pages,
  writes variant markup into source, and on copy edits runs `package.json`'s optional
  `impeccable:manual-edit-validate` script in a shell (`README.md:447`).

## Notable findings

1. **It chooses the design direction for new work.** For a new visual world, a randomized roll
   assigns the direction: "No substitute, no skip … writing artifact code before this script has
   run … is a contract violation" (`reference/new-work.md:48`). The user picks from dealt cards,
   re-rolls, or takes "the category standard", and a brief the user pinned beats the roll. If the
   decision page closes unanswered it proceeds with the assigned direction (`new-work.md:51`).
   This conflicts directly with "we build it ourselves and control the design."
2. **Strong built-in taste, stated as rules.**
   - The persona: "Go all out… Dream big and bold" (`SKILL.md:13-14`).
   - A list of fonts treated as "training-data defaults" that need special justification
     (Fraunces, Playfair, IBM Plex, DM Sans, Space Grotesk and others) (`new-work.md:67`).
   - An absolute ban on eyebrow/kicker labels above headings (`reference/craft-floor.md:27`).
   - Palette seeds with a target distribution of about "50% pure white, 25% pure black, 25%
     tinted" (`crates/context/src/palette_data.rs:136`).
   Some of this is good craft. It is still someone else's taste, and it would run in every design
   session.
3. **It runs on every edit.** The PostToolUse hook scans every UI file edit and pushes findings
   into the session, and a deeper pass runs at every Stop. This is in addition to our own hooks.
4. **The agent can silence its own findings.** On a "confident false positive" the agent may
   add a value-level ignore with a written reason, without asking (`reference/hooks.md:58-61`).
   Broader ignores need the user. This is doer-and-checker in one.
5. **Unsourced numbers drive pass/fail.**
   - The comp-led hero gate passes at 72% (`new-work.md:115`).
   - Craft-floor measures: 65–75ch body measure, 6rem display maximum, -0.04em tracking floor
     (`craft-floor.md:12`).
   - "Most real interfaces score 20-32 out of 40" (`reference/critique.md:118`).
   The working-memory rule does cite a source (Cowan 2001, `critique.md:338`).
6. **An internal inconsistency.** Critique looks for a `## Design Context` section in `CLAUDE.md`
   "generated by `impeccable init`" (`critique.md:790`), but `init` now writes `PRODUCT.md`
   (`reference/init.md`). On our repo that persona step would find nothing.
7. **Its init asks the right stack question.** For a project with no framework, "the stack is a
   user decision": plain static HTML/CSS, a framework, or a recommendation (`init.md:39`).
8. **The reviewer design is sound on paper.** The finish reviewer runs fresh with no inherited
   conversation, reviews screenshots rather than the builder's narration, and "the parent … has no
   authority to soften" its verdict (`.claude/agents/impeccable-finish-reviewer.md`). It still
   shares the builder's inputs and model.

## Parts usable without installing

- **Detector only:** `npx impeccable detect <file|dir|url>` runs the 61 rules with no skill, no
  hooks and no LLM (`README.md`, CLI section). It still downloads the engine binary.
- **Reading material:** the command prompts are clear frontend guidance: `craft-floor.md`
  (states, contrast, browser surfaces), `typeset.md`, `layout.md`, `animate.md`, `colorize.md`,
  `audit.md` and `harden.md`.

## Open questions

- Is the detector worth a downloaded binary, or does a standard accessibility checker cover
  what we need?
- If we install anything: project scope only, hooks off (`--no-hooks`), and telemetry off.
