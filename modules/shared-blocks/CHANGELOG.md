# Changelog — shared-blocks

Shared blocks and styles used across all ai4se6d modules.

## [0.2.1] — 2026-04-09

### Changed
- TDD glossary definition expanded with GenAI context (acceptance criteria)

## [0.2.0] — 2026-04-08

### Added
- Centralized `references.bib` (48 entries, single source of truth for all modules)
- `shared_widgets.py` with `st_hover_tooltip()` (CSS hover tooltip with scale, position, styles)
- `stat_hero`, `stat_hero_primary`, `stat_hero_critical` styles in `shared_styles.py`

### Changed
- Shared glossary now used by all 3 modules via chained registry

## [0.1.0] — 2026-04-07

### Added
- Shared styles module (`shared_styles.py`)
- Shared blocks directory for cross-module reuse
- Static assets directory for shared images
