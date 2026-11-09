# Adapted from streamtex-all-trainings@7707c1c5:content/genai_landscape/bck_genai_ai_agent_concept.py
# Adapted from streamtex-all-trainings@7707c1c5:content/genai_landscape/bck_genai_documents_concept.py
"""Slide — The Model Has No Memory: context re-sent each request; continuity = files + git; what to do meanwhile.

Edition 2, day-1 notion 2 (board peda1, P10). New text, seeded by the trainer notes of the two
all-trainings concept slides ("an AI agent learns nothing: its instruction is reread in every conversation";
"the model does not learn the document: it sees it again for every answer").
"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


_page_fill = s.project.containers.page_fill_top

_col = Style.create(
    s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md,
    "nomem_col",
)
_punch_box = Style.create(s.project.containers.callout + s.center_txt, "nomem_punch_box")


class BlockStyles:
    """Slide: no memory — three columns (what happens / where continuity lives / what you do)."""
    heading = s.project.titles.section_title + s.center_txt
    col_title = Style.create(
        s.project.colors.accent + s.bold + s.text.sizes.pt32 + s.text.wrap.hyphens, "nomem_col_title",
    )
    body = Style.create(s.text.sizes.pt24, "nomem_body")
    key = Style.create(s.text.sizes.pt24 + s.bold + s.project.colors.highlight, "nomem_key")
    code = Style.create(
        s.text.sizes.pt24 + s.text.fonts.font_monospace + s.project.colors.primary, "nomem_code",
    )
    punch = Style.create(s.text.sizes.pt32 + s.bold + s.text.wrap.hyphens, "nomem_punch")


bs = BlockStyles

_NOTES = [
    ("Message", "Nothing is remembered between requests: the tool re-sends everything each time. "
                "What must survive goes into files and git."),
    ("Link", "This is why day 2 starts with git and AGENTS.md, and why GSE-One keeps its state in .gse/."),
    ("Ask the room", "\"Your session crashed. What does the agent still know?\" — only what is on disk."),
]


def _bullets(items):
    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
        for parts in items:
            with l.item():
                st_write(bs.body, *parts)


def build():
    with st_block(_page_fill):
        with st_grid(cols="92% 8%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell():
                st_write(bs.heading, "The Model Has No Memory", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — no memory", entries=_NOTES, position="left", width="45vw")

        with st_grid(cols="1fr 1fr 1fr", gap="16px", cell_styles=_col) as g:
            with g.cell():
                st_write(bs.col_title, "What really happens", tag=t.div)
                _bullets([
                    ("Every request ", (bs.key, "re-sends the whole context"),
                     ": instructions, conversation, files read so far."),
                    ("The model ", (bs.key, "learns nothing"), " from you between requests."),
                    ("New session = blank page.",),
                ])
            with g.cell():
                st_write(bs.col_title, "Continuity lives in files", tag=t.div)
                _bullets([
                    ((bs.code, "AGENTS.md"), " — project rules, read at each session"),
                    ((bs.code, "docs/plan.md"), " — your plan, task by task"),
                    ((bs.code, ".gse/"), " — GSE-One state: where the project is"),
                    ((bs.key, "git history"), " — what changed, when, and why"),
                ])
            with g.cell():
                st_write(bs.col_title, "While the agent works", tag=t.div)
                _bullets([
                    ((bs.key, "Read its plan"), " before you approve."),
                    ((bs.key, "Prepare the next check"), ": which test, what to look at."),
                    ((bs.key, "Don't type over it"), ": one instruction at a time."),
                    ((bs.key, "Review the diff"), " (", (bs.code, "git diff"), ") before you commit."),
                ])

        with st_block(_punch_box):
            st_write(bs.punch, "If it is not in a file or in git, the next session does not know it.")
