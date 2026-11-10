"""Slide — Testing rules in AGENTS.md before coding."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


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


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Testing Rules in AGENTS.md', tag=t.div, toc_lvl='+1')
            st_write(
                bs.body,
                'opencode reads ',
                (bs.cmd, 'AGENTS.md'),
                ' in every session. Check that it contains:',
                tag=t.div,
            )
            st_code(s.none, code=_RULES, language='markdown', line_numbers=False, font_size="36pt")
            st_write(bs.foot, 'Missing? Add it, then commit: docs: testing rules.', tag=t.div)
