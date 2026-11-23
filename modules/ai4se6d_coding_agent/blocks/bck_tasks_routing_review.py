"""Slide — Review checklist — routing."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Review checklist — routing — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_routing_review_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_routing_review_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "tasks_routing_review_foot")
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Walk through the five checks; learners apply them to the agent's"
     " routing code during the 13:30 exercise."),
    ("The message",
     "Five checks on the agent's routing code, each answerable in seconds — the first review habit of the "
     "afternoon."),
    ("What each check catches",
     "The wrong package (react-router-dom instead of react-router); plain <a href> links that reload the whole "
     "page; pages not in their own file under src/pages/; a test silently modified; a navigation that only "
     "looks right."),
    ("The key check",
     "git diff -- tests/ must show nothing: the GREEN prompt said « Do not modify the test ». If the agent "
     "changed it, the green result means nothing."),
    ("Try it in the browser",
     "npm run dev, click both links, use the back button: the tests do not cover everything."),
    ("Link",
     "« Trust, but verify » — the habit the review section practises at 14:30."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, "Review the Agent's Routing", tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Review the Agent's Routing", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # One row per check, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ((bs.cmd, 'react-router'), ' in ', (bs.cmd, 'package.json'), ', no ', (bs.cmd, 'react-router-dom'), '?'),
            ('Navigation with ', (bs.cmd, 'Link'), ', not ', (bs.cmd, '&lt;a href&gt;'), ' (no full reload)?'),
            ('One file per page in ', (bs.cmd, 'src/pages/'), '?'),
            ('Test untouched? ', (bs.cmd, 'git diff -- tests/'), ' shows nothing'),
            ((bs.cmd, 'npm run dev'), ': click both links, back button works?'),
        ]
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2,))
        with st_zoom(97), st_grid(cols=cols, gap="3.5vh 0.5vw", cell_styles=cells) as g:
            for parts in items:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "4vh")
        with st_zoom(105):
            st_write(bs.foot, 'Trust, but verify — you will need this habit at 14:30.', tag=t.div)
