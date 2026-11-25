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

_CODE_ZOOM = 96  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)


_RULES = """\
## Testing rules
- Write the test BEFORE the implementation (an empty shell next to the test is fine)
- Vitest + React Testing Library; tests go in tests/
- Use fireEvent from @testing-library/react
- Import from react-router (NOT react-router-dom)
- Never install Jest; never skip, weaken or delete a test
- Run tests with `npm run test:run` (never watch mode)"""

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. 2 min: everyone opens AGENTS.md, checks the six testing rules, "
     "adds the missing ones and commits « docs: testing rules » before the 11:45 exercise."),
    ("The message",
     "opencode reads AGENTS.md in every session: the testing rules written there apply to every prompt, "
     "without repeating them."),
    ("What the rules fix",
     "Test before implementation — an empty shell next to the test is allowed, so red fails on the expected "
     "value, not on a missing file (see the live demo); the tools of the project (Vitest + React Testing Library, tests in "
     "tests/, fireEvent, react-router not react-router-dom); never install Jest; never skip, weaken or delete "
     "a test."),
    ("Why npm run test:run",
     "npm test is watch mode: it never ends, and the agent would wait. test:run runs once."),
    ("Link to this morning",
     "Same mechanism as the AGENTS.md rules of the opencode part: the project's memory for the agent."),
    ("Action",
     "Missing? Add it, then commit: docs: testing rules."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("File — AGENTS.md (Markdown)",
     "A text file at the root of the project that opencode adds to every session (/init drafts one). ## Testing "
     "rules = a level-2 title; each line starting with - is a bullet; text between backticks (`npm run test:run`)"
     " is shown as code. Edit it in any editor, then git add AGENTS.md && git commit -m \"docs: testing rules\"."),
    ("Words — Vitest, React Testing Library, fireEvent, tests/",
     "Vitest = the test runner of this Vite project (it finds and runs the *.test.tsx files). React Testing "
     "Library = renders a component in a fake browser and finds elements as a user would (by text, label, role). "
     "fireEvent = its function to simulate a click or a typing. tests/ = the folder where the test files go."),
    ("Words — react-router vs react-router-dom; Jest",
     "react-router is the routing library already in package.json (version 7); since v7 everything is imported "
     "from « react-router », react-router-dom is an older name the agent often reaches for. Jest is another test "
     "runner: installing it next to Vitest creates two competing setups."),
    ("Words — « never watch mode »",
     "npm test = vitest, which in a terminal stays in watch mode (waits and re-runs at every save; q quits). npm "
     "run test:run = vitest run: one pass, then it stops — what you want from an agent and in a check."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Testing Rules in AGENTS.md', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Testing Rules in AGENTS.md", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(120):
            st_write(
                bs.body,
                'opencode reads ',
                (bs.cmd, 'AGENTS.md'),
                ' in every session. Check that it contains:',
                tag=t.div,
            )
        st_space("v", "2vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_RULES, language='markdown', line_numbers=False, font_size="38pt")
        st_space("v", "3vh")
        with st_zoom(120):
            st_write(bs.foot, 'Missing? Add it, then commit: docs: testing rules.', tag=t.div)
