# My Standards, Their Keyboard — Script

**JRush 2026** · 30 min · Pasha Finkelshteyn · pacing 130–150 WPM

> Read top to bottom. Bold-bracketed lines are production cues. Italic parentheticals are delivery notes — pause, tone, audience interaction. Bolded ALL-CAPS names are speaker headers; consecutive items under one header are the same speaker.

---

## Slide 0 — A PR I Approved

**[SLIDE 0 UP]**

This is a pull request I merged. AI wrote it, I read the diff, it did what I asked, I approved it.

AUTHOR-01 — one sentence on what the PR actually did, so the room has context.

Nothing broke. There is no incident story at the end of this.

---

## Slide 1 — A Week Later

*On screen:*

> I would have rejected this

**[SLIDE 1 UP — same screenshot, annotated]**

A week later I read it properly. These are the comments I would have left if this had come from anyone on my team.

AUTHOR-02 — name two or three of the actual objections. None of them are bugs. All of them are choices.

*(beat — let them read one of the annotations)*

I approved code I would have sent back. So whose fault is that? Not the model's, and that is the uncomfortable part.

---

## Slide 2 — My Standards, Their Keyboard

*On screen:*

> My Standards, Their Keyboard
> Four AI processes, and then there was one

**[SLIDE 2 UP]**

That is the talk. Five processes, four of them dropped, and the one thing all four got wrong.

---

## Slide 3 — Who Is Complaining

*On screen:*

> Pasha Finkelshteyn · @asm0dey
> Ten-plus years in the JVM. Developer Advocate at BellSoft.

**[SLIDE 3 UP]**

Quickly, so you know whose taste you are about to hear about: ten-plus years in the JVM ecosystem, mostly Java and Kotlin, developer advocate at BellSoft.

That decade is where my preferences come from, and it is the only reason any of this bothers me.

---

## Slide 4 — The Model Has No Preferences

*On screen:*

> The model has no preferences.
> Mine took ten years.

**[SLIDE 4 UP]**

Ten-plus years in the JVM ecosystem gave me strong opinions about how code should look and which tools I reach for.

The model has none of that. Ask it the same question twice and you can get two different styles back, and both are fine by it.

---

## Slide 5 — The Process Is the Channel

*On screen:*

> The process is the only channel my standards travel through.

**[SLIDE 5 UP]**

It is their keyboard now. So how does anything of mine get in? Through the process I put around it, and nowhere else.

So every time I call the process overhead, I am calling my own standards overhead.

---

## Slide 6 — Five Attempts

*On screen:*

> 1  2  3  4  5

**[SLIDE 6 UP]**

Five processes on real work.

**[BUILD 01]**

I dropped four.

**[BUILD 02]**

Every one I dropped failed the same way: it made a decision that was mine to make. Keep that in your head, we come back to it at the end.

---

## Slide 7 — Attempt One: Vibe Coding

*On screen:*

> 1 — Vibe coding

**[SLIDE 7 UP]**

Attempt one. Describe what I want, let it write, look at what came back.

---

## Slide 8 — It Was Fast

*On screen:*

> Fastest of the five

**[SLIDE 8 UP]**

One commit: a working disk-usage tool with a drill-down pie chart, 1769 lines, sixteen files. AUTHOR-03 — say how long that actually took.

It was the fastest of all five. I want to be honest about that, because everything after this is slower and has to earn the difference.

---

## Slide 9 — Nothing to Review Against

*On screen:*

> A diff records the what.
> My standards live in the why.

**[SLIDE 9 UP]**

There was no artifact. Nothing recorded a single decision, so there was nothing to review against.

A diff tells you what changed, and never why that shape instead of another one. And why is exactly where all my standards live.

So, is vibe coding a moral failing? No. It is fast, and giving that speed up costs something real. It set the bar the other four had to clear.

---

## Slide 10 — Attempt Two: Guidelines First

*On screen:*

> 2 — Guidelines first

**[SLIDE 10 UP]**

Attempt two. Write the guidelines up front, then hand it tasks against them.

---

## Slide 11 — The Guidelines File

**[SLIDE 11 UP]**

This is the artifact. AUTHOR-04 — read out one rule that is unmistakably mine and would never appear in a default template.

