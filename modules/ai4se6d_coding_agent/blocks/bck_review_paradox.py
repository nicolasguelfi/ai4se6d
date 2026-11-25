"""Slide — The speed paradox — AI writes bugs faster."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """The speed paradox — AI writes bugs faster — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_paradox_body")
    body_center = Style.create(s.project.titles.body + s.center_txt, "review_paradox_body_c")
    keyword = s.bold + s.project.colors.highlight
    stat = Style.create(s.Giant + s.bold + s.project.colors.highlight + s.center_txt, "review_paradox_stat")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "review_paradox_foot")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


_NOTES = [
    ("The message",
     "Typing by hand slowed the production of bugs. An agent removes that throttle: code comes faster, and so "
     "do bugs — review matters MORE with AI, not less."),
    ("The figure",
     "1.7× more issues per pull request (a pull request = a proposed change submitted for review before it is "
     "merged) in AI-co-authored code: 10.83 vs 6.45 issues per PR, on 470 open-source "
     "GitHub pull requests (320 AI-co-authored, 150 human-only). Security issues were up to 2.74× higher."),
    ("Read it with care",
     "A vendor study (CodeRabbit, December 2025) on a small sample, and the authorship labels are not "
     "guaranteed. Use it for the direction, not the exact ratio."),
    ("Link",
     "Next slides: the scale of AI review today, then what review finds that tests miss."),
    ("Ask the room",
     "« In your Part 2 code, how many issues would a reviewer find per task? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'The Speed Paradox', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — The Speed Paradox", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(111):
            st_write(
                bs.body,
                'Typing by hand was a natural throttle on bugs. An agent removes it: code comes faster — ',
                (bs.keyword, 'and so do bugs'),
                '.',
                tag=t.div,
            )
            st_space("v", "3vh")
            st_write(bs.stat, '1.7×', tag=t.div)
            st_space("v", "2vh")
            st_write(
                bs.body_center,
                'more issues per pull request in AI-co-authored code (10.83 vs 6.45, 470 open-source PRs)',
                tag=t.div,
            )
            st_write(bs.source, cite('coderabbit-ai-vs-human2025'), tag=t.div)
            st_space("v", "3vh")
            st_write(
                bs.foot,
                'A vendor study on a small sample — but the direction is clear: review matters MORE with AI.',
                tag=t.div,
            )
