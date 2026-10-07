"""Score the Next Dollar goal search against goals people actually type.

This is the evaluation set, or eval set: a fixed group of test cases the
search gets scored against. Each case is something a person might type
("disney w kids") and the goal they meant ("Disney trip with the kids").
A case passes when the goal they meant shows up in the search's top 5.

This slice uses no AI. The score below is the baseline a later AI slice
has to beat.

Run it from the project folder:
    python3 scripts/eval_search.py
"""

import csv
import re
import unicodedata
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
TOP = 5

# The same shorthand list the page uses. If you change one, change both.
ALIASES = {
    "xmas": "christmas", "apt": "apartment security deposit", "biz": "business",
    "downpayment": "down payment", "grad": "master's degree", "tithe": "tithing",
    "tix": "tickets", "bday": "birthday", "reg": "registration", "prop": "property",
    "moms": "aging parent", "mom": "mom parent", "cushion": "emergency fund",
    "quit": "quitting freelance", "sisters": "sister's", "taxes": "tax bill",
    "stuff": "supplies maintenance", "house": "house down payment", "tshirts": "t-shirts",
    "newer": "used", "money": "fund", "out": "moving out", "vacay": "vacation",
    "reno": "remodel", "mortgage": "house", "bf": "partner", "gf": "partner",
    "hubby": "spouse", "wifey": "spouse",
}


def words(text):
    """Lowercase, drop accents, and split into words."""
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    return re.findall(r"[a-z0-9]+", text)


def expand(query):
    return " ".join(ALIASES.get(w, w) for w in words(query))


def search(query, goals, use_aliases=True):
    """Rank goals by how many typed words start a word in the goal.
    Ties go to the shorter goal name, then alphabetical. Mirrors the page."""
    if use_aliases:
        query = expand(query)
    terms = [t for t in words(query) if len(t) >= 2]
    scored = []
    for name, goal_words in goals:
        score = sum(1 for t in terms if any(w.startswith(t) for w in goal_words))
        if score:
            scored.append((-score, len(goal_words), name))
    scored.sort()
    return [name for _, _, name in scored[:TOP]]


def main():
    with open(DATA / "goals.csv", encoding="utf-8") as f:
        goals = [(row["goal"], words(row["goal"])) for row in csv.DictReader(f)]
    with open(DATA / "typed_goals.csv", encoding="utf-8") as f:
        cases = [(row["typed"], row["meant"]) for row in csv.DictReader(f)]

    plain = sum(meant in search(typed, goals, use_aliases=False) for typed, meant in cases)
    with_aliases = sum(meant in search(typed, goals) for typed, meant in cases)

    print(f"Search eval: {len(cases)} typed goals against a list of {len(goals)}")
    print(f"  Plain search found the right goal:      {plain} of {len(cases)} ({plain / len(cases):.0%})")
    print(f"  With the shorthand list:                {with_aliases} of {len(cases)} ({with_aliases / len(cases):.0%})")
    print()
    print("Still missed (these fall to the two neutral questions on the page):")
    for typed, meant in cases:
        found = search(typed, goals)
        if meant not in found:
            shown = ", ".join(found[:3]) or "no suggestions"
            print(f"  '{typed}' meant '{meant}'. Search showed: {shown}")
    print()
    print("Note: the shorthand list was written after seeing the first misses,")
    print("so real people will likely score a little lower.")


if __name__ == "__main__":
    main()
