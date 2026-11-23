"""Slide 29 — The Evidence: FlowGen (SOEN-101) stat-hero — process-emulating agents."""
# @guideline: maximize-viewport
# @pattern: ptn_stat_hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Evidence slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = s.project.titles.stat_hero
    body = s.project.titles.body + s.center_txt
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

_NOTES = [
    ('The message',
     'Process helps agents too: when LLM agents follow a software process, their benchmark pass rate is 15% higher.'),
    ('The study',
     'FlowGen (SOEN-101, Lin, Kim and Chen, 2024) makes GPT-3.5 agents play the roles of a software process (Waterfall, TDD, Scrum). The 15% is the Scrum variant (average Pass@1 gain over GPT-3.5 without process, on HumanEval and MBPP); Waterfall and TDD gain less. Design and code review also cut code smells. The paper does not claim the result holds for agile methods in general or for any life cycle.'),
    ('Why it matters here',
     'It is the VibeEngineering argument in numbers: the six principles are not bureaucracy, they make the generated code better.'),
    ('The limits',
     'A benchmark of small programming tasks, with an older model (GPT-3.5): the direction counts more than the exact figure.'),
    ('Ask the room',
     '« If a process helps the AI, why do we drop it when we work with the AI? »'),
]

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            # title and « i » on the same line, title smaller (NG, 2026-11-23)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(100):
                    st_write(bs.heading, "The Evidence", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — The Evidence", entries=_NOTES,
                                     position="left", width="50vw")
            st_space("v", 4)
            with st_zoom(70):
                st_write(bs.stat, "15%")

            with st_zoom(108):   # 108 since the longer Scrum line (2026-11-23)
                st_write(
                    bs.body,
                    "higher benchmark pass rate when GPT-3.5 agents emulate Scrum (vs. no process); "
                    "Waterfall and TDD gain less",
                )
                st_write(
                    bs.body,
                    "FlowGen (GPT-3.5) \u2014 design + code review also cut code smells",
                )
                # REF: https://arxiv.org/abs/2403.15852
                st_write(bs.source, cite("soen101-2024"))
