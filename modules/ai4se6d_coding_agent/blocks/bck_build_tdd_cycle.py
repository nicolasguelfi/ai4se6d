"""Slide — TDD in one picture — red, green, refactor (cycle drawn with StreamTeX grids, NG 2026-11-24)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """TDD in one picture — red, green, refactor — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body, "build_tdd_cycle_body")
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "build_tdd_cycle_cmd")
    wrong = Style.create(s.project.colors.muted + s.italic, "build_tdd_cycle_wrong")
    right = Style.create(s.bold + s.project.tone_red.fg, "build_tdd_cycle_right")
    circle = Style("border-radius: 50% !important; width: 35vh; min-width: 35vh; aspect-ratio: 1 / 1; "
                   "margin: 0 auto; padding: 0 1.5vh !important;", "tdd_circle")
    step = Style.create(s.project.titles.body + s.bold + s.center_txt, "tdd_step")
    what = Style.create(s.project.titles.caption + s.center_txt, "tdd_what")
    result = Style.create(s.project.titles.caption + s.bold + s.center_txt, "tdd_result")
    who = Style.create(s.project.titles.caption + s.italic + s.center_txt, "tdd_who")
    arrow = Style.create(s.project.titles.body + s.bold + s.center_txt + Style("line-height: 1; color: #9E9E9E;",
                                                                             "tdd_arrow_c"), "tdd_arrow")
    arrow_cmd = Style.create(s.project.titles.caption + s.text.fonts.font_monospace + s.project.colors.accent + s.center_txt, "tdd_arrow_cmd")
bs = BlockStyles

_CYCLE_ZOOM = 92    # the three circles; tuned by measure (content bottom <= 1000 px at 1920x1080)
_ARROW_ZOOM = 200
_ARROW_CMD_ZOOM = 80   # « npm run test:run » on each arrow
_STEP_ZOOM = 80     # text inside the circles
_WHO_ZOOM = 70      # who does the step, small legend under each circle
_TEXT_ZOOM = 80     # the three points on the right

# Each circle: the action (a verb), who does it, what the test shows at the end (NG, 2026-11-25)
# 3 x 3 grid: RED on top, GREEN bottom right, REFACTOR bottom left; arrows turn clockwise
_CYCLE = [
    ("arrow", "↗"),
    ("step", s.project.tone_red, "RED", "Write a test for the expected behaviour", "✗ fails on the expected value",
     "Agent writes, you review"),
    ("arrow", "↘"),
    (".",), ("centre",), (".",),
    ("step", s.project.tone_blue, "REFACTOR", "Improve the design, same behaviour", "✓ still passes",
     "You decide, agent applies"),
    ("arrow", "←"),
    ("step", s.project.tone_green, "GREEN", "Write the minimal code that passes", "✓ passes",
     "Agent writes, test untouched"),
]

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "build_tdd_cycle_text_cell")

