#!/usr/bin/env python3
"""Measure a live reference site: screenshots plus computed design values.

Usage: python3 measure_reference.py <url> <name>

Writes to 02-site/01-direction/study/reference/:
  <name>-viewport-1440.png, <name>-fullpage-1440.png, <name>-viewport-390.png,
  <name>-measurements.json

Needs the Python Playwright library and its Chromium build (both installed on this VM).
The browser renders with the fonts installed here. A site that asks for a system font this
machine lacks is screenshotted in a fallback font; the measurements record the requested
font-family, which is what counts.
"""

import json
import pathlib
import subprocess
import sys

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "study" / "reference"
EXTRACT = (HERE / "extract.js").read_text()

# Measurements extract.js does not take: layout regions, borders, SVG strokes and fills,
# gradient background patterns, reading measurements, CSS custom properties on :root.
EXTRA = r"""() => {
  const px = v => Math.round(v);
  const box = el => { const r = el.getBoundingClientRect(); return {x: px(r.x), y: px(r.y), w: px(r.width), h: px(r.height)}; };
  const regions = [];
  for (const el of document.querySelectorAll('body *')) {
    const r = el.getBoundingClientRect();
    const s = getComputedStyle(el);
    if (r.width <= 1000 || (s.display !== 'grid' && s.display !== 'flex')) continue;
    const kids = [...el.children].filter(k => k.getBoundingClientRect().width > 60);
    if (kids.length < 2) continue;
    regions.push({tag: el.tagName, cls: String(el.className).slice(0, 60), display: s.display,
      gridTemplateColumns: s.gridTemplateColumns, gap: s.gap, padding: s.padding, box: box(el),
      children: kids.map(k => ({tag: k.tagName, cls: String(k.className).slice(0, 40), box: box(k)}))});
  }
  const tally = () => new Map();
  const add = (m, k) => m.set(k, (m.get(k) || 0) + 1);
  const top = (m, n) => [...m.entries()].sort((a, b) => b[1] - a[1]).slice(0, n);
  const borders = tally(), strokes = tally(), fills = tally();
  for (const el of document.querySelectorAll('body *')) {
    const s = getComputedStyle(el);
    for (const side of ['Top', 'Right', 'Bottom', 'Left']) {
      const w = s['border' + side + 'Width'], st = s['border' + side + 'Style'];
      if (st !== 'none' && parseFloat(w) > 0) add(borders, w + ' ' + st + ' ' + s['border' + side + 'Color']);
    }
  }
  for (const el of document.querySelectorAll('svg *')) {
    const s = getComputedStyle(el);
    if (s.stroke && s.stroke !== 'none')
      add(strokes, s.stroke + ' ' + s.strokeWidth + (s.strokeDasharray !== 'none' ? ' dash ' + s.strokeDasharray : ''));
    if (s.fill && s.fill !== 'none' && el.tagName !== 'text') add(fills, s.fill);
  }
  const vars = {};
  for (const sheet of document.styleSheets) {
    let rules; try { rules = sheet.cssRules; } catch (e) { continue; }
    for (const r of rules)
      if (r.selectorText && /:root|html|body/.test(r.selectorText))
        for (const p of r.style) if (p.startsWith('--')) vars[p] = r.style.getPropertyValue(p).trim();
  }
  // Background patterns (grids, washes) drawn with gradients, including on ::before/::after,
  // on anything at least 600px wide.
  const patterns = [];
  for (const el of [document.documentElement, document.body, ...document.querySelectorAll('body *')]) {
    for (const pseudo of [null, '::before', '::after']) {
      const s = getComputedStyle(el, pseudo);
      if (!/gradient/.test(s.backgroundImage) || s.opacity === '0') continue;
      const r = el.getBoundingClientRect();
      if (r.width < 600) continue;
      patterns.push({tag: el.tagName, cls: String(el.className).slice(0, 50), pseudo, box: box(el),
        backgroundImage: s.backgroundImage.slice(0, 600), backgroundSize: s.backgroundSize,
        backgroundColor: s.backgroundColor, filter: s.filter, opacity: s.opacity, position: s.position});
    }
  }
  // Reading measurements: the paragraph style that carries the most text, its column width and
  // characters per line, the title style, and paragraph spacing.
  let reading = null;
  const byStyle = new Map();
  for (const p of document.querySelectorAll('p')) {
    const r = p.getBoundingClientRect(); const len = (p.innerText || '').trim().length;
    if (!r.width || len < 80) continue;
    const s = getComputedStyle(p);
    const key = [s.fontFamily, s.fontSize, s.lineHeight].join('|');
    const e = byStyle.get(key) || {chars: 0, el: p, count: 0}; e.chars += len; e.count++; byStyle.set(key, e);
  }
  const top1 = [...byStyle.values()].sort((a, b) => b.chars - a.chars)[0];
  if (top1) {
    const p = top1.el, s = getComputedStyle(p), r = p.getBoundingClientRect();
    const probe = document.createElement('span');
    probe.style.cssText = `font:${s.fontStyle} ${s.fontWeight} ${s.fontSize} ${s.fontFamily};letter-spacing:${s.letterSpacing};position:absolute;visibility:hidden;white-space:nowrap`;
    probe.textContent = 'the quick brown fox jumps over the lazy dog, and then the dog wakes up'.repeat(2);
    document.body.appendChild(probe); const avg = probe.getBoundingClientRect().width / probe.textContent.length; probe.remove();
    // The title is the largest visible h1 (a publication's name is often an h1 too, but smaller).
    const h1 = [...document.querySelectorAll('h1')].filter(h => h.getBoundingClientRect().width > 0)
      .sort((x, y) => parseFloat(getComputedStyle(y).fontSize) - parseFloat(getComputedStyle(x).fontSize))[0];
    const hs = h1 && getComputedStyle(h1);
    reading = {
      paragraphs: top1.count, family: s.fontFamily, size: s.fontSize, lineHeight: s.lineHeight,
      letterSpacing: s.letterSpacing, weight: s.fontWeight, color: s.color,
      marginBottom: s.marginBottom, marginTop: s.marginTop,
      columnWidth: Math.round(r.width), columnLeft: Math.round(r.x), viewportWidth: innerWidth,
      approxCharsPerLine: Math.round(r.width / avg),
      title: hs && {text: h1.innerText.slice(0, 80), family: hs.fontFamily, size: hs.fontSize, weight: hs.fontWeight,
        lineHeight: hs.lineHeight, letterSpacing: hs.letterSpacing, width: Math.round(h1.getBoundingClientRect().width)},
    };
  }
  const b = getComputedStyle(document.body);
  const blocked = /attention required|you have been blocked|verify you are human|just a moment/i.test(document.title + ' ' + (document.body.innerText || '').slice(0, 500));
  return {
    blocked,
    rootVars: vars,
    body: {bg: b.backgroundColor, color: b.color, font: b.fontFamily, size: b.fontSize, lineHeight: b.lineHeight},
    fontsLoaded: [...document.fonts].map(f => [f.family, f.weight, f.style, f.status]),
    regions: regions.slice(0, 6),
    backgroundPatterns: patterns.slice(0, 12),
    reading,
    borders: top(borders, 12),
    svgStrokes: top(strokes, 12),
    svgFills: top(fills, 10),
  };
}"""


