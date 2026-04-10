# Changelog — ai4se6d_various

Q&A Companion — Detailed answers to participant questions, enriched throughout the training.

## [0.1.0] — 2026-04-10

### Added
- 8 blocks: navigation (Where Are All the Slides?), concepts, architecture, execution, tool control, case study Maria, Maria architecture, Maria execution
- Q/A document structure with level-1 umbrella question and level-2 sub-topics
- Tool-agnostic explanations with "Tool-specific variants" callout boxes (Claude Code, Codex CLI, Cursor, Copilot)
- "Variants by Tool" sections below architecture and execution diagrams
- Mermaid diagram export helper with dark/light theme support (SVG, PNG, PDF)
- Clickable links to COURSEPACK, CONCEPTS, and PRACTICALS resources

### Design
- Dark theme aligned with other modules (config.toml, shared styles, slide_title/subtitle hierarchy)
- maximize-viewport design guideline
- Paginated mode with slide breaks, presentation config (16/9), markers on level 1+2

### Integration
- Registered in ai4se6d_collection as "Q&A Companion" (order 4)
