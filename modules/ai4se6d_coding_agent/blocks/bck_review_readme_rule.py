"""Slide — Living documentation — the 80/20 rule."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Living documentation — the 80/20 rule — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_readme_rule_body")
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "review_readme_rule_cmd")
bs = BlockStyles

# Text left-aligned (NG, 2026-11-23: same recipes as the intro module)
_left = Style("text-align:left;", "review_readme_rule_left")

_NOTES = [
    ("The message",
     "Documentation is shared: the agent writes the WHAT (about 80 %), you write the WHY (about 20 %)."),
    ("The WHAT",
     "Stack, install and run, scripts, structure, feature list: facts the agent can read from the code and "
     "write quickly."),
    ("The WHY",
     "Why this design, known limits, trade-offs you accepted: decisions that are not in the code. Only you "
     "know them."),
    ("Read the example",
     "The agent states a fact (saveExpenses stores the list under calcapp.expenses). You state the reason: "
     "localStorage on purpose, v0.1 is single-user and offline, no backend until the plan needs one."),
    ("Ask the room",
     "« Which sentence of your README could only you have written? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Living Docs: the 80/20 Rule', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Living Docs: the 80/20 Rule", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        with st_zoom(99):
            with st_grid(cols='5% 1fr 1fr 5%', gap="1vw",
                         cell_styles=[s.none, s.project.containers.row_fill_1 + _left,
                                      s.project.containers.row_fill_2 + _left, s.none]) as g:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.label, 'The agent writes the WHAT (80%)', tag=t.div)
                    with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body,
                                 text_align="left", item_gap=0.6) as l:
                        with l.item():
                            st_write(bs.body, 'Stack, install, run')
                        with l.item():
                            st_write(bs.body, 'Scripts, structure')
                        with l.item():
                            st_write(bs.body, 'Feature list')
                with g.cell():
                    st_write(bs.label, 'You write the WHY (20%)', tag=t.div)
                    with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body,
                                 text_align="left", item_gap=0.6) as l:
                        with l.item():
                            st_write(bs.body, 'Why this design')
                        with l.item():
                            st_write(bs.body, 'Known limits')
                        with l.item():
                            st_write(bs.body, 'Trade-offs you accepted')
                with g.cell():
                    pass  # right margin
            st_space("v", "7vh")

            # the example: one row per voice, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
            cols = "5% 15% 75% 5%"
            cells = s.project.containers.rows(2, cols, filled=(2, 3))
            with st_grid(cols=cols, gap="2vh 0.5vw", cell_styles=cells) as g:
                for label, parts in [
                    ('Agent: ', ('“saveExpenses stores the list under ', (bs.cmd, 'calcapp.expenses'), '.”')),
                    ('You: ', ('“localStorage on purpose: v0.1 is single-user and offline — no backend until '
                               'the plan needs one.”',)),
                ]:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.body, (bs.label, label), tag=t.div)
                    with g.cell():
                        st_write(bs.body, *parts, tag=t.div)
                    with g.cell():
                        pass  # right margin
