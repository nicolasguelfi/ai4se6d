"""Slide — The AGENTS.md shipped with the CalcApp starter."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """CalcApp AGENTS.md styles."""
    heading = s.project.titles.heading
    closing = Style.create(s.project.titles.body_accent + s.center_txt, "occalc_closing")
bs = BlockStyles

_AGENTS_MD = """\
# CalcApp — project conventions for coding agents   (excerpt)
## Stack (pinned)
React 19 + React Router 7, TypeScript 5.9, Vite 7, Vitest 4
## Layout
src/App.tsx = routes · src/pages/ = one component per route
tests/ mirrors src/ · docs/ = your plan and documentation
## Rules
1. TDD: failing test first, never weaken a test
2. `npm run test:run` and `npm run lint` pass before a commit
3. One branch per task — never commit directly to main
4. Never commit secrets (.env* stays out of git)"""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "The CalcApp AGENTS.md", tag=t.div, toc_lvl="+1")
        st_space("v", 0.5)
        st_code(s.none, code=_AGENTS_MD, language="markdown", line_numbers=False, font_size="22pt")
        st_space("v", 0.5)
        st_write(bs.closing, "Already in your starter: read it before your first prompt.", tag=t.div)
