#!/usr/bin/env python3
"""Fetch the public GitHub contribution calendar without an API token."""

from __future__ import annotations

import html
import json
import os
import re
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path


class ContributionParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.days: list[dict[str, object]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "td":
            return
        values = dict(attrs)
        classes = (values.get("class") or "").split()
        if "ContributionCalendar-day" not in classes:
            return
        date = values.get("data-date")
        level = values.get("data-level")
        if date and level is not None:
            self.days.append({"date": date, "level": int(level)})


def main() -> None:
    username = os.environ.get("GITHUB_USERNAME", "Brightwav3")
    url = f"https://github.com/users/{username}/contributions"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Brightwav3-profile-contribution-map/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        source = response.read().decode("utf-8")

    parser = ContributionParser()
    parser.feed(source)
    if not parser.days:
        raise RuntimeError("GitHub returned no contribution cells")

    total_match = re.search(
        r"([\d,]+)\s+contributions?\s+in\s+the\s+last\s+year",
        html.unescape(re.sub(r"<[^>]+>", " ", source)),
        flags=re.IGNORECASE,
    )
    total = int(total_match.group(1).replace(",", "")) if total_match else None

    payload = {
        "username": username,
        "source": url,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "total": total,
        "days": parser.days,
    }
    output = Path("data/contributions.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Fetched {len(parser.days)} days for {username}; total={total}")


if __name__ == "__main__":
    main()

