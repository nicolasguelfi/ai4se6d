# Changelog — ai4se6d

All notable changes to this project are documented in this file.

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