A written guideline is a decision I made once, in my words, that the model reads at the start of every session.

---

## Slide 12 — My Preferences Survived a Session

*On screen:*

> One rule. Two files. Hours apart.

**[SLIDE 12 UP]**

Rule five of that file says: do not add the multipart extension, Quarkus 3 already has those APIs. Top excerpt is the build file, where it tried anyway and then commented the line out.

Bottom excerpt is a different file, written later in the same build, using the API the rule points at instead.

That is the whole win, and it is a small one. Before this, my preferences lasted about three files before the assistant drifted back to its own defaults. Here one of them was still in force at the other end of the codebase, because it was written down instead of remembered.

If the talk ended here, it would be a happy talk. It runs another twenty minutes.

---

## Slide 13 — It Solved the Task. I Still Did Not Like the Code.

*On screen:*

> Every guideline satisfied.
> Nothing in the file said anything about package names.

**[SLIDE 13 UP]**

It solved the task. Every rule in the file was respected. And I still did not want this code in my repository.

Read the package name. Every file in that project is under com.github.com — the scaffold's placeholder, never renamed, and no guideline of mine said anything about package names.

Guidelines encode rules. But the code I would have written comes out of a sequence of decisions, and most of those never take the shape of a rule.

---

## Slide 14 — And It Never Explained Itself

*On screen:*

> No rationale, so nothing to correct.
> Only overrule, session after session.

**[SLIDE 14 UP]**

And it never explained a single choice it made.

Without a rationale, how do I tell a deliberate call from a coin flip? I cannot. So I never correct anything, I just overrule it, session after session.

So, on to something that writes its reasoning down.

---

## Slide 15 — Attempt Three: Full Spec Rigor

*On screen:*

> 3 — Specify first, then implement

**[SLIDE 15 UP]**

Attempt three. Nothing gets implemented until it has been specified.

---

## Slide 16 — It Was Right About Everything

**[SLIDE 16 UP]**

To be fair to this one: it is right about what good practice looks like. Intent stated before implementation, acceptance criteria written down, nothing hand-waved.

AUTHOR-06 — one thing it caught that the previous process would have let through.

---

## Slide 17 — I Stopped Opening It

*On screen:*

> A process you abandon encodes nothing.

**[SLIDE 17 UP]**

So what went wrong? Nothing, on paper. It was just heavy, and after a few weeks I stopped opening it.

*(beat)*

A process you abandon encodes nothing. Whatever you still run on a Tuesday afternoon is its real ceiling.

---

## Slide 18 — Rigor Is Not Free

*On screen:*

> The cost lands on the one part of the system that can quit.

**[SLIDE 18 UP]**

Rigor has a price, and it is paid in my attention. I am also the one component in this system that can quietly opt out, and that is what I did.

---

## Slide 19 — Attempt Four: One Enormous Gate

> *Cuttable for short slot.*

*On screen:*

> 4 — Plan everything, then approve it

**[SLIDE 19 UP]**

Attempt four. On paper, the best-designed of the five.

---

## Slide 20 — Credit Where It Is Due

> *Cuttable for short slot.*

*On screen:*

> Worktrees by default

**[SLIDE 20 UP]**

It got real things right. Worktrees by default, so parallel work stopped colliding. I did not have to ask for that.

I dropped it anyway, over one structural choice.

---

## Slide 21 — One Step, One Enormous Plan

> *Cuttable for short slot.*

*On screen:*

> Read all of this. Approve. Go.

**[SLIDE 21 UP]**

There is essentially one step where I read an enormous plan with all its specs, and approve the lot.

AUTHOR-07 — say how long the plan actually was.

Every decision in there was mine to make, and every one was correctly surfaced. They were just handed to me in a single lump.

---

## Slide 22 — A Lump Does Not Get Reviewed

> *Cuttable for short slot.*

*On screen:*

> Nobody reviews a lump this size.
> They skim it.

**[SLIDE 22 UP]**

And what does anyone do with a lump that size? Skim it.

*(point back at the opening PR)*

Which is the same skim as slide one, moved one step earlier and much better documented.

Attempt three drowned me in volume. This one got the volume right and the timing wrong: every decision arrives at one moment, instead of at the moments when I can actually make them.

