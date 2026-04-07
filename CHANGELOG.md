# Changelog — ai4se6d

All notable changes to this project are documented in this file.

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
