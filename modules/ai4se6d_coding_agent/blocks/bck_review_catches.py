"""Slide — What AI review catches well and what it misses."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """What AI review catches well and what it misses — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_catches_body")
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.highlight
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "review_catches_foot")
bs = BlockStyles


_NOTES = [
    ("The message",
     "AI review gives breadth, the human reviewer gives depth. Neither alone is enough."),
    ("What AI review catches well",
     "Local, pattern-like problems it can see in the code itself: missing error handling, null / undefined "
     "risks, type slips, dead code, hook dependency mistakes, known security anti-patterns."),
    ("What it misses",
     "Everything that needs knowledge outside the diff: what the user needs, the right place in the design, "
     "effects across distant files, subtle authorization rules — and whether the code should exist at all."),
    ("How to use it",
     "Let the agent sweep for the left column; spend your own attention on the right one."),
    ("Link",
     "Next slides: how to prompt for a review, how to triage the findings, and why you remain the judge."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'What AI Review Sees and Misses', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — What AI Review Sees and Misses", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "1vh")

        # Two columns side by side, one row per pair, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        pairs = [
            (('Missing error handling',), ('Does it do what the ', (bs.keyword, 'user'), ' needs?')),
            (('null / undefined risks',), ('Is this the right place in the design?',)),
            (('Type slips, dead code',), ('Effects across distant files',)),
            (('Hook dependency mistakes',), ('Subtle authorization rules',)),
            (('Known security anti-patterns',), ('Should this code exist at all?',)),
        ]
        cols = "5% 43% 43% 5%"
        with st_zoom(101):
            with st_grid(cols=cols, gap="1vh 2vw", cell_styles=s.project.containers.row_cell_left) as g:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.label, 'Catches well — breadth', tag=t.div)
                with g.cell():
                    st_write(bs.label, 'Misses — depth: you', tag=t.div)
                with g.cell():
                    pass  # right margin
            cells = s.project.containers.rows(len(pairs), cols, filled=(2, 3))
            with st_grid(cols=cols, gap="2.5vh 2vw", cell_styles=cells) as g:
                for left, right in pairs:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.body, *left, tag=t.div)
                    with g.cell():
                        st_write(bs.body, *right, tag=t.div)
                    with g.cell():
                        pass  # right margin
        st_space("v", "3vh")
        with st_zoom(106):
            st_write(bs.foot, 'AI = breadth, you = depth. Neither alone is enough.', tag=t.div)
