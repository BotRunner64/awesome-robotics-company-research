#!/usr/bin/env python3
"""
Generate keyword frequencies from company entries in README.md.

If optional dependencies `wordcloud` and `matplotlib` are installed, the script
writes assets/wordcloud.png. It always prints the keyword frequency table.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
ASSETS = ROOT / "assets"
WORDCLOUD_OUTPUT = ASSETS / "wordcloud.png"

STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "company",
    "companies",
    "customer",
    "customers",
    "data",
    "for",
    "from",
    "hq",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "robot",
    "robotics",
    "robots",
    "source",
    "sources",
    "status",
    "the",
    "to",
    "with",
}


def markdown_files() -> list[Path]:
    return [README] if README.exists() else []


def extract_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if path == README:
        text = extract_readme_entries(text)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    return text


def extract_readme_entries(readme_text: str) -> str:
    lines = []
    for line in readme_text.splitlines():
        if line.startswith("- ") and not line.startswith("- [Awesome"):
            lines.append(line)
    return "\n".join(lines)


def tokenize(text: str) -> list[str]:
    words: list[str] = []
    for word in re.findall(r"[A-Za-z][A-Za-z0-9-]*", text):
        normalized = word.lower().strip("-")
        if len(normalized) > 2 and normalized not in STOP_WORDS:
            words.append(normalized)
    return words


def print_frequency_table(counter: Counter[str], top_n: int = 40) -> None:
    print(f"\n{'Rank':<6}{'Keyword':<28}{'Count':<8}")
    print("-" * 42)
    for rank, (word, count) in enumerate(counter.most_common(top_n), 1):
        print(f"{rank:<6}{word:<28}{count:<8}")
    print(f"\nTotal unique words: {len(counter)}")
    print(f"Total word count: {sum(counter.values())}")


def write_wordcloud(counter: Counter[str], output_path: Path) -> bool:
    try:
        from wordcloud import WordCloud
    except ImportError:
        return False

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return False

    if not counter:
        return False

    output_path.parent.mkdir(parents=True, exist_ok=True)
    cloud = WordCloud(
        width=1600,
        height=800,
        background_color="white",
        colormap="viridis",
        max_words=150,
        min_font_size=10,
        prefer_horizontal=0.75,
        relative_scaling=0.5,
    )
    cloud.generate_from_frequencies(counter)

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.imshow(cloud, interpolation="bilinear")
    ax.axis("off")
    fig.savefig(output_path, dpi=150, bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)
    return True


def main() -> None:
    text = "\n".join(extract_text(path) for path in markdown_files())
    counter = Counter(tokenize(text))
    print_frequency_table(counter)

    if write_wordcloud(counter, WORDCLOUD_OUTPUT):
        print(f"\nWord cloud saved to: {WORDCLOUD_OUTPUT}")
    else:
        print("\nSkipped PNG word cloud; install wordcloud and matplotlib to enable it.")


if __name__ == "__main__":
    main()
