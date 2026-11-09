"""Slide — The artifact chain: each session produces what the next one uses."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Artifact chain styles."""
    heading = s.project.titles.heading
    step = Style.create(s.project.titles.table_label + s.center_txt, "d2_chain_step")
    artifact = Style.create(s.project.titles.table_cell + s.center_txt, "d2_chain_artifact")
    closing = Style.create(s.project.titles.body_accent + s.center_txt, "d2_chain_closing")
bs = BlockStyles

_CHAIN = [
    ("1 · Git", "a safety net: commit, branch, restore"),
    ("2 · opencode", "AGENTS.md + the right context"),
    ("3 · Plan", "docs/plan.md, 5-8 atomic tasks"),
    ("4 · Build", "tests then code, one branch per task"),
    ("5 · Review", "findings triaged HIGH / MEDIUM / LOW"),
    ("6 · Deliver", "v0.1 merged and tagged"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "The Artifact Chain", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_grid(
            cols="repeat(auto-fit, minmax(420px, 1fr))", gap="20px",
            cell_styles=s.project.containers.grid_cell_centered,
        ) as g:
            for step, artifact in _CHAIN:
                with g.cell():
                    with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                        st_write(bs.step, step, tag=t.div)
                        st_write(bs.artifact, artifact, tag=t.div)
        st_space("v", 1)
        st_write(bs.closing, "Each step feeds the next. By 17:00: a tested, reviewed, versioned app.", tag=t.div)
