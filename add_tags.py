#!/usr/bin/env python3
"""Rewrite frontmatter tags in chalkdust *_ko markdown files."""

from __future__ import annotations

import argparse
import math
import re
from pathlib import Path

from krwordrank.hangle import normalize
from krwordrank.word import KRWordRank
from kiwipiepy import Kiwi

NOUN_TAGS = {"NNG", "NNP", "NNB", "NR", "NP"}
EN_STOPWORDS = {
    "a",
    "an",
    "and",
    "by",
    "for",
    "from",
    "in",
    "of",
    "on",
    "or",
    "the",
    "to",
    "with",
}
KIWI = Kiwi()


def find_markdown_files(root: Path) -> list[Path]:
    return list(root.rglob("*.md"))


def _strip_quotes(value: str) -> str:
    value = value.strip()
    if value.startswith(('"', "'")) and value.endswith(('"', "'")):
        return value[1:-1]
    return value


def _split_frontmatter(lines: list[str]) -> tuple[list[str] | None, list[str]]:
    if not lines or lines[0].strip() != "---":
        return None, lines
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return None, lines
    return lines[: end_idx + 1], lines[end_idx + 1 :]


def _extract_title(frontmatter_lines: list[str]) -> str:
    for line in frontmatter_lines[1:-1]:
        if line.startswith("title:"):
            return _strip_quotes(line.split(":", 1)[1])
    return ""


def _first_heading(body_lines: list[str]) -> str:
    for line in body_lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return ""


def _collect_body_text(body_lines: list[str]) -> str:
    collected: list[str] = []
    in_code_block = False
    for line in body_lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if not stripped:
            continue
        if stripped.startswith("!["):
            continue
        cleaned = re.sub(r"https?://\\S+", " ", stripped)
        cleaned = cleaned.strip()
        if not cleaned:
            continue
        collected.append(cleaned)
    return " ".join(collected)

def _is_valid_token(token: str) -> bool:
    token = token.strip("_")
    if not token:
        return False
    if token.isdigit():
        return False
    return True


def _strip_latex(text: str) -> str:
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.DOTALL)
    text = re.sub(r"\$.*?\$", " ", text)
    return text


def _extract_nouns(text: str) -> list[str]:
    nouns: list[str] = []
    for token in KIWI.tokenize(text):
        if token.tag in NOUN_TAGS:
            cleaned = token.form.strip()
        elif token.tag == "SL":
            cleaned = token.form.strip()
            if cleaned.isascii() and cleaned.isalpha():
                if cleaned.casefold() in EN_STOPWORDS:
                    continue
        else:
            continue
        if not cleaned:
            continue
        if not _is_valid_token(cleaned):
            continue
        nouns.append(cleaned)
    return nouns


def _combined_text(text: str) -> str:
    lines = text.splitlines()
    frontmatter, body = _split_frontmatter(lines)
    title = ""
    if frontmatter:
        title = _extract_title(frontmatter)
    heading = _first_heading(body)
    body_text = _collect_body_text(body)

    sources: list[str] = []
    if title:
        sources.append(title)
    if heading:
        sources.append(heading)
    if body_text:
        sources.append(body_text)
    return " ".join(sources).strip()


