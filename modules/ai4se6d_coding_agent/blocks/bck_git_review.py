"""Slide — Pattern 1: review before stage."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Review-before-stage styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    number = Style.create(s.project.titles.body + s.bold + s.project.colors.highlight, "gitrev_number")
    closing = Style.create(s.project.titles.body_accent + s.center_txt, "gitrev_closing")
bs = BlockStyles

_STEPS = [
    ((bs.keyword, "git status"), " — which files did the agent touch?"),
    ((bs.keyword, "git diff --stat"), " — how many lines, in which files? As expected?"),
    ((bs.keyword, "git diff"), " — read what is small or risky"),
    ((bs.keyword, "git add src/App.tsx"), " — only what you approve"),
    ((bs.keyword, "git diff --staged"), " — last look"),
    ((bs.keyword, "git commit"), " — a message that says what and why"),
]

_NOTES = [
    ("The message",
     "First habit of the day: nothing the agent wrote goes into a commit before you have checked it. You own every "
     "change — you check its scope first, then read what matters."),
    ("The five steps",
     "git status (which files), git diff --stat (how much, where), git diff (read), git add src/App.tsx (one file, e.g.: only what you approve), "
     "git diff --staged (last look), git commit (what and why)."),
    ("The key steps",
     "Steps 2 and 3. --stat is the scope check: a 3-line task that touched 40 files, or a test file changed, is a "
     "red flag before reading anything. Then git diff: today the tasks are small, so read all of it; on a big change, "
     "read the risky parts (security, data, money, configuration, tests) — the rest is checked by tests and, this "
     "afternoon, by an AI review (slide « Too Big to Read Every Line? » at the end of this section)."),
    ("Command — git diff --stat",
     "Summary of git diff: one line per changed file with the number of lines added (+) and removed (-), then a "
     "total. --stat = statistics only, no content. Works on big changes too: the first thing to read."),
    ("The trap",
     "Committing what you never looked at. After the agent worked: git add . is fine — then read git diff "
     "--staged --stat before you commit (new files included); git restore --staged (file) takes a file back out."),
    ("Link to the afternoon",
     "The code review session (14:30) builds on the same reflex, with the AI helping to read the diff."),
    ("Ask the room",
     "« What would you do if git status shows a file you did not expect? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git status",
     "Lists the files that changed: « Changes to be committed » (staged, green), « Changes not staged » (modified,"
     " red) and « Untracked files » (new files Git does not follow yet). It changes nothing: run it as often as "
     "you like. « nothing to commit, working tree clean » = everything is committed."),
    ("Command — git diff",
     "Shows, line by line, what changed in your files since the last commit and that is not staged yet: lines "
     "starting with - (red) were removed, lines with + (green) were added. Nothing is modified. Long output opens "
     "in a viewer: arrows to scroll, q to quit. Trap: a brand-new file (« untracked ») does not appear."),
    ("Command — git add src/App.tsx",
     "Puts the current content of that file into the staging area: it will be part of the next commit. Argument = "
     "the file to stage (path from the project folder); you can list several files. Edit the file again after git "
     "add? Run git add again, or the new edit is not included."),
    ("Command — git diff --staged",
     "Same as git diff, but shows what is already staged, i.e. exactly what git commit will save. --staged (same "
     "as --cached) = compare the staging area with the last commit. Only way to see a new file before committing "
     "it."),
    ("Command — git commit",
     "Saves the staged changes as a commit. Without -m, Git opens a text editor (often nano or vim) for the "
     "message: write it, save, close. In vim: press i to type, then Esc, :wq and Enter. Quicker: git commit -m "
     "\"fix(list): round the total\"."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "1 · Review Before Stage", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Review Before Stage", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        # one numbered row per step, alternating fills — motif L2 + fonds f1 (margins 5 %, numbering column)
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(_STEPS), cols, filled=(2, 3))
        with st_zoom(96), st_grid(cols=cols, gap="2vh 0.5vw", cell_styles=cells) as g:
            for n, step in enumerate(_STEPS, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *step, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "4vh")
        with st_zoom(115):
            st_write(bs.closing, "You own every change: check its scope, read what matters.", tag=t.div)
