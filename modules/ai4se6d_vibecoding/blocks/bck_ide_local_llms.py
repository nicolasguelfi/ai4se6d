"""Act IV — Local LLMs: when running the model on your own machine makes sense, and its limits.

opencode facts (Ollama through an OpenAI-compatible provider, larger context needed for tool
calls) checked against opencode.ai/docs/providers, November 2026.
"""
# Adapted from AI4SE6d/slides/day1/01_tools_ecosystem.md (section "Local LLMs")
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


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


_NOTES = [
    ("The message",
     "Ollama or LM Studio run an open model on your own machine, and opencode can use it as a provider."),
    ("When it makes sense",
     "Privacy (nothing leaves the machine), offline work (plane, secure site), a fixed cost (no token bill), and "
     "small jobs such as explaining or completing code."),
    ("Limits for agents",
     "Local models are weaker on multi-file plans, their tool calls are less reliable, they need a big GPU and RAM "
     "and run slower, and you install and update them yourself."),
    ("The rule of the week",
     "This week: a cloud model with your capped key. At work: a local model when the data must stay inside."),
    ("Ask the room",
     "« Which code or data of your company may not be sent to a cloud model? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(85):
                st_write(bs.heading, "Local LLMs", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Local LLMs", entries=_NOTES, position="left", width="50vw")
        with st_zoom(100):
            st_write(
                bs.body + s.center_txt,
                (bs.keyword, "Ollama"), " or ", (bs.keyword, "LM Studio"),
                " run an open model on your machine \u2014 opencode can use it.",
                tag=t.div,
            )
        st_space("v", "2vh")

        with st_zoom(85), st_grid(
            cols="1fr 1fr",
            gap="32px",
            cell_styles=s.project.containers.callout,
        ) as g:
            with g.cell():
                st_write(bs.column_title, "When it makes sense", tag=t.div)
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered,
                             text_align="left", item_gap=0.6) as l:
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
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered,
                             text_align="left", item_gap=0.6) as l:
                    with l.item():
                        st_write(bs.body, (bs.keyword_warn, "Weaker"), " — multi-file plans")
                    with l.item():
                        st_write(bs.body, (bs.keyword_warn, "Tool calls"), " — less reliable")
                    with l.item():
                        st_write(bs.body, (bs.keyword_warn, "Hardware"), " — big GPU/RAM, slower")
                    with l.item():
                        st_write(bs.body, (bs.keyword_warn, "You run it"), " — setup, updates")

        st_space("v", "3vh")
        with st_zoom(115):
            st_write(
                bs.takeaway,
                "This week: cloud model, capped key. At work: local when data must stay.",
                tag=t.div,
            )
