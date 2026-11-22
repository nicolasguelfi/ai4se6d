"""Slide — Task — routing and navigation (prompts)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Task — routing and navigation (prompts) — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_routing_body")
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_routing_cmd")
bs = BlockStyles


_ROUTING_RED = """\
Write a failing test in tests/App.test.tsx: render `routes` from
src/App.tsx with createMemoryRouter + RouterProvider; expect links
"Dashboard" and "Add Expense". A second test starts at "/add"
(initialEntries) and expects a heading "Add Expense". Test only."""

_ROUTING_GREEN = """\
Make it pass with react-router (NOT react-router-dom): export `routes`
from src/App.tsx (Layout with nav Links + Outlet; "/" Dashboard,
"/add" AddExpense); App keeps createBrowserRouter(routes).
One file per page in src/pages/. Do not modify the test."""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Task: Routing & Navigation', tag=t.div, toc_lvl='+1')
            st_write(
                bs.body,
                'Two pages: ',
                (bs.cmd, '/'),
                ' → ',
                (bs.keyword, 'Dashboard'),
                ' (expenses + total), ',
                (bs.cmd, '/add'),
                ' → ',
                (bs.keyword, 'Add Expense'),
                ' (the form).',
                tag=t.div,
            )
            st_write(bs.label, 'RED', tag=t.div)
            st_code(s.none, code=_ROUTING_RED, language='text', line_numbers=False, font_size="36pt")
            st_write(bs.label, 'GREEN', tag=t.div)
            st_code(s.none, code=_ROUTING_GREEN, language='text', line_numbers=False, font_size="36pt")
