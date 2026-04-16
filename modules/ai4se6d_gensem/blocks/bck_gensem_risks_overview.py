"""Slide — Risks of Generative SE: 6 risk categories in a 2x3 grid."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Risks overview styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    stat = s.project.titles.stat
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


_RISKS = [
    (
        "Security",
        "12\u201365% vulnerability rate depending on language/model. "
        "Generated code inherits training-data weaknesses.",
    ),
    (
        "Hallucinations",
        "Package hallucinations 5.2\u201321.7% \u2014 supply chain attack vectors. "
        "LLMs invent plausible but nonexistent dependencies.",
    ),
    (
        "Technical Debt",
        "Homogenization reduces solution diversity. "
        "Fowler: \u201clong-term catastrophe\u201d from uniform codebases.",
    ),
    (
        "Automation Bias",
        "Verification overhead and over-reliance, "
        "especially among novices who trust AI output uncritically.",
    ),
    (
        "IP & Legal",
        "Unsettled legal status of AI-generated code. "
        "Ongoing Copilot litigation on training data consent.",
    ),
    (
        "Ethics",
        "Bias in generated code, training data consent issues, "
        "\u201cmissing rung\u201d in junior developer skill development.",
    ),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Risks of Generative SE", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols="repeat(auto-fit, minmax(350px, 1fr))",
            gap="16px",
            cell_styles=s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md,
        ) as g:
            for title, description in _RISKS:
                with g.cell():
                    st_write(bs.label, title, tag=t.div)
                    st_space("v", 0.5)
                    st_write(bs.body, description)

        st_space("v", 1)
        st_write(
            bs.source,
            cite("basic-codesecurity-slr2025"), " | ",
            cite("spracklen-packages2025"),
        )
