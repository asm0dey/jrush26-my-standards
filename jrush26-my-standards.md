---
theme: default
colorSchema: dark
layout: default
class: artifact
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


<div class='filepath'>github.com/asm0dey/calit — pull request #122, merged</div>

<img class='shot' src='/pr-122.png' alt='github.com/asm0dey/calit — pull request #122, merged'>

<!--
**SLIDE 0 UP**

This is a pull request I merged. AI wrote it, I read the diff, it did what I asked, I approved it.

AUTHOR-01 — one sentence on what the PR actually did, so the room has context.

Nothing broke. There is no incident story at the end of this.
-->

---
class: artifact
---

<div class='claim full'><div>I would have rejected this</div></div>

<div class='filepath'>the same pull request — the review I would have left</div>

<img class='shot' src='/pr-122-annotated.png' alt='the same pull request, annotated with the review comments I would have written'>

<!--
**SLIDE 1 UP — same screenshot, annotated**

A week later I read it properly. These are the comments I would have left if this had come from anyone on my team.

Two thousand nine hundred lines. Thirty-five files. One comment on the whole thing, and it was mine.

And then this. Three assignments, next to each other, in the same method. The locale is validated. The time format is validated. The timezone is taken straight off the form.

That is not a bug. The dropdown can only submit a real zone, so nothing was broken the day I merged it. It is three lines that disagree with each other about whether input is trustworthy — and that is a choice, not a defect.

*(beat — let them read the annotation)*

Six days later it was a bug: a crafted POST parks a junk zone, and eleven call sites throw a DateTimeException. One of them is the public booking page.

I approved code I would have sent back. So whose fault is that? Not the model's, and that is the uncomfortable part.
-->

---
layout: cover
class: text-center
---

# My Standards, Their Keyboard

## Four AI processes, and then there was one


<div class='byline'>Pasha Finkelshteyn · @asm0dey | #JRush | #AIcoding</div>

<!--
**SLIDE 2 UP**

That is the talk. Five processes, four of them dropped, and the one thing all four got wrong.
-->

---
layout: center
class: bio
---

<div class='who'>Pasha Finkelshteyn</div>

<div class='ctx'>@asm0dey · Developer Advocate at BellSoft · ten-plus years in the JVM</div>

<div class='now'>
<div>These days: production-like open source.</div>
<div class='repo'><a href="https://github.com/asm0dey/calit">github.com/asm0dey/calit</a></div>
<div class='punch'>No particular customer. Only users.</div>
</div>


<div class='vnote'>Name, handle, one line of context. Small type, no logo wall, no career timeline.</div>

<!--
**SLIDE 3 UP**

Quickly, so you know whose taste you are about to hear about: ten-plus years in the JVM ecosystem, mostly Java and Kotlin, developer advocate at BellSoft.

That decade is where my preferences come from, and it is the only reason any of this bothers me.

These days I write production-like code again. calit is open source — a scheduling app with real users, not a demo. What it does not have is a particular customer. Nobody signs off on it but me, so the only standards in that repo are mine — which is exactly what makes it a fair test.
-->

---
layout: center
class: statement
---

<div>The model has no preferences.</div>

<div>Mine took ten years.</div>


<div class='vnote'>Typographic statement slide. One line, large, centered.</div>

<!--
**SLIDE 4 UP**

Ten-plus years in the JVM ecosystem gave me strong opinions about how code should look and which tools I reach for.

The model has none of that. Ask it the same question twice and you can get two different styles back, and both are fine by it.
-->

---
layout: center
class: statement
---

<div>The process is the only channel my standards travel through.</div>


<div class='vnote'>Single diagram: me on one side, keyboard/repo on the other, one labelled channel between them marked PROCESS. Everything else greyed.</div>

<!--
**SLIDE 5 UP**

It is their keyboard now. So how does anything of mine get in? Through the process I put around it, and nowhere else.

So every time I call the process overhead, I am calling my own standards overhead.
-->

---
layout: center
class: tiles
---

<div class='row'>
<div class='tile' v-mark.crossed-off.red='2'>1</div>
<div class='tile' v-mark.crossed-off.red='2'>2</div>
<div class='tile' v-mark.crossed-off.red='2'>3</div>
<div class='tile' v-mark.crossed-off.red='2'>4</div>
<div class='tile' v-mark.circle.orange='3'>5</div>
</div>

<div v-click='1' class='cap'>Five processes on real work.</div>
<div v-click='2' class='cap'>I dropped four.</div>
<div v-click='3' class='cap'>One is still running.</div>

<!--
**SLIDE 6 UP**

Five processes on real work.

**BUILD 01**

I dropped four.

**BUILD 02**

Every one I dropped failed the same way: it made a decision that was mine to make. Keep that in your head, we come back to it at the end.
-->

---
layout: section
class: chapter
---

<div class='numeral'>1</div>

# Vibe coding

<div v-click class='gag'>“Build it. Make no mistakes.”</div>

<!--
**SLIDE 7 UP**

The assistant was Junie. Same assistant as attempt two — the only thing that changes between them is the process, and here there is none: no spec, no plan, no guidelines file anywhere in the tree.

Attempt one. Describe what I want, let it write, look at what came back.

[click] The whole process fits on one line. You have all seen this prompt.

*(let it land)*

And it is a fine prompt, except it never says which mistakes. Those are exactly the decisions that are mine — and the prompt does not mention a single one.
-->

