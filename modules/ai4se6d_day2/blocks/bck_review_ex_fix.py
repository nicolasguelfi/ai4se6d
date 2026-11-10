"""Slide — Fix one finding, test first."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Fix one finding, test first — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_ex_fix_body")
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "review_ex_fix_cmd")
bs = BlockStyles


_FIX = """\
Fix RVW-1 from docs/review.md. First write a failing test that exposes
it and run npm run test:run (RED), then fix the code (GREEN).
Change nothing else."""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Fix One Finding — Test First', tag=t.div, toc_lvl='+1')
            st_write(
                bs.body,
                'Tab back to the ',
                (bs.keyword, 'build'),
                ' agent, on branch ',
                (bs.cmd, 'fix/review'),
                ':',
                tag=t.div,
            )
            st_code(s.none, code=_FIX, language='text', line_numbers=False, font_size="36pt")
            with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(bs.body, 'Read the diff: did it touch anything else?')
                with l.item():
                    st_write(bs.body, (bs.cmd, 'npm run test:run'), ' green → commit ', (bs.cmd, 'fix: RVW-1 …'))
                with l.item():
                    st_write(bs.body, 'In ', (bs.cmd, 'docs/review.md'), ': RVW-1 → ', (bs.keyword, 'fixed'))
