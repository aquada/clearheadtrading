"""Week-ahead calendar graphic (one row per day, key days highlighted).

Usage:
  python3 scripts/week_calendar.py OUT.png days.json

days.json:
  {"title": "The week ahead: Nov 16-20",
   "subtitle": "One-line summary of the week",
   "days": [{"name": "Monday", "date": "Nov 16", "major": false, "events": ["Fed Chair Warsh speaks"]}, ...]}

Line breaks inside an event are ignored; long events wrap automatically.

The figure is drawn 7.2in wide, the same as the 720px post column, so the
text shows at close to body size instead of being shrunk to fit (the old
13in five-card layout rendered its event text at ~7px).

Run inside: nix-shell -p 'python3.withPackages(ps: [ps.matplotlib])'
"""
import json
import sys
import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

HERE = Path(__file__).resolve().parent
for f in ("Inter.ttf", "Newsreader.ttf"):
    font_manager.fontManager.addfont(str(HERE / "fonts" / f))

BG = "#FFFDF9"
CARD = "#FFFFFF"
ACCENT = "#C96442"
ACCENT_BG = "#FBEDE6"
BORDER = "#E6DED4"
HEADING = "#2F3338"
MUTED = "#6B5E52"

W = 7.2                 # inches; matches the 720px content column
MARGIN = 0.22           # outer margin, inches
LEFT_COL = 1.75         # width of the day-name column inside a card
EVENT_PT = 11           # event text size
LINE = EVENT_PT * 1.55 / 72   # event line height, inches
CARD_PAD = 0.16         # vertical padding inside a card
GAP = 0.1               # gap between cards
WRAP = 60               # characters per event line


def lines_for(day):
    out = []
    for ev in day["events"]:
        out.extend(textwrap.wrap(" ".join(ev.split()), WRAP) or [""])
    return out


def draw(out, spec):
    days = spec["days"]
    rows = []
    for d in days:
        lines = lines_for(d)
        min_lines = 3 if d.get("major") else 2
        h = max(len(lines), min_lines) * LINE + 2 * CARD_PAD
        rows.append((d, lines, h))

    header = 0.95
    total_h = header + sum(h for _, _, h in rows) + GAP * (len(rows) - 1) + MARGIN

    fig = plt.figure(figsize=(W, total_h), dpi=200)
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(total_h, 0)   # y in inches from the top
    ax.axis("off")

    ax.text(MARGIN, 0.2, spec["title"], fontfamily="Newsreader", fontsize=19,
            color=HEADING, va="top")
    ax.text(MARGIN, 0.6, spec["subtitle"], fontfamily="Inter", fontsize=10.5,
            color=MUTED, va="top")

    y = header
    for d, lines, h in rows:
        major = d.get("major", False)
        ax.add_patch(FancyBboxPatch(
            (MARGIN, y), W - 2 * MARGIN, h,
            boxstyle="round,pad=0,rounding_size=0.08",
            linewidth=1.6 if major else 0.8,
            edgecolor=ACCENT if major else BORDER,
            facecolor=ACCENT_BG if major else CARD,
        ))
        tx = MARGIN + 0.2
        ty = y + CARD_PAD
        ax.text(tx, ty - 0.02, d["name"], fontfamily="Newsreader", fontsize=15,
                color=HEADING, va="top")
        ax.text(tx, ty + 0.27, d["date"], fontfamily="Inter", fontsize=10,
                color=MUTED, va="top")
        if major:
            ax.text(tx, ty + 0.5, "KEY DAY", fontfamily="Inter", fontsize=8.5,
                    color=ACCENT, va="top", fontweight="bold")
        divider_x = MARGIN + LEFT_COL
        ax.plot([divider_x, divider_x], [y + CARD_PAD, y + h - CARD_PAD],
                color=ACCENT if major else BORDER, linewidth=1)
        ex = divider_x + 0.22
        ey = y + CARD_PAD + 0.01
        for ln in lines:
            ax.text(ex, ey, ln, fontfamily="Inter", fontsize=EVENT_PT,
                    color=HEADING, va="top")
            ey += LINE
        y += h + GAP

    fig.savefig(out, facecolor=BG)
    plt.close(fig)


if __name__ == "__main__":
    out, spec_path = sys.argv[1:3]
    draw(out, json.loads(Path(spec_path).read_text()))
