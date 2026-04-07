"""Slide — Phase 5: Compound, the distinctive contribution of CE."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s

class BlockStyles:
    """Compound phase slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    card_title = s.bold + s.project.colors.primary + s.Large
    body = s.project.titles.body
    closing = s.project.titles.body + s.project.colors.highlight + s.bold
    analogy = s.project.titles.body + s.project.colors.accent
bs = BlockStyles

_OUTPUTS = [
    ("Pattern Documentation", "What worked, what failed, and why \u2014 captured as reusable patterns"),
    ("Project Rules Updates", "CLAUDE.md enriched with new constraints and conventions"),
    ("Skill Refinement", "Better prompts, improved decomposition strategies, sharper instructions"),
    ("Architecture Decision Records", "Decisions and their rationale preserved for future reference"),
]

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(
                bs.heading,
                "Phase 5: Compound \u2014 The Distinctive Contribution",
                tag=t.div,
                toc_lvl="1",
            )
            st_space("v", 1)

        with st_grid(
            cols=s.project.containers.responsive_2col,
            gap="16px",
            cell_styles=s.project.containers.cell_primary_bg
            + s.project.containers.cell_pad_md,
        ) as g:
            for title, description in _OUTPUTS:
                with g.cell():
                    st_write(bs.card_title, title, tag=t.div)
                    st_space("v", 0.3)
                    st_write(bs.body, description)

        st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.closing,
                "Without this phase, each session starts from zero. "
                "With it, knowledge compounds.",
            )

        st_space("v", 0.5)
        with st_block(s.center_txt):
            st_write(
                bs.analogy,
                "Compound interest analogy: 1% improvement per cycle = exponential gains over time.",
            )
