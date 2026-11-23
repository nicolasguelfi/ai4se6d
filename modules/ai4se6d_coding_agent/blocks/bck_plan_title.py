"""Section title — Technical planning workshop (11:00, 30 min)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Section title styles."""
    section = Style.create(s.project.titles.section_title + s.center_txt, "sec_title")
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "sec_subtitle")
    info = Style.create(s.project.titles.caption + s.center_txt, "sec_info")
    body = s.project.titles.body
    keyword = s.project.titles.keyword
bs = BlockStyles

_NOTES = [
    ("The message",
     "30 minutes to go from a vision to docs/plan.md: the plan that drives the afternoon."),
    ("Timing",
     "Frame 5 min · practice 20 min · debrief 5 min."),
    ("The three steps",
     "Elicit requirements with the plan agent; split them into atomic, testable tasks; commit the plan."),
    ("Link to the morning",
     "Participants reuse what they just practised: plan agent (Shift+Tab), AGENTS.md, @files and Context7."),
    ("Link to the afternoon",
     "The committed plan drives the afternoon: its tasks are what participants build next."),
]


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_zoom(120):
            st_write(bs.info, "11:00 — 30 min · frame 5 · practice 20 · debrief 5", tag=t.div)
        # title and « i » on the same line (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="5% 90% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell():
                pass  # balances the « i » column so the title stays centred
            with h.cell():
                st_write(bs.section, "Workshop: Technical Planning", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Workshop: Technical Planning", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(120):
            st_write(bs.subtitle, "From a vision to docs/plan.md", tag=t.div)
        st_space("v", "4vh")
        with st_zoom(120):
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered, block_align="center",
                         text_align="left", item_gap=0.6) as l:
                with l.item(): st_write(bs.body, "Elicit requirements with the ", (bs.keyword, "plan agent"))
                with l.item(): st_write(bs.body, "Split them into ", (bs.keyword, "atomic, testable tasks"))
                with l.item(): st_write(bs.body, (bs.keyword, "Commit"), " the plan that drives your afternoon")
