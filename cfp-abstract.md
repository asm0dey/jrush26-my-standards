# My Standards, Their Keyboard

*Four AI processes, and then there was one*

**Venue:** JRush · **Slot:** 30 min · **Status:** CFP abstract only, no deck built

## Abstract

The model has no preferences. Yours took ten years to form. You let it write, skim the diff, and ship, then read it properly and find code you would have rejected from anyone on your team. That gap is the whole problem.

Ten-plus years in the JVM ecosystem gave me strong preferences about how code should look and which tools I reach for. Four processes later, I am on my fifth. Vibe coding was fast and completely unreviewable. The next one made me write the guidelines up front, and my preferences survived a whole session for the first time. Rigor killed the third: it was thorough enough that I stopped opening it. The fourth never fit the way I work. The fifth is what I run today. You will see all five on screen: what each one did, where four of them fell over, and the artifacts from real work.

Every process I dropped had the same defect: it made the decisions that are mine to make. The one I kept leaves them to me and writes down what I decide. You leave with a test you can run against any AI process, including the one you use now. Their keyboard, your standards.

## Abstract (short, <1000 chars)

The model has no preferences. Yours took ten years to form. You let it write, skim the diff, and ship, then read it properly and find code you would have rejected from anyone on your team.

Four processes later, I am on my fifth. Vibe coding was fast and completely unreviewable. The next made me write guidelines up front, and my preferences survived a session for the first time. Rigor killed the third: too thorough to keep opening. The fourth never fit how I work. You will see all five on screen, with the artifacts from real work.

Every process I dropped made the decisions that are mine to make. The one I kept leaves them to me and writes down what I decide. Their keyboard, your standards.

## Key Takeaways

You'll leave able to:

- Test any AI-assisted process against one question: does it encode your preferences, or make the decisions for you?
- Name the failure mode that kills each class of process: too loose, too heavy, wrong shape
- Run the process I use now on your own work

## Outline

1. **Hook** (3 min) — the shipped PR I would have rejected in review
2. **Thesis** (2 min) — the model has no preferences; the process is how yours get in
3. **Attempt one: vibe coding** (4 min) — fast, unreviewable, and why it still taught something
4. **Attempt two: guidelines first** (5 min) — first time my preferences survived a whole session
5. **Attempt three: full spec rigor** (4 min) — thorough, and too heavy to keep opening
6. **Attempt four: wrong shape** (4 min) — good on paper, never fit how I work
7. **What I run today** (5 min) — the current stack, live, with its real artifacts
8. **Coda** (4 min) — the encode-vs-replace test, applied to whatever you use now

## Small Print (for the Program Committee)

- **Mode:** Journey Mapping (fellow-learner discovery, story opening). Vendor-neutral, zero commercial intent, no BellSoft positioning. Not a tool review — the five processes are the evidence, not the subject.
- **Target:** JRush, 30 min. Speaker delivered *Open Source Security* at JRush 2025.
- **Slot fit:** built for 30 min. Cut line: merge sections 5–6 into one "the heavyweights" beat for a 20-min version without breaking the arc.
- **Overlap check:** distinct from *Git Panic to Git Zen* (AI driving one tool via MCP) and *JOIN Club* (reading AI-written SQL). This one is the harness around the AI, not its output in one domain.
- **Tools named on stage, withheld from the public abstract:** vibe coding, a generate-guidelines-then-hand-it-tasks flow (Junie), intent-integrity-kit, OpenSpec, and the current superpowers + grill-with-docs + beans tracker stack. Deliberate — the specific five are the talk's payoff, not its advertising. The abstract sells the shape of the journey; the room gets the names.
- **Time-sensitive:** the on-stage tool list dates fast. Re-verify section 7 before each delivery.
- **Guardrail:** speaker's recurring `shortchanged` antipattern — closing gets a hard 4-minute allocation, not whatever time is left.
- **Anti-pattern check:** PASS (0 high, 1 medium) via `blog-writer@1.1.27`, three-pass scan. Retained medium: "Their keyboard, your standards" is a balanced phrase (#5), kept as the title callback.
- **Subtitle reference:** riffs on Agatha Christie's *And Then There Were None*, inverted to "one" because a survivor is the point. Deliberately the only broad pop-culture reference in the talk — the vault records this speaker's register as "minimal broad pop culture, used sparingly."
- **Terminology note:** body says *preferences*; title says *Standards*. The preferences are negotiable. Consider retitling to *My Preferences, Their Keyboard*.

## Open Items

- Slug not derived — needs the live shownotes directory to read the current convention. Expected shape: `jrush26-my-standards`.
- Pattern history unavailable: 22 talks sit at `needs-reprocessing` pending a `vault-ingress` batch re-score against catalog schema 6.
