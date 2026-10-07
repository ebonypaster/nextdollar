"""Build the goal list for Next Dollar.

What it does, in order:
  1. Reads the raw goals in goals_data.py.
  2. Gives every goal a bucket based on how its money behaves.
  3. Trims the list to exactly 1,000 goals.
  4. Writes data/goals.csv (the list) and data/typed_goals.csv (the search test).
  5. Puts the list into index.html, between the GOALS:START and GOALS:END markers.

Run it from the project folder:
    python3 scripts/build_goals.py
"""

import csv
import json
import re
from collections import Counter
from pathlib import Path

from goals_data import CATS, MESSY

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
PAGE = ROOT / "index.html"
TARGET = 1000

# The four buckets. The page shows these words to people.
BUCKETS = {
    "C": "One-time, within 5 years",
    "L": "One-time, 5+ years out",
    "M": "Changes monthly money",
    "J": "Just in case",
}
NEED_WANT = {"n": "need", "w": "want", "d": "depends on the person"}


def bucket_for(labels):
    """Sort by how the money behaves, never by how important the goal is."""
    if labels["s"] == "m":
        return "M"
    if labels["s"] == "j":
        return "J"
    return "L" if labels["h"] == "l" else "C"


def read_goals():
    """Turn the text lists in goals_data.py into one row per goal."""
    rows, seen = [], set()
    for area, defaults, text in CATS:
        for raw in text.replace("\n", " ").split(";"):
            raw = raw.strip()
            if not raw:
                continue
            name, _, overrides = raw.partition("::")
            labels = dict(defaults)
            for pair in filter(None, overrides.split(",")):
                key, _, value = pair.partition("=")
                labels[key.strip()] = value.strip()
            name = name.strip()
            if name.lower() in seen:  # skip duplicates
                continue
            seen.add(name.lower())
            bucket = bucket_for(labels)
            also = labels.get("a", "")
            rows.append({
                "goal": name,
                "area": area,
                "bucket": bucket,
                "also": "" if also == bucket else also,
                "need_want": labels["n"],
            })
    return rows


def read_typed():
    """Pairs of (what someone typed, the goal they meant)."""
    pairs = []
    for item in MESSY.replace("\n", " ").split(";"):
        if "=>" in item:
            typed, meant = item.split("=>")
            pairs.append((typed.strip(), meant.strip()))
    return pairs


def trim(rows, keep):
    """Drop goals from the end of the biggest areas until 1,000 remain.
    Goals the search test points at are never dropped."""
    while len(rows) > TARGET:
        biggest = Counter(r["area"] for r in rows).most_common(1)[0][0]
        last = max(i for i, r in enumerate(rows)
                   if r["area"] == biggest and r["goal"] not in keep)
        rows.pop(last)
    return rows


def write_csvs(rows, typed):
    DATA.mkdir(exist_ok=True)
    with open(DATA / "goals.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["goal", "area", "bucket", "bucket_words", "could_also_fit", "old_need_want_label"])
        for r in rows:
            w.writerow([r["goal"], r["area"], r["bucket"], BUCKETS[r["bucket"]],
                        r["also"], NEED_WANT[r["need_want"]]])
    with open(DATA / "typed_goals.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["typed", "meant"])
        w.writerows(typed)


def write_page(rows):
    """Replace the goal list inside index.html, leaving everything else alone."""
    html = PAGE.read_text(encoding="utf-8")
    data = json.dumps([[r["goal"], r["bucket"]] for r in rows],
                      ensure_ascii=False, separators=(",", ":"))
    pattern = re.compile(r"/\*GOALS:START\*/.*?/\*GOALS:END\*/", re.S)
    if not pattern.search(html):
        raise SystemExit("Couldn't find the GOALS:START and GOALS:END markers in index.html")
    html = pattern.sub(lambda _: "/*GOALS:START*/" + data + "/*GOALS:END*/", html)
    PAGE.write_text(html, encoding="utf-8")


def main():
    typed = read_typed()
    rows = trim(read_goals(), keep={meant for _, meant in typed})
    missing = [meant for _, meant in typed if meant not in {r["goal"] for r in rows}]
    if missing:
        raise SystemExit(f"The search test points at goals that aren't in the list: {missing}")
    write_csvs(rows, typed)
    write_page(rows)

    counts = Counter(r["bucket"] for r in rows)
    print(f"Built {len(rows)} goals across {len({r['area'] for r in rows})} areas of life.")
    for key, words in BUCKETS.items():
        print(f"  {words:<26} {counts[key]:>4}  ({counts[key] / len(rows):.0%})")
    print(f"Wrote data/goals.csv, data/typed_goals.csv, and updated index.html.")


if __name__ == "__main__":
    main()
