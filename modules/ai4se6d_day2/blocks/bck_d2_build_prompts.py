"""Slide — Two prompts per task — RED then GREEN."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Two prompts per task — RED then GREEN — styles."""
    heading = s.project.titles.heading
    label = s.project.titles.label
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "d2_build_prompts_foot")
bs = BlockStyles


_RED = """\
@docs/plan.md Task 1 only. Write the failing test first, in tests/.
Do NOT write the implementation. Run npx vitest run and show the failure."""

_GREEN = """\
Implement the minimal code that makes tests/<file>.test.tsx pass.
Do not modify the test file. Run npx vitest run."""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Two Prompts per Task', tag=t.div, toc_lvl='+1')
            st_write(bs.label, '1 · RED — test only (build agent)', tag=t.div)
            st_code(s.none, code=_RED, language='text', line_numbers=False, font_size="36pt")
            st_write(bs.label, '2 · GREEN — once you have reviewed the test', tag=t.div)
            st_code(s.none, code=_GREEN, language='text', line_numbers=False, font_size="36pt")
            st_write(
                bs.foot,
                'In prompts, ask for npx vitest run: npm test watches forever and the agent would wait.',
                tag=t.div,
            )
