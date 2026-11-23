"""Title slide — Day 2: Driving a Coding Agent, CalcApp v0.1."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Title slide styles."""
    title = Style.create(
        s.Huge + s.bold + s.center_txt + s.project.colors.primary
        + Style("line-height:1.1;", "calcapp_day_title_lh"),
        "calcapp_day_title",
    )
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "calcapp_day_title_subtitle")
    info = Style.create(s.project.titles.caption + s.center_txt, "calcapp_day_title_info")
    motto = Style.create(s.project.titles.body_accent + s.center_txt, "calcapp_day_title_motto")
bs = BlockStyles

_NOTES = [
    ("The message",
     "Day 2 uses the same tools as day 1 (opencode, the tutor window, GitHub) with a different discipline: the app "
     "is planned, tested, reviewed and delivered."),
    ("The product of the day",
     "CalcApp v0.1 — by 17:00 a tested, reviewed, versioned app, merged and tagged."),
    ("The path",
     "Git first, then driving opencode, technical planning, the build with tests first, code review with AI, "
     "delivery, and the bridge to GSE-One."),
    ("Link to day 1",
     "Yesterday's FreeSelfApp was a naive prototype built fast; today shows what changes when you drive the agent "
     "with intent."),
    ("Ask the room",
     "« Who would ship yesterday's prototype to a customer? »"),
]


def build():
    with st_block(s.project.containers.page_fill_center):
        # the « i » at the top right, on the first line (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell():
                st_write(bs.info, "AI for Software Engineering — Day 2", tag=t.div)
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Driving a Coding Agent", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "16vh")
        with st_block(s.center_txt), st_zoom(110):
            st_write(
                bs.title, "Driving a Coding Agent", tag=t.div, toc_lvl="1",
                label="Day 2 — Driving a Coding Agent",
            )
            st_space("v", "8vh")
            st_write(bs.subtitle, "CalcApp v0.1 — planned, tested, reviewed, delivered", tag=t.div)
            st_space("v", "14vh")
            st_write(bs.motto, "Same tools as yesterday. A different discipline.", tag=t.div)
