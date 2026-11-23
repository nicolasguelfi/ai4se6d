"""Slide — Live demo — one full red-green-refactor cycle in opencode."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Live demo — one full red-green-refactor cycle in opencode — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_demo_body")
    keyword = s.bold + s.project.colors.highlight
    number = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "build_demo_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "build_demo_timer")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "build_demo_foot")
bs = BlockStyles

_NOTES = [
    ("The message",
     "One full cycle, live, in 10 minutes or less, on the demo feature: ExpenseItem shows « Lunch » and « €25.50 »."),
    ("RED",
     "Ask the build agent for the test only, read it, run npm run test:run: it fails because the component "
     "does not exist."),
    ("GREEN",
     "Ask for the minimal code, without touching the test; npm run test:run goes green."),
    ("The proof",
     "Break the code on purpose: a test must fail. Then two commits — test: … first, then feat: …"),
    ("Link to what follows",
     "Each step of the demo returns in the exercise on task 1 of your own plan."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'Live Demo: One Full Cycle', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Live Demo: One Full Cycle", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(100):
            st_write(bs.timer, '≤ 10 min', tag=t.div)
        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        steps = [
            ((bs.keyword, 'build'), ' agent: ask for the ', (bs.keyword, 'test only'), ' → read it'),
            ((bs.cmd, 'npm run test:run'), ' → ', (bs.keyword, 'RED'), ' (the component does not exist)'),
            ('Ask for the minimal code — ', (bs.keyword, 'do not touch the test')),
            ((bs.cmd, 'npm run test:run'), ' → ', (bs.keyword, 'GREEN')),
            ('Break the code on purpose → a test must fail',),
            ('Two commits: ', (bs.cmd, 'test: …'), ' first, then ', (bs.cmd, 'feat: …')),
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(steps), cols, filled=(2, 3))
        with st_zoom(105), st_grid(cols=cols, gap="1.8vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(steps, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "3vh")
        with st_zoom(100):
            st_write(bs.foot, 'Demo feature: ExpenseItem shows “Lunch” and “€25.50”.', tag=t.div)
