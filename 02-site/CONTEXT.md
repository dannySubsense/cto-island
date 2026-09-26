# 02-site

**Job:** the website itself: its design, layout, code, and published pages.

**Inputs:** approved pieces from `01-content/`; design references in `_references/design/`.

**Outputs:** a built site, ready for `03-deploy/`.

## Stages

Work moves through these in order. Each stage ends at Danny's approval before the next one starts.

| Stage | Job | Output |
|---|---|---|
| `01-direction/` | Turn the references and Danny's intent into design decisions and a stack choice | `DIRECTION.md`, approved |
| `02-system/` | Put every design value in one place and enforce it | The code project, one tokens file, a lint check, a specimen page |
| `03-shell/` | Build the page frame from the tokens | The layout template, shared components, the site map |
| `04-pages/` | Build real pages from approved content | Pages ready for `03-deploy/` |

Each stage's `CONTEXT.md` states its inputs, process, and outputs. Load only the stage you're working in.

## Rules

These exist because earlier Claude-built sites failed in exactly these ways.

- **Danny makes the design calls.** References are inspiration, never templates to copy. No stock
  styles, and no tool that picks a direction for us.
- **One source for design values.** Every colour, font, size, and spacing value lives in the tokens
  file. Anything else that needs a value uses a token. A lint check fails the build on a raw value
  anywhere else, so correctness never depends on a grep.
- **One site map, kept current.** `03-shell/` writes it: pages, layouts, components, where the tokens
  live. It stays short enough to read in full.
- **No backend until a feature needs one.** Anything server-side that gets added is listed in the site
  map when it lands.
- **Keep the machinery minimal.** Each piece of work should serve getting Danny's writing in front of
  leadership.
