"""Shared layout — "How GSE-One solves it" slide, one per CCSET cycle (edition 2).

Each theory part of a cycle ends with one such slide: the problem the theory raised,
then the solution GSE-One chose for it. It is a conceptual illustration only: no demo,
no screenshot of a run, no command for the learners to type (decision 2026-11-10,
docs/plans/2026-11-10-012-six-days-cycles-plan.html).

Usage in a block:
    from gse_solution import gse_solution, CMD
    def build():
        gse_solution(
            cycle="CCSET01 · From LLM to agent",
            label="GSE-One solution — project memory",
            problem="The model forgets everything between two sessions.",
            solution=[
                "The project memory is written in files, in the .gse/ folder.",
                ("Every session starts by reading them back: ", (CMD, "/gse-resume")),
            ],
        )

Each item of ``solution`` is a string or a tuple of st_write parts (str or (style, str)).
"""
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt

from shared_styles import Styles as s

CMD = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "gse_solution_cmd")

_CYCLE = Style.create(s.project.titles.caption + s.center_txt, "gse_solution_cycle")
_HEADING = s.project.titles.heading
_LABEL = s.project.titles.label
_BODY = s.project.titles.body
_FOOT = Style.create(s.project.titles.caption + s.italic + s.center_txt, "gse_solution_foot")

DEFAULT_FOOT = "Concept only — you will use GSE-One from day 3."


def gse_solution(*, cycle, label, problem, solution, foot=DEFAULT_FOOT, zoom=60, notes=None):
    """Render the slide: cycle tag, heading, the problem, GSE-One's solution, a footnote.

    ``notes``: optional trainer notes, a list of (heading, text); when given, the « i » sits on the title line
    (header grid 95% / 5%, NG 2026-11-23). Without it the slide is drawn as before.
    """
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(zoom):
            st_write(_CYCLE, cycle, tag=t.div)
            if notes:
                from shared_widgets import st_hover_tooltip
                with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                    with h.cell():
                        st_write(_HEADING, "How GSE-One Solves It", tag=t.div, toc_lvl="+1", label=label)
                    with h.cell():
                        st_hover_tooltip(title=f"Trainer notes — {label}", entries=notes,
                                         position="left", width="50vw")
            else:
                st_write(_HEADING, "How GSE-One Solves It", tag=t.div, toc_lvl="+1", label=label)
            with st_block(s.project.containers.callout):
                st_write(_BODY, (_LABEL, "The problem — "), problem, tag=t.div)
            st_write(_LABEL, "The solution GSE-One chose", tag=t.div)
            with st_list(l_style=_BODY, li_style=_BODY, list_type=lt.unordered) as l:
                for item in solution:
                    parts = item if isinstance(item, tuple) else (item,)
                    with l.item():
                        st_write(_BODY, *parts)
            if foot:
                st_write(_FOOT, foot, tag=t.div)
