#!/usr/bin/env python3
"""Emit the Slidev deck from outline.yaml. Deck is derived, never hand-edited."""
import html
import re
import sys
from pathlib import Path

import yaml

OUT = Path("jrush26-my-standards.md")
FOOTER = "@asm0dey | #JRush | #AIcoding"

HEADMATTER = f"""---
theme: default
colorSchema: dark
{{slide0}}
title: My Standards, Their Keyboard
info: Four AI processes, and then there was one — JRush 2026
author: Pasha Finkelshteyn
duration: 30min
transition: fade
drawings:
  persist: false
mdc: true
fonts:
  sans: Inter
  mono: JetBrains Mono
---
"""

# A chapter card is any slide whose whole overlay is "<n> — <name>". Deriving it
# beats a hard-coded slide list, which silently goes stale on every renumber.
CHAPTER_CARD_RE = re.compile(r"^\d+\s+—\s+\S")


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def notes(slide: dict) -> str:
    """Speaker notes: cues as bold stage directions, parentheticals italic."""
    out = []
    for item in slide.get("script", []):
        if item.get("cue"):
            out.append(f"**{item['cue']}**")
        elif item.get("parenthetical"):
            out.append(f"*{item['parenthetical']}*")
        elif item.get("line"):
            out.append(item["line"])
    if not out:
        return ""
    return "<!--\n" + "\n\n".join(out) + "\n-->\n"


def load_assets() -> dict:
    path = Path("deck-assets.yaml")
    return yaml.safe_load(path.read_text()) if path.exists() else {}


ASSETS = load_assets()


def snippet(slide: dict) -> str | None:
    """Copy the quoted range into snippets/ and emit a Slidev code block.

    The deck quotes real files from other repos; copying at build time keeps
    the deck reproducible when those repos move on.
    """
    spec = ASSETS.get(slide["n"])
    if not spec:
        return None
    if spec.get("img"):
        return (
            f"<div class='filepath'>{spec.get('label', spec['img'])}</div>\n\n"
            f"<img class='shot' src='/{spec['img']}' alt='{spec.get('label','')}'>\n"
        )
    src = Path(spec["src"])
    if not src.exists():
        print(f"  ! slide {slide['n']}: missing {src}", file=sys.stderr)
        return None
    text = src.read_text().splitlines()
    if spec.get("lines"):
        lo, _, hi = spec["lines"].partition("-")
        text = text[int(lo) - 1 : int(hi)]
    out = Path("snippets") / f"slide-{slide['n']:02d}.{spec.get('lang', 'txt')}"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(text) + "\n")
    focus = "{" + spec["focus"] + "}" if spec.get("focus") else ""
    dense = " dense" if len(text) > 14 else ""
    return (
        f"<div class='filepath{dense}'>{spec.get('label', src.name)}</div>\n\n"
        f"<div class='code{dense}'>\n\n"
        f"```{spec.get('lang', 'text')} {focus}\n"
        + "\n".join(text)
        + "\n```\n\n</div>\n"
    )


def placeholder_box(slide: dict) -> str:
    tags = ", ".join(slide.get("placeholders", []))
    return (
        '<div class="ph">\n'
        f'<div class="ph-tag">{tags or "ASSET"}</div>\n'
        f'<div class="ph-desc">{esc(slide.get("visual") or "")}</div>\n'
        "</div>\n"
    )


def overlay_lines(slide: dict) -> list[str]:
    text = slide.get("text_overlay")
    if not text or text == "none":
        return []
    return text.split("\n")


