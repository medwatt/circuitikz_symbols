# Circuitikz Symbols For Inkscape

Circuit symbols for drawing schematics in Inkscape. They are generated from the
Circuitikz package, so they look the same as what you'd get in LaTeX, with a few
changes to taste: the resistor is bolder with rounded corners, sources have
thicker outlines, current sources use a thin arrow with an open head, and the
ground has a bit more space between its bars.

Every pin sits on a 0.5mm grid, so parts snap together and wires drawn with grid
snapping on meet the leads exactly.

![schematic example](./example.svg)

There are two files:

- `circuitikz_common.svg`: about 70 parts I use all the time
  (resistors, capacitors, sources, diodes, MOSFETs and BJTs, op amps,
  logic gates, switches, grounds, supplies) plus a set of arrows and
  small markers like `+`, `-` and a circle for node numbers.
- `circuitikz_all.svg`: pretty much everything Circuitikz has, about 270
  parts. Useful when you need something unusual, but it's a long list
  to scroll through.

## Installation

1. Copy `circuitikz_common.svg` and `circuitikz_all.svg` into Inkscape's
   symbols folder. On Linux that's `~/.config/inkscape/symbols`. On
   Windows it's `%APPDATA%\inkscape\symbols`.
2. Install the fonts in `lmfonts.tar.gz` (Latin Modern). On Linux,
   extract it and move the folder to `~/.fonts` or
   `~/.local/share/fonts`. The part labels use Latin Modern Sans.
3. Restart Inkscape and open `Object > Symbols` (`Ctrl+Shift+Y`). The two
   sets show up in the drop-down as "CircuiTikZ - Common" and
   "CircuiTikZ - All".

## Labelling parts (R1, M2, ...)

Getting labels to sit at the same distance from every part by hand is
tedious, so there's a small extension that does it. Each symbol knows
where its label should go, and the extension puts it there and numbers
it (R1, R2, C1, M1, ...).

1. Copy `extension/label_parts.py` and `extension/label_parts.inx` into
   Inkscape's extensions folder (`~/.config/inkscape/extensions` on
   Linux, `%APPDATA%\inkscape\extensions` on Windows).
2. Restart Inkscape. It's now under `Extensions > Circuit > Label parts`.
3. Select some parts and run it. With nothing selected it labels every
   part in the drawing.

Labels are ordinary text, so you can double-click one and change it to
whatever you want. If you move parts around, run it again: existing
labels keep their text and just move back into place, and new parts
continue the numbering. It also handles rotated and mirrored parts, so a
flipped transistor gets its label on the other side and the text stays
readable.

### Keyboard shortcut

Going through the menu every time gets old quickly. To bind it to a key,
open `Edit > Preferences > Interface > Keyboard`, search for "Label
parts", click in the shortcut column and press the keys you want. I use
`Ctrl+Alt+L`. Avoid plain `Alt+letter`, since those open the menus.

## Grid and wire settings

The symbols are made for a 0.5mm grid and 0.5pt wires.

### Grid

1. Go to `File > Document Properties > Grids`.
2. Set the units to `mm` and both spacings to `0.5`.

### Wires

1. Select the pen tool (`B`).
2. Open `Object > Fill and Stroke` and set the stroke width to `0.5pt`.
3. Double-click the pen tool, choose `This tool's own style`, then
   `Take from selection` with a wire selected, so every new wire gets
   this width.

### Making it the default

Set up an empty document the way you like it, then use `File > Save
Template`, give it a name and tick `Set as default template`. New
documents will start with the grid already set up.
