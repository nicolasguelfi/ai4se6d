"""Slide — Task — minimal UI (10 minutes max)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Task — minimal UI (10 minutes max) — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_ui_body")
    keyword = s.bold + s.project.colors.highlight
    timer = Style.create(s.project.titles.stat + s.center_txt, "tasks_ui_timer")
bs = BlockStyles


_UI = """\
Add minimal plain CSS in src/App.css: horizontal nav bar, Dashboard
list (description, category, amount, date) with a total, labelled
form fields with spacing, centred layout with a max-width.
No animations, no CSS library. Keep all tests green."""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Task: Minimal UI', tag=t.div, toc_lvl='+1')
            st_write(bs.timer, '10 min max', tag=t.div)
            st_write(
                bs.body,
                'Target: ',
                (bs.keyword, 'readable and functional'),
                ', not production-ready.',
                tag=t.div,
            )
            st_code(s.none, code=_UI, language='text', line_numbers=False, font_size="36pt")
            st_write(
                bs.body,
                'Pure styling has no test: the rule is ',
                (bs.keyword, 'the tests stay green'),
                '.',
                tag=t.div,
            )
