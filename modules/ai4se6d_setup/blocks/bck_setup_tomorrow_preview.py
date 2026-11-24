"""Slide — Tomorrow (day 2): CalcApp, git first, you drive the agent with a plan."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Day 2 preview styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    caption = Style.create(s.project.titles.caption + s.center_txt, "setup_tomorrow_caption")
bs = BlockStyles

_NOTES = [
    ("The message",
     "Day 2 in four points: CalcApp, a shared starter project; git first; you drive the agent with your plan; "
     "AI code review with HIGH / MEDIUM / LOW findings."),
    ("What changes",
     "« Same tools, different discipline »: the same opencode loop as today, but with save points, a plan "
     "written before the prompts, and a review before anything is kept."),
    ("Why a shared project",
     "Today everyone built a different app; tomorrow everyone works on CalcApp, so results can be compared and "
     "the debriefs are concrete."),
    ("Practical",
     "No homework — but keep your key (the trainer's Teams message or e-mail): the same key is used tomorrow."),
    ("Ask the room",
     "« After this afternoon, which of the four do you think you need most? »"),
]

_ITEMS = [
    ((bs.keyword, "CalcApp"), " — a shared starter project"),
    ((bs.keyword, "Git first"), " — status, diff, commit, branch"),
    ("You ", (bs.keyword, "drive the agent with your plan")),
    ((bs.keyword, "AI code review"), " — HIGH / MEDIUM / LOW"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Tomorrow — Day 2", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Tomorrow — Day 2", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "4vh")

        # One row per point of day 2, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(_ITEMS), cols, filled=(2,))
        with st_zoom(100):
            with st_grid(cols=cols, gap="6vh 0.5vw", cell_styles=cells) as g:
                for parts in _ITEMS:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.body, *parts, tag=t.div)
                    with g.cell():
                        pass  # right margin
            st_space("v", "7vh")
            st_write(bs.caption, "Same tools, different discipline. No homework — keep your key.", tag=t.div)
