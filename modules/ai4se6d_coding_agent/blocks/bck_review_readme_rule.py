"""Slide — Living documentation — the 80/20 rule."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Living documentation — the 80/20 rule — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_readme_rule_body")
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "review_readme_rule_cmd")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Living Docs: the 80/20 Rule', tag=t.div, toc_lvl='+1')
            with st_grid(cols='1fr 1fr', gap="24px", cell_styles=s.project.containers.cell_pad_sm) as g:
                with g.cell():
                    st_write(bs.label, 'The agent writes the WHAT (80%)', tag=t.div)
                    with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body) as l:
                        with l.item():
                            st_write(bs.body, 'Stack, install, run')
                        with l.item():
                            st_write(bs.body, 'Scripts, structure')
                        with l.item():
                            st_write(bs.body, 'Feature list')
                with g.cell():
                    st_write(bs.label, 'You write the WHY (20%)', tag=t.div)
                    with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body) as l:
                        with l.item():
                            st_write(bs.body, 'Why this design')
                        with l.item():
                            st_write(bs.body, 'Known limits')
                        with l.item():
                            st_write(bs.body, 'Trade-offs you accepted')
            st_write(
                bs.body,
                (bs.label, 'Agent: '),
                '“saveExpenses stores the list under ',
                (bs.cmd, 'calcapp-data'),
                '.”',
                tag=t.div,
            )
            st_write(
                bs.body,
                (bs.label, 'You: '),
                '“localStorage on purpose: v0.1 is single-user and offline — no backend until the plan needs one.”',
                tag=t.div,
            )
