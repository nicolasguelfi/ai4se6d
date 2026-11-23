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
    ("The message",
     "35 minutes to review everything you changed today, triage it, and fix what matters — the whole review "
     "loop on your own code."),
    ("The steps",
     "Back on mywork, see what changed since j2-start; review it with the read-only plan agent; write the "
     "triage in docs/review.md; fix 2-3 HIGH/MEDIUM findings on a fix/review branch, test first; refuse at "
     "least one finding with a written reason."),
    ("The trap",
     "Fixing on mywork directly, or fixing without a failing test first. The fix branch keeps the review "
     "changes separate and easy to read."),
    ("Link to the rest of the day",
     "The fix/review branch is merged into mywork when you ship v0.1 at 16:15."),
    ("Ask the room",
     "« How many lines did you change today? Is one review pass enough for that? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(55):
                st_write(bs.heading, "Exercise — Review Today's Diff", tag=t.div, toc_lvl='1',
                         label='Review Practice (15:15)')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Exercise — Review Today's Diff", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(75):
            st_write(bs.timer, '15:15 → 15:50 · 35 min', tag=t.div)
        with st_zoom(85):
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
            ('Shift+Tab → ', (bs.keyword, 'plan'), ' agent (read-only): run the review prompt'),
            ('Write the triage in ', (bs.cmd, 'docs/review.md')),
            ((bs.cmd, 'git switch -c fix/review'), ': fix 2-3 HIGH/MEDIUM, test first'),
            ('Refuse at least ', (bs.keyword, 'one'), ' finding, with a written reason'),
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(steps), cols, filled=(2, 3))
        with st_zoom(92), st_grid(cols=cols, gap="3vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(steps, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
