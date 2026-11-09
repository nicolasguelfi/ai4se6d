"""Slide 29 — The Evidence: FlowGen (SOEN-101) stat-hero — process-emulating agents."""
# @guideline: maximize-viewport
# @pattern: ptn_stat_hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s

class BlockStyles:
    """Evidence slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = s.project.titles.stat_hero
    body = s.project.titles.body + s.center_txt
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Evidence", tag=t.div, toc_lvl="1")
            st_space("v", 1)
            with st_zoom(80):
                st_write(bs.stat, "15%")
            st_space("v", 1)
            with st_zoom(130):
                st_write(
                    bs.body,
                    "higher benchmark pass rate when LLM agents follow a process (Scrum)",
                )
                st_write(
                    bs.body,
                    "FlowGen (GPT-3.5) \u2014 design + code review also cut code smells",
                )
                # REF: https://arxiv.org/abs/2403.15852
                st_write(bs.source, cite("soen101-2024"))
