#!/usr/bin/env python3
"""Label circuit symbols (R1, M2, ...) at the anchor stored in each symbol.

Symbols carry data-label="prefix x y dx dy" (anchor point, and the direction from the
body towards the label). Selected parts are labelled -- or every part if nothing is
selected. Parts that already have a label keep its text and only get it realigned,
so re-running after moving parts tidies the labels up again.
"""
import inkex
from inkex import Transform, Tspan, TextElement, Use

FONT_SIZE = "9pt"
STYLE = "font-family:'Latin Modern Sans';font-weight:normal;fill:#000000;stroke:none"


class LabelParts(inkex.EffectExtension):
    def effect(self):
        uses = list(self.svg.selection.filter(Use).values()) or list(self.svg.descendants().filter(Use))
        labels = {t.get("data-label-for"): t for t in self.svg.xpath("//svg:text[@data-label-for]")}
        count = {}
        for t in labels.values():
            p, n = t.get("data-prefix"), int(t.get("data-num", 0))
            count[p] = max(count.get(p, 0), n)
        # number in reading order: rows top to bottom, then left to right
        parts = [(u, self.anchor(u)) for u in uses]
        parts = sorted((p for p in parts if p[1]), key=lambda p: (round(p[1][1][1] / 5), p[1][1][0]))
        for use, (prefix, point, direction) in parts:
            text = labels.get(use.get_id())
            if text is None:
                count[prefix] = count.get(prefix, 0) + 1
                text = self.new_label(prefix, count[prefix])
                text.set("data-label-for", use.get_id())
                use.getparent().append(text)
            self.place(text, point, direction)

    def anchor(self, use):
        sym = use.href
        spec = sym.get("data-label") if sym is not None else None
        if not spec:
            return None
        prefix, x, y, dx, dy = spec.split()
        x, y, dx, dy = map(float, (x, y, dx, dy))
        t = use.transform @ Transform(translate=(float(use.get("x", 0)), float(use.get("y", 0))))
        p, q = t.apply_to_point((x, y)), t.apply_to_point((x + dx, y + dy))
        return prefix, (p.x, p.y), (q.x - p.x, q.y - p.y)

    def new_label(self, prefix, num):
        text = TextElement()
        text.set("data-prefix", prefix)
        text.set("data-num", str(num))
        text.set("xml:space", "preserve")
        letter = Tspan(prefix)
        letter.style = "font-style:oblique"
        sub = Tspan(str(num))
        sub.style = "font-style:normal;font-size:70%;baseline-shift:sub"
        text.append(letter)
        text.append(sub)
        return text

    def place(self, text, point, direction):
        fs = self.svg.unittouu(FONT_SIZE)
        (x, y), (dx, dy) = point, direction
        if abs(dx) >= abs(dy):  # beside the part, vertically centred on the anchor
            anchor, y = ("end" if dx < 0 else "start"), y + 0.35 * fs
        else:                   # above or below, horizontally centred
            anchor, y = "middle", (y if dy < 0 else y + 0.7 * fs)
        text.set("x", f"{x:.3f}")
        text.set("y", f"{y:.3f}")
        text.set("transform", None)
        text.style = f"{STYLE};font-size:{fs:.4f}px;text-anchor:{anchor};text-align:{ {'end': 'end', 'start': 'start', 'middle': 'center'}[anchor]}"


if __name__ == "__main__":
    LabelParts().run()
