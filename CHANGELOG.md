# Changelog — ai4se6d

All notable changes to this project are documented in this file.

## [0.3.2] — 2026-04-17

### Changed
- GenSEM: alignment with GSE-One spec updates (FIX conditional, 7 structural signals, Lightweight workflow includes REQS, plugin inventory 23 skills / 19 templates / 57 files)
- GenSEM: 8 blocks updated — `t8_modes`, `t8_advanced`, `plugin_architecture`, `t2_philosophy`, `ce_five_phases`, `practice_p8`, `ce_plan_summary`, `t6_engineering`

### Verified
- `.stx-version` = 0.6.10 still aligned with latest streamtex on PyPI (0.6.10, uploaded 2026-04-15)
- `pyproject.toml` constraint `streamtex[cli,pdf,ai,inspector]>=0.6.10` unchanged
- `uv.lock` refreshed after version bump
- Dockerfile continues to rebuild `.stx_cache` + static HTML at container start (entrypoint.sh clears stale caches)
- Dual serve mode (Nginx `/html/` + Streamlit `:8501`) active for all 5 Coolify apps

## [0.3.1] — 2026-04-16

### Added
- GenSEM: activated Sessions 3 & 4 in `book.py` (T5 requirements, T6 engineering, T7 delivery, T8 advanced — previously commented out)
- GenSEM: 6 new blocks — `bck_gensem_ce_plan_living`, `bck_gensem_ce_plan_summary`, `bck_gensem_t6_vv`, `bck_gensem_t6_test_run`, `bck_gensem_t6_test_evidence`, `bck_gensem_t6_test_review_tiers`
- GenSEM: v5 plan addendum in `docs/plans/2026-04-16-005-C-gensem-plan-v5-addendum.md`
- Dockerfile: documented optional Chromium/Playwright install for PDF export (disabled by default)

### Changed
- GenSEM: refinements across 20+ blocks (title, method, plugin, practice P3/P8, T2 commands & philosophy, T3 plan, T5 requirements, T6 engineering, T7 deliver/health)
- GenSEM: `book.py` T3 sequence extended (living plan + plan summary), T6 sequence extended (V&V foundation + test run + evidence + review tiers)
- GenSEM: asset update `gse_lifecycle_4stages.json`

### Verified
- `.stx-version` = 0.6.10 aligned with latest streamtex on PyPI
- Dockerfile uses `--no-sources --upgrade-package streamtex` to always fetch latest PyPI
- entrypoint.sh clears `.stx_cache` and regenerates warmup + static HTML at container start
- Dual serve mode (Nginx static + Streamlit dynamic) active for all 4 Coolify apps

## [0.3.0] — 2026-04-15

### Added
- GenSEM: complete 4-session restructuring with 47 new blocks (T2–T8 themes, P1–P8 practices, command slides)
- GenSEM: 8 practice blocks (P1–P8) with briefing/timer/debrief structure per session
- GenSEM: 23 GSE-One command slides (`/gse:go`, `/gse:status`, `/gse:hug`, `/gse:collect`, etc.)
- GenSEM: new theme blocks — T2 philosophy (6 slides), T3 discovery (4 slides), T4 decisions (6 slides)
- GenSEM: T5 requirements, T6 engineering, T7 delivery, T8 advanced blocks (Sessions 3–4, currently commented)
- GenSEM: risks block (6 risk cards + "More AI ≠ fix" + Gap), SDLC orchestrator & paradigms blocks
- GenSEM: evidence restructuring — new `evidence_rcts` and `evidence_reality` blocks
- GenSEM: GSE logo assets, promo videos (24s/64s), deploy superhero videos
- GenSEM: design guideline configuration (`custom/design-guideline.md`)
- GenSEM: slide-break migration guide in `docs/`
- docs: CE plans v3 and v4 for gensem production
- docs: 5 new capitalization solutions (anti-scroll, guideline-before-blocks, image-centering, tooltip-positioning, video-size, task-card-2row)

### Changed
- GenSEM: book.py fully restructured into 4 sessions × 8 themes (T1–T8) with practice interleaving
- GenSEM: evidence blocks consolidated (Cui/METR/Peng merged into `evidence_rcts` + `evidence_reality`)
- GenSEM: multi-agent framework blocks consolidated into `bck_gensem_frameworks` (was 4 separate files)
- GenSEM: 49 existing blocks refactored (style, layout, spacing, zoom, content updates)
- GenSEM: Agile→GSE-One bridge slide added to T2
- shared-blocks: `shared_widgets.py` updates, `references.bib` expanded
- vibecoding: minor fix in `bck_vibecoding_conversation.py`

