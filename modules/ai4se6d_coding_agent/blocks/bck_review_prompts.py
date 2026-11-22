"""Slide — Weak vs effective review prompts."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Weak vs effective review prompts — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_prompts_body")
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "review_prompts_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "review_prompts_foot")
bs = BlockStyles


_GOOD1 = """\
@src/pages/AddExpense.tsx Review edge cases and error handling.
The input comes from a user form: empty, negative, huge amounts?"""

_GOOD2 = """\
@src/utils/storage.ts What happens if localStorage holds corrupt JSON
or is full? Classify each finding HIGH / MEDIUM / LOW."""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Weak vs Effective Prompts', tag=t.div, toc_lvl='+1')
            st_write(bs.body, (bs.label, 'Weak: '), (bs.cmd, 'Review this code.'), tag=t.div)
            st_write(
                bs.body,
                (bs.label, 'Effective: '),
                (bs.keyword, 'plan'),
                ' agent (Shift+Tab — read-only), one file, one concern, the context:',
                tag=t.div,
            )
            st_code(s.none, code=_GOOD1, language='text', line_numbers=False, font_size="36pt")
            st_code(s.none, code=_GOOD2, language='text', line_numbers=False, font_size="36pt")
            st_write(
                bs.foot,
                'Name the file, the concern, the context: specific prompt, actionable findings.',
                tag=t.div,
            )
