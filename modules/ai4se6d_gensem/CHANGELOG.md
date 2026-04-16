# Changelog — ai4se6d_gensem

GenSEM module — Generative Software Engineering Methods.

## [0.4.0] — 2026-04-16

### Added
- 6 new blocks:
  - `bck_gensem_ce_plan_living` — Living plan + 3 coherence alerts (Inform-tier)
  - `bck_gensem_ce_plan_summary` — plan-summary.md archive (DELIVER output)
  - `bck_gensem_t6_vv` — V&V foundation (Verification & Validation)
  - `bck_gensem_t6_test_run` — Canonical Test Run (7 immutable steps, spec §6.3)
  - `bck_gensem_t6_test_evidence` — Per-TASK YAML result block
  - `bck_gensem_t6_test_review_tiers` — Test Review 3 tiers (STRATEGY / TST-SPEC / IMPL)

### Changed
- `book.py`: Sessions 3 & 4 now active (T5 requirements → T8 advanced); previously commented
- T3 sequence: added living plan and plan-summary around `ce_plan_artifact`
- T6 sequence: added V&V + test run + test evidence + review tiers before `/gse:produce`
- Refined 20+ blocks: `title`, `method_checklist`, `method_step2`, `plugin_architecture`, `plugin_cursor`, `practice_p3`, `practice_p8`, `t2_cmd_backlog`, `t2_cmd_pause_resume`, `t2_cmd_status`, `t2_commands`, `t2_philosophy`, `t3_cmd_plan`, `t5_requirements`, `t6_cmd_fix`, `t6_cmd_produce`, `t6_cmd_tests`, `t6_engineering`, `t7_cmd_deliver`, `t7_cmd_health`, `ce_plan_artifact`
- Asset update: `static/images/managed/gse_lifecycle_4stages.json`

## [0.3.0] — 2026-04-15

### Added
- Complete 4-session restructuring: T1–T8 themes with P1–P8 practice interleaving
- 47 new blocks: command slides (23), practice blocks (8), theme blocks (T2–T8), evidence/risks/paradigms
- T2: philosophy (6 slides), Agile bridge, HUG profile, commands & agents (4 slides)
- T3: discovery (COLLECT/ASSESS/PLAN), frontmatter traceability
- T4: decisions, risks & AI integrity (6 slides)
- T5–T8: requirements, engineering, delivery, advanced (Sessions 3–4, staged)
- Evidence restructuring: `evidence_rcts` (Productivity Paradox) and `evidence_reality` blocks
- Risks block: 6 risk cards + "More AI ≠ fix" + Gap visualization
- SDLC orchestrator and paradigms blocks
- GSE logo assets, promo videos, deploy superhero videos
- Design guideline configuration
- Slide-break migration guide

### Changed
- book.py restructured into Session 1–4 with T1–T8 sequencing
- 49 existing blocks refactored (style, layout, spacing, zoom, content)
- Evidence blocks consolidated (Cui/METR/Peng → evidence_rcts + evidence_reality)
- Multi-agent framework blocks consolidated into single `frameworks` block

### Removed
- 8 deprecated blocks: evidence_cui, evidence_metr, evidence_peng, fw_multiagent (×4), plugin_lfg

## [0.2.0] — 2026-04-08

### Changed
- Switched to centralized bibliography (`shared-blocks/static/references.bib`)
- Harmonized bibkeys to KBSCI convention (`stackoverflow-survey2026`, `bain2025`)
- Factorized `stat_hero` styles into `shared_styles.py`
- Chained registry in `__init__.py` for shared block resolution

## [0.1.0] — 2026-04-07

### Added
- Complete module with ~132 blocks, ~150 slides, ~3h content
- Part 1: Le Métier du Generative SE (25 blocks) — SDLC changes, 15 concepts, human factor
- Part 2: L'Évidence Empirique (14 blocks) — RCTs, surveys, enterprise evidence
- Part 3: Frameworks Méthodologiques (30 blocks) — AgileGen, SE 3.0, V-Bounce, Promptware, Multi-Agent
- Part 4: Compound Engineering (35 blocks) — philosophy, brainstorm, plan, work, review, compound
- Part 5: CalcApp v0.3 Activities (10 blocks) — FR/NFR examples, CE mapping, traceability
- Part 6: GenSemOne Method (15 blocks) — 5-step method, timeline, vs vibecoding
- Part 7: CE Plugin Demo (11 blocks) — architecture, demo phases, Cursor
- Glossary and references blocks
- CE review report and production plans
- Bibliography with APA format and hover citations
- Export configs (HTML + PDF)
- `doc_version` display
