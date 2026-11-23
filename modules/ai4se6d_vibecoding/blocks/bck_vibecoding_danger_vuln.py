"""Slide — Stat-hero: 45% of AI code samples fail security tests (Veracode 2025)."""
# @guideline: maximize-viewport
# @pattern: ptn_stat_hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Vulnerability stat-hero slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = s.project.titles.stat_hero
    body = s.project.titles.body
    source = s.project.citation + s.large
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: recipes of the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"), "vc_danger_vuln_text_cell")

_PROMPT = (
    f"{_PREFIX} A shield icon in electric blue with deep cracks running through it, "
    "revealing amber danger glow beneath. Percentage numbers float around the shield "
    "in teal. Represents security vulnerabilities hidden in AI-generated code "
    f"that appears to work correctly. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(cols="95% 5%", gap="0px", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(80):   # one-line title
                    st_write(bs.heading+"zoom:1.3;", "Security Vulnerabilities", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(
                        title="Trainer notes \u2014 Security Vulnerabilities",
                        entries=[
                            (
                                "45%",
                                "Veracode (July 2025): 100+ LLMs on Java, "
                                "Python, C# and JavaScript tasks. 45% of "
                                "samples introduced OWASP Top 10 flaws.",
                            ),
                            (
                                "62%",
                                "At least 62.07% of 331,000 AI-generated C "
                                "programs (FormAI-v2) are vulnerable, "
                                "proven with the ESBMC model checker.",
                            ),
                            (
                                "9 LLMs tested",
                                "GPT-4o-mini, Gemini Pro 1.0, Falcon 180B, "
                                "Code Llama 13B, and 5 others.",
                            ),
                        ],
                        position="left", width="50vw",
                    )

            with st_grid(
                cols="1.5fr 3.5fr",
                gap="3vw",
                cell_styles=[s.project.containers.grid_cell_centered, _text_cell],
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
                    with st_zoom(105):   # text cell fills the slide (NG, 2026-11-23)
                        with st_zoom(60):
                            st_write(bs.stat, "45%")
                        st_write(
                            bs.body,
                            "of AI code samples failed security tests (100+ models).",
                        )
                        # REF: https://www.veracode.com/blog/genai-code-security-report/
                        st_write(bs.source, cite("veracode-genai2025"))
                        st_space("v", "2vh")
                        st_write(
                            bs.body,
                            "\u2265 62% of 331,000 AI-generated C programs: vulnerable.",
                        )
                        # REF: https://arxiv.org/abs/2404.18353
                        st_write(bs.source, cite("tihanyi-secure2024"))
                        st_space("v", "2vh")
                        with st_zoom(150):
                            st_write(
                                bs.body+s.project.colors.muted,
                                "We'll see yours soon!",
                            )
