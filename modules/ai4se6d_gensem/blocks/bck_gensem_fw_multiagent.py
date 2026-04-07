"""Slide — Multi-Agent Systems: 4 categories in a 2x2 grid."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Multi-agent systems slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    cat_name = Style.create(
        s.Large + s.bold + s.project.colors.primary,
        "gs_ma_cat_name",
    )
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    stat = s.bold + s.project.colors.highlight
    takeaway = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_ma_takeaway",
    )
bs = BlockStyles

_CATEGORIES = [
    ("SOP-Driven", [
        ("MetaGPT", "role-based SOP orchestration"),
        ("ChatDev", "waterfall with AI agents"),
        ("FlowGen", "structured process \u2192 15% improvement"),
        ("AgentCoder", "96.3% Pass@1 on HumanEval"),
    ]),
    ("Conversational", [
        ("AutoGen", "multi-agent conversation framework"),
        ("CAMEL", "communicative agents for exploration"),
        ("CrewAI", "44K\u2605 \u2014 role-playing agent teams"),
    ]),
    ("ACI (Agent-Computer Interface)", [
        ("SWE-agent", "Princeton \u2014 terminal-based coding agent"),
        ("OpenHands", "64K\u2605 \u2014 open-source coding platform"),
        ("Devin", "first commercial autonomous SE agent"),
    ]),
    ("Integrated", [
        ("Claude Code", "Anthropic \u2014 CLI-native agentic coding"),
        ("Cursor", "AI-first IDE with deep context"),
        ("GitHub Copilot", "most widely adopted, agent mode emerging"),
    ]),
]

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Multi-Agent Systems", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        with st_grid(
            cols="repeat(auto-fit, minmax(350px, 1fr))",
            gap="16px",
            cell_styles=s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md,
        ) as g:
            for cat_name, entries in _CATEGORIES:
                with g.cell():
                    st_write(bs.cat_name, cat_name, tag=t.div)
                    st_space("v", 0.5)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        for name, desc in entries:
                            with l.item():
                                st_write(bs.body, (bs.keyword, name), f" \u2014 {desc}")

        st_space("v", 2)
        st_write(bs.takeaway, "Key finding: process discipline improves even AI agent output.")
