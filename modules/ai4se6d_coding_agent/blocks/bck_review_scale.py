"""Slide — Review at scale — 60 million Copilot code reviews."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Review at scale — 60 million Copilot code reviews — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_scale_body")
    body_center = Style.create(s.project.titles.body + s.center_txt, "review_scale_body_c")
    keyword = s.bold + s.project.colors.highlight
    stat = Style.create(s.Giant + s.bold + s.project.colors.highlight + s.center_txt, "review_scale_stat")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "review_scale_foot")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


_NOTES = [
    ("The message",
     "AI review is already mainstream: 60 million Copilot code reviews by March 2026, more than one in five "
     "code reviews on GitHub."),
    ("The figure",
     "From the GitHub Blog (5 March 2026): Copilot code review usage grew 10× since its April 2025 launch."),
    ("Why it matters",
     "The volume of generated code is enormous: someone — or something — must check all of it. Humans alone "
     "cannot keep up, so AI review becomes part of the loop."),
    ("The trap",
     "Reading the figure as « AI review is enough »: the next slides show what tests and review each remove, "
     "and what AI review misses."),
    ("Ask the room",
     "« Does your team already use an AI reviewer on pull requests? What does it catch? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'Review at Scale', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Review at Scale", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(95):
            st_space("v", "3vh")
            st_write(bs.stat, '60 million', tag=t.div)
            st_space("v", "2vh")
            st_write(
                bs.body_center,
                'Copilot code reviews by March 2026 — ',
                (bs.keyword, 'more than 1 in 5'),
                ' code reviews on GitHub',
                tag=t.div,
            )
            st_write(bs.source, cite('github-ccr-60m2026'), tag=t.div)
            st_space("v", "4vh")
            st_write(
                bs.body,
                'The volume of generated code is enormous: someone — or something — must check all of it.',
                tag=t.div,
            )
            st_space("v", "3vh")
            st_write(bs.foot, 'Speed without review is just faster failure.', tag=t.div)
