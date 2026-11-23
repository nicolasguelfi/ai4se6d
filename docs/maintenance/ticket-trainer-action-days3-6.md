# Ticket — « Trainer action » first entry in every tooltip, days 3-6 (gensem deck)

- **Status**: open, scheduled from the weekend of 28-29 November 2026 (NG, 2026-11-23: « fais un ticket pour
  le faire pour les autres journées à partir du prochain week-end »).
- **Owner**: ss2-ul-stx (slides). Tell ss2-ul-gse before editing gensem blocks.
- **Done already**: days 1-2 (commit e074e80, 2026-11-23: coding_agent 66, setup 22, vibecoding 9; genai_intro has none) — use them as
  the model (see `git log --grep "Trainer action"`).

## Request

Only for slides that show **code / commands, an exercise or a demo** (pure concept slides are left alone —
NG, 2026-11-23): the trainer must know, from the tooltip, what he does with it — exactly one of:

1. **Read and comment** — he reads and comments; nobody types anything.
2. **Live demo** — he types / shows it live himself (terminal, browser, on-screen widget).
3. **Learners do it** — the participants do it now, on their machine (or phone for a poll / QCM).

Form: first entry of each tooltip's entries list —
`("Trainer action", "<Action> — <short tail>. <why: concrete what / when>")`.
Such a slide without a tooltip gets one on the title line (95 % / 5 % header grid, « i » on the right).

## Scope (measured 2026-11-23)

Module `modules/ai4se6d_gensem`, the blocks wired through its sequences (139 wired blocks):

| Sequence | Half-day | Blocks |
|---|---|---|
| sequence_concepts.py | day 3 morning (HD05) | 48 |
| sequence_discovery.py | day 3 afternoon (HD06) | 13 |
| sequence_quality.py | day 4 morning (HD07) | 18 |
| sequence_delivery.py | day 4 afternoon (HD08) | 20 |
| sequence_deployment.py | day 5 morning (HD09) | 19 |
| sequence_sprint.py | day 5 afternoon (HD10) | 3 |
| sequence_finish.py | day 6 morning (HD11) | 9 |
| sequence_gallery.py | day 6 afternoon (HD12) | 9 |

Decide each action from the slide and the half-day syllabus sheet
(`ai4se-kit/syllabus/hd05…hd12-*.md`): from day 3 the learners have GSE-One installed, so `/gse-…` command
slides before an exercise are « Read and comment » or « Live demo », exercise / step slides « Learners do it ».

## Done when

- Every wired gensem slide with code, an exercise or a demo has a tooltip that starts with its Trainer action entry; slides still fit 1920×1080.
- Walk of the gensem book: all stops, 0 exceptions; `uv run ruff check`; walk-through audit OK.
- No on-slide wording change, so no syllabus delta (tooltips only).
