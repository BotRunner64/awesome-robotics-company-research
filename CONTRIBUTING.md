# Contributing

Thanks for helping improve this robotics company research list.

## What To Add

- Robotics companies, labs, or products with public research or technical
  updates.
- Official company posts, research pages, papers, demos, product pages, or
  credible primary sources.
- Short descriptions that help readers understand why the company or update is
  relevant.

Avoid adding unsourced claims, marketing-only summaries, or private information.

## README Format

Keep `README.md` as the primary source of truth.

Company index entries should use this format:

```markdown
- [Company](#company-anchor), short description, [website](https://example.com).
```

Company section entries should use this format when a month is available:

```markdown
- YYYY.MM, Title or short update summary, [website](https://example.com)
```

Within each company section, keep entries in reverse chronological order.

## Source Guidelines

- Prefer official company, research, blog, product, or publication pages.
- Use stable links when possible.
- Keep descriptions factual and concise.
- If a source is not official, make sure it is credible and clearly relevant.

## Before Submitting

Run the lightweight checks that match your change:

```sh
git diff --check
```

If you changed `scripts/generate_wordcloud.py`, also run:

```sh
python3 -m py_compile scripts/generate_wordcloud.py
python3 scripts/generate_wordcloud.py
```

## Pull Requests

- Keep each pull request focused.
- Explain what company or entries were added or updated.
- Mention any sources that may need extra review.
- Do not add new dependencies unless the change explicitly requires them and the
  rationale is clear.