_NOTES = [
    ("The message",
     "Test-driven development in three steps, repeated for every small piece of behaviour. Each circle says the "
     "action, who does it (under the circle) and what the test shows at the end; every arrow is a run of npm run "
     "test:run."),
    ("Red for the right reason (point 2)",
     "Two real messages from npm run test:run. « ExpenseItem not found »: the test cannot even run, so red proves "
     "nothing. « Expected €25.50, got nothing »: the test runs and the behaviour is missing — that red is the proof "
     "the test checks what you want. How to get the right red: first an ExpenseItem that shows nothing yet (an "
     "empty shell, returns null), see the live demo."),
    ("RED",
     "Write the test, plus an empty shell of the code (the function or component exists but does nothing yet), "
     "and run it: it must fail on the expected value, not because a file or function is missing. A test that "
     "fails only on « cannot find module » proves nothing about the behaviour; a test that fails on « expected "
     "€25.50, received nothing » proves it checks what you want. A failing test before the code is the expected "
     "start, not a problem."),
    ("Who runs the tests",
     "A test framework: Vitest, already installed in CalcApp (package.json, devDependencies) — the agent does not "
     "need to add one. Test files live in tests/ and end in .test.ts(x). npm run test:run (= vitest run) runs them "
     "all once and prints ✓ or ✗ per test: green = all pass, red = at least one fails, with expected vs received. "
     "Seen this morning in the Git exercise."),
    ("GREEN",
     "The minimal code that passes — nothing more. The test is not touched."),
    ("REFACTOR — Fowler's definition",
     "« Refactoring: a change made to the internal structure of software to make it easier to understand and "
     "cheaper to modify without changing its observable behavior » (Martin Fowler, Refactoring). So: improve the "
     "design — remove duplication, extract a function, rename — same behaviour, the tests stay green. Not « clean "
     "up » in the sense of adding or fixing features."),
    ("Who does what",
     "RED: you + agent — the agent drafts the test, you review it: it is your spec. GREEN: the agent writes the "
     "minimal code, the test is not touched. REFACTOR: you decide what to improve, the agent applies it; the tests"
     " stay green. Detailed on the Golden Rule slide."),
    ("Here: ATDD at the scale of a task",
     "In our tasks the failing test comes from the task's acceptance criteria: acceptance-test-driven "
     "development (ATDD) at the scale of one task. Textbook TDD (Beck) goes further: many tiny steps driven by "
     "unit tests, and a refactor after each green. From day 3, GSE-One runs this same loop for you."),
    ("Link to what follows",
     "Code first, theory later: the live demo shows the three steps on ExpenseItem, REFACTOR included."),
]


def _circle(tone, word, action, result, who):
    with st_block(tone.card + bs.circle), st_zoom(_STEP_ZOOM):
        st_write(bs.step + tone.fg, word, tag=t.div)
        st_write(bs.what, action, tag=t.div)
        st_space("v", "0.6vh")
        st_write(bs.result + tone.fg, result, tag=t.div)
    with st_zoom(_WHO_ZOOM):
        st_write(bs.who, who, tag=t.div)


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'TDD in One Picture', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — TDD in One Picture", entries=_NOTES,
                                 position="left", width="50vw")
        with st_grid(cols='3fr 2fr', gap="2vw",
                     cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
            with g.cell(), st_zoom(_CYCLE_ZOOM), st_grid(cols="1fr 1.2fr 1fr", gap="0",
                                                       cell_styles=s.project.containers.grid_cell_centered) as c:
                for cell in _CYCLE:
                    with c.cell():
                        if cell[0] == "step":
                            _circle(*cell[1:])
                        elif cell[0] == "arrow":
                            with st_zoom(_ARROW_ZOOM):
                                st_write(bs.arrow, cell[1], tag=t.div)
                            with st_zoom(_ARROW_CMD_ZOOM):  # one mention per arrow (NG, 2026-11-25)
                                st_write(bs.arrow_cmd, "npm run test:run", tag=t.div)
                        elif cell[0] == "centre":
                            st_write(bs.what, "TDD", tag=t.div)
            # the list no longer repeats the circles: where, fail for the right reason, what refactor means
            with g.cell(), st_zoom(_TEXT_ZOOM):
                with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body,
                             text_align="left", item_gap=0.8) as l:
                    with l.item():
                        st_write(bs.body, (bs.keyword, 'Where: '), 'tests live in ', (bs.cmd, 'tests/'), '; ',
                                 (bs.keyword, 'Vitest'), ' runs them; ', (bs.cmd, 'npm run test:run'), ' → ✓ / ✗')
                    with l.item():
                        # wrong red vs right red: two real terminal messages (NG, 2026-11-25, option B)
                        st_write(bs.body, (bs.keyword, 'Red for the right reason'), tag=t.div)
                        st_write(bs.body, (bs.wrong, '✗ “ExpenseItem not found”'), ' → wrong red: nothing is checked',
                                 tag=t.div)
                        st_write(bs.body, (bs.right, '✗ “Expected €25.50, got nothing”'), ' → right red: the test '
                                 'checks the behaviour', tag=t.div)
                    with l.item():
                        st_write(bs.body, (bs.keyword, 'Refactor'), ' = change the structure, not the behaviour: '
                                 'remove duplication, extract a function, rename')
