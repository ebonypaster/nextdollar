# Next Dollar

See your next money step through three popular frameworks side by side: Dave Ramsey's Baby Steps, the Money Guy's Financial Order of Operations, and the Reddit flowchart.

You answer a few questions about your employer match, emergency fund, debt, and what's coming up, then enter the money you have. The page shows where each plan would put it, month by month or all at once, and where the plans disagree. It shows the frameworks, not a recommendation, so the choice stays with you.

This is slice one. It is for learning, not financial advice.

## What's in this folder

- `index.html` is the whole page. No build step, no server, no tracking, and nothing you type is saved or sent.
- `data/goals.csv` is the list of 1,000 things people save for, each sorted into a bucket.
- `data/typed_goals.csv` is 51 goals typed the way people actually type them ("disney w kids," "downpayment"), each paired with the goal they meant.
- `scripts/goals_data.py` is the raw goal list, grouped into 25 areas of life.
- `scripts/build_goals.py` builds the two CSV files and puts the goal list into the page.
- `scripts/eval_search.py` scores the page's goal search against the typed goals.

## The goal list and why it exists

The page asks what else is coming up in the next few years, and people can search for a goal or type their own. The first plan used AI to sort typed goals. Before building that, I tested whether a fixed list could do the job.

- Goals are sorted by how the money behaves, not by how important they are. The four buckets are one-time within 5 years, one-time 5+ years out, changes monthly money, and just in case.
- An earlier need-and-want sort was dropped. 46% of goals depended on the person, and goals like family reunions, Eid, Hajj, and funerals would have been labeled a want.
- Only 4% of goals could fit two buckets, mostly moves and home buying.

## The search eval

An evaluation set, or eval set, is a fixed group of test cases a system gets scored against. This one checks whether the goal someone meant shows up in the search's top five.

| Search | Found the right goal |
|---|---|
| Plain search | 34 of 51 (67%) |
| With a short shorthand list (xmas, apt, biz) | 47 of 51 (92%) |

The shorthand list was written after seeing the first misses, so real people will likely score a little lower. Anything the search misses goes to two neutral questions on the page: is it a one-time cost or a change to your monthly money, and when do you need it.

This slice uses no AI. The next slice adds AI only for the goals search misses, and it has to beat this baseline.

## Run the scripts

You need Python 3. From this folder:

```
python3 scripts/build_goals.py
python3 scripts/eval_search.py
```

The first rebuilds the list and updates the page. The second prints the eval score and the goals it still misses. If you change the shorthand list in `index.html`, change it in `eval_search.py` too.

## Publish on GitHub Pages

1. Put this folder in a new repository.
2. In the repository, go to Settings, then Pages.
3. Under Build and deployment, choose Deploy from a branch, pick `main` and `/ (root)`, and save.
4. The site appears at `https://<your-username>.github.io/<repository-name>/` within a few minutes.

## Sources

- [Ramsey Solutions: The 7 Baby Steps](https://www.ramseysolutions.com/dave-ramsey-7-baby-steps)
- [Ramsey Solutions: When to pause your debt snowball](https://www.ramseysolutions.com/debt/3-reasons-to-pause-debt-snowball)
- [Money Guy: Financial Order of Operations](https://moneyguy.com/guide/foo/)
- [Money Guy: Should I pay off debt or invest?](https://moneyguy.com/faq/should-i-pay-off-my-debt-before-saving-for-retirement/) for the age-based interest cutoffs
- [r/personalfinance guide](https://www.reddit.com/r/personalfinance/wiki/commontopics/) and the flowchart built on it, Version 4.3 by u/happyasianpanda (2023)
