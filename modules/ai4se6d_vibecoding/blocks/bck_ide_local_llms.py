"""Act IV — Local LLMs: when running the model on your own machine makes sense, and its limits.

opencode facts (Ollama through an OpenAI-compatible provider, larger context needed for tool
calls) checked against opencode.ai/docs/providers, November 2026.
"""
# Adapted from AI4SE6d/slides/day1/01_tools_ecosystem.md (section "Local LLMs")
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Local LLMs slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    column_title = Style.create(
        s.project.titles.subtitle + s.center_txt,
        "ide_local_column_title",
    )
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    takeaway = Style.create(
        s.Large + s.italic + s.project.colors.accent + s.center_txt,
        "ide_local_takeaway",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Local LLMs", tag=t.div, toc_lvl="1")
            st_write(
                bs.body,
                (bs.keyword, "Ollama"), " or ", (bs.keyword, "LM Studio"),
                " run an open model on your machine \u2014 opencode can use it.",
                tag=t.div,
            )

            with st_zoom(85), st_grid(
                cols="1fr 1fr",
                gap="32px",
                cell_styles=s.project.containers.callout,
            ) as g:
                with g.cell():
                    st_write(bs.column_title, "When it makes sense", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "Privacy"), " — nothing leaves")
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "Offline"), " — plane, secure site")
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "Fixed cost"), " — no token bill")
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "Small jobs"), " — explain, complete")
                with g.cell():
                    st_write(bs.column_title, "Limits for agents", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword_warn, "Weaker"), " — multi-file plans")
                        with l.item():
                            st_write(bs.body, (bs.keyword_warn, "Tool calls"), " — less reliable")
                        with l.item():
                            st_write(bs.body, (bs.keyword_warn, "Hardware"), " — big GPU/RAM, slower")
                        with l.item():
                            st_write(bs.body, (bs.keyword_warn, "You run it"), " — setup, updates")

            st_write(
                bs.takeaway,
                "This week: cloud model, capped key. At work: local when data must stay.",
                tag=t.div,
            )
