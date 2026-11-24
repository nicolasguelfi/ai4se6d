"""Slide — Exercise sheet — review today's diff (goal and steps)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Exercise sheet — review today's diff — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_ex_steps_body")
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "review_ex_steps_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "review_ex_steps_timer")
    number = Style.create(s.bold + s.project.colors.highlight + s.center_txt, "review_ex_steps_num")
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Exercise 15:15 → 15:50: review today's diff, triage it, fix 2-3 "
     "findings test first; leave this slide on screen while they work."),
    ("The message",
     "35 minutes to review everything you changed today, triage it, and fix what matters — the whole review "
     "loop on your own code."),
    ("The steps",
     "Back on mywork, see what changed since j2-start; review it with the plan agent (it explores, it does not edit your files); write the "
     "triage in docs/review.md; fix 2-3 HIGH/MEDIUM findings on a fix/review branch, test first; refuse at "
     "least one finding with a written reason."),
    ("The trap",
     "Fixing on mywork directly, or fixing without a failing test first. The fix branch keeps the review "
     "changes separate and easy to read."),
    ("Link to the rest of the day",
     "The fix/review branch is merged into mywork when you ship v0.1 at 16:15."),
    ("Ask the room",
     "« How many lines did you change today? Is one review pass enough for that? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git switch mywork",
     "Moves you onto the existing branch mywork (your main line since this morning): the files in the folder "
     "become mywork's version. Git refuses if uncommitted changes would be lost: commit first (git status shows "
     "them)."),
    ("Command — git diff j2-start --stat",
     "Compares your files now with the tag j2-start (start of the day). --stat = a summary only: one line per "
     "changed file with its count of changed lines, and a total. New files never added with git add are not "
     "counted."),
    ("Key — Shift+Tab (in opencode)",
     "Switches the primary agent: build (edits files, runs commands) ↔ plan (explores and proposes; by default it"
     " asks before any file edit or shell command, so it does not change your project). Tab does the same in the "
     "other direction; with two agents both just toggle. The current agent's name is shown under the input box."),
    ("File — docs/review.md",
     "Create it in the editor (or ask the build agent after the review): one line per finding, RVW-n, severity, "
     "file, decision (fix / defer / refuse + reason), as on the « You Are the Judge » slide."),
    ("Command — git switch -c fix/review",
     "Creates a new branch named fix/review and moves onto it. A branch is a named line of commits: work on it "
     "does not touch the other branches. -c = create; the branch starts from the commit you are on, so be on "
     "mywork first. The prefix before the slash is only a naming habit (feat/ = feature, fix/ = correction). « "
     "already exists »? Use git switch fix/review (without -c)."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Exercise — Review Today's Diff", tag=t.div, toc_lvl='1',
                         label='Review Practice (15:15)')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Exercise — Review Today's Diff", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(82):
            st_write(bs.timer, '15:15 → 15:50 · 35 min', tag=t.div)
        with st_zoom(93):
            st_write(
                bs.body,
                (bs.label, 'Goal: '),
                'review everything you changed today, triage it, fix what matters.',
                tag=t.div,
            )
        st_space("v", "3vh")

        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        steps = [
            ((bs.cmd, 'git switch mywork'), ' → ', (bs.cmd, 'git diff j2-start --stat')),
            ('Shift+Tab → ', (bs.keyword, 'plan'), ' agent (no file edits): run the review prompt'),
            ('Write the triage in ', (bs.cmd, 'docs/review.md')),
            ((bs.cmd, 'git switch -c fix/review'), ': fix 2-3 HIGH/MEDIUM, test first'),
            ('Refuse at least ', (bs.keyword, 'one'), ' finding, with a written reason'),
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(steps), cols, filled=(2, 3))
        with st_zoom(101), st_grid(cols=cols, gap="3vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(steps, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
