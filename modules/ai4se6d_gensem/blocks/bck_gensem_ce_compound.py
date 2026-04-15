"""Slide — Phase 5: Compound, the distinctive contribution of GSE-One."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Compound phase slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    card_title = s.bold + s.project.colors.primary + s.Large
    body = s.project.titles.body
    closing = s.project.titles.body + s.project.colors.highlight + s.bold
    analogy = s.project.titles.body + s.project.colors.accent
bs = BlockStyles

_OUTPUTS = [
    ("Pattern Documentation", "What worked, what failed, and why — captured as reusable patterns"),
    ("Project Rules Updates", "CLAUDE.md enriched with new constraints and conventions"),
    ("Skill Refinement", "Better prompts, improved decomposition strategies, sharper instructions"),
    ("Architecture Decision Records", "Decisions and their rationale preserved for future reference"),
]

def build():
    st_marker("Compound: 4 Outputs")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(
                bs.heading,
                "Phase 5: Compound — The Distinctive Contribution",
                tag=t.div,
                toc_lvl="+1",
            )
            st_hover_tooltip(
                title="Compound Phase",
                entries=[
                    ("What it is", "The phase where project knowledge is captured and reused, turning one-off work into compounding value."),
                    ("Why it matters", "Without Compound, every session starts from zero. With it, rules accumulate and AI gets smarter with each cycle."),
                    ("GSE-One difference", "This phase is what separates GSE-One from ad-hoc prompting -- systematic knowledge capitalization."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(120):
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