---
layout: two-cols
class: artifact
---

<div class='claim'><div>Fastest of the five</div></div>

::right::

<div class='filepath'>diskinventory — the first commit</div>

<div class='code'>

```text 
7b67e8d 2026-08-10  Disk Inventory: drill-down pie chart over a headless disk-usage model

 16 files changed, 1769 insertions(+)

process artifacts in repo at that commit:
  matching files: 0
```

</div>

<!--
**SLIDE 8 UP**

One commit: a working disk-usage tool with a drill-down pie chart, 1769 lines, sixteen files. One evening.

It was the fastest of all five. I want to be honest about that, because everything after this is slower and has to earn the difference.
-->

---
layout: center
class: statement
---

<div>A diff records the what.</div>

<div>My standards live in the why.</div>


<div class='vnote'>An empty folder labelled 'decisions'. Beside it, a fat diff labelled 'the only record'.</div>

<!--
**SLIDE 9 UP**

There was no artifact. Nothing recorded a single decision, so there was nothing to review against.

A diff tells you what changed, and never why that shape instead of another one. And why is exactly where all my standards live.

So, is vibe coding a moral failing? No. It is fast, and giving that speed up costs something real. It set the bar the other four had to clear.
-->

---
layout: section
class: chapter
---

<div class='numeral'>2</div>

# Guidelines first

<div class='toolref'>JetBrains Junie · jetbrains.com/junie</div>

<!--
**SLIDE 10 UP**

Attempt two. Write the guidelines up front, then hand it tasks against them.
-->

---
layout: default
class: artifact stack
---

<div class='claim'><div>One file. Read at the start of every session.</div><div class='sub'>JetBrains Junie · jetbrains.com/junie</div></div>

<div class='filepath'>attempt two — the tool and its one file</div>

<div class='spec'>
<div class='k'>what it is</div><div class='v'>JetBrains' coding agent, inside the IDE</div><div class='u'></div>
<div class='k'>the artifact</div><div class='v'>.junie/guidelines.md — numbered rules, plain prose</div><div class='u'></div>
<div class='k'>how it runs</div><div class='v'>reads the file at the start of every session</div><div class='u'></div>
<div class='k'>what I write</div><div class='v'>the rules. Nothing else is asked of me.</div><div class='u'></div>
<div class='k'>link</div><div class='v'><a href='https://jetbrains.com/junie'>jetbrains.com/junie</a></div><div class='u'></div>
</div>

<!--
**SLIDE 11 UP**

Attempt two is Junie, JetBrains' agent in the IDE. The whole process is one file.

I write the rules; it reads them before it does anything. That is the entire contract.
-->

---
layout: default
class: artifact
---

<div class='filepath'>fb2ebup/.junie/guidelines.md</div>

<div class='code'>

```md {5}
1. Whenever there is a file "plan.md" always follow the plan.
2. When a point of a plan is completed, mark it as finished in plan.md
3. When you need to work with a library/framework use context7 to check if your usage is correct
4. When you need to add a dependency to project - check the latest version at context7
5. Do NOT add `quarkus-resteasy-reactive-multipart`; in Quarkus 3, multipart APIs (`@RestForm`, `FileUpload`) are available via `quarkus-rest` already.
6. To test how fb2c works, you can execute "/home/finkel/Downloads/fb2c-linux-amd64/fb2c" binary
```

</div>

<!--
**SLIDE 12 UP**

This is the artifact. AUTHOR-04 — read out one rule that is unmistakably mine and would never appear in a default template.

A written guideline is a decision I made once, in my words, that the model reads at the start of every session.
-->

---
layout: two-cols
class: artifact
---

<div class='claim'><div>One rule. Two files. Hours apart.</div><div class='sub'>Rule 5 said not to add the multipart extension — Quarkus 3 already ships those APIs.</div></div>

::right::

<div class='filepath'>fb2ebup — guideline rule 5, holding in two different files</div>

<div class='code'>

```kotlin 
// build.gradle.kts:29 — it tried, then backed off
//    implementation("io.quarkus:quarkus-resteasy-reactive-multipart")

// api/ConversionResource.kt:16 — different file, later in the same build
import org.jboss.resteasy.reactive.RestForm
import org.jboss.resteasy.reactive.multipart.FileUpload

@POST
fun convert(@RestForm(FileUpload.ALL) uploads: List<FileUpload>): UploadResponse {
```

</div>

<!--
**SLIDE 13 UP**

Rule five of that file says: do not add the multipart extension, Quarkus 3 already has those APIs. Top excerpt is the build file, where it tried anyway and then commented the line out.

Bottom excerpt is a different file, written later in the same build, using the API the rule points at instead.

That is the whole win, and it is a small one. Before this, my preferences lasted about three files before the assistant drifted back to its own defaults. Here one of them was still in force at the other end of the codebase, because it was written down instead of remembered.

If the talk ended here, it would be a happy talk. It runs another twenty minutes.
-->

---
layout: two-cols
class: artifact
---

<div class='claim'><div>Every guideline satisfied.</div><div class='sub'>Nothing in the file said anything about package names.</div></div>

::right::

<div class='filepath dense'>fb2ebup/src/main/kotlin/com/github/com/ExampleResource.kt</div>

<div class='code dense'>

