"""Slide — TDD in one picture — red, green, refactor."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """TDD in one picture — red, green, refactor — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_tdd_cycle_body")
    keyword = s.bold + s.project.colors.highlight
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "build_tdd_cycle_foot")
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "build_tdd_cycle_text_cell")

_NOTES = [
    ("The message",
     "Test-driven development in three steps, repeated for every small piece of behaviour."),
    ("RED",
     "Write a test that fails. A failing test before the code is the expected start, not a problem: it proves "
     "the test checks something that does not exist yet."),
    ("GREEN",
     "The minimal code that passes — nothing more."),
    ("REFACTOR",
     "Clean up; the tests stay green, so you know the clean-up broke nothing."),
    ("Link to what follows",
     "Code first, theory later: the live demo runs one full cycle in opencode."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'TDD in One Picture', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — TDD in One Picture", entries=_NOTES,
                                 position="left", width="50vw")
        with st_grid(cols='1.5fr 3.5fr', gap="3vw",
                     cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
            with g.cell():
                st_image(s.none, width='100%', uri='images/pm/red_green_refactor_cycle.png')
            with g.cell(), st_zoom(125):
                with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body,
                             text_align="left", item_gap=0.6) as l:
                    with l.item():
                        st_write(bs.body, (bs.keyword, 'RED'), ' — write a test that fails')
                    with l.item():
                        st_write(bs.body, (bs.keyword, 'GREEN'), ' — the minimal code that passes')
                    with l.item():
                        st_write(bs.body, (bs.keyword, 'REFACTOR'), ' — clean up, tests stay green')
                st_space("v", "3vh")
                st_write(
                    bs.body,
                    'A failing test ',
                    (bs.keyword, 'before'),
                    ' the code is the expected start, not a problem.',
                    tag=t.div,
                )
        st_space("v", "2vh")
        with st_zoom(110):
            st_write(bs.foot, 'Code first, theory later: watch one full cycle.', tag=t.div)
