# Producer Profile

## Metadata

| Field | Value |
|-------|-------|
| Created | 2026-04-01 |
| Last updated | 2026-04-01 |
| Projects count | 2 (ai4se6d_genai_intro, ai4se6d_vibecoding) |

## Document Types

- Auditorium presentations (16:9, dark theme, 10-20m projection)
- Professional training materials (5-20 participants)
- Technical content (AI, software engineering)

## Workflow Preferences

- CE fix mode: **interactive** — validate each fix individually (validated 2026-03-31)
- CE plan mode: **interactive (3-pass)** — structure → content → consolidation
- CE produce mode: **per-sequence** — produce groups of related blocks, validate together before next group
- Slide review: **one by one** — verify each slide against source and plan before moving on

## Style Preferences

- Design guideline: maximize-viewport (auditorium projection)
- Dark theme with high-contrast palette
- Font hierarchy: 96/80/48/32pt (projection-safe)
- Minimalist: one idea per slide, max 5 bullets, max 7 words per bullet
- AI images: flat vector, soft gradients, geometric shapes, dark background

## Anti-patterns

- **No hardcoded black/white**: never use `s.text.colors.white` or `s.text.colors.black` — use `s.project.colors.*` instead. Breaks theme compatibility and violates design system separation. Common temptation: white text on dark backgrounds, initials on colored circles.
- **No inline RGBA values**: extract to `custom/styles.py` as composable styles when used in 3+ blocks.
- **No duplicated prompt strings**: extract to `custom/prompts.py` when 5+ blocks share the same graphic line.

## Pedagogical Patterns

- **Personal anchoring before theory**: always start a new concept with a self-positioning question ("How much of your code is AI-generated?") before introducing the framework. Creates a mental reference point that participants revisit during theory.
- **Progressive questioning**: start with a broad question, then narrow ("How much AI code?" → "Do you review it?"). The logical link between questions reinforces engagement.
- **Exercise flow**: briefing (instructions) → timer (giant centered) → debrief (discussion questions). Standard 3-phase structure for all hands-on exercises.

## Content Conventions

- Glossary block at end of each module (not inline definitions)
- Terminology convention established by glossary, not enforced in titles
- Cross-module solutions stored at collection root (`docs/solutions/`)