---

## Slide 23 — Attempt Five: What I Run Today

*On screen:*

> 5 — What I run today

**[SLIDE 23 UP]**

This is the one I still run.

---

## Slide 24 — The Stack, On One Repo

*On screen:*

> github.com/asm0dey/calit

**[SLIDE 24 UP]**

Everything from here is one real repository. calit — a self-hosted Calendly alternative on Quarkus and Java 25, multi-user, Google Calendar sync. Public, so you can go read all of this after.

AUTHOR-08 — name the three moving parts in one sentence each: the skills that drive the work, the docs that hold my decisions, the tracker that holds the work items.

Forget the tool names for a second. Every one of those files exists because the process made me decide something, and then wrote down what I decided.

---

## Slide 25 — It Asks Me Small Questions

*On screen:*

> One decision, at the moment it comes up

**[SLIDE 25 UP]**

It asks me one decision at a time, at the moment that decision comes up. Small enough that I actually read it.

That is the fix for attempt four: the same decisions, spread out.

---

## Slide 26 — Buffers Are Constraints, Not Settings

**[SLIDE 26 UP]**

Here is one of four decision records in that repo. Read the title: buffers are constraints, so the strictest one governs.

*(let them read the title)*

That is a domain judgement, in my words, with the consequences I accepted written underneath it. No linter has an opinion about that sentence.

This is what attempt two was missing: the reasoning behind a decision, kept where the next session will read it.

---

## Slide 27 — Including the Words I Refuse to Use

*On screen:*

> Owner. Not user, not admin, not account.

**[SLIDE 27 UP]**

And this one I like most, because it is pure preference. The glossary says what a thing is called, and then lists the words I have decided we never use for it.

Could anyone derive that from the code? No. It is a taste decision, it is mine, and now it survives every session without me repeating myself.

So when I read a diff now, the why is already sitting next to it: in a decision record, in a task file, or in the glossary.

---

## Slide 28 — This Is Attempt Five, Not the Answer

*On screen:*

> There will be a sixth.

**[SLIDE 28 UP]**

Two honest limits. This is one person's evidence — five processes, my work, my preferences. I am not claiming a study.

And the specific tools on the previous slides date fast. There will be a sixth attempt, and I will have to run the same test on it.

The stack will change again. I expect the test to outlive it.

---

## Slide 29 — The Test

*On screen:*

> Does this process encode the decisions that are mine —
> or make them for me?

**[SLIDE 29 UP]**

So, the test I said we would come back to.

*(let them read it)*

Encode, or replace. Two words, and they sorted every process I have tried.

---

## Slide 30 — Run It on the Four

*On screen:*

> Takeaway — four failures, one shape:
> no artifact · rules without reasons · more than I would read · all at one gate

**[SLIDE 30 UP]**

Vibe coding: no artifact, so nothing was encoded at all.

Guidelines: rules encoded, reasons left out. And reasons are where the decisions live.

Spec rigor: encoded everything, at a volume I stopped reading. Unread is unencoded.

The big-plan one: every decision surfaced, all at one gate, so I skimmed instead of deciding.

Different failures, same shape: each one took a decision out of my hands, or put it somewhere I would never pick it up.

---

## Slide 31 — Now Run It on Yours

*On screen:*

> Open the process you used this morning.
> Point at where your standards live in it.

**[SLIDE 31 UP]**

So: open whatever you used this morning and point at where your standards live in it.

If you cannot point at a file, they live in your head, and they are getting re-derived, badly, every session.

Next step, and it is a small one: on Monday, write down one decision you made for the assistant, with the reason, in a file it reads. One. That is the whole starting move.

---

## Slide 32 — Their Keyboard, Your Standards

*On screen:*

> Their keyboard, your standards.

**[SLIDE 32 UP — back to the opening PR]**

Same pull request. Under a process that encodes, this is one I would have written — because every decision in it would have been mine, and written down.

*(beat)*

It is their keyboard. The standards are still yours. Thank you.

---

## Slide 33 — Thanks

*On screen:*

> @asm0dey | #JRush | #AIcoding
> 
> Does it encode your decisions — or make them for you?

**[SLIDE 33 UP]**

That is me, that is the test, and there is time for questions.
