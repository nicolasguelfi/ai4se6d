"""Slide — Task — minimal UI (10 minutes max)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Task — minimal UI (10 minutes max) — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_ui_body")
    keyword = s.bold + s.project.colors.highlight
    timer = Style.create(s.project.titles.stat + s.center_txt, "tasks_ui_timer")
bs = BlockStyles

_CODE_ZOOM = 104  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)


_UI = """\
Add minimal plain CSS in src/App.css: horizontal nav bar, Dashboard
list (description, category, amount, date) with a total, labelled
form fields with spacing, centred layout with a max-width.
No animations, no CSS library. Keep all tests green."""

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Show the one CSS prompt and its 10-min cap; learners run it as "
     "the last task of the 13:30 exercise."),
    ("The message",
     "The last task of Part 2, capped at 10 minutes: plain CSS so that the app is readable and functional — "
     "not production-ready."),
    ("One prompt, no RED",
     "Pure styling has no test: here the rule is that all existing tests stay green after the change."),
    ("The prompt's limits",
     "One file (src/App.css), a short list of what to style, and explicit exclusions: no animations, no CSS "
     "library."),
    ("The trap",
     "Polishing the look for half an hour: the time box protects the review section at 14:30."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Prompt — minimal UI",
     "Plain CSS (no framework) in one file, src/App.css: a horizontal nav bar, the Dashboard list (description, "
     "category, amount, date) with a total, labelled form fields with spacing, a centred layout with a max-width "
     "(the content stops growing on wide screens). « No animations, no CSS library » forbids extras; « Keep all "
     "tests green » = run npm run test:run after the change."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Task: Minimal UI', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Task: Minimal UI", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(116):
            st_write(bs.timer, '10 min max', tag=t.div)
            st_space("v", "2vh")
            st_write(
                bs.body,
                'Target: ',
                (bs.keyword, 'readable and functional'),
                ', not production-ready.',
                tag=t.div,
            )
            st_space("v", "2vh")
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_UI, language='text', line_numbers=False, font_size="36pt")
            st_space("v", "2vh")
            st_write(
                bs.body,
                'Pure styling has no test: the rule is ',
                (bs.keyword, 'the tests stay green'),
                '.',
                tag=t.div,
            )
