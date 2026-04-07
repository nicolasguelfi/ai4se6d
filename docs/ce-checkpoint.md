# CE Checkpoint — ai4se6d_gensem

**Date**: 2026-04-07
**Project**: ai4se6d_gensem (Generative Software Engineering Methods)
**Current plan**: `docs/plans/2026-04-06-002-C-gensem-plan-v2.md`
**Phase**: PRODUCE complete → REVIEW v2 complete → FIX pending

---

## Session Metadata

| Field | Value |
|-------|-------|
| Plan | v2 (7 parts, ~131 blocks, ~180 min / 3h) |
| Blocks in book.py | 131 |
| Block files on disk | 132 (1 orphan: `bck_gensem_poll_method.py` — removed from book.py) |
| Reviews | v1 (`2026-04-06-gensem-review.md`) + v2 (`2026-04-06-gensem-v2-review.md`) |
| SOTA coverage | Excellent — no CRITICAL gaps (audit 2026-04-06) |
| Ruff | All checks passed |
| Runtime test | 132 blocks imported, build() validated, Streamlit starts cleanly |
| Bib entries | 32 defined, 25 used |
| AI image blocks | 6 (title, ce_title, ce_five_phases, fw_vbounce, sdlc_human, method_title) |

---

## Current Phase: FIX (pending)

The module has been through 2 review cycles. The v2 review identified 3 CRITICAL, 9 MAJOR, 10 MINOR findings. A 3-phase fix plan was proposed but NOT yet executed.

### Fix Phase 1 — Critical + quick wins (NOT DONE)
- [ ] CR1: Fix Forrester text in `bck_gensem_roadmap.py` ("at least one org" not "50% of enterprises")
- [ ] CR2: Qualify "90%+" in `bck_gensem_plugin_demo_compound.py` (add "in our experience" or remove)
- [ ] MJ6: Add cite() to `bck_gensem_fw_se30.py`, `bck_gensem_fw_vbounce.py`, `bck_gensem_fw_agilegen.py`
- [ ] MJ7: Fix synthesis table labels in `bck_gensem_fw_synthesis.py` (replace opaque symbols with descriptive labels)
- [ ] m1: Fix METR +20% → +24% in `bck_gensem_evidence_perception.py`
- [ ] m6: Standardize GenSE → GenSEM in `bck_gensem_calcapp_v03_traceability.py`, `bck_gensem_calcapp_v03_prompts.py`

### Fix Phase 2 — Style factoring (NOT DONE)
- [ ] MJ2-MJ5: Factor `closing`, `card_title`, `dont/do_callout`, `stat_hero` into custom/styles.py
- [ ] CR3: Update all 15+ v1 blocks to use factored styles (`s.project.titles.heading`, `.keyword`, `.label`, `.stat`, `.source`) instead of local BlockStyles duplicates
- [ ] m3-m5: Remove `callout_body` alias (9 blocks), fix vbounce_diagram pt48 duplication, factor `message` style (6 blocks)

### Fix Phase 3 — Content additions (NOT DONE)
- [ ] MJ9: Add cross-tool terminology block (how concepts map across Claude Code / Cursor / Copilot)
- [ ] MJ1: Differentiate the 2 Fowler blocks (human_fowler vs evidence_fowler — same quote)
- [ ] m7: Remove `bck_gensem_fw_multiagent.py` (v1 compact) from book.py — superseded by v2 detail blocks
- [ ] m9: Enrich `bck_gensem_risks_overview.py` with ethics detail (EU AI Act, responsibility gap, environmental cost)
- [ ] m8: Remove duplicate junior/senior stats from `bck_gensem_sdlc_human.py` (now covered by `human_junior_senior.py`)

---

## Decisions Log

1. **Plan v1 → v2**: Extended from 63 slides/105 min to ~131 blocks/180 min after feedback "rajouter du contenu, pas juste diluer"
2. **7 parts instead of 5**: Added Part 2 (Evidence empirique, 14 blocks) and restructured Part 1 (15 tasks, 15 concepts, human factor)
3. **Substantive new content**: 72 blocks added exploiting SOTA depth (3 RCTs, Daniotti 160K, multi-agent taxonomy, CE artifacts/anti-patterns, specialization as research platform)
4. **Font sizes fixed**: body = explicit 48pt, caption = explicit 32pt via `_pt48`/`_pt32` in styles.py — no longer reliant on CSS variable defaults
5. **Styles factored**: heading, keyword, label, stat, source, critical added to custom/styles.py — but v1 blocks NOT yet updated (technical debt)
6. **Glossary expanded**: 9 → 36 terms (including CHOP, ACI, Agent Mode, Hooks, SOP, etc.) + shared glossary created in shared-blocks
7. **LOT 1 applied**: session_map generic ("3-Parts Journey" no dates), poll removed, SDLC/codegen tables transposed, RE title reduced
8. **g.cell(style=) bug fixed**: 13 files corrected (GridController.cell() takes no arguments — use st_block() inside cell)
9. **Bib enriched**: 19 → 32 entries, gitlab key renamed, duplicates removed, Cui/Daniotti/MetaGPT/ChatDev/OpenHands added
10. **v1 fixes deferred**: Forrester text, "90%+" claim, missing cite() calls, synthesis labels, style factoring — all identified but not yet applied

---

## Pending Issues

| # | Issue | Impact | Effort |
|---|-------|--------|--------|
| 1 | v1 review fixes not applied (CR1, CR2, MJ6, MJ7) | Credibility risk on 4 slides | 15 min |
| 2 | Style duplication in 15+ v1 blocks | Maintenance debt, visual inconsistency | 30 min |
| 3 | Duplicate Fowler content (2 blocks) | Audience sees same quote twice | 10 min |
| 4 | v1 compact multiagent block redundant | Redundant slide after 6 detailed ones | 2 min |
| 5 | Cross-tool terminology block missing | SOTA gap (Appendix B not covered) | 20 min |
| 6 | Ethics section thin | EU AI Act, responsibility gap missing | 15 min |
| 7 | Orphan file `bck_gensem_poll_method.py` on disk | No impact (not in book.py) | 1 min |

---

## Context for Next Session

The module is **functionally complete** — 131 blocks compile and render, SOTA coverage is excellent, the narrative flow is validated. What remains is **polish**: applying the review fixes (text corrections, style consistency, deduplication) and a few content additions (cross-tool terminology, ethics enrichment).

**Recommended next actions**:
1. Run `/stx-ce:fix` to apply the 3-phase fix plan from the v2 review
2. Remove orphan `bck_gensem_poll_method.py` from disk
3. After fixes: run `/stx-ce:review --quick` to verify
4. Then `/stx-ce:compound` to capitalize learnings

**The module is ready for visual review** — the trainer can open `stx run --port 8585` and navigate through all 131 slides to provide visual feedback (LOT 2+).
