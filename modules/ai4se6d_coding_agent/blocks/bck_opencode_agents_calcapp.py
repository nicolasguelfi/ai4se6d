"""Slide — The AGENTS.md shipped with the CalcApp starter."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


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

_NOTES = [
    ("The message",
     "The CalcApp starter already ships an AGENTS.md: participants do not start from a blank page. Read it before "
     "the first prompt."),
    ("What it contains",
     "Three sections — the pinned stack (React 19 + React Router 7, TypeScript 5.9, Vite 7, Vitest 4), the layout "
     "(routes in src/App.tsx, one page component per route, tests/ mirrors src/, docs/ for the plan) and four rules."),
    ("The four rules",
     "TDD with a failing test first and never weakening a test; tests and lint pass before a commit; one branch "
     "per task, never commit directly to main; never commit secrets."),
    ("Link to the day",
     "Each rule comes back later today: branches and commits (Git), the plan in docs/ (planning workshop), TDD "
     "(build session), review before merge."),
    ("Ask the room",
     "« Which of these rules would the agent break first if the file were missing? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(75):
                st_write(bs.heading, "The CalcApp AGENTS.md", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — The CalcApp AGENTS.md", entries=_NOTES,
                                 position="left", width="50vw")
        with st_grid(cols="5% 90% 5%") as g:
            with g.cell():
                pass  # left margin
            with g.cell():
                st_code(s.none, code=_AGENTS_MD, language="markdown", line_numbers=False, font_size="26pt")
            with g.cell():
                pass  # right margin
        st_space("v", "2vh")
        with st_zoom(110):
            st_write(bs.closing, "Already in your starter: read it before your first prompt.", tag=t.div)
