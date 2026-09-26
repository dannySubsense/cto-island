# cto-island — workspace map

Read `docs/NORTHSTAR.md` for what this project is for. This project designs, builds, and deploys
the site. It publishes the content it receives and never writes that content.

## Where things live

| Path | Job |
|---|---|
| `01-inbox/` | Content exactly as Danny delivers it |
| `02-staging/` | One folder per piece, prepared for publishing, waiting for Danny's OK |
| `03-site/` | The website: design, layout, code, published pages |
| `04-deploy/` | Taking the site live |
| `_references/` | Stable reference material (design inspiration, rules) |
| `docs/` | Northstar and decision records |
| `scripts/`, `.claude/` | Session tooling (startup probe, relay command, hooks). Not a workspace; don't change as part of site work |

## Routing

| Task | Go to | Also load | Ignore |
|---|---|---|---|
| New content arrived | `01-inbox/CONTEXT.md` | — | `03-site/`, `04-deploy/` |
| Prepare a piece for publishing | `02-staging/CONTEXT.md` | the piece in `01-inbox/` | `03-site/` code |
| Design, layout, site code | `03-site/CONTEXT.md` | `_references/design/` | `01-inbox/`, `02-staging/` |
| Deploy | `04-deploy/CONTEXT.md` | — | `01-inbox/`, `02-staging/` |

Each folder's `CONTEXT.md` states its job, inputs, process, and outputs. Load only what the task
needs.

## Naming

`YYYY-MM-DD_type_slug`, where `type` is `paper`, `initiative`, or `notebook`.
Example: `2026-10-02_paper_working-theory`.

## Human checkpoints

- Nothing moves from `02-staging/` to `03-site/` without Danny's publish OK.
- Content text is never edited unless Danny asks.
