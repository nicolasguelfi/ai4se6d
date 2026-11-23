"""Slide — The AI-TDD discipline and its golden rule."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """The AI-TDD discipline and its golden rule — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_golden_rule_body")
    keyword = s.bold + s.project.colors.highlight
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "build_golden_rule_foot")
    table_hdr = Style.create(s.project.titles.table_header + s.center_txt, "build_golden_rule_th")
    table_txt = s.project.titles.table_cell
    table_lbl = s.project.titles.table_label
bs = BlockStyles

_NOTES = [
    ("The message",
     "In AI-assisted TDD each step has an owner. The test is your specification, so you review it before any "
     "code is written."),
    ("RED",
     "You + agent: the agent drafts the test, you review it — it is your spec."),
    ("GREEN and REFACTOR",
     "GREEN: the agent writes the minimal code to pass, the test is not touched. REFACTOR: you decide; the "
     "tests stay green."),
    ("The golden rule",
     "Never let the agent write the test AND the code without your review in between. Otherwise the test mirrors "
     "what the agent meant to write — it proves nothing."),
    ("Link to what follows",
     "The mutant test trick checks that a test really proves something."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'The Golden Rule', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — The Golden Rule", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "1vh")
        with st_zoom(110):
            # header row, then one row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
            cols = "5% 22% 18% 50% 5%"
            with st_grid(cols=cols, gap="0.5vw",
                         cell_styles=[s.none, s.project.containers.table_header_cell,
                                      s.project.containers.table_header_cell,
                                      s.project.containers.table_header_cell, s.none]) as g:
                for label in ('', 'Step', 'Who', 'What', ''):
                    with g.cell():
                        if label:
                            st_write(bs.table_hdr, label)
            st_space("v", "1vh")
            rows = [
                ('RED', 'You + agent', ('The agent drafts the test, ', (bs.keyword, 'you'), ' review it: it is your spec')),
                ('GREEN', 'Agent', ('Minimal code to pass. The test is not touched.',)),
                ('REFACTOR', 'You decide', ('Clean up; the tests stay green',)),
            ]
            cells = s.project.containers.rows(len(rows), cols, filled=(2, 3, 4))
            with st_grid(cols=cols, gap="1.5vh 0.5vw", cell_styles=cells) as g:
                for step, who, what in rows:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.table_lbl, step, tag=t.div)
                    with g.cell():
                        st_write(bs.table_txt, who, tag=t.div)
                    with g.cell():
                        st_write(bs.table_txt, *what, tag=t.div)
                    with g.cell():
                        pass  # right margin
            st_space("v", "3vh")
            with st_block(s.project.containers.callout):
                st_write(
                    bs.body,
                    (bs.keyword, 'Golden rule'),
                    ': never let the agent write the test ',
                    (bs.keyword, 'and'),
                    ' the code without your review in between.',
                )
            st_space("v", "1vh")
            st_write(
                bs.foot,
                'Otherwise the test mirrors what the agent meant to write — it proves nothing.',
                tag=t.div,
            )
