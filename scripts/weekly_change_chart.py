"""Weekly-change bar chart for week-ahead blog covers, in the site's own style.

Usage:
  python3 scripts/weekly_change_chart.py OUT.png "Week ending Friday 13 November 2026" DAX=3.6 Dow=2.1 NASD=3.5
  python3 scripts/weekly_change_chart.py --from-post content/blog/<slug>/index.md

Run inside: nix-shell -p 'python3.withPackages(ps: [ps.matplotlib])'
"""
import re
import sys
from datetime import date, timedelta
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

HERE = Path(__file__).resolve().parent
for f in ("Inter.ttf", "Newsreader.ttf"):
    font_manager.fontManager.addfont(str(HERE / "fonts" / f))

SURFACE = "#FFFDF9"
HEADING = "#2F3338"
MUTED = "#6B5E52"
RULE = "#DDD5CB"
ACCENT = "#C96442"
UP = "#0E8770"    # validated against DOWN with the dataviz palette checker (CVD-safe)
DOWN = "#C96442"
FLAT = "#A39A8F"

ORDER = ["DAX", "Dow", "NASD", "Nasdaq"]


def draw(out, subtitle, values, kicker="Weekly change"):
    values = sorted(values, key=lambda kv: ORDER.index(kv[0]) if kv[0] in ORDER else 99)
    fig = plt.figure(figsize=(16, 9), dpi=100)
    fig.patch.set_facecolor(SURFACE)

    fig.text(0.06, 0.865, kicker.upper(), fontfamily="Inter", fontsize=17,
             color=ACCENT, fontweight="semibold")
    fig.text(0.06, 0.775, subtitle, fontfamily="Newsreader", fontsize=34, color=HEADING)

    ax = fig.add_axes([0.22, 0.08, 0.72, 0.6])
    ax.set_facecolor(SURFACE)
    nums = [v for _, v in values]
    lo, hi = min(0.0, min(nums)), max(0.0, max(nums))
    span = max(hi - lo, 1.0)
    pad = span * 0.26
    has_flat = any(v == 0 for v in nums)
    left = pad if lo < 0 else span * 0.04
    right = pad if (hi > 0 or has_flat) else span * 0.04
    ax.set_xlim(lo - left, hi + right)
    n = len(values)
    ax.set_ylim(-0.6, n - 0.4)

    for i, (label, v) in enumerate(values):
        y = n - 1 - i
        colour = UP if v > 0 else DOWN if v < 0 else FLAT
        width = v if v != 0 else span * 0.006
        ax.barh(y, width, height=0.42, color=colour, linewidth=0)
        offset = span * 0.025
        ax.text(v + (offset if v >= 0 else -offset), y, f"{v:+.1f}%",
                va="center", ha="left" if v >= 0 else "right",
                fontfamily="Inter", fontsize=26, color=HEADING)
        fig.text(0.06, ax.transData.transform((0, y))[1] / fig.bbox.height, label,
                 va="center", fontfamily="Newsreader", fontsize=38, color=HEADING)

    ax.axvline(0, color=RULE, linewidth=2)
    ax.axis("off")
    fig.savefig(out, facecolor=SURFACE)
    plt.close(fig)


def from_post(md_path):
    text = Path(md_path).read_text()
    image = re.search(r'^\s+image:\s*"?([^"\n]+)"?', text, re.M).group(1)
    alt = re.search(r'^\s+alt:\s*"([^"]+)"', text, re.M).group(1)
    post_date = re.search(r'^date:\s*(\d{4})-(\d{2})-(\d{2})', text, re.M)
    pairs = re.findall(r'(DAX|Dow|NASD|Nasdaq)\s*\(?([+-]\d+(?:\.\d+)?)%', alt)
    values = [(name, float(v)) for name, v in pairs]

    kicker, subtitle = "Weekly change", None
    m = re.search(r'week ending Friday, (\w+ \d+)', alt)
    year = post_date.group(1)
    if m:
        subtitle = f"Week ending Friday {m.group(1).split()[1]} {m.group(1).split()[0]} {year}"
    elif "pullback" in alt.lower():
        d = date(int(year), int(post_date.group(2)), int(post_date.group(3)))
        tuesday = d - timedelta(days=(d.weekday() - 1) % 7)
        kicker = "Pullback from the week's highs"
        subtitle = f"To the close on Tuesday {tuesday.day} {tuesday:%B %Y}"
    else:
        d = date(int(year), int(post_date.group(2)), int(post_date.group(3)))
        friday = d - timedelta(days=(d.weekday() - 4) % 7 or 7)
        subtitle = f"Week ending Friday {friday.day} {friday:%B %Y}"
    out = Path(md_path).parent / image
    draw(out, subtitle, values, kicker)
    print(f"{out}: {subtitle} {values}")


if __name__ == "__main__":
    if sys.argv[1] == "--from-post":
        for p in sys.argv[2:]:
            from_post(p)
    else:
        out, subtitle, *pairs = sys.argv[1:]
        draw(out, subtitle, [(k, float(v)) for k, v in (p.split("=") for p in pairs)])
