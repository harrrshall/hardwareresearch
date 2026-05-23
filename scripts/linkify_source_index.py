#!/usr/bin/env python3
"""
For each sector's research.md, within the '## Source Index' section, linkify
the title cell of every data row in every pipe-table.

Strategy:
  1. Find the '## Source Index' section (until next '## ' heading at top level).
  2. Inside it, iterate pipe tables. For each header, identify:
     - the Title column (header contains 'title', 'source', or 'name')
     - the URL column (header contains 'url' or 'link') — optional
  3. For each data row, if title is plain text:
     a. Use the row's URL column if available.
     b. Else, fuzzy-match the title against sources.json titles to find a URL.
  4. Replace the title cell with `[Title](URL)`. Leave row otherwise unchanged.
  5. Skip rows whose title is already a link.

Robust to multiple tables and sub-sections under 'Source Index'.
"""

import json
import re
import difflib
from pathlib import Path

ROOT = Path("/home/cybernovas/Desktop/2026/experiments/hardware/research")
SECTORS = [
    "GPUs", "CPUs", "memory", "chip_fabrication", "AI_accelerators",
    "packaging", "photonics", "interconnects", "datacenter_hardware",
    "edge_AI_hardware",
]
URL_PATTERN = re.compile(r"https?://[^\s)|<>]+")

def load_sources_map(sector_dir: Path):
    """Return list of (title_lower, url, id) for all sources in sources.json."""
    j = sector_dir / "sources.json"
    if not j.exists():
        return []
    try:
        data = json.loads(j.read_text(encoding="utf-8"))
    except Exception:
        return []
    items = data if isinstance(data, list) else data.get("sources", [])
    out = []
    for it in items:
        title = str(it.get("title", "")).strip()
        url = str(it.get("url", "")).strip()
        sid = str(it.get("id", "")).strip()
        if title and url.startswith(("http://", "https://")):
            out.append((title.lower(), url, sid))
    return out


def split_cells(row: str):
    """Split a pipe-table row into cells, preserving outer pipes."""
    # Strip leading/trailing | if present
    s = row.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def is_table_separator(line: str) -> bool:
    """Detect markdown table alignment row like |---|---|."""
    if "|" not in line:
        return False
    parts = [p.strip() for p in line.strip().strip("|").split("|")]
    return all(re.match(r"^:?-{3,}:?$", p) for p in parts if p)


def is_table_row(line: str) -> bool:
    s = line.strip()
    return s.startswith("|") and s.count("|") >= 2 and not is_table_separator(line)


def is_already_link(title: str) -> bool:
    s = title.strip()
    return s.startswith("[") and "](" in s


def find_col(headers, *keywords):
    """Find first column whose header contains any of the keywords (case-insensitive)."""
    for i, h in enumerate(headers):
        hl = h.lower()
        for kw in keywords:
            if kw in hl:
                return i
    return -1


def linkify_md(md_path: Path, sources_list):
    text = md_path.read_text(encoding="utf-8")
    lines = text.split("\n")

    # 1. Find Source Index section bounds
    si_start = None
    si_end = len(lines)
    for i, line in enumerate(lines):
        s = line.strip().lower()
        if si_start is None and re.match(r"^#{2,3}\s*source\s*index", s):
            si_start = i
        elif si_start is not None and re.match(r"^##\s+", line) and i > si_start:
            si_end = i
            break

    if si_start is None:
        return 0  # no Source Index section

    # Build a fuzzy lookup of titles → url
    titles_lower = [t for (t, _, _) in sources_list]
    title_to_url = {t: url for (t, url, _) in sources_list}

    changed_count = 0
    i = si_start + 1
    while i < si_end:
        line = lines[i]
        if not is_table_row(line):
            i += 1
            continue
        # Found header row. Next line should be separator.
        if i + 1 >= si_end or not is_table_separator(lines[i + 1]):
            i += 1
            continue
        headers = split_cells(line)
        title_col = find_col(headers, "title", "source", "name")
        url_col = find_col(headers, "url", "link")
        if title_col == -1:
            # Can't linkify this table; skip past it
            i += 2
            while i < si_end and is_table_row(lines[i]):
                i += 1
            continue

        # Process data rows
        j = i + 2
        while j < si_end and is_table_row(lines[j]):
            cells = split_cells(lines[j])
            if title_col < len(cells):
                title = cells[title_col]
                if title and not is_already_link(title):
                    url = ""
                    # 1) URL in row?
                    if url_col != -1 and url_col < len(cells):
                        # Cell might already be a markdown link; extract URL
                        cell_url = cells[url_col].strip()
                        m = URL_PATTERN.search(cell_url)
                        if m:
                            url = m.group(0).rstrip(".,);")
                    # 2) Any URL in any cell?
                    if not url:
                        for c in cells:
                            m = URL_PATTERN.search(c)
                            if m:
                                url = m.group(0).rstrip(".,);")
                                break
                    # 3) Fallback: fuzzy-match against sources.json
                    if not url and titles_lower:
                        match = difflib.get_close_matches(
                            title.lower(), titles_lower, n=1, cutoff=0.55
                        )
                        if match:
                            url = title_to_url.get(match[0], "")
                    if url:
                        # Escape ] inside title for Markdown
                        safe = title.replace("]", "\\]")
                        cells[title_col] = f"[{safe}]({url})"
                        lines[j] = "| " + " | ".join(cells) + " |"
                        changed_count += 1
            j += 1
        i = j

    if changed_count:
        md_path.write_text("\n".join(lines), encoding="utf-8")
    return changed_count


def main():
    grand_total = 0
    for sector in SECTORS:
        sd = ROOT / sector
        rmd = sd / "research.md"
        if not rmd.exists():
            continue
        sources = load_sources_map(sd)
        n = linkify_md(rmd, sources)
        grand_total += n
        print(f"  {sector}: {n} titles linkified  (sources_loaded={len(sources)})")
    print(f"\nGrand total: {grand_total} rows linkified")


if __name__ == "__main__":
    main()
