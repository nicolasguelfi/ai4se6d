"""Slide — AI review output is input to your judgment — accept, defer, refuse."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """AI review output is input to your judgment — accept, defer, refuse — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_review_judgment_body")
    keyword = s.bold + s.project.colors.highlight
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "d2_review_judgment_foot")
bs = BlockStyles


_TRIAGE = """\
RVW-1 [HIGH]   storage.ts: corrupt JSON crashes the app → FIX
RVW-2 [MEDIUM] AddExpense: negative amount accepted     → FIX
RVW-3 [LOW]    rename amount → amountEur          → REFUSED
               reason: v0.1 has one currency (docs/plan.md)"""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'You Are the Judge', tag=t.div, toc_lvl='+1')
            st_write(
                bs.body,
                'For each finding: ',
                (bs.keyword, 'fix'),
                ', ',
                (bs.keyword, 'defer'),
                ', or ',
                (bs.keyword, 'refuse — with a written reason'),
                '.',
                tag=t.div,
            )
            st_code(s.none, code=_TRIAGE, language='markdown', line_numbers=False, font_size="36pt")
            st_write(
                bs.foot,
                'A written refusal is a decision, not laziness — and someone else can review it.',
                tag=t.div,
            )