```kotlin {1}
package com.github.com

import jakarta.ws.rs.GET
import jakarta.ws.rs.Path
import jakarta.ws.rs.Produces
import jakarta.ws.rs.core.MediaType

/**
 * Baseline health endpoint (Section 1: clean baseline)
 */
@Path("/health")
class ExampleResource {

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    fun ping() = "OK"
```

</div>

<!--
**SLIDE 14 UP**

It solved the task. Every rule in the file was respected. And I still did not want this code in my repository.

Read the package name. Every file in that project is under com.github.com — the scaffold's placeholder, never renamed, and no guideline of mine said anything about package names.

Guidelines write down rules. But the code I would have written comes out of a sequence of decisions, and most of those never take the shape of a rule.
-->

---
layout: center
class: statement
---

<div>No rationale, so nothing to correct.</div>

<div>Only overrule, session after session.</div>


<div class='vnote'>A choice fork rendered twice: one path taken, the other faded. No annotation anywhere on either path.</div>

<!--
**SLIDE 15 UP**

And it never explained a single choice it made.

Without a rationale, how do I tell a deliberate call from a coin flip? I cannot. So I never correct anything, I just overrule it, session after session.

So, on to something that writes its reasoning down.
-->

---
layout: section
class: chapter
---

<div class='numeral'>3</div>

# Specify first, then implement

<div class='toolref'>Intent Integrity Kit · github.com/intent-integrity-chain/kit</div>

<!--
**SLIDE 16 UP**

Attempt three. Nothing gets implemented until it has been specified.
-->

---
layout: default
class: artifact stack
---

<div class='claim'><div>Ten phases. The intent is locked before code.</div><div class='sub'>Intent Integrity Kit · github.com/intent-integrity-chain/kit</div></div>

<div class='filepath'>attempt three — the kit, and what each phase leaves behind</div>

<div class='spec'>
<div class='k'>what it is</div><div class='v'>Intent Integrity Kit — intent locked before code</div><div class='u'></div>
<div class='k'>the artifacts</div><div class='v'>constitution, spec.md, plan.md, tasks.md, contracts/, checklists/, .feature files</div><div class='u'></div>
<div class='k'>how it runs</div><div class='v'>constitution&nbsp;→ specify&nbsp;→ clarify&nbsp;→ plan&nbsp;→ checklist&nbsp;→ testify&nbsp;→ tasks&nbsp;→ analyze&nbsp;→ implement</div><div class='u'></div>
<div class='k'>what it locks</div><div class='v'>the .feature files, hashed before implementation — the agent may rewrite code, never what passing means</div><div class='u'></div>
<div class='k'>installed as</div><div class='v'>tessl-labs/intent-integrity-kit 2.1.0</div><div class='u'></div>
<div class='k'>link</div><div class='v'><a href='https://github.com/intent-integrity-chain/kit'>github.com/intent-integrity-chain/kit</a></div><div class='u'></div>
</div>

<!--
**SLIDE 17 UP**

This one is the Intent Integrity Kit. Ten phases, and the interesting bit is what it locks: the feature files are hashed before implementation starts.

The agent can rewrite the code as much as it likes. It cannot rewrite what passing means.
-->

---
layout: two-cols
class: artifact
---

<div class='claim'><div>It was right about everything.</div><div class='sub'>A gate table, checked before a line of code was written.</div></div>

::right::

<div class='filepath'>femtocli/specs/001-codegen-parser/plan.md — 1 of 22 files</div>

<div class='code'>

```md 
## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Minimalism | PASS | No new runtime dependencies; JavaPoet and AutoService are compile-time only |
| II. API Stability | PASS | Existing annotations unchanged; XParser classes are additive |
| III. Test Coverage | TBD | Tests must be generated for each user story |
| IV. Documentation Completeness | TBD | Quickstart.md created; API docs needed during implementation |
| V. Documentation Reference | PASS | JavaPoet docs not available via tessl, using project knowledge |
| VI. Java Compatibility | PASS | Target Java 11+ to match existing; JPMS support planned |
```

</div>

<!--
**SLIDE 18 UP**

To be fair to this one: it is right about what good practice looks like. Intent stated before implementation, acceptance criteria written down, nothing hand-waved.

It got the architecture I wanted, and then it kept asking. Every detail came back to me as a user story I had to accept or reject before it would write anything. Look at row three: tests per user story, because by that point the stories were mine.

Attempt two decided all of that on its own, and never told me it had.
-->

---
layout: two-cols
class: artifact
---

<div class='claim'><div>It audited itself and scored 99.5 out of 100.</div><div class='sub'>Every principle: PASS.</div></div>

::right::

<div class='filepath dense'>femtocli/specs/001-codegen-parser/analysis.md</div>

<div class='code dense'>

```md 
# Analysis Report: Code-Generated Command Line Parser

**Feature**: 001-codegen-parser
**Date**: 2026-02-23
**Health Score**: 99.5/100

## Specification Analysis Report

| ID | Category | Severity | Location(s) | Summary | Recommendation |
|----|----------|-------------|-------------|---------|----------------|
| ALIGNED | Constitution | PASS | spec.md, plan.md, tasks.md | All constitutional principles satisfied |
| ALIGNED | Coverage | PASS | spec.md, plan.md, tasks.md | All user stories have acceptance criteria |
| ALIGNED | Coverage | PASS | spec.md, plan.md, tasks.md | Success criteria are measurable |
| ALIGNED | Coverage | PASS | spec.md, tasks.md | All FRs have corresponding tasks |
| ALIGNED | Coverage | PASS | spec.md, plan.md | All test scenarios have task references |

```

