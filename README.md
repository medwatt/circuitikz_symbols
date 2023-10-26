# Circuitikz Symbols For Inkscape

This repository offers a collection of electrical circuit symbols,
extracted from the Circuitikz package, that can be used in Inkscape for
schematic creation.

## Installation and Setup

1. **Download SVG File**: Download the SVG file named
   `circuitikz_1mm_grid.svg`.
2. **Locate Inkscape Directory**: Move the downloaded SVG file to
   Inkscape's symbol directory. On Linux systems, this is typically
   `$HOME/.config/inkscape/symbols`.
3. **Download and Install Font**: Download the Latin Modern Roman font
   package (`lmfonts.tar.gz`). Unzip and install the fonts. On Linux,
   installation involes simple moving the extracted folder to
   `$HOME/.fonts`.
4. **Access Symbols in Inkscape**: To use the symbols, go to `Object >
   Symbols` within Inkscape and pick the SVG file from the drop-down list.

## Configuration Guidelines

These symbols are optimized for a grid size of 1mm and a wire width of
0.75pt.

### Grid Setup

1. Navigate to `File > Document Properties > Grids`.
2. Set `Grid Units` to `mm`.
3. Configure both `SpacingX` and `SpacingY` to `1`.

### Wire Width Adjustment

1. Activate the pen tool by clicking on it or pressing `B`.
2. Open the `Object > Fill and Stroke` menu.
3. Under `Stroke Style`, set the width to `0.75pt`.

To maintain these settings:

1. Double-click on the pen tool.
2. Select `This tool's own style` and `Take from selection`.

### Setting as Default

To make these configurations the default for future Inkscape sessions:

1. Go to `File > Save Template`.
2. Name the template and check `Set as default template`.
3. Restart Inkscape.

This ensures that you won't need to repeat these steps each time you open Inkscape.
