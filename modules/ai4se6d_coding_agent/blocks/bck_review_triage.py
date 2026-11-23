"""Slide — Triage findings — HIGH / MEDIUM / LOW."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Triage findings — HIGH / MEDIUM / LOW — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_triage_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "review_triage_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "review_triage_foot")
    table_hdr = Style.create(s.project.titles.table_header + s.center_txt, "review_triage_th")
    table_txt = Style.create(s.project.titles.table_cell, "review_triage_td")
    table_lbl = Style.create(s.project.titles.table_label + s.center_txt, "review_triage_tl")
bs = BlockStyles

_NOTES = [
    ("The message",
     "Every review finding gets a severity before anyone fixes anything: HIGH, MEDIUM or LOW. The severity "
     "decides the action."),
    ("The scale",
     "HIGH: crash, data loss, security hole — fix before delivering. MEDIUM: missing error handling, hard to "
     "maintain — fix, or decide explicitly. LOW: naming, style, documentation gap — note it, fix if cheap."),
    ("The trap",
     "Treating the agent's list as a to-do list. Not every finding is true: you are the judge, not the agent."),
    ("Link to Day 3",
     "It is the same scale as GSE-One's /gse-review: what you do by hand today, the plugin does tomorrow."),
    ("Ask the room",
     "« A finding says the code is hard to maintain. HIGH, MEDIUM or LOW — and who decides? »"),
]

_ROWS = [
    ('HIGH', 'Crash, data loss, security hole', 'Fix before delivering'),
    ('MEDIUM', 'Missing error handling, hard to maintain', 'Fix, or decide explicitly'),
    ('LOW', 'Naming, style, documentation gap', 'Note it; fix if cheap'),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(60):
                st_write(bs.heading, 'Triage: HIGH / MEDIUM / LOW', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Triage: HIGH / MEDIUM / LOW", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # header row + one row per severity, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 16% 44% 30% 5%"
        cells = s.project.containers.rows(len(_ROWS) + 1, cols, filled=(2, 3, 4))
        cells[1:4] = [s.project.containers.table_header_cell] * 3
        with st_zoom(110), st_grid(cols=cols, gap="3.5vh 0.5vw", cell_styles=cells) as g:
            for cell in ('', 'Severity', 'Typical finding', 'Action', ''):
                with g.cell():
                    if cell:
                        st_write(bs.table_hdr, cell)
            for sev, finding, action in _ROWS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.table_lbl, sev, tag=t.div)
                with g.cell():
                    st_write(bs.table_txt, finding, tag=t.div)
                with g.cell():
                    st_write(bs.table_txt, action, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "6vh")
        with st_zoom(85):
            st_write(bs.body, "The same scale as GSE-One's ", (bs.cmd, '/gse-review'), ' (Day 3).', tag=t.div)
            st_space("v", "2vh")
            st_write(bs.foot, 'Not every finding is true: you are the judge, not the agent.', tag=t.div)
