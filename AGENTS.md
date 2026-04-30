# Repository Instructions

This repository is a lightweight awesome-list style collection of robotics
company research links.

## Project Shape

- Keep `README.md` as the primary source of truth.
- Avoid adding docs, data files, or per-company profile scaffolds unless the user
  explicitly asks for them.
- Current expected structure: `README.md`, `CONTRIBUTING.md`, `LICENSE`,
  `.gitignore`, `assets/.gitkeep`, `scripts/generate_wordcloud.py`, and this
  file.
- Keep diffs small, reviewable, and reversible.
- Prefer deletion over addition during cleanup.
- Do not add new dependencies without an explicit request.

## README Conventions

- Keep entries short and source-backed.
- Prefer official company, research, blog, or product pages as sources.
- Company index entries should use this form:

  ```markdown
  - [Company](#company-anchor), short description, [website](https://example.com).
  ```

- Company sections should list research/news entries in reverse chronological
  order when dates are available.
- Use `YYYY.MM` for month-level dates.
- Preserve the concise awesome-list tone.

## Script Conventions

- `scripts/generate_wordcloud.py` must keep PNG generation dependencies optional.
- The keyword frequency table should continue to work with the Python standard
  library only.
- Do not require generated image assets for normal repository use unless the user
  explicitly asks for them.

## Verification

- README-only changes: run `git diff --check`.
- Python script changes: run `python3 -m py_compile scripts/generate_wordcloud.py`.
- If behavior changes in `scripts/generate_wordcloud.py`, also run
  `python3 scripts/generate_wordcloud.py`.
- Check `git status --short` before final reporting.

## Commit Protocol

When asked to commit, use a Lore-style message:

```text
<intent line: why the change was made, not just what changed>

<body: narrative context, constraints, and approach rationale>

Constraint: <external constraint that shaped the decision>
Rejected: <alternative considered> | <reason for rejection>
Confidence: <low|medium|high>
Scope-risk: <narrow|moderate|broad>
Directive: <forward-looking warning for future modifiers>
Tested: <what was verified>
Not-tested: <known gaps in verification>
```

Use only the trailers that add value. Always include honest `Tested:` and
`Not-tested:` trailers when committing.