</div>

<!--
**SLIDE 19 UP**

And it checked its own work. Health score ninety-nine point five out of a hundred, every constitutional principle passing, every requirement traced to a task.

I want to be fair to it: none of that is wrong. It is a genuinely good report about a genuinely thorough process.
-->

---
layout: two-cols
class: artifact
---

<div class='claim'><div>Twenty-two files. Two thousand seven hundred lines.</div><div class='sub'>Spec, plan, tasks, contracts, checklists, feature files.</div></div>

::right::

<div class='filepath dense'>femtocli/specs/001-codegen-parser — every file the process demanded</div>

<div class='code dense'>

```text 
analysis.md                                               141
checklists/requirements-quality.md                        121
checklists/requirements.md                                 53
context.json                                                8
contracts/option-parsing.md                               209
contracts/positional-parameters.md                         86
contracts/type-conversion.md                              206
data-model.md                                             176
plan.md                                                   326
quickstart.md                                             314
research.md                                               137
spec.md                                                   230
tasks.md                                                  248
tests/features/agent-args-mode.feature                     34
tests/features/basic-command-with-options.feature          70
tests/features/custom-spec-implementation.feature          46
tests/features/did-you-mean-suggestions.feature            40
tests/features/help-generation.feature                     52
tests/features/java-modules-support.feature                40
tests/features/positional-parameters.feature               64
tests/features/subcommands-and-mixins.feature              46
tests/features/type-conversion-and-validation.feature      82
-------------------------------------------------------------
22 files, before a line of code                          2729
```

</div>

<!--
**SLIDE 20 UP**

That is the directory. Twenty-two files, twenty-seven hundred lines, and not one of those lines is code.
-->

---
layout: two-cols
class: artifact
---

<div class='claim'><div>I read all of this before writing any code.</div><div class='sub'>Once.</div></div>

::right::

<div class='filepath'>femtocli/specs/001-codegen-parser — all 22 documents</div>

<img class='shot' src='/spec-kit-sheet.png' alt='femtocli/specs/001-codegen-parser — all 22 documents'>

<!--
**SLIDE 21 UP**

Here it is at a glance. You are not meant to read it — that is the point. I read it once, properly, for the first feature.

*(beat)*

Then never again.
-->

---
layout: center
class: statement
---

<div>A process you abandon remembers nothing.</div>


<div class='vnote'>A usage line that starts high and decays to zero over a few weeks. No axis drama, just the shape.</div>

<!--
**SLIDE 22 UP**

So what went wrong? Nothing, on paper. It was just heavy, and after a few weeks I stopped opening it.

*(beat)*

A process you abandon remembers nothing. Whatever you still run on a Tuesday afternoon is its real ceiling.
-->

---
layout: center
class: statement
---

<div>The cost lands on the one part of the system that can quit.</div>


<div class='vnote'>A scale: on one side the spec's guarantees, on the other the attention it costs. The attention side is labelled with one word — me.</div>

<!--
**SLIDE 23 UP**

Rigor has a price, and it is paid in my attention. I am also the one component in this system that can quietly opt out, and that is what I did.
-->

---
layout: section
class: chapter
---

<div class='numeral'>4</div>

# Plan everything, then approve it

<div class='toolref'>OpenSpec · github.com/Fission-AI/OpenSpec</div>

<div class='toolref'>Claude via OpenRouter · openrouter.ai</div>

<!--
**SLIDE 24 UP**

Attempt four. On paper, the best-designed of the five.
-->

---
layout: default
class: artifact stack
---

<div class='claim'><div>OpenSpec shapes it. Claude runs it.</div><div class='sub'>One proposal to approve.</div></div>

<div class='filepath'>attempt four — the two tools</div>

<div class='spec'>
<div class='k'>OpenSpec</div><div class='v'>the spec format — one change proposal plus delta specs, approved as a single unit.</div><div class='u'><a href='https://github.com/Fission-AI/OpenSpec'>github.com/Fission-AI/OpenSpec</a></div>
<div class='k'>Claude</div><div class='v'>the agent that drives it, through OpenRouter.</div><div class='u'><a href='https://openrouter.ai'>openrouter.ai</a></div>
</div>

<!--
**SLIDE 25 UP**

OpenSpec is a spec format: one change proposal plus the deltas it makes to the specs, approved as a single unit. Hold onto that last part.

Claude drives it, through OpenRouter.
-->

---
layout: two-cols
class: artifact
---

<div class='claim'><div>Credit where it is due</div><div class='sub'>A worktree per change. And an archive I still miss.</div></div>

::right::

<div class='filepath'>spring-git-mcp/openspec — after ten changes</div>

<div class='code'>

```text {1-6|8-18}
specs/                    what is true now
  git-bisect/
  git-interactive-rebase/
  git-log/
  git-reflog/
  tool-service-marker-interface/

changes/archive/          how it got that way
  2026-03-24-add-git-bisect-tool/
  2026-03-24-add-reflog-support/
  2026-03-24-tool-services-marker-interface/
  2026-03-25-extend-reflog-reset-limit/
  2026-03-25-git-interactive-rebase-tool/
  2026-03-25-git-log-tool/
  2026-03-27-git-log-custom-fields/
  2026-04-17-bisect-actionable-response/
  2026-04-17-bisect-labels-based-state/
  2026-04-17-fix-git-bisect-review-findings/
```

</div>

