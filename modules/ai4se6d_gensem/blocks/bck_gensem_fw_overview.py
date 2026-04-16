"""Slide — Landscape overview of GenSE frameworks."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s

class BlockStyles:
    """Framework overview styles."""
    heading = s.project.titles.slide_title + s.center_txt
    category = Style.create(
        s.Large + s.bold + s.project.colors.accent,
        "gs_fw_category",
    )
    entry = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    highlight_cat = Style.create(
        s.Large + s.bold + s.project.colors.highlight,
        "gs_fw_highlight_cat",
    )
bs = BlockStyles

_CATEGORIES = [
    (bs.category, "Adaptations", [
        ("AgileGen", "Gherkin-bridge approach to agile + GenAI"),
        ("Agentic DevOps", "Microsoft\u2019s AI agents in CI/CD pipelines"),
    ]),
    (bs.category, "AI-Native", [
        ("SE 3.0", "Intent-centric, conversation-oriented development"),
        ("V-Bounce", "Humans validate, AI implements across V-model"),
        ("Promptware Eng.", "SE lifecycle applied to prompt systems"),
        ("MAISTRO", "Multi-agent orchestration with SOP processes"),
    ]),
    (bs.highlight_cat, "Process Plugins", [
        ("Compound Engineering", "5-phase workflow adaptable to any SDLC"),
    ]),
]

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "Framework Landscape", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        for cat_style, cat_name, entries in _CATEGORIES:
            with st_block(
                s.project.containers.cell_primary_bg
                + s.project.containers.cell_pad_md
                + Style("margin-bottom: 12px;", "gs_fw_row_mb"),
            ):
                st_write(cat_style, cat_name, tag=t.div)
                st_space("v", 0.5)
                with st_grid(
                    cols="repeat(auto-fit, minmax(280px, 1fr))",
                    gap="12px",
                    cell_styles=s.project.containers.cell_accent_bg + s.project.containers.cell_pad_sm,
                ) as g:
                    for name, desc in entries:
                        with g.cell():
                            st_write(bs.entry, (bs.keyword, name), f" \u2014 {desc}")
