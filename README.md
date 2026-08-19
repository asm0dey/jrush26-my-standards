# My Standards, Their Keyboard

Talk for **JRush 2026** — 30 minutes, by [Pasha Finkelshteyn](https://github.com/asm0dey).

I ran five AI-assisted development processes on real work and kept one. The deck
shows all five with their actual artifacts: what each produced, and the specific
way four of them fell over.

## The five

| # | process | repo it ran on |
|---|---|---|
| 1 | no process at all | `diskinventory` |
| 2 | a guidelines file — [Junie](https://jetbrains.com/junie) | `fb2ebup` |
| 3 | full spec rigor — [Intent Integrity Kit](https://github.com/intent-integrity-chain/kit) | `femtocli` |
| 4 | one enormous gate — [ThinkRail](https://thinkrail.ai) + [OpenSpec](https://github.com/Fission-AI/OpenSpec) | `spring-git-mcp` |
| 5 | what I run today — [Claude Code](https://claude.com/claude-code), [superpowers](https://github.com/obra/superpowers), [mattpocock/skills](https://github.com/mattpocock/skills), [beans](https://github.com/hmans/beans) | [`calit`](https://github.com/asm0dey/calit) |

## Building the deck

The deck is [Slidev](https://sli.dev). `outline.yaml` is the source of truth;
`build-slidev.py` renders it to `jrush26-my-standards.md`, copying every quoted
file range into `snippets/` so the deck keeps working when the source repos move on.

```bash
bun install          # or npm install
python3 build-slidev.py
npx slidev jrush26-my-standards.md
```

`deck-assets.yaml` maps slide numbers to the real files they quote. Those paths are
local to my machine — regenerating the snippets needs the five repos checked out.
The committed `snippets/` are what the deck actually renders.

## Layout

| file | what it is |
|---|---|
| `outline.yaml` | every slide: title, claim, speaker notes, cut tier |
| `deck-assets.yaml` | slide number to quoted file and line range |
| `assets-src/` | hand-written excerpts and the contact-sheet generator |
| `timing.md` | per-slide timing, chapter checkpoints, cut ladder |
| `narrative.md`, `script.md` | the argument in prose |
