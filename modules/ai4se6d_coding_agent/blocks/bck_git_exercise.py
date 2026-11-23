"""Slide — Try it: Git on the CalcApp starter (steps)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Exercise steps styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    label = s.project.titles.label
    timer = Style.create(s.project.titles.stat + s.center_txt, "git_ex_timer")
bs = BlockStyles

_STEPS = """\
git clone https://github.com/nicolasguelfi/calcapp-starter ~/ai4se/calcapp
cd ~/ai4se/calcapp && git checkout -b mywork j2-start && npm ci
npm run test:run            # all green?
git switch -c feat/hello
# change one line of README.md, then:
git status && git diff
git add README.md && git commit -m "docs: say hello"
# break a file in src/ on purpose, look at git diff, then:
git restore <that-file> && npm run test:run"""


_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine, 15 min in a terminal. Everyone clones the starter, commits on feat/hello,"
     " breaks a file and restores it; walk around."),
    ("The message",
     "15 minutes in a terminal: commit on a branch, break a file, restore it."),
    ("Steps",
     "Clone the starter, git checkout -b mywork j2-start, npm ci, run the tests, create feat/hello, change one line "
     "of README.md, check status and diff, commit."),
    ("The point",
     "Break a file in src/ on purpose, look at git diff, then git restore it and run the tests again: green."),
    ("Watch for",
     "Participants who skip git diff before git add: the review reflex is the goal of the exercise."),
    ("If stuck",
     "Tutor window, then a fresh clone at j2-start in a new folder, then a raised hand (next slide)."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(70):
                st_write(bs.heading, "Try it: Git on CalcApp", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Try it: Git on CalcApp", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")
        with st_zoom(110):
            st_write(bs.timer, "15 min — in a terminal", tag=t.div)
            st_write(
                bs.body,
                (bs.label, "Goal: "),
                "commit on a branch, break, restore.",
                tag=t.div,
            )
        st_space("v", "7vh")
        with st_zoom(120):
            st_code(s.none, code=_STEPS, language="bash", line_numbers=False, font_size="24pt")
