"""Slide — TDD in one picture — red, green, refactor (cycle drawn with StreamTeX grids, NG 2026-11-24)."""
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
    circle = Style("border-radius: 50% !important; width: 29vh; min-width: 29vh; aspect-ratio: 1 / 1; "
                   "margin: 0 auto; padding: 0 !important;", "tdd_circle")
    step = Style.create(s.project.titles.body + s.bold + s.center_txt, "tdd_step")
    what = Style.create(s.project.titles.caption + s.center_txt, "tdd_what")
    arrow = Style.create(s.project.titles.body + s.bold + s.center_txt + Style("line-height: 1; color: #9E9E9E;",
                                                                             "tdd_arrow_c"), "tdd_arrow")
bs = BlockStyles

_CYCLE_ZOOM = 100   # the three circles; tuned by measure (content bottom <= 1000 px at 1920x1080)
_ARROW_ZOOM = 240
_STEP_ZOOM = 80     # text inside the circles
_TEXT_ZOOM = 100    # the numbered list on the right

# 3 x 3 grid: RED on top, GREEN bottom right, REFACTOR bottom left; arrows turn clockwise
_CYCLE = [
    ("arrow", "↗"), ("step", s.project.tone_red, "RED", "write a failing test"), ("arrow", "↘"),
    (".",), ("centre",), (".",),
    ("step", s.project.tone_blue, "REFACTOR", "clean the code"), ("arrow", "←"),
    ("step", s.project.tone_green, "GREEN", "make it pass"),
]

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
    ("Here: ATDD at the scale of a task",
     "In our tasks the failing test comes from the task's acceptance criteria: acceptance-test-driven "
     "development (ATDD) at the scale of one task. Textbook TDD (Beck) goes further: many tiny steps driven by "
     "unit tests, and a refactor after each green. From day 3, GSE-One runs this same loop for you."),
    ("Link to what follows",
     "Code first, theory later: the live demo runs one full cycle in opencode."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'TDD in One Picture', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — TDD in One Picture", entries=_NOTES,
                                 position="left", width="50vw")
        with st_grid(cols='3fr 2fr', gap="3vw",
                     cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
            with g.cell(), st_zoom(_CYCLE_ZOOM), st_grid(cols="1fr 1fr 1fr", gap="0",
                                                       cell_styles=s.project.containers.grid_cell_centered) as c:
                for cell in _CYCLE:
                    with c.cell():
                        if cell[0] == "step":
                            tone, word, what = cell[1], cell[2], cell[3]
                            with st_block(tone.card + bs.circle), st_zoom(_STEP_ZOOM):
                                st_write(bs.step + tone.fg, word, tag=t.div)
                                st_write(bs.what, what, tag=t.div)
                        elif cell[0] == "arrow":
                            with st_zoom(_ARROW_ZOOM):
                                st_write(bs.arrow, cell[1], tag=t.div)
                        elif cell[0] == "centre":
                            st_write(bs.what, "TDD", tag=t.div)
            with g.cell(), st_zoom(_TEXT_ZOOM):
                with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body,
                             text_align="left", item_gap=0.6) as l:
                    with l.item():
                        st_write(bs.body, (bs.keyword + s.project.tone_red.fg, 'RED'), ' — write a test that fails')
                    with l.item():
                        st_write(bs.body, (bs.keyword + s.project.tone_green.fg, 'GREEN'), ' — the minimal code that passes')
                    with l.item():
                        st_write(bs.body, (bs.keyword + s.project.tone_blue.fg, 'REFACTOR'), ' — clean up, tests stay green')
                st_space("v", "3vh")
                st_write(
                    bs.body,
                    'A failing test ',
                    (bs.keyword, 'before'),
                    ' the code is the expected start, not a problem.',
                    tag=t.div,
                )
        st_space("v", "2vh")
        with st_zoom(108):
            st_write(bs.foot, 'Code first, theory later: watch one full cycle.', tag=t.div)