<!--
**SLIDE 26 UP**

It got real things right. OpenSpec gave every change its own git worktree, so parallel work stopped colliding. I did not have to ask for that.

And the archive. When a change ships, its spec deltas merge into the living specs. So specs always say what is true now.

[click] And the proposal, design and tasks move into a dated folder. The archive says how it got that way.

What I run today keeps the decisions — decision records in the repo, precedent across all of them. What it does not have is that fold. calit has nineteen specs and sixty-four plans in two flat folders, and nothing merges them into what is true now. That is the one thing I still miss.

I dropped it anyway, over one structural choice.
-->

---
layout: two-cols
class: artifact
---

<div class='claim'><div>Read all of this. Approve. Go.</div></div>

::right::

<div class='filepath'>openspec/changes/git-log-custom-fields/proposal.md — 1 of 4</div>

<div class='code'>

```md 
## Why

Currently, the `git_log` tool returns a fixed set of fields for every commit. This can lead to excessive data transfer when only specific information (e.g., just hashes or just messages) is needed. Allowing users to specify fields improves efficiency and flexibility for AI/LLM consumption.

## What Changes

- Add an optional `fields` parameter to the `git_log` tool.
- The `fields` parameter will accept an array of strings representing the desired commit fields.
- Minimal default fields will be returned if the parameter is omitted (to maintain backward compatibility while allowing future optimization).
- The tool will only populate and return the requested fields in the JSON output.
- Optional filters and pagination options are grouped in a separate `filters` object.

```

</div>

<!--
**SLIDE 27 UP**

There is essentially one step where I read an enormous plan with all its specs, and approve the lot.

Four documents in one change folder: why it is happening, the technical decisions, the spec delta, and the task list. One read, one approval, and no second gate anywhere after it.

Every decision in there was mine to make, and every one was correctly surfaced. They were just handed to me in a single lump.
-->

---
layout: two-cols
class: artifact
---

<div class='claim'><div>Four documents. One yes.</div><div class='sub'>1534 words, 19 scenarios, no second gate.</div></div>

::right::

<div class='filepath'>openspec/changes/git-log-custom-fields — the whole approval</div>

<div class='code'>

```text 
openspec/changes/git-log-custom-fields/
  proposal.md             28 lines   why, and what changes
  design.md               43 lines   the technical decisions
  tasks.md                25 lines   14 checkboxes, in 4 groups
  specs/git-log/spec.md   80 lines   1 requirement, 19 scenarios
                         ---------
                         176 lines, 1534 words

one approval covers all four. There is no second gate.
```

</div>

<!--
**SLIDE 28 UP**

This is what I was approving in one go. Proposal, design, tasks, and the spec delta: a hundred and seventy-six lines, fifteen hundred words, fourteen checkboxes, nineteen scenarios.

It is not enormous. That is the uncomfortable part — it is a perfectly reasonable amount of reading, and I still skimmed it, because it arrived as one block with one decision attached: yes or no.
-->

---
layout: center
class: statement
---

<div>Nobody reviews a lump this size.</div>

<div>They skim it.</div>


<div class='vnote'>The annotated PR from slide 2 shrunk into the corner beside the enormous plan. Same reader, same skim.</div>

<!--
**SLIDE 29 UP**

And what does anyone do with a lump that size? Skim it.

*(point back at the opening PR)*

Which is the same skim as slide one, moved one step earlier and much better documented.

Attempt three drowned me in volume. This one got the volume right and the timing wrong: every decision arrives at one moment, instead of at the moments when I can actually make them.
-->

---
layout: section
class: chapter
---

<div class='numeral'>5</div>

# What I run today

<div class='toolref'>Claude Code · superpowers · beans · ponytail</div>

<div class='toolref'>grill-with-docs + domain-modeling · github.com/mattpocock/skills</div>

<div class='toolref'>precedent · github.com/asm0dey/precedent</div>

<!--
**SLIDE 30 UP**

This is the one I still run.
-->

---
layout: default
class: artifact stack
---

<div class='claim'><div>Six tools. I write none of it.</div><div class='sub'>All of it public: github.com/asm0dey/calit</div></div>

<div class='filepath'>github.com/asm0dey/calit — in Claude Code, I talk to</div>

<div class='spec'>
<div class='k'>superpowers</div><div class='v'>plans the work, then sizes a subagent to each task</div><div class='u'><a href='https://github.com/obra/superpowers'>github.com/obra/superpowers</a></div>
<div class='k'>grill-with-docs</div><div class='v'>questions me until we agree, then writes the ADR</div><div class='u'><a href='https://github.com/mattpocock/skills'>github.com/mattpocock/skills</a></div>
<div class='k'>domain-modeling</div><div class='v'>argues with my words, then records them</div><div class='u'><a href='https://github.com/mattpocock/skills'>github.com/mattpocock/skills</a></div>
<div class='k'>ponytail</div><div class='v'>keeps what gets written small</div><div class='u'><a href='https://github.com/DietrichGebert/ponytail'>github.com/DietrichGebert/ponytail</a></div>
<div class='k'>beans</div><div class='v'>keeps the work list out of my head</div><div class='u'><a href='https://github.com/hmans/beans'>github.com/hmans/beans</a></div>
<div class='k'>precedent</div><div class='v'>a local graph of what I decided, across every repo</div><div class='u'><a href='https://github.com/asm0dey/precedent'>github.com/asm0dey/precedent</a></div>
</div>

