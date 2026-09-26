# Substack (and Medium): reading

- **Sources:** two Substack essays, on two different publication themes:
  - `substack-article`: https://markatwood.substack.com/p/the-strategy-of-technology-was-a (dark
    theme)
  - `substack-article-2`: https://slowfutures.substack.com/p/long-read-ai-in-2026 (light theme)
- **Measured on:** 2026-09-26, with `tools/measure_reference.py`
- **Files:** `substack-article*-measurements.json` (see `extra.reading` and `phone390Reading`), plus
  1440 viewport, full-page and 390 phone screenshots
- **Medium: not measured.** Medium served a Cloudflare "you have been blocked" page to the
  automated browser. We don't work around bot blocks, so no Medium numbers here. If Danny wants
  Medium, the way in is his own browser.

## The reading column

Both essays use the same body settings, whatever the publication's theme:

| | Desktop (1440) | Phone (390) |
|---|---|---|
| Body face | Spectral (serif), 400 | same |
| Body size / line height | 19px / 30.4px (1.6) | 17px / 27.2px (1.6) |
| Text column width | 664–704px, centred | 294–334px |
| Characters per line (estimated) | about 76–81 | about 38–44 |
| Paragraph spacing | 8–20px (differs by theme) | same |
| Letter-spacing | normal | normal |

- **Titles:** set by the theme: SF Pro Display 32px/700 on one, Lora 38px/600 on the other. They
  sit directly above the column at the same width, followed by a subtitle, a small uppercase byline
  and date, then the text.
- **The column is the whole design.** There's no frame around the text, and nothing sits beside
  the column on desktop. Only a thin top bar with the publication name and buttons, and a small
  section-outline marker at the far left edge.
- **Sections are separated by thin horizontal rules** across the column width, with headings about
  twice the body size.
- **The whole page scrolls, top bar included.** That differs from our current study, where only
  the text block scrolls.

## What this means for our reader (observations for Danny to decide on)

- **Unframed works because the column is narrow and the side space is empty.** In our layout, the
  equivalent would be the frame fading away and the text column centred on the grid background.
  The side columns would step back while reading.
- **Their numbers are a reasonable starting point for our reading text:** about 19px body, about
  1.6 line height, about 660–700px column. That column fits inside our 690px square area, so the
  text could keep the same centre position the square had.
- **Their reading face is a serif, not a mono.** The study page already lets Danny compare mono,
  serif and sans in the reader.
- **Page scroll vs inner scroll** is a real choice. Substack scrolls the page; our current study
  keeps the page still and scrolls only the text. Both can work with an unframed column.
