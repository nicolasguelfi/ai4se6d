"""Slide — Exercise sheet — review today's diff (goal and steps)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_ask_opencode, st_hover_tooltip


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

_STEP_ZOOM = 80    # tuned by measure: content bottom <= 1000 px at 1920x1080
_PROMPT_ZOOM = 68   # the « Or ask opencode » line: smaller than the step it replaces

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
    ("Or ask opencode",
     "Under steps 1 and 4, the same thing asked to opencode — build agent (step 2 is the plan agent: switch back "
     "with Shift+Tab before step 4). It shows the commands, then runs them. Git specialists can skip these lines."),
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
     "Switches the primary agent: build (edits files, runs commands) ↔ plan (reads and proposes; it"
     " cannot edit your project files). Tab does the same in the "
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
        st_space("v", "2vh")

        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23); under a step with a
        # terminal command, the same thing asked to opencode — build agent (NG, 2026-11-25)
        steps = [
            (((bs.cmd, 'git switch mywork'), ' → ', (bs.cmd, 'git diff j2-start --stat')),
             "Give me the git commands to go back to mywork and show how much changed since j2-start, then run them."),
            (('Shift+Tab → ', (bs.keyword, 'plan'), ' agent (no file edits): run the review prompt'), None),
            (('Write the triage in ', (bs.cmd, 'docs/review.md'), ' (your editor, or ', (bs.keyword, 'Shift+Tab → build'),
              ')'),
             "Write the findings above to docs/review.md, one line each: RVW-n, severity, file, problem, then my "
             "decision FIX / DEFER / REFUSED and its reason (ask me for them)."),
            (((bs.cmd, 'git switch -c fix/review'), ': fix 2-3 HIGH/MEDIUM, test first'),
             "Give me the git command to create and switch to the branch fix/review, then run it."),
            (('Refuse at least ', (bs.keyword, 'one'), ' finding, with a written reason'), None),
        ]
        cols = "5% 5% 85% 5%"
        for i, (parts, prompt) in enumerate(steps):
            if i:
                st_space("v", "0.8vh")
            cells = s.project.containers.rows(i + 1, cols, filled=(2, 3))[-4:]  # keeps the alternation
            with st_zoom(_STEP_ZOOM), st_grid(cols=cols, gap="0 0.5vw", cell_styles=cells) as g:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{i + 1}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
            if prompt:
                st_space("v", "0.4vh")
                st_ask_opencode(prompt, zoom=_PROMPT_ZOOM, cols="5% 90% 5%")
