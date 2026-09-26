# taste-skill

- **Repo:** https://github.com/senlindesign/taste-skill
- **Commit read:** `6dce223f2f5665d3636ca9a44ec3a7aa1322a9b8` (2026-07-07), version 1.1.0
- **Read on:** 2026-09-26, in full, from the raw files at that commit
- **Read:** `README.md`, `SKILL.md`, `references/step1-4*.md`, `references/export-formats.md`,
  `references/extract.js`, `evals/evals.json`
- **Not read:** `docs/` (landing page HTML and images; the skill never uses them)
- **License:** MIT
- **Status:** not installed

## What it is

A Claude Code skill. `/taste <url>` opens the live page in a browser via Playwright MCP, takes a
1440×900 screenshot, runs `extract.js` inside the page to measure colours, type, spacing, radii,
shadows and grid, then runs four prompts (Measure → Pattern → Taste → Observer). Output is
`{domain}.md` and `{domain}.json`: a Design Map of exact values plus 3–4 principles written as
Trigger / Decision ("chose A over B") / Reason / Evidence.

## What it would install or touch

- Clones into `~/.claude/skills/taste` (every project).
- Requires Playwright MCP: `claude mcp add playwright -s user -- npx -y @playwright/mcp@latest --isolated`
  (`SKILL.md:62`). This is user scope and an unpinned version.
- Writes `{domain}.md`, `{domain}.json` and screenshots into the current working directory and
  overwrites existing files without asking (`SKILL.md:273`, `SKILL.md:278`).
- Optional export step writes to agent config: the Claude Code target appends a `## Design Taste`
  section to `CLAUDE.md` (`references/export-formats.md:64-66`; `README.md:115`).
- `extract.js` runs only inside the analysed web page. It reads computed styles and makes no network
  calls.

## Notable findings

1. **Export writes another site's taste into our agent rules.** The Claude Code export appends
   always/never directives to `CLAUDE.md`. Here `CLAUDE.md` is a pointer, and standing rules drawn
   from someone else's site conflict with "inspo, not copy". If used, choose export target **Skip**.
2. **Overwrites without asking**, into whatever directory the session is in (`SKILL.md:273-278`).
   Run it only from a dedicated output folder.
3. **Eager self-triggering.** "lean toward activating … When in doubt, use it" on any URL mentioned
   alongside a design topic (`SKILL.md:47`).
4. **Pitched partly as mimicry**: "build me a landing page in the style of <url>", "port this site's
   design" (`SKILL.md:43`). The trade-off analysis itself (why, not just what) fits our use;
   the export and mimicry framing do not.
5. **Live URLs only.** It refuses local files (`SKILL.md:350`), so the PNGs in
   `_references/design/inspo/` can't go in; it needs the live sites.
6. **The area measurement doesn't measure what the colour rule assumes.** The rule: a colour covering
   <5% of *visible surface area* is decorative, not brand (`SKILL.md:236`,
   `references/step1-measure.md:15`). The only area number the extractor provides, `areaPct`
   (`references/extract.js:120-121`, `:187`), sums the bounding-box area of every element with a
   background, across the full page, with nested elements counted again on top of their parents.
   It is a share of a double-counted total, not of what is visible.
7. **Unsourced claims and constants.**
   - "validated in production" for the Gemini pipeline the prompts came from (`SKILL.md:358`).
   - "validated against 5 real sites" for the 6× page-height screenshot rule (`README.md:258`).
   - Thresholds with no stated source: 5% area, ≤3% shadow opacity (`SKILL.md:236`), 8,000
     elements (`references/extract.js:31`), 60KB payload cap (`references/extract.js:390`).
   - `evals/evals.json` describes 3 evals (linear.app, are.na, stripe.com), but the repo has no
     code that runs them.
8. **Tied to Playwright MCP tool names** (`mcp__playwright__*`, e.g. `SKILL.md:140`). It does not
   work with Playwright CLI without changes.
9. **Payload truncation is flagged.** When trimmed, the extractor sets `truncated: true`
   (`references/extract.js:390-407`), so a trimmed result is visible, not silent.

## Worth keeping regardless of install

- The principle format: Trigger / Decision (A over B, where B is a real alternative) / Reason /
  Evidence.
- At least one restraint principle: what the design chose *not* to do.
- The test for a weak principle: "could I have written this without ever seeing this specific
  website?" (`SKILL.md` philosophy section).

## Open questions

- Which live URLs sit behind the Formas and Kojima references?
- If we install: which Playwright MCP version to pin, and at project scope only?
