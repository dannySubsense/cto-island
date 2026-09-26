# cto-island — workspace map

Read `docs/NORTHSTAR.md` for what this project is for. This project designs, builds, and deploys
the site. It publishes the content it receives and never writes that content.

## Where things live

| Path | Job |
|---|---|
| `01-content/` | One folder per piece of Danny's writing, ready to publish, waiting for his OK |
| `02-site/` | The website: design, layout, code, published pages. Built in four stages: direction, system, shell, pages |
| `03-deploy/` | Taking the site live |
| `_references/` | Stable reference material (design inspiration, notes on outside tools) |
| `docs/` | Northstar and decision records |
| `scripts/`, `.claude/` | Session tooling (startup probe, relay command, hooks). Not a workspace; don't change as part of site work |

## Routing

| Task | Go to | Also load | Ignore |
|---|---|---|---|
| New content arrived, or prepare a piece | `01-content/CONTEXT.md` | — | `02-site/` code, `03-deploy/` |
| Design, layout, site code | `02-site/CONTEXT.md`, then the current stage's `CONTEXT.md` (`01-direction` → `02-system` → `03-shell` → `04-pages`) | `_references/design/` | `01-content/` |
| Evaluate or install an outside tool or skill | `_references/tools/` (one notes file per tool) | — | `01-content/` |
| Deploy | `03-deploy/CONTEXT.md` | — | `01-content/` |

Each folder's `CONTEXT.md` states its job, inputs, process, and outputs. Load only what the task
needs.

## Naming

`YYYY-MM-DD_type_slug`, where `type` is `paper`, `initiative`, or `notebook`.
Example: `2026-10-02_paper_working-theory`.

## Human checkpoints

- Nothing moves from `01-content/` to `02-site/` without Danny's publish OK.
- Content text is never edited unless Danny asks.
