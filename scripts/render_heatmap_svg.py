#!/usr/bin/env python3
"""Render the contribution JSON as a self-contained animated SVG."""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import date, timedelta
from html import escape
from pathlib import Path

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]
CELL = 12
GAP = 3
PITCH = CELL + GAP
LEFT = 42
TOP = 28
COLS = 53
ROWS = 7
WIDTH = LEFT + COLS * PITCH + 92
HEIGHT = TOP + ROWS * PITCH + 64


def week_start(value: date) -> date:
    return value - timedelta(days=(value.weekday() + 1) % 7)


def main() -> None:
    payload = json.loads(Path("data/contributions.json").read_text(encoding="utf-8"))
    raw_days = payload.get("days", [])
    days: dict[date, int] = {
        date.fromisoformat(item["date"]): int(item["level"])
        for item in raw_days
    }
    weeks = sorted({week_start(day) for day in days})[-COLS:]
    if not weeks:
        raise RuntimeError("No contribution weeks to render")
    weeks = [weeks[0] + timedelta(days=PITCH * 0) for _ in []] or weeks

    total = payload.get("total")
    total_label = f"{int(total):,} contributions in the last year" if total is not None else "Contribution activity"
    username = escape(str(payload.get("username", "Brightwav3")))
    source = escape(str(payload.get("source", "https://github.com/Brightwav3")), quote=True)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">',
        f"<title id=\"title\">{total_label} for {username}</title>",
        '<desc id="desc">A GitHub-style contribution calendar, generated from the public GitHub contribution page.</desc>',
        "<style>",
        "@keyframes cell-in { from { opacity: 0; transform: translateY(-7px); } to { opacity: 1; transform: translateY(0); } }",
        ".cell { animation: cell-in 560ms cubic-bezier(.22,.8,.32,1) forwards; transform-box: fill-box; transform-origin: center; opacity: 0; }",
        ".label { fill: #8b949e; font: 11px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; }",
        ".title { fill: #f0f6fc; font: 600 13px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; }",
        ".meta { fill: #8b949e; font: 11px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; }",
        "</style>",
        f'<rect width="{WIDTH}" height="{HEIGHT}" rx="12" fill="#0d1117" stroke="#30363d"/>',
        f'<text x="18" y="19" class="title">{total_label}</text>',
        f'<a href="{source}"><text x="{WIDTH - 18}" y="19" text-anchor="end" class="meta">@{username}</text></a>',
    ]

    # Month labels are positioned at the first visible week of each month.
    seen_months: set[tuple[int, int]] = set()
    for col, start in enumerate(weeks):
        month_key = (start.year, start.month)
        if month_key not in seen_months and (col == 0 or start.day <= 7):
            seen_months.add(month_key)
            label = start.strftime("%b")
            parts.append(f'<text x="{LEFT + col * PITCH}" y="{TOP - 9}" class="label">{label}</text>')

    for row, label in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        parts.append(f'<text x="4" y="{TOP + row * PITCH + 10}" class="label">{label}</text>')

    for col, start in enumerate(weeks):
        for row in range(ROWS):
            current = start + timedelta(days=row)
            level = max(0, min(5, days.get(current, 0)))
            x = LEFT + col * PITCH
            y = TOP + row * PITCH
            delay = (col * 0.018) + (row * 0.012)
            title = f"{current.isoformat()}: level {level}"
            parts.append(
                f'<rect class="cell" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="3" fill="{PALETTE[level]}" style="animation-delay:{delay:.3f}s"><title>{title}</title></rect>'
            )

    footer_y = TOP + ROWS * PITCH + 22
    parts.append(f'<text x="{LEFT}" y="{footer_y}" class="meta">Less</text>')
    for index, color in enumerate(PALETTE):
        x = LEFT + 35 + index * 17
        parts.append(f'<rect x="{x}" y="{footer_y - 10}" width="12" height="12" rx="3" fill="{color}"/>')
    parts.append(f'<text x="{LEFT + 35 + len(PALETTE) * 17 + 4}" y="{footer_y}" class="meta">More</text>')
    parts.append(f'<text x="{WIDTH - 18}" y="{footer_y}" text-anchor="end" class="meta">updated daily</text>')
    parts.append("</svg>\n")

    Path("contrib-heatmap.svg").write_text("\n".join(parts), encoding="utf-8")
    print(f"Rendered {len(weeks)} weeks to contrib-heatmap.svg")


if __name__ == "__main__":
    main()

