"""Slide — Project structure is your first prompt (before / after)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


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

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Compare the flat and the structured project; learners see the structured"
     " CalcApp starter in Try it 1."),
    ("The message",
     "Before any prompt, the agent reads your folders and file names. The project structure is the first prompt "
     "it receives."),
    ("Before",
     "Same request, « Add sign-up with email validation », in a flat project (app.ts, helpers.ts, stuff.ts): "
     "the agent has to guess where the route, the validation and the tests go. Anywhere is possible."),
    ("After",
     "With routes/, services/, validators/ and tests/ mirroring src/, the agent sees the pattern: right folder, "
     "same names, tests mirrored. docs/architecture.md and README.md tell it the rest."),
    ("The trap",
     "Thinking structure is cosmetic. For an agent it decides where new code lands and whether tests follow."),
    ("What comes next",
     "Five habits for an AI-friendly project, then AGENTS.md: the rules the agent reads at every start."),
    ("Ask the room",
     "« In your current project, where would an agent put a new validator? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Structure = First Prompt", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Structure = First Prompt", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(122):
            st_write(bs.body, "Prompt: “Add sign-up with email validation.”", tag=t.div)
        st_space("v", "4vh")
        with st_zoom(116), st_grid(cols="5% 0.9fr 1.6fr 5%", gap="2vw") as g:
            with g.cell():
                pass  # left margin
            with g.cell():
                st_write(bs.bad, "Before: it guesses", tag=t.div)
                st_code(s.none, code=_BEFORE, language="text", line_numbers=False, font_size="30pt")
                st_write(bs.note, "Route? Validation? Tests? Anywhere.", tag=t.div)
            with g.cell():
                st_write(bs.good, "After: it sees the pattern", tag=t.div)
                st_code(s.none, code=_AFTER, language="text", line_numbers=False, font_size="30pt")
                st_write(bs.note, "Right folder, same names, tests mirrored.", tag=t.div)
            with g.cell():
                pass  # right margin
