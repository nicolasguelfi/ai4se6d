"""Slide — Testing rules in AGENTS.md before coding."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Testing rules in AGENTS.md before coding — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_agents_md_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "build_agents_md_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "build_agents_md_foot")
bs = BlockStyles


_RULES = """\
## Testing rules
- Write the test file BEFORE the implementation file
- Vitest + React Testing Library; tests go in tests/
- Use fireEvent from @testing-library/react
- Import from react-router (NOT react-router-dom)
- Never install Jest; never skip, weaken or delete a test
- Run tests with `npm run test:run` (never watch mode)"""

_NOTES = [
    ("The message",
     "opencode reads AGENTS.md in every session: the testing rules written there apply to every prompt, "
     "without repeating them."),
    ("What the rules fix",
     "Test file before implementation; the tools of the project (Vitest + React Testing Library, tests in "
     "tests/, fireEvent, react-router not react-router-dom); never install Jest; never skip, weaken or delete "
     "a test."),
    ("Why npm run test:run",
     "npm test is watch mode: it never ends, and the agent would wait. test:run runs once."),
    ("Link to this morning",
     "Same mechanism as the AGENTS.md rules of the opencode part: the project's memory for the agent."),
    ("Action",
     "Missing? Add it, then commit: docs: testing rules."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'Testing Rules in AGENTS.md', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Testing Rules in AGENTS.md", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(110):
            st_write(
                bs.body,
                'opencode reads ',
                (bs.cmd, 'AGENTS.md'),
                ' in every session. Check that it contains:',
                tag=t.div,
            )
        st_space("v", "2vh")
        st_code(s.none, code=_RULES, language='markdown', line_numbers=False, font_size="38pt")
        st_space("v", "3vh")
        with st_zoom(110):
            st_write(bs.foot, 'Missing? Add it, then commit: docs: testing rules.', tag=t.div)
