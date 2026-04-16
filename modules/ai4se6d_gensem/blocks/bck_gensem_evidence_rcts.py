"""Slide — The Productivity Paradox (synthesizes Peng +55%, Cui +26%, METR -19%)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: evidence-insight
# @reuse: bck_gensem_evidence_peng, _cui, _metr, _paradox (v01) — condensed into 1 slide
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

_page_fill = s.project.containers.page_fill_top

_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "rct_cell",
)


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "rct_body")
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary, "rct_kw",
    )
    critical = Style.create(
        s.Large + s.bold + s.project.colors.critical + s.center_txt, "rct_crit",
    )
    success = Style.create(
        s.Large + s.bold + s.project.colors.success, "rct_ok",
    )
    takeaway = Style.create(
        s.Large + s.bold + s.project.colors.accent + s.center_txt, "rct_takeaway",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

_PROMPT_PARADOX = (
    f"{_PREFIX} A large question mark made of two halves: "
    "left half in green/teal (positive, upward arrow), "
    "right half in red/amber (negative, downward arrow). "
    "The two halves are joined but pulling apart. "
    f"{_SUFFIX}"
)


def build():
    st_marker("The Productivity Paradox")
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(
                bs.heading, "The Productivity Paradox",
                tag=t.div, toc_lvl="1",
                )
            st_hover_tooltip(
                title="3 Randomized Controlled Trials (RCTs)",
                entries=[
                    ("Peng +55.8%", "Developers with GitHub Copilot completed an HTTP server task 55.8% faster. But this was a single simple task — 95% CI is 21-89%, very wide."),
                    ("Cui +26%", "4,867 developers at Microsoft/Accenture over 2-8 months: AI group completed 26% more tasks. Juniors gained +27-39%, seniors only +8-13%."),
                    ("METR -19%", "16 experienced OSS developers on familiar code were 19% SLOWER with AI. They predicted +24% — prompt overhead and context-switching ate the gains."),
                    ("Resolution", "The gains depend on task complexity, developer experience, and codebase familiarity. Without structured process, AI creates as many problems as it solves."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

            with st_grid(cols="2fr 3fr", gap="24px", cell_styles=_cell) as g:
                with g.cell():
                    st_image(
                        s.none, width="80%",
                        editable=IS_EDITABLE,
                        name="gse_evidence_paradox",
                        prompt=_PROMPT_PARADOX,
                        provider="openai",
                        ai_size="1024x1536",
                    )
                with g.cell():
                    with st_zoom(120):
                        st_write(
                            bs.body,
                            (bs.success, "+55%"),
                            (bs.body, " on simple tasks  vs  "),
                            (bs.critical, "-19%"),
                            (bs.body, " on familiar code"),
                        )
                        st_space("v", 1)
                        st_write(
                            bs.takeaway,
                            "Scale, context, and expertise determine whether AI helps or hinders.",
                        )
                        st_space("v", 1)
                        st_write(
                            bs.source,
                            cite("peng-copilot2023"), " | ",
                            cite("cui-fieldexperiments2024"), " | ",
                            cite("metr2025"),
                        )