<!--
**SLIDE 31 UP**

Everything from here is one real repository. calit — a self-hosted Calendly alternative on Quarkus and Java 25, multi-user, Google Calendar sync. Public, so you can go read all of this after.

I do not write any of this. I talk to it. brainstorming pulls the idea apart before there is a plan, writing-plans turns what we agreed into one, and grill-with-docs keeps asking until we mean the same thing.

domain-modeling argues with my vocabulary and records what we settle on. ponytail keeps what gets written as small as it can be. beans keeps the work list out of my head. And precedent — the one I did build, with this same process — remembers what I decided, across every repo.

Then I read the spec, and I read the code. Usually not the plan. The plan is written for the agent — longer, and full of detail it needs and I do not. The spec is the part addressed to me.

The names will date. The shape will not: every one of these makes me decide something before it writes anything down.

And the repository is open. If you want to see what sixteen weeks of this actually looks like, or you have opinions about scheduling software, issues and pull requests are welcome.
-->

---
layout: default
class: artifact stack
---

<div class='claim'><div class='eyebrow'>superpowers · brainstorming + writing-plans</div><div>The spec is written for me. The plan is written for the agent.</div><div class='sub'>Both name the work item they came from.</div></div>

<div class='filepath'>calit/docs/superpowers — one change, two documents</div>

<div class='spec'>
<div class='g'>specs/2026-08-17-per-meeting-type-write-target-design.md</div>
<div class='k'>written for</div><div class='v'>me</div><div class='u'></div>
<div class='k'>says</div><div class='v'>today an owner has exactly one write calendar, and why that is wrong</div><div class='u'></div>
<div class='g'>plans/2026-08-17-per-meeting-type-write-target.md</div>
<div class='k'>written for</div><div class='v'>the agent</div><div class='u'></div>
<div class='k'>says</div><div class='v'>let each Host give one meeting type its own write override, and how</div><div class='u'></div>
</div>

<!--
**SLIDE 32 UP**

This is one change, as two documents, and they have different readers. The spec states the problem in domain terms — that one is addressed to me, and it is the one I approve.

The plan is longer and more detailed, because it is written for the agent. Most of the time I do not read it, and that is the point: the layer that needs my judgement is separated from the layer that does not.

That detail pays twice. superpowers hands every task in the plan to its own subagent, and picks the model per task: Haiku when the plan already spells out the code, Sonnet for integration and debugging, Opus for design and the final review of the whole branch. The more precise the plan, the cheaper the model that can carry it.

Both of them carry the work item id, so a year from now the why is one grep away.
-->

---
layout: two-cols
class: artifact
---

<div class='claim'><div class='eyebrow'>superpowers</div><div>One decision, at the moment it comes up</div></div>

::right::

<div class='filepath'>three real calit questions, verbatim — and which step asked</div>

<div class='code'>

```text
# writing-plans · while planning the Google-disconnect fix
When calit can't read your Google calendar (disconnected/token revoked),
what should the public booking page show?
  → Fail-closed (recommended)   ·   Notify-only

# finishing-a-development-branch · right after the merge
How should the booking window be determined?
  → Use type.horizonDays   ·   Bump the constant   ·   Leave as-is

# finishing-a-development-branch · when the PR's quality gate failed
Sonar's duplication + too-many-params failures are the flat-param design
you approved. How do you want to resolve them?
  → Suppress, keep flat params   ·   Adopt a shared view record
```

</div>

<!--
**SLIDE 33 UP**

It asks me one decision at a time, at the moment that decision comes up. Small enough that I actually read it.

And it is not one gate. The first question came from superpowers while it was still writing the plan. The other two came at the very end, while it was finishing the branch: one right after the merge, one when the pull request's quality gate went red. Planning asks, and finishing asks again.

That is the fix for attempt four: the same decisions, spread out.
-->

---
layout: default
class: artifact
---

<div class='eyebrow'>grill-with-docs</div>

<div class='filepath'>calit/docs/adr/0002-buffers-are-constraints-not-settings.md</div>

<div class='code'>

```md 
# Buffers are constraints, so the strictest one governs

A buffer expresses a minimum a host requires, not a value someone configures for a meeting. A
meeting cannot be created until every participating host's constraints are satisfied, so where
several buffers apply to the same booking — a co-host's own override and (once meeting types
offer several lengths) the chosen duration's override — the effective buffer is the **maximum**
of them, never the most specific one.

```

</div>

<!--
**SLIDE 34 UP**

Here is one of eleven decision records in that repo. Read the title: buffers are constraints, so the strictest one governs.

*(let them read the title)*

That is a domain judgement, in my words, with the consequences I accepted written underneath it. No linter has an opinion about that sentence.

This is what attempt two was missing: the reasoning behind a decision, kept where the next session will read it.
-->

---
layout: two-cols
class: artifact
---

<div class='claim'><div class='eyebrow'>grill-with-docs + domain-modeling</div><div>Owner. Not user, not admin, not account.</div></div>

::right::

<div class='filepath dense'>calit/CONTEXT.md</div>

<div class='code dense'>

```md 

**Owner**:
The user whose time is being booked and who configures the meeting types, availability and
settings. Every tenant row belongs to exactly one.
_Avoid_: user (a login), admin (site-wide privilege), account (a connected Google account)

**Invitee**:
The person who books an Owner's time. Has no login and no calit row of their own beyond the
booking.
_Avoid_: guest (an extra attendee added to a booking), booker, attendee, customer

**Host**:
An Owner who participates in a meeting type and whose calendar a booking must fit — the Creator
or an accepted Co-host. The unit availability and buffers are resolved per.
_Avoid_: participant, organizer (that is the one host whose Google account the event is created on)
```

