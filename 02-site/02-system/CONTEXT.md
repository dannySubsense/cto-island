# 02-system

**Job:** put every design value in one place and make it impossible to bypass.

**Inputs:** the approved `01-direction/DIRECTION.md`.

**Process:**

1. Create the code project for the stack chosen in `01-direction/`.
2. Write the tokens file: colours, font families, the type scale, spacing, the grid. Name tokens by
   role, not by value.
3. Add a lint check that fails on any raw colour, font, size, or spacing value outside the tokens
   file.
4. Build a specimen page that renders every token from the tokens file.

**Outputs:**

- the code project
- the tokens file
- a lint check that passes
- the specimen page

**Checkpoint:** Danny reviews the specimen page and approves it. A change to a design decision goes
back to `01-direction/` first.
