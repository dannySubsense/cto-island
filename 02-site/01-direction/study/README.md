# Study page — how to view it

The study page is `colour.html` in this folder: the layout, colours, grid, clouds and reader we
designed. It is a plain HTML file; viewing it just needs a small web server on the VM.

## View it

1. On the VM, from the repo root, run:

   ```bash
   cd ~/cto-island/02-site/01-direction/study
   python3 -m http.server 8765 --bind 100.70.21.69
   ```

   That starts a web server for this folder, reachable only on the Tailscale address. Leave it
   running while you look.

2. On any machine on Tailscale, open:

   **http://100.70.21.69:8765/colour.html**

   The saved screenshots are at **http://100.70.21.69:8765/shots/**, for example
   `shots/unframed-1000-1440.png`.

3. When you're done, go back to the terminal and press **Ctrl+C** to stop the server.

## Using the page

- **Study controls:** the button at the bottom left, or press **H**. They set colours, grid, fonts,
  the reader style and the scroll model.
- **Open a piece:** click the centre square, a *Recent* item, or a paper in the right column.
- **Close a piece:** `← BACK`, or **Esc**.
- **Save a set of picks:** everything you set is written into the page address. Copy the URL to
  keep or share exactly that combination. The approved picks are:

  http://100.70.21.69:8765/colour.html#f=blue&bh=244&mh=340&fl=0.24&fc=0.09&cell=28&gs=1

- **Clean view for screenshots:** add `?clean` before the `#`, for example
  `colour.html?clean#f=blue&bh=244`.

## Measure a new reference site

To capture a site's fonts, colours, spacing and layout, run this from the repo root on the VM:

```bash
cd ~/cto-island/02-site/01-direction
python3 tools/measure_reference.py "<url>" <short-name>
```

The results (screenshots plus a measurements file) land in `study/reference/`. How this step fits
the stage is in `../CONTEXT.md`.
