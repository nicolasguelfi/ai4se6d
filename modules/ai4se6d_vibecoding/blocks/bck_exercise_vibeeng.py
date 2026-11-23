"""Slide — Tomorrow: VibeEngineering in Practice (framing for Day 2 CalcApp)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Exercise VibeEngineering framing slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    watch_q = Style.create(
        s.Large + s.project.colors.accent,
        "ex_ve_watch_q",
    )
    transition = Style.create(
        s.large + s.italic + s.center_txt + s.project.colors.muted,
        "ex_ve_transition",
    )
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "ex_ve_text_cell")

_NOTES = [
    ("The message",
     "Today was pure VibeCoding (FreeSelfApp); tomorrow the same people build CalcApp v0.1 with the six "
     "VibeEngineering principles. Same tools, different discipline."),
    ("What changes tomorrow",
     "Requirements written first, acceptance criteria before any generation, the architecture declared to the agent "
     "(AGENTS.md) — then generation, tests and review."),
    ("The four questions",
     "Ask the participants to compare both experiences on Quality (which result is more robust?), Confidence (which "
     "do you trust more?), Speed (was the overhead worth it?) and the Trade-off (where is the sweet spot?)."),
    ("How to run it",
     "Have them note their answers for FreeSelfApp tonight; they answer again after CalcApp and compare."),
    ("Link to the course",
     "This comparison feeds the debrief of day 2 and the move to GSE-One on day 3."),
]

_PROMPT = (
    f"{_PREFIX} A person at a desk with a glowing laptop, this time with a structured "
    "blueprint beside them and a checklist floating in the air. Code streams flow from "
    "the screen but pass through a filter/gate of teal light. Test tubes with green "
    f"checkmarks float nearby. Symbolizes disciplined AI-assisted development. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(62):   # long title kept on one line
                st_write(bs.heading, "Tomorrow: VibeEngineering in Practice", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Tomorrow: VibeEngineering in Practice", entries=_NOTES,
                                 position="left", width="50vw")
        with st_block(s.center_txt), st_zoom(80):
            st_write(bs.body, (bs.keyword, "CalcApp v0.1"), " \u2014 Day 2", tag=t.div)
        st_space("v", 2)

        with st_grid(cols="1.5fr 3.5fr", gap="3vw",
                     cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
            with g.cell():
                st_image(
                    s.none,
                    width="100%",
                    editable=IS_EDITABLE,
                    name="ex_vibeeng",
                    prompt=_PROMPT,
                    provider="openai",
                    ai_size="1536x1024",
                )

            with g.cell(), st_zoom(82):
                st_write(
                    bs.body,
                    "Tomorrow, you'll apply these 6 principles to a real project. "
                    "Requirements first, acceptance criteria before generation, architecture declared.",
                )
                st_space("v", "2vh")

                st_write(bs.body, (bs.keyword_warn, "Compare Both Approaches"), tag=t.div)
                st_space("v", 0.5)
                with st_list(l_style=bs.watch_q, li_style=bs.watch_q, list_type=lt.unordered,
                             text_align="left", item_gap=0.6) as l:
                    with l.item(): st_write(bs.watch_q, (bs.keyword, "Quality"), " \u2014 which result is more robust?")
                    with l.item(): st_write(bs.watch_q, (bs.keyword, "Confidence"), " \u2014 which do you trust more?")
                    with l.item(): st_write(bs.watch_q, (bs.keyword, "Speed"), " \u2014 was the overhead worth it?")
                    with l.item(): st_write(bs.watch_q, (bs.keyword_warn, "Trade-off"), " \u2014 where is the sweet spot?")

        st_space("v", 4)
        with st_block(s.center_txt):
            st_write(
                bs.transition,
                "After today's FreeSelfApp and tomorrow's CalcApp \u2014 you'll have experienced both sides",
            )