def render(slide: dict, chapter_title: str) -> str:
    n, fmt = slide["n"], slide["format"]
    lines = overlay_lines(slide)
    body = []

    if fmt == "TITLE":
        body.append("---\nlayout: cover\nclass: text-center\n---\n")
        body.append(f"# {lines[0]}\n")
        body.append(f"## {lines[1]}\n" if len(lines) > 1 else "")
        body.append(f"\n<div class='byline'>Pasha Finkelshteyn · {FOOTER}</div>\n")
    elif lines and CHAPTER_CARD_RE.match(lines[0]):
        num, _, name = lines[0].partition(" — ")
        body.append("---\nlayout: section\nclass: chapter\n---\n")
        body.append(f"<div class='numeral'>{num.strip()}</div>\n\n# {name.strip()}\n")
        # Remaining overlay lines name the tooling that attempt actually ran on.
        for tool in lines[1:]:
            body.append(f"<div class='toolref'>{esc(tool)}</div>\n")
    elif fmt == "EXCEPTION" or ASSETS.get(n):
        art = snippet(slide) or (placeholder_box(slide) if fmt == "EXCEPTION" else "")
        if lines:
            body.append("---\nlayout: two-cols\nclass: artifact\n---\n")
            head = esc(lines[0])
            rest = "".join(f"<div class='sub'>{esc(x)}</div>" for x in lines[1:])
            # Claim goes in the LEFT column: the eye reads the point, then the proof.
            body.append(f"<div class='claim'><div>{head}</div>{rest}</div>\n")
            body.append("::right::\n")
            body.append(art)
        else:
            body.append("---\nlayout: default\nclass: artifact\n---\n")
            body.append(art)
    else:  # FULL — typographic statement
        pats = {p["id"] for p in slide.get("applied_patterns", [])}
        if "delayed-self-introduction" in pats:
            cls = "bio"  # an aside, not a claim — deliberately quieter type
        else:
            cls = "statement" if len(" ".join(lines)) < 90 else "statement small"
        body.append(f"---\nlayout: center\nclass: {cls}\n---\n")
        for line in lines:
            body.append(f"<div>{esc(line)}</div>\n")
        if slide.get("visual"):
            body.append(f"\n<div class='vnote'>{esc(slide['visual'])}</div>\n")

    return "\n".join(x for x in body if x) + "\n" + notes(slide)


def render_builds(slide: dict) -> str:
    """Slide 5 — the five tiles, revealed in three click steps."""
    tiles = []
    for i in range(1, 6):
        mark = "crossed-off.red='2'" if i < 5 else "circle.orange='3'"
        tiles.append(f"<div class='tile' v-mark.{mark}>{i}</div>")
    return (
        "---\nlayout: center\nclass: tiles\n---\n\n"
        "<div class='row'>\n" + "\n".join(tiles) + "\n</div>\n\n"
        "<div v-click='1' class='cap'>Five processes on real work.</div>\n"
        "<div v-click='2' class='cap'>I dropped four.</div>\n"
        "<div v-click='3' class='cap'>One is still running.</div>\n\n"
        + notes(slide)
    )


def main() -> int:
    outline = yaml.safe_load(Path("outline.yaml").read_text())
    chapters = {c["id"]: c["title"] for c in outline["chapters"]}
    parts = []
    for slide in outline["slides"]:
        if slide["n"] == 0:
            # Slide 0 has no separator of its own: in Slidev the headmatter IS
            # the first slide's frontmatter. Emitting both made an empty cover.
            rendered = render(slide, chapters[slide["chapter"]])
            fm, _, body = rendered.partition("---\n")
            if rendered.startswith("---\n"):
                fm, _, body = rendered[4:].partition("---\n")
                parts.append(HEADMATTER.replace("{slide0}", fm.strip()))
            else:
                parts.append(HEADMATTER.replace("{slide0}", "layout: cover"))
                body = rendered
            parts.append(body)
            continue
        elif slide.get("builds"):
            parts.append(render_builds(slide))
        else:
            parts.append(render(slide, chapters[slide["chapter"]]))
    parts.append(Path("deck-style.md").read_text() if Path("deck-style.md").exists() else "")
    OUT.write_text("\n".join(p for p in parts if p.strip()))
    print(f"wrote {OUT} — {len(outline['slides'])} slides")
    return 0


if __name__ == "__main__":
    sys.exit(main())
