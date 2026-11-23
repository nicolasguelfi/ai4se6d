"""Slide — Why start with tests?."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Why start with tests? — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_why_tests_body")
    keyword = s.bold + s.project.colors.highlight
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "build_why_tests_foot")
bs = BlockStyles

_NOTES = [
    ("The message",
     "The #1 risk with a coding agent is losing control: code arrives fast, but nobody knows if it works."),
    ("Why tests",
     "Clicking through the app is not a proof. A test answers in milliseconds, yes or no, and can be run again "
     "after every change of the agent."),
    ("Who does what",
     "You set the specification (the test); the agent writes the implementation. You stay in the driver's seat."),
    ("Link to what follows",
     "The next slides show the cycle (red, green, refactor), a live demo, and the golden rule: review the test "
     "before the code is written."),
    ("Ask the room",
     "« How did you check, yesterday, that what the agent built actually worked? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'Why Start with Tests?', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Why Start with Tests?", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        with st_zoom(120):
            st_write(
                bs.body,
                'The #1 risk with a coding agent: ',
                (bs.keyword, 'losing control'),
                '.',
                tag=t.div,
            )
            with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body,
                         text_align="left", item_gap=0.6) as l:
                with l.item():
                    st_write(bs.body, 'Code arrives fast — but does it work?')
                with l.item():
                    st_write(bs.body, 'Clicking through the app is not a proof')
                with l.item():
                    st_write(bs.body, 'A test answers in milliseconds: ', (bs.keyword, 'yes or no'))
            st_space("v", "2vh")
            with st_block(s.project.containers.callout):
                st_write(
                    bs.body,
                    (bs.keyword, 'You'),
                    ' set the specification (the test). The ',
                    (bs.keyword, 'agent'),
                    " writes the implementation. You stay in the driver's seat.",
                )
            st_space("v", "2vh")
            st_write(bs.foot, 'Tests = control. No tests = hope.', tag=t.div)
