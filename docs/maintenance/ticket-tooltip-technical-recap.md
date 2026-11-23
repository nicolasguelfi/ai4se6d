# Ticket — "Technical recap" section at the bottom of every technical slide's tooltip

- **Status**: open, not scheduled (NG, 2026-11-23: « crée un ticket, c'est une grosse mission, je ne sais pas
  quand je vais l'annoncer »).
- **Requested by**: NG, through the WATCH session, 2026-11-23 19:57; turned into this ticket at 19:59.
- **Owner when scheduled**: ss2-ul-stx (slides); ss2-ul-gse to be told before gensem blocks are edited.

## Request

« Parcourir tous les slides techniques pour ajouter dans le tooltip un rappel, une section éventuellement
« rappel », qui explique les éléments techniques de chaque slide, en bas du tooltip. »

Audience: learners who do not know the tools. Every tool-specific name on a slide (command, key, file, agent,
protocol, option) is explained in plain words in the tooltip, after the trainer notes.

## Model already done

`modules/ai4se6d_vibecoding/blocks/bck_ide_opencode.py` (commit 5ccf346, 2026-11-23): each of its three
`_NOTES_*` lists ends with entries titled `Technical recap — <term>` (terminal agent, model provider, plan /
build agents, Shift+Tab, AGENTS.md and /init, permissions, MCP, opencode.json, $ vs >, @file, tutor, JSON…).
Same form everywhere: one entry per term, 1-3 sentences, no jargon left unexplained, facts checked against the
tool's documentation.

## Scope (measured 2026-11-23, HEAD 1bb4c3a, by the WATCH session)

| Module | blocks | with a tooltip |
|---|---|---|
| ai4se6d_coding_agent | 108 | 103 |
| ai4se6d_gensem | 296 (139 wired) | 98 |
| ai4se6d_vibecoding | 64 | 49 |
| ai4se6d_setup | 33 | 33 |
| ai4se6d_genai_intro | 71 | 9 |
| various / collection / shared-blocks | 10 | 0 |

"Technical" slides still to be selected: the tools part of vibecoding (IDE / opencode / MCP / VSCodium), all of
setup, coding_agent (git, opencode plan/build, review, tests), gensem (GSE-One commands, CI/CD, deployment).
Blocks without a tooltip get one first (title-line « i », 95 % / 5 % header grid).

## Known fact to fix in the same pass

opencode's plan agent is **not** read-only (opencode.ai/docs/agents: it explores without editing normal project
files, may write its plan files, shell commands stay permission-controlled). Still written « read-only » in:
- `modules/ai4se6d_coding_agent/blocks/bck_review_ex_fix.py:26`
- `modules/ai4se6d_coding_agent/blocks/bck_review_ex_steps.py:26`, `:63` (on the slide)
- `modules/ai4se6d_coding_agent/blocks/bck_review_prompts.py:27`
- `modules/ai4se6d_vibecoding/blocks/bck_ide_comparison_concepts.py:31` (table cell)

## Done when

- Every selected slide's tooltip ends with its technical recap entries; slides still fit 1920×1080.
- Walk of each module: all stops, 0 exceptions; `uv run ruff check`; walk-through audit OK.
- Syllabus deltas sent to ss2-ul-gse when an on-slide wording changes.
