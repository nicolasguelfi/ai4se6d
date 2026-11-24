"""Slide — FreeSelfApp exercise sheet: done when, mid-point, if stuck, debrief."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Workshop exercise sheet styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    done_label = Style.create(s.project.titles.label + s.project.colors.success, "setup_done_label_lbl")
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Read and comment — 1 min, while learners build. Point out « Done when », the mid-point and the stuck "
     "order; then walk around the room."),
    ("The message",
     "The contract of the workshop on one slide: the goal, when it is done, the mid-point, what to do if stuck, "
     "and when you present."),
    ("Done when",
     "Three checks anyone can verify: v1 and the client's feature run, git log shows 2+ commits, the presentation "
     "opens in the browser."),
    ("14:45 — the client's feature",
     "v1 runs + 1 commit. Walk around at that time: whoever has nothing running gets help first. Then announce the "
     "client's feature (see « Iteration 2 »)."),
    ("If stuck",
     "In this order: the tutor window, then rephrase or paste the error to the agent, then raise your hand — "
     "the trainer is the last resort, not the first."),
    ("15:30 — presentations",
     "6 min each on Google Meet, no questions; all questions at 16:30, where notes.md gives each one a concrete "
     "example."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git log",
     "Lists the commits of the current branch, newest first: an identifier (hash), author, date and message for each. "
     "2+ commits = 2+ entries. If the list is long, it stops with « : » at the bottom: arrows to scroll, q to quit. "
     "Shorter: git log --oneline = one line per commit."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Exercise Sheet", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Exercise Sheet", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        rows = [
            ((bs.label, "Goal:"), ("your small web app, by prompting only.",)),
            ((bs.done_label, "Done when:"),
             ("v1 and the client's feature both run, ", (bs.cmd, "git log"), " shows 2+ commits, and your presentation opens in the browser.")),
            ((bs.label, "14:45:"), ("v1 runs + 1 commit — then the client's feature.",)),
            ((bs.label, "If stuck:"),
             ("1. your tutor window  2. rephrase or paste the error to the agent  3. raise your hand.",)),
            ((bs.label, "15:30:"), ("you present 6 min, sharing your screen on Google Meet.",)),
        ]
        # One row per item of the sheet, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 30% 60% 5%"
        cells = s.project.containers.rows(len(rows), cols, filled=(2, 3))
        with st_zoom(90), st_grid(cols=cols, gap="4vh 0.5vw", cell_styles=cells) as g:
            for label, text in rows:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, label, tag=t.div)
                with g.cell():
                    st_write(bs.body, *text, tag=t.div)
                with g.cell():
                    pass  # right margin