### Removed
- GenSEM: 8 deprecated blocks (evidence_cui, evidence_metr, evidence_peng, fw_multiagent × 4, plugin_lfg)

## [0.2.2] — 2026-04-10

### Added
- Q&A Companion module (`ai4se6d_various`) — 8 blocks with tool-agnostic explanations
- Q&A Companion registered in collection hub (order 4)

## [0.2.1] — 2026-04-09

### Changed
- genai_intro: zoom/layout refinements across 8+ slides, orange highlight on "manual feature engineering"
- genai_intro: context benchmark chart height reduced (1300→1100px), GPT-3.5→GPT-3 correction
- vibecoding: major style/layout refactoring across 30+ blocks, TDD→acceptance criteria terminology
- vibecoding: book restructured (principles overview before requirements, IDE section deferred)
- shared-blocks: TDD glossary definition expanded with GenAI context

### Fixed
- `.stx-version` aligned to PyPI latest (0.3.3) — was 0.6.8, causing Docker build failures
- Added gensem service to CI/CD deploy workflow (was missing from `hetzner-deploy.yml`)
- Trainer slides spacing improvements (bottom padding before slide breaks)

## [0.2.0] — 2026-04-08

### Added
- Cross-module coherence review (5-axis: inter-module, KBSCI, co-trainer, temporal, completeness)
- 4 new empirical blocks in vibecoding (METR paradox, Trust crisis, Copilot RCT, Experience Gap)
- Shared hover tooltip widget (`shared_widgets.py`) with scale, position, and CSS hover
- AI Intelligence Index benchmarks (4 slides) in genai_intro
- OpenAI Codex coverage in vibecoding tool ecosystem
- KBSCI errata registry (`docs/reviews/2026-04-08-kbsci-errata.md`)
- Capitalization solutions (8 new/enriched) from CE compound phase

### Changed
- Centralized glossary via `shared-blocks/blocks/bck_shared_glossary.py` (chained registry)
- Centralized bibliography in `shared-blocks/static/references.bib` (48 entries, single source)
- Harmonized all bibkeys to KBSCI convention across 3 modules
- Factorized `stat_hero` styles into `shared_styles.py` (3 variants: highlight, primary, critical)
- Exercises 2+3 reframed as teasers (FreeSelfApp PM / CalcApp Day 2)
- Corrected StackOverflow stats (76%/63%/82%, verified on site)
- Roadmap Day 1: added VibeEngineering; Day 6: reordered Presentations/Ethics/Closure

### Fixed
- VibeCoding definition inconsistency across modules ("pair programmer" → KBSCI-aligned)
- Statistics contradiction (84% vs 76%) resolved
- Collins Dictionary Word of Year 2025 added to VibeCoding origin
- `st_space` negative values now use `margin-top`/`margin-left` (lib fix)
- Multiple text centering issues in vibecoding blocks

## [0.1.0] — 2026-04-07

### Added
- Plotly dependency and enhanced citation styling in GenAI intro
- Enhanced AI and GenAI content with updated definitions and references
- VibeCoding session 2 module + GenAI intro updates
- WebP migration, AI auto-generate, export fixes, vibecoding module
- GenSEM module (~132 blocks, ~150 slides) — Generative Software Engineering Methods
- Dual-mode Dockerfile (Nginx static HTML + Streamlit interactive)
- `doc_version` to all `book.py` files
- CI deploys replicas alongside primary services
- CE artifact directories and collection design guideline
- Environment flags coding rule

### Fixed
- Resolved all 172 merge conflict markers across 45 files
- Resolved merge conflicts in `uv.lock`, aligned Dockerfile with docs pattern
- Correct `/html/` redirect per FOLDER — nginx 302 instead of meta refresh

### Changed
- Bumped `.stx-version` to 0.6.8 for latest PyPI streamtex
- Restructured as monorepo with `modules/` directory
- Aligned collection structure with streamtex-docs pattern + deployment infra

### Infrastructure
- Hetzner server (cax21) with Coolify for deployment
- Wildcard DNS `*.streamtex.org` → 138.199.148.59
- Dual serve mode: static HTML at `/html/` + Streamlit interactive at `/`
- Pre-warm page cache and pre-generate static HTML in Docker build
