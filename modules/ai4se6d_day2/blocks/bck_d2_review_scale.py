"""Slide — Review at scale — 60 million Copilot code reviews."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Review at scale — 60 million Copilot code reviews — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_review_scale_body")
    body_center = Style.create(s.project.titles.body + s.center_txt, "d2_review_scale_body_c")
    keyword = s.bold + s.project.colors.highlight
    stat = Style.create(s.Giant + s.bold + s.project.colors.highlight + s.center_txt, "d2_review_scale_stat")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "d2_review_scale_foot")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Review at Scale', tag=t.div, toc_lvl='+1')
            st_write(bs.stat, '60 million', tag=t.div)
            st_write(
                bs.body_center,
                'Copilot code reviews by March 2026 — ',
                (bs.keyword, 'more than 1 in 5'),
                ' code reviews on GitHub',
                tag=t.div,
            )
            st_write(bs.source, cite('github-ccr-60m2026'), tag=t.div)
            st_write(
                bs.body,
                'The volume of generated code is enormous: someone — or something — must check all of it.',
                tag=t.div,
            )
            st_write(bs.foot, 'Speed without review is just faster failure.', tag=t.div)