</div>

<!--
**SLIDE 35 UP**

And this one I like most, because it is pure preference. The glossary says what a thing is called, and then lists the words I have decided we never use for it.

Could anyone derive that from the code? No. It is a taste decision, it is mine, and now it survives every session without me repeating myself.

So when I read a diff now, the why is already sitting next to it: in a decision record, in a task file, or in the glossary.
-->

---
layout: default
class: artifact stack
---

<div class='claim'><div class='eyebrow'>precedent</div><div>It remembers what I decided.</div><div class='sub'>Including where I decided otherwise.</div></div>

<div class='spec precedent-spec'>
<div class='k'>what it is</div><div class='v'>a skill with a local graph database of my decisions — technical, business, process — each with its why and what I rejected</div><div class='u'><a href='https://github.com/asm0dey/precedent'>github.com/asm0dey/precedent</a></div>
<div class='k'>what it does</div><div class='v'>query before choosing · override per project · regret, and it stops counting</div><div class='u'></div>
</div>

<div class='filepath'>precedent check --topic encryption — excerpt, from the calit session</div>

<div class='code'>

```text
PRINCIPLE     Encrypt secrets and PII at rest with Google Tink. Never hand-roll an AES-GCM helper.
              calit's EncryptedStringConverter predates this and is a known, regretted divergence.

calit         stays on EncryptedStringConverter despite the Tink principle
   rejected   migrate calit to Tink now · run Tink and the converter side by side
   why        A second at-rest crypto stack in the same app is worse than the wrong single one:
              two key env vars, two rotation stories, and a reader that must guess which scheme
              a row uses. Recorded so the graph stops proposing Tink for calit specifically
              while still proposing it everywhere else.

exchange-bot  App-level encryption with Tink, identifiers as keyed hashes
```

</div>

<!--
**SLIDE 36 UP**

Decision records and a glossary live in one repo. My preferences do not. So the last tool is one I built — with this same process — and it keeps what I decided across every project.

It is a skill with a small local graph database behind it. Technical decisions, business ones, process ones — each with the why and the options I rejected. Before a choice, the agent queries it. When a project needs to break the rule, I record an override for that project only. And when a choice turns out wrong, I regret it, and it stops counting as precedent everywhere.

Here is the rule: secrets at rest go through Tink. And here is calit, breaking it on purpose. Migrating means re-encrypting every token in a live deployment, and two crypto stacks in one app is worse than the wrong single one.

*(let them read the "why")*

It did not decide that. It asked, I answered, and it wrote down my answer — including the exception. Next project, it proposes Tink again. In calit, it stops nagging.

My decision, and it remembers it. That is the whole test.
-->

---
layout: two-cols
class: artifact
---

<div class='claim'><div>More writing than attempt three.</div><div class='sub'>I never stopped opening it.</div></div>

::right::

<div class='filepath'>calit — every process artifact, sixteen weeks in</div>

<div class='code'>

```text 
sixteen weeks, one repo, still running

830   commits
 64   plans             docs/superpowers/plans/
 19   specs             docs/superpowers/specs/
138   work items        .beans/     107 done, 28 open, 3 scrapped
 11   decision records  docs/adr/
  1   glossary          CONTEXT.md
```

</div>

<!--
**SLIDE 37 UP**

Look at the counts. Sixty-four plans, nineteen specs, a hundred and thirty-eight work items. That is far more prose than the twenty-two files that made me quit attempt three.

The difference is not volume. It is that each of these arrived when I needed it, and none of them asked me to read the others first.
-->

---
layout: two-cols
class: artifact
---

<div class='claim'><div class='eyebrow'>beans</div><div>The PR from slide one, backwards.</div><div class='sub'>It is why the stack looks like this.</div></div>

::right::

<div class='filepath'>calit/.beans — the chain behind pull request</div>

<div class='code'>

```text {1-9|11-13}
calit-0hyn  completed  Issue #116: 24h/locale-correct time format
                       on booking page
calit-184b  completed    Task 3: Persist host's 12h/24h preference
calit-wk3r  completed    Task 4: Settings UI for the preference
calit-syal  completed  Fix no-JS admin fallback + label wording
calit-4whp  completed  Validate OwnerSettings.timezone on save
calit-mhgs  completed  /me pages disagree on which timezone they show

closed by pull request #122 — the one from slide one

2026-08-16  #122 merged       superpowers + beans, nothing else
2026-08-17  glossary + ADRs   grill-with-docs, first run
2026-09-12  precedent         decisions across every repo
```

</div>

<!--
**SLIDE 38 UP**

This is the same pull request from the opening, seen from the other end. One work item, its numbered tasks, and the two follow-ups it spawned. Both are closed now. The first one — validate the timezone on save — is the fix for the bug from slide one.

[click] Attempt five did not start finished. The day I merged this, it was superpowers and beans, and nothing else. Nothing in it could hold a decision, so the rule about trusting input lived in my head — and I skimmed right past it.

The next day, grill-with-docs ran for the first time: a glossary and decision records. A month later, precedent. Most of what I just showed you grew out of this one pull request.

Nothing here was invented for the talk. The dates are in the git log.
-->

