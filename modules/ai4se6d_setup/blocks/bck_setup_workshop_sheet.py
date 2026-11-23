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
    ("The message",
     "The contract of the workshop on one slide: the goal, when it is done, the mid-point, what to do if stuck, "
     "and what to bring to the debrief."),
    ("Done when",
     "Three checks anyone can verify: it opens in the browser, it does one thing you wanted, and git log shows "
     "2+ commits."),
    ("Mid-point (14:55)",
     "It opens + 1 commit. Walk around at that time: whoever has nothing running gets help first."),
    ("If stuck",
     "In this order: the tutor window, then rephrase or paste the error to the agent, then raise your hand — "
     "the trainer is the last resort, not the first."),
    ("Debrief (16:15)",
     "Participants bring their notes (notes.md) and one example: what they would have done by hand vs. what "
     "the AI did."),
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
             ("it opens in the browser, does one thing you wanted, and ", (bs.cmd, "git log"), " shows 2+ commits.")),
            ((bs.label, "Mid-point (14:55):"), ("it opens + 1 commit.",)),
            ((bs.label, "If stuck:"),
             ("1. your tutor window  2. rephrase or paste the error to the agent  3. raise your hand.",)),
            ((bs.label, "Debrief (16:15):"), ("your notes + one example.",)),
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
