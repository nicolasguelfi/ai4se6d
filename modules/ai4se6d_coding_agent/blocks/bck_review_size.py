"""Slide — Optimal review size — 200 to 400 lines."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Optimal review size — 200 to 400 lines — styles."""
    heading = s.project.titles.heading
    body_center = Style.create(s.project.titles.body + s.center_txt, "review_size_body_c")
    stat = Style.create(s.Giant + s.bold + s.project.colors.highlight + s.center_txt, "review_size_stat")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "review_size_foot")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


_STAT = """\
git diff j2-start --stat    # how many lines did you change today?"""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'How Much per Review?', tag=t.div, toc_lvl='+1')
            st_write(bs.stat, '200–400 lines', tag=t.div)
            st_write(
                bs.body_center,
                'per review — beyond that, defect detection drops. And no more than 60 minutes per session.',
                tag=t.div,
            )
            st_write(bs.source, cite('cohen2006-peer-review'), tag=t.div)
            st_code(s.none, code=_STAT, language='bash', line_numbers=False, font_size="36pt")
            st_write(
                bs.foot,
                'An agent writes 1,000 lines in a session: review per task, not per day.',
                tag=t.div,
            )
