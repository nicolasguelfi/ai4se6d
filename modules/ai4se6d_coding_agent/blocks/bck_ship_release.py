"""Slide — Exercise — ship v0.1 (merge, tag, then main takes mywork)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Exercise — ship v0.1 (merge and tag) — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "ship_release_body")
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "ship_release_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "ship_release_timer")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "ship_release_done")
bs = BlockStyles

_CODE_ZOOM = 112  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)

# Text left-aligned (NG, 2026-11-23: same recipes as the intro module)
_left = Style("text-align:left;", "ship_release_left")

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Exercise 16:15 → 16:30: merge, run the tests, tag v0.1, move "
     "main; wait until all see v0.1 in git tag."),
    ("The message",
     "15 minutes to ship v0.1: all the green work on your main line, tagged v0.1."),
    ("The commands",
     "On mywork, merge fix/review (and any finished feat/ branch), run the tests — fix before tagging if one is "
     "red —, tag v0.1, then move main onto mywork with git switch -C main mywork."),
    ("Why main",
     "From tomorrow, the methodology plugin treats main as the reference. Until now main held only the starter."),
    ("The expected warning",
     "Git says main and origin/main have diverged. That is normal: origin is the starter. Do not pull; you push "
     "to your own repository tomorrow morning."),
    ("If stuck",
     "Tutor window first; else the recovery tag j2-v0.1, then git tag v0.1 on it; else raise your hand."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git switch mywork",
     "Moves you onto the existing branch mywork (your main line since this morning): the files in the folder "
     "become mywork's version. Git refuses if uncommitted changes would be lost: commit first (git status shows "
     "them)."),
    ("Command — git merge fix/review",
     "Brings the commits of branch fix/review into the branch you are on (mywork). If mywork has not moved "
     "meanwhile, git just moves it forward (« Fast-forward »). Otherwise it creates a merge commit and may open a"
     " text editor for its message: save and close it (nano: Ctrl+O, Enter, Ctrl+X; vim: Esc then :wq). « "
     "CONFLICT » = both branches changed the same lines: raise your hand."),
    ("Symbol — # (comment)",
     "Everything after # on a line is a comment for you, ignored by the terminal."),
    ("Command — npm run test:run",
     "Runs all the tests once with Vitest (script « vitest run » of package.json) and gives the prompt back; "
     "green = all pass, red = at least one fails. npm test would stay in watch mode in your terminal (q quits)."),
    ("Command — git tag v0.1",
     "Puts the label v0.1 on the commit you are on (the tip of mywork after the merge). A tag never moves, unlike"
     " a branch. git tag alone lists the tags. Wrong commit? git tag -d v0.1 deletes it, then tag again."),
    ("Command — git switch -C main mywork",
     "-C = create the branch main, or if it already exists (it does: it held the starter) reset it, so that it "
     "points to the same commit as mywork; then switch to it. main's old position is dropped — nothing of yours "
     "is lost, it was only the starter. Without capital C (-c) git refuses because main exists."),
    ("Command — git log --oneline --graph --decorate -10",
     "Shows the history. --oneline = one line per commit; --graph = lines on the left drawing the branches and "
     "merges; --decorate = shows branch and tag names next to their commit, e.g. (HEAD -> main, tag: v0.1, "
     "mywork); -10 = the last 10 commits only. HEAD -> main = you are on main."),
    ("Command — git tag / git branch -v",
     "git tag lists all tags (alphabetical): v0.1 must be there, next to the course tags. git branch -v lists "
     "your local branches with each one's last commit (short id + message); * marks the current branch. main and "
     "mywork must show the same id."),
    ("Message — « main and origin/main have diverged »",
     "origin = the GitHub project you cloned (the starter); origin/main = its main as last seen. Your main now "
     "has commits it lacks, and the other way round: expected. Do not run git pull."),
]


_SHIP = """\
git switch mywork
git merge fix/review          # + any finished feat/ branch not merged yet
npm run test:run              # all green? if not, fix before tagging
git tag v0.1
git switch -C main mywork     # main = your v0.1 (it held only the starter)
git log --oneline --graph --decorate -10"""


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Exercise — Ship v0.1', tag=t.div, toc_lvl='1', label='Ship v0.1 (16:15)')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Exercise — Ship v0.1", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(69):
            st_write(bs.timer, '16:15 → 16:30 · 15 min', tag=t.div)
        with st_zoom(78), st_block(_left):
            st_write(
                bs.body,
                (bs.label, 'Goal: '),
                'all green work on your main line, tagged ',
                (bs.cmd, 'v0.1'),
                '.',
                tag=t.div,
            )
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_SHIP, language='bash', line_numbers=False, font_size="36pt")
            st_write(
                bs.body,
                (bs.label, 'Why main: '),
                'from tomorrow, the methodology plugin treats ',
                (bs.cmd, 'main'),
                ' as the reference. Git says main and origin/main have diverged: normal, do not pull'
                ' (origin is the starter); you push to your own repository tomorrow morning.',
                tag=t.div,
            )
            with st_block(bs.done_box):
                st_write(
                    bs.body,
                    (bs.done_label, 'Done when: '),
                    (bs.cmd, 'git tag'),
                    ' lists ',
                    (bs.cmd, 'v0.1'),
                    ', on a commit where the tests are green, and ',
                    (bs.cmd, 'main'),
                    ' is on that same commit (',
                    (bs.cmd, 'git branch -v'),
                    ').',
                )
            st_write(
                bs.body,
                (bs.label, 'If stuck: '),
                '1. ',
                'your tutor window',
                '  2. tag ',
                (bs.cmd, 'j2-v0.1'),
                ', then ',
                (bs.cmd, 'git tag v0.1'),
                ' on it  3. raise your hand',
                tag=t.div,
            )
