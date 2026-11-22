"""Slide — Project structure is your first prompt (before / after)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Before/after styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "ocstr_body")
    bad = Style.create(s.project.titles.subtitle + s.project.colors.critical, "ocstr_bad")
    good = Style.create(s.project.titles.subtitle + s.project.colors.success, "ocstr_good")
    note = s.project.titles.table_cell
bs = BlockStyles

_BEFORE = """\
my-app/
  app.ts
  helpers.ts
  stuff.ts
  test.ts"""

_AFTER = """\
my-app/
  src/routes/auth.routes.ts
  src/services/auth.service.ts
  src/validators/auth.validator.ts
  tests/services/auth.service.test.ts
  docs/architecture.md
  README.md"""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Structure = First Prompt", tag=t.div, toc_lvl="+1")
        st_write(bs.body, "Prompt: \u201cAdd sign-up with email validation.\u201d", tag=t.div)
        with st_grid(cols="repeat(auto-fit, minmax(500px, 1fr))", grid_style=s.project.containers.gap_24) as g:
            with g.cell():
                st_write(bs.bad, "Before: it guesses", tag=t.div)
                st_code(s.none, code=_BEFORE, language="text", line_numbers=False, font_size="22pt")
                st_write(bs.note, "Route? Validation? Tests? Anywhere.", tag=t.div)
            with g.cell():
                st_write(bs.good, "After: it sees the pattern", tag=t.div)
                st_code(s.none, code=_AFTER, language="text", line_numbers=False, font_size="22pt")
                st_write(bs.note, "Right folder, same names, tests mirrored.", tag=t.div)
