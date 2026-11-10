"""Slide — How every topic works: the 16 CCSET cycles of the week (edition 2)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Cycle map styles."""
    heading = s.project.titles.heading
    steps = Style.create(s.project.titles.body_accent + s.center_txt, "cycles_steps")
    day = Style.create(s.project.titles.table_header + s.center_txt, "cycles_day")
    item = s.project.titles.table_cell
    tool = Style.create(s.project.titles.caption + s.center_txt, "cycles_tool")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "cycles_foot")
    card = Style.create(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md, "cycles_card")
bs = BlockStyles

DAYS = [
    ("Day 1", "by hand", ["01 Generative AI", "02 VibeCoding → VibeEngineering", "03 Tools, AI Act"]),
    ("Day 2", "by hand", ["04 Git", "05 Driving an agent", "06 Planning", "07 Tests", "08 Review, delivery"]),
    ("Day 3", "with GSE-One", ["09 SE concepts, your GenSEM", "10 Requirements elicitation",
                               "11 Non-functional requirements", "12 Verification & validation"]),
    ("Day 4", "with GSE-One", ["13 Measuring quality", "14 Delivery, capitalisation", "15 Framing a project"]),
    ("Day 5", "with GSE-One", ["16 Deployment"]),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(60):
            st_write(bs.heading, "How Every Topic Works", tag=t.div, toc_lvl="+1", label="The 16 cycles")
            st_write(bs.steps, "Theory → How GSE-One solves it → Exercise → Debrief", tag=t.div)
            with st_grid(cols="repeat(auto-fit, minmax(260px, 1fr))", gap="16px", cell_styles=bs.card) as g:
                for day, tool, items in DAYS:
                    with g.cell():
                        st_write(bs.day, day, tag=t.div)
                        st_write(bs.tool, tool, tag=t.div)
                        with st_list(l_style=bs.item, li_style=bs.item, list_type=lt.unordered) as l:
                            for item in items:
                                with l.item():
                                    st_write(bs.item, item)
            st_write(bs.foot, "Days 5-6: your mini-project uses all sixteen.", tag=t.div)
