# 03-shell

**Job:** build the page frame that every page sits in.

**Inputs:** the approved tokens and specimen from `02-system/`; the layout regions in
`01-direction/DIRECTION.md`.

**Process:**

1. Build the layout template with the regions `DIRECTION.md` names, using tokens only.
2. Build only the shared components the frame needs now (for example a card, a frame, a label). A
   component is added when a page needs it, not in advance.
3. Define how the frame behaves at phone, tablet, and desktop widths.
4. Write the site map: pages, layouts, components, where the tokens live, anything server-side.

**Outputs:**

- the layout template
- the shared components
- the site map, in `02-site/SITEMAP.md`

**Checkpoint:** Danny approves the empty frame at desktop and phone widths.