def extract_keywords(
    noun_text: str,
    noun_set: set[str],
    doc_freq: dict[str, int],
    total_docs: int,
    core_tags: int,
    unique_tags: int,
    max_common_ratio: float,
) -> list[str]:
    if not noun_text:
        return []
    normalized = normalize(noun_text, english=True, number=True)
    extractor = KRWordRank(min_count=2, max_length=10, verbose=False)
    keywords, _, _ = extractor.extract([normalized], beta=0.85, max_iter=10)
    candidates: list[tuple[str, str, float]] = []
    for word, score in keywords.items():
        cleaned = word.strip()
        if not _is_valid_token(cleaned):
            continue
        key = cleaned.casefold()
        if key not in noun_set:
            continue
        candidates.append((cleaned, key, score))

    if not candidates:
        return []

    core_ranked = sorted(candidates, key=lambda item: (-item[2], item[0]))
    core: list[str] = []
    seen: set[str] = set()
    for word, _key, _score in core_ranked:
        if word in seen:
            continue
        core.append(word)
        seen.add(word)
        if len(core) >= core_tags:
            break

    unique_ranked: list[tuple[str, float, float]] = []
    for word, key, score in candidates:
        freq = doc_freq.get(key, 0)
        if total_docs and (freq / total_docs) > max_common_ratio:
            continue
        idf = math.log((total_docs + 1) / (freq + 1)) + 1.0
        unique_ranked.append((word, score * idf, score))
    unique_ranked.sort(key=lambda item: (-item[1], -item[2], item[0]))

    unique: list[str] = []
    for word, _adj, _score in unique_ranked:
        if word in seen:
            continue
        unique.append(word)
        seen.add(word)
        if len(unique) >= unique_tags:
            break

    target_total = core_tags + unique_tags
    if len(seen) < target_total:
        for word, _key, _score in core_ranked:
            if word in seen:
                continue
            unique.append(word)
            seen.add(word)
            if len(seen) >= target_total:
                break

    return core + unique


def _format_block_tags(tags: list[str]) -> list[str]:
    lines = ["tags:"]
    lines.extend(f"  - {tag}" for tag in tags)
    return lines


def rewrite_tags(text: str, tags: list[str]) -> tuple[str, bool]:
    has_trailing_newline = text.endswith("\n")
    lines = text.splitlines()
    frontmatter, body = _split_frontmatter(lines)

    if frontmatter is None:
        tag_lines = "\n".join(_format_block_tags(tags))
        new_text = f"---\n{tag_lines}\n---\n\n{text}"
        return new_text, True

    new_frontmatter = ["---"]
    i = 1
    while i < len(frontmatter) - 1:
        line = frontmatter[i]
        if line.startswith("tags:"):
            i += 1
            if line.strip() == "tags:":
                while i < len(frontmatter) - 1 and frontmatter[i].lstrip().startswith("-"):
                    i += 1
            continue
        new_frontmatter.append(line)
        i += 1
    new_frontmatter.extend(_format_block_tags(tags))
    new_frontmatter.append("---")

    new_lines = new_frontmatter + body
    new_text = "\n".join(new_lines)
    if has_trailing_newline:
        new_text += "\n"
    return new_text, new_text != text


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Rewrite tags in chalkdust *_ko markdown frontmatter."
    )
    parser.add_argument(
        "--root",
        default="crwal/chalkdust",
        help="Root directory to scan (default: crwal/chalkdust)",
    )
    parser.add_argument(
        "--core-tags",
        type=int,
        default=3,
        help="Number of core tags per document (default: 3)",
    )
    parser.add_argument(
        "--unique-tags",
        type=int,
        default=5,
        help="Number of unique tags per document (default: 5)",
    )
    parser.add_argument(
        "--max-common-ratio",
        type=float,
        default=0.2,
        help="Drop keywords appearing in too many docs (default: 0.2)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List files that would change without writing.",
    )
    args = parser.parse_args()

    root = Path(args.root)
    if not root.exists():
        raise SystemExit(f"Root not found: {root}")

    files = find_markdown_files(root)
    doc_info: dict[Path, tuple[str, set[str], str]] = {}
    doc_freq: dict[str, int] = {}

    for path in files:
        text = path.read_text(encoding="utf-8")
        combined = _combined_text(text)
        cleaned = _strip_latex(combined)
        nouns = _extract_nouns(cleaned)
        noun_text = " ".join(nouns)
        noun_set = {noun.casefold() for noun in nouns}
        for noun in noun_set:
            doc_freq[noun] = doc_freq.get(noun, 0) + 1
        doc_info[path] = (text, noun_set, noun_text)

    total_docs = len(files)
    for path, (text, noun_set, noun_text) in doc_info.items():
        tags = extract_keywords(
            noun_text,
            noun_set,
            doc_freq,
            total_docs,
            args.core_tags,
            args.unique_tags,
            args.max_common_ratio,
        )
        updated, changed = rewrite_tags(text, tags)
        if changed:
            if args.dry_run:
                print(path)
            else:
                path.write_text(updated, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
