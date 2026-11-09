"""Slide — The speed paradox — AI writes bugs faster."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """The speed paradox — AI writes bugs faster — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_review_paradox_body")
    body_center = Style.create(s.project.titles.body + s.center_txt, "d2_review_paradox_body_c")
    keyword = s.bold + s.project.colors.highlight
    stat = Style.create(s.Giant + s.bold + s.project.colors.highlight + s.center_txt, "d2_review_paradox_stat")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "d2_review_paradox_foot")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'The Speed Paradox', tag=t.div, toc_lvl='+1')
            st_write(
                bs.body,
                'Typing by hand was a natural throttle on bugs. An agent removes it: code comes faster — ',
                (bs.keyword, 'and so do bugs'),
                '.',
                tag=t.div,
            )
            st_write(bs.stat, '1.7×', tag=t.div)
            st_write(
                bs.body_center,
                'more issues per pull request in AI-co-authored code (10.83 vs 6.45, 470 open-source PRs)',
                tag=t.div,
            )
            st_write(bs.source, cite('coderabbit-ai-vs-human2025'), tag=t.div)
            st_write(
                bs.foot,
                'A vendor study on a small sample — but the direction is clear: review matters MORE with AI.',
                tag=t.div,
            )