def main(url: str, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fonts_requested = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.on("request", lambda r: fonts_requested.append(r.url) if r.resource_type == "font" else None)
        page.goto(url, wait_until="networkidle", timeout=60000)
        page.wait_for_timeout(2500)
        page.screenshot(path=str(OUT / f"{name}-viewport-1440.png"))
        page.screenshot(path=str(OUT / f"{name}-fullpage-1440.png"), full_page=True)
        scroll_height = page.evaluate("() => document.documentElement.scrollHeight")
        dom = page.evaluate(EXTRACT)
        extra = page.evaluate(EXTRA)
        page.set_viewport_size({"width": 390, "height": 844})
        page.wait_for_timeout(1000)
        page.screenshot(path=str(OUT / f"{name}-viewport-390.png"))
        phone_reading = page.evaluate(EXTRA).get("reading")
        browser.close()
    fallback = subprocess.run(["fc-match", "monospace"], capture_output=True, text=True).stdout.strip()
    record = {
        "url": url,
        "viewport": [1440, 900],
        "scrollHeight": scroll_height,
        "fontFilesDownloaded": fonts_requested,
        "thisMachineMonospaceFallback": fallback,
        "extract": dom,
        "extra": extra,
        "phone390Reading": phone_reading,
    }
    (OUT / f"{name}-measurements.json").write_text(json.dumps(record, indent=1, ensure_ascii=False))
    print(f"wrote {OUT}/{name}-*  errors={dom.get('errors')} truncated={dom.get('truncated')}")
    if extra.get("blocked"):
        print("WARNING: the site served a bot-check or block page; these measurements are not of the reference.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
