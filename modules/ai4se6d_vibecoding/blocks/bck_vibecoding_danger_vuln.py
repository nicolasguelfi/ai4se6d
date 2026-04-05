"""Slide — Stat-hero: 12-65% vulnerability rates."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """Vulnerability stat-hero slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = Style.create(
        s.GIANT + s.bold + s.project.colors.highlight + s.center_txt,
        "vc_danger_vuln_stat",
    )
    body = s.project.titles.body
    source = s.project.titles.caption + s.center_txt
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A shield icon in electric blue with deep cracks running through it, "
    "revealing amber danger glow beneath. Percentage numbers float around the shield "
    "in teal. Represents security vulnerabilities hidden in AI-generated code "
    f"that appears to work correctly. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Security Vulnerabilities", tag=t.div, toc_lvl="1")

            with st_grid(
                cols="2fr 3fr",
                gap="24px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="vc_danger_vuln",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    st_write(bs.stat, "12\u201365%")
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "of AI-generated code contains vulnerabilities, "
                        "depending on language, model, and prompting strategy.",
                    )
                    st_space("v", 1)
                    # REF: https://arxiv.org/abs/2404.18353
                    st_write(bs.source, cite("tihanyi2024formai"))
                    st_write(
                        bs.body,
                        "At least 62.07% of generated C programs "
                        "contain vulnerabilities (zero-shot).",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.source,
                        "Your exercise code likely has security flaws.",
                    )
