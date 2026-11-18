"""Week-ahead calendar graphic (five day cards, key days highlighted).

Usage:
  python3 scripts/week_calendar.py OUT.png days.json

days.json:
  {"title": "The week ahead: Nov 16-20",
   "subtitle": "One-line summary of the week",
   "days": [{"name": "Monday", "date": "Nov 16", "major": false, "events": ["Fed Chair Warsh\\nspeaks"]}, ...]}

Run inside: nix-shell -p 'python3.withPackages(ps: [ps.matplotlib])'
"""
import json
import sys
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


def draw(out, spec):
    days = spec["days"]
    n = len(days)
    fig, ax = plt.subplots(figsize=(13, 5.2), dpi=200)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, n)
    ax.set_ylim(0, 1)
    ax.axis("off")

    pad, top, bottom = 0.05, 0.86, 0.05
    for i, d in enumerate(days):
        x0, width = i + pad, 1 - 2 * pad
        major = d.get("major", False)
        ax.add_patch(FancyBboxPatch(
            (x0, bottom), width, top - bottom,
            boxstyle="round,pad=0,rounding_size=0.035",
            linewidth=2.0 if major else 1.0,
            edgecolor=ACCENT if major else BORDER,
            facecolor=ACCENT_BG if major else CARD,
            clip_on=False,
        ))
        cx = x0 + width / 2
        if major:
            ax.text(cx, top - 0.06, "KEY DAY", ha="center", va="top",
                    fontfamily="Inter", fontsize=8.5, color=ACCENT)
        name_y = top - 0.13
        ax.text(cx, name_y, d["name"], ha="center", va="top",
                fontfamily="Newsreader", fontsize=16, color=HEADING)
        ax.text(cx, name_y - 0.09, d["date"], ha="center", va="top",
                fontfamily="Inter", fontsize=9.5, color=MUTED)
        ax.plot([cx - 0.12, cx + 0.12], [name_y - 0.17] * 2,
                color=ACCENT if major else BORDER, linewidth=1)
        y = name_y - 0.22
        for ev in d["events"]:
            ax.text(cx, y, ev, ha="center", va="top", fontfamily="Inter",
                    fontsize=9.5, color=HEADING, linespacing=1.45)
            y -= 0.075 * (ev.count("\n") + 1) + 0.06

    fig.text(0.02, 0.955, spec["title"], fontfamily="Newsreader", fontsize=19, color=HEADING, va="top")
    fig.text(0.02, 0.885, spec["subtitle"], fontfamily="Inter", fontsize=10, color=MUTED, va="top")
    plt.subplots_adjust(top=0.84, bottom=0.03, left=0.012, right=0.988)
    fig.savefig(out, facecolor=BG)
    plt.close(fig)


if __name__ == "__main__":
    out, spec_path = sys.argv[1:3]
    draw(out, json.loads(Path(spec_path).read_text()))
