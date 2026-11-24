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

_CODE_ZOOM = 118  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)

_STEPS = """\
git clone https://github.com/nicolasguelfi/calcapp-starter ~/ai4se/calcapp
cd ~/ai4se/calcapp && git checkout -b mywork j2-start && npm ci
npm run test:run            # all green?
git switch -c feat/hello
# change one line of README.md, then:
git status && git diff
git add README.md && git commit -m "docs: say hello"
# break a file in src/ on purpose, look at git diff, then:
BROKEN=src/App.tsx          # the file you broke
git restore "$BROKEN" && npm run test:run"""


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
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git clone (address) ~/ai4se/calcapp",
     "Copies the CalcApp starter from GitHub onto your machine, with its history and tags. First argument: the "
     "project address. Second: the folder to create, ~/ai4se/calcapp (~ = your home folder); it must not exist "
     "yet, otherwise git refuses."),
    ("Command — cd ~/ai4se/calcapp && git checkout -b mywork j2-start && npm ci",
     "cd = change directory, into the project. && = run the next command only if the previous one succeeded. git "
     "checkout -b mywork j2-start creates the branch mywork starting at the tag j2-start (-b = create the branch) "
     "and moves onto it. npm ci installs the libraries exactly as in package-lock.json (ci = clean install)."),
    ("Command — npm run test:run",
     "Runs the script named test:run in package.json; in the starter it is vitest run: all tests, once, then stop."
     " Green ✓ = pass, red ✗ = fail. (npm test would start Vitest in watch mode, which keeps running: q to quit.)"),
    ("Command — git switch -c feat/hello",
     "Creates the branch feat/hello from where you are (mywork) and moves onto it. -c = create."),
    ("Command — git status && git diff",
     "git status lists the changed files; then, if it worked, git diff shows the changed lines (- removed, + "
     "added; q to quit)."),
    ("Command — git add README.md && git commit -m \"docs: say hello\"",
     "Stages README.md only, then saves it as a commit. -m = the message in quotes; « docs: » = a documentation "
     "change. If Git asks who you are, see the next slide (git config)."),
    ("Command — BROKEN=src/App.tsx",
     "Not a git command: stores the path of the file you broke in a variable named BROKEN (this terminal only). "
     "Replace src/App.tsx by the file you actually broke. No spaces around =."),
    ("Command — git restore \"$BROKEN\" && npm run test:run",
     "$BROKEN is replaced by the stored path; the quotes keep it as one word. git restore puts that file back to "
     "its last committed version (your break is thrown away), then the tests run again: green."),
    ("Symbol — #",
     "Starts a comment: the shell ignores the rest of the line. Not typed."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Try it: Git on CalcApp", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Try it: Git on CalcApp", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")
        with st_zoom(120):
            st_write(bs.timer, "15 min — in a terminal", tag=t.div)
            st_write(
                bs.body,
                (bs.label, "Goal: "),
                "commit on a branch, break, restore.",
                tag=t.div,
            )
        st_space("v", "7vh")
        with st_zoom(120):
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_STEPS, language="bash", line_numbers=False, font_size="24pt")
