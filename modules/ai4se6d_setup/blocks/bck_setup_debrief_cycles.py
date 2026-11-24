"""Slide — Debrief: this afternoon's experience in this morning's words (cycles 01-03, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Debrief — link to the morning cycles."""
    heading = s.project.titles.slide_title + s.center_txt
    table_hdr = Style.create(s.project.titles.table_header + s.center_txt, "setup_cycles_th")
    table_txt = s.project.titles.body
    table_lbl = Style.create(s.project.titles.body + s.bold, "setup_cycles_tl_body")
    cycle = Style.create(s.project.titles.body + s.project.colors.accent + s.center_txt, "setup_cycles_cycle")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "setup_cycles_foot")
bs = BlockStyles

ROWS = [
    ("It filled what you did not say with its own guesses", "An LLM predicts the most likely continuation", "CCSET01"),
    ("The agent did more than you asked", "Autonomy needs a human in the loop", "CCSET02"),
    ("It works — would you ship it?", "VibeCoding is not engineering", "CCSET02"),
    ("Your key, its permissions, what you pasted", "Practical rules, the AI Act", "CCSET03"),
]

_NOTES = [
    ("The message",
     "Each experience of the afternoon matches an idea of the morning: the debrief closes the loop between "
     "theory and practice."),
    ("Prediction (CCSET01)",
     "A stack, a layout or features nobody asked for = an LLM predicts the most likely continuation and fills the "
     "gaps of the prompt. Tomorrow they meet the other face of CCSET01: a NEW session knows nothing of the project "
     "(no memory) — hence AGENTS.md."),
    ("Human in the loop (CCSET02)",
     "The agent did more than you asked = autonomy needs a human in the loop; « it works — would you ship it? » "
     "= VibeCoding is not engineering."),
    ("Rules (CCSET03)",
     "Your key, its permissions, what you pasted = the practical rules and the AI Act seen this morning."),
    ("Link to tomorrow",
     "« Tomorrow: the same app idea, engineered — by hand, on CalcApp. »"),
    ("Ask the room",
     "« Which line did you live this afternoon? » — let participants pick a row before you comment."),
]

_COLS = "5% 37% 37% 16% 5%"


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Back to This Morning", tag=t.div, toc_lvl="1",
                         label="Debrief — link to the cycles")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Back to This Morning", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        hdr = [s.none] + [s.project.containers.table_header_cell] * 3 + [s.none]
        # One row per experience, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cells = s.project.containers.rows(len(ROWS), _COLS, filled=(2, 3, 4))
        with st_zoom(84):
            with st_grid(cols=_COLS, gap="0.5vw", cell_styles=hdr) as g:
                with g.cell():
                    pass
                with g.cell(): st_write(bs.table_hdr, "This afternoon")
                with g.cell(): st_write(bs.table_hdr, "This morning's idea")
                with g.cell(): st_write(bs.table_hdr, "Cycle")
                with g.cell():
                    pass
            st_space("v", "2vh")
            with st_grid(cols=_COLS, gap="2.5vh 0.5vw", cell_styles=cells) as g:
                for lived, idea, cycle in ROWS:
                    with g.cell():
                        pass  # left margin
                    with g.cell(): st_write(bs.table_lbl, lived, tag=t.div)
                    with g.cell(): st_write(bs.table_txt, idea, tag=t.div)
                    with g.cell(): st_write(bs.cycle, cycle, tag=t.div)
                    with g.cell():
                        pass  # right margin
            st_space("v", "3vh")
            st_write(bs.foot, "Tomorrow: the same app idea, engineered — by hand, on CalcApp.", tag=t.div)