---
layout: center
class: statement
---

<div>There will be a sixth.</div>


<div class='vnote'>The five tiles again, with an empty sixth tile outlined faintly at the end.</div>

<!--
**SLIDE 39 UP**

Two honest limits. This is one person's evidence — five processes, my work, my preferences. I am not claiming a study.

And the specific tools on the previous slides date fast. There will be a sixth attempt, and I will have to run the same test on it.

The stack will change again. I expect the test to outlive it.
-->

---
layout: center
class: statement
---

<div>Who made this decision —</div>

<div>me, or the process?</div>

<div v-click class='answer'>It should be me. A good process asks me, then writes my answer down.</div>


<div class='vnote'>The test as one question, alone on the slide, large.</div>

<!--
**SLIDE 40 UP**

So, the test I said we would come back to.

*(let them read it)*

[click] It should be me. The process I kept asks me at the moment a decision comes up, then writes my answer down, so nobody has to guess it again.

Every process I dropped got that backwards. It decided for me — or it handed me every decision at once, and I skimmed, which comes to the same thing.
-->

---
layout: two-cols
class: artifact
---

<div class='claim'><div>Four of them lasted a day.</div><div class='sub'>The fifth is still open.</div></div>

::right::

<div class='filepath'>git log across the five repositories</div>

<div class='code dense'>

```text 
                    first        last      commits   process files

1  diskinventory    2026-08-10   +1 day        23    none
2  fb2ebup          2025-11-09   same day       1    1, under .junie/
3  femtocli         2026-02-23   +1 day         3    22, under specs/
4  spring-git-mcp   2026-03-28   +26 days       2    60, under openspec/
5  calit            2026-06-08   still open   830    growing every week
```

</div>

<!--
**SLIDE 41 UP**

Here they are as git sees them. Attempt one, twenty-three commits in two days. Two, three and four: one to three commits, then nothing.

Attempt five: eight hundred and thirty commits, sixteen weeks, still going. That is the whole claim, and it is the only measurement in this talk I did not have to argue for.
-->

---
layout: center
class: takeaway
---

<div class='tk-title'>Four failures, one shape</div>

<div class='tk-rows'>
<div v-click class='tk-row'><span class='n'>1</span><span class='a'>Junie, no process<small>vibe coding</small></span><span class='f'>nothing written down — the model made every call</span></div>
<div v-click class='tk-row'><span class='n'>2</span><span class='a'>Junie + guidelines.md<small>guidelines first</small></span><span class='f'>rules written down, reasons left out</span></div>
<div v-click class='tk-row'><span class='n'>3</span><span class='a'>Intent Integrity Kit<small>specify first</small></span><span class='f'>everything written down — more than I would read</span></div>
<div v-click class='tk-row'><span class='n'>4</span><span class='a'>OpenSpec + Claude<small>plan, then approve</small></span><span class='f'>every decision at once, at one gate — so I skimmed</span></div>
</div>

<div v-click class='tk-shape'>Each one took a decision out of my hands.</div>

<!--
**SLIDE 42 UP**

[click] Vibe coding: nothing written down, so the model made every decision.

[click] Guidelines: rules written down, reasons left out. And reasons are where the decisions live.

[click] Spec rigor: wrote everything down, at a volume I stopped reading. What I do not read, I did not decide.

[click] The big-plan one: every decision surfaced, all at one gate, so I skimmed instead of deciding.

[click] Different failures, same shape: each one took a decision out of my hands, or put it somewhere I would never pick it up.
-->

---
layout: center
class: statement
---

<div>Open the process you used this morning.</div>

<div>Point at where your standards live in it.</div>


<div class='vnote'>One instruction, and space beneath it. Nothing else on the slide.</div>

<!--
**SLIDE 43 UP**

So: open whatever you used this morning and point at where your standards live in it.

If you cannot point at a file, they live in your head, and they are getting re-derived, badly, every session.

Next step, and it is a small one: on Monday, write down one decision you made for the assistant, with the reason, in a file it reads. One. That is the whole starting move.
-->

---
layout: two-cols
class: artifact
---

<div class='claim'><div>Their keyboard, your standards.</div></div>

::right::

<div class='filepath'>the same pull request</div>

<img class='shot' src='/pr-122.png' alt='the same pull request'>

<!--
**SLIDE 44 UP — back to the opening PR**

Same pull request. Under a process that asks me and writes it down, this is one I would have written — because every decision in it would have been mine.

*(beat)*

It is their keyboard. The standards are still yours. Thank you.
-->

---
layout: center
class: statement
---

<div>Who made this decision&nbsp;—<br>you, or the process?</div>


<div class='contacts'>
<div class='ct'><span class='i-ph-globe'></span><span><a href='https://asm0dey.site'>asm0dey.site</a></span></div>
<div class='ct'><span class='i-ph-envelope'></span><span><a href='mailto:me@asm0dey.site'>me@asm0dey.site</a></span></div>
<div class='ct'><span class='i-ph-butterfly'></span><span>@asm0dey.site</span></div>
<div class='ct'><span class='i-carbon-logo-x'></span><span>@asm0di0</span></div>
</div>


<div class='vnote'>Closing card. Contacts and conference hashtag large enough to photograph from the back row. The test repeated beneath, so the photo carries it.</div>

<!--
**SLIDE 45 UP**

That is me, that is the test, and there is time for questions. Everything is on that site, and calit is a link away from it.
-->
