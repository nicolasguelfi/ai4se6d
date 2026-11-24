"""Slide — Task — routing and navigation (prompts)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Task — routing and navigation (prompts) — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_routing_body")
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_routing_cmd")
bs = BlockStyles

_CODE_ZOOM = 99  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)


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

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Show the RED and GREEN prompts; learners use them in the 13:30 "
     "exercise when their plan's wording is unclear."),
    ("The message",
     "The first task of Part 2: two pages, / (Dashboard) and /add (Add Expense), with the two prompts of the "
     "loop ready to copy — RED first, then GREEN."),
    ("The RED prompt",
     "A test only, in tests/App.test.tsx: it renders the exported routes in a memory router, expects the two "
     "links, and a second test starts directly at /add."),
    ("The GREEN prompt",
     "Precise constraints the agent would not guess: react-router, NOT react-router-dom; routes exported from "
     "src/App.tsx; one file per page in src/pages/; « Do not modify the test »."),
    ("Why export routes",
     "The test can then mount the same routes in a memory router, while the app keeps createBrowserRouter."),
    ("Link",
     "The next slide is the review checklist for exactly these constraints."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Task: Routing & Navigation', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Task: Routing & Navigation", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(98):
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
            st_space("v", "1vh")
            st_write(bs.label, 'RED', tag=t.div)
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_ROUTING_RED, language='text', line_numbers=False, font_size="36pt")
            st_write(bs.label, 'GREEN', tag=t.div)
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_ROUTING_GREEN, language='text', line_numbers=False, font_size="36pt")
