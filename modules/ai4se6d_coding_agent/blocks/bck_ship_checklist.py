"""Slide — v0.1 — what you just built."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """v0.1 — what you just built — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "ship_checklist_body")
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "ship_checklist_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "ship_checklist_foot")
bs = BlockStyles

_NOTES = [
    ("The message",
     "A look back at the day: in one day, CalcApp v0.1 went from a starter to a tagged release, and every step "
     "was decided by you."),
    ("What is in v0.1",
     "Two pages with navigation; adding an expense that survives a refresh; 4+ tests, each written before its "
     "code; a review with triage, fixes and one reasoned refusal; a README with your Why; the tag v0.1."),
    ("The point",
     "You drove, the agent typed. That is VibeEngineering: the speed of the agent, the decisions of the "
     "engineer."),
    ("Ask the room",
     "« Which item of this list would be missing if you had just vibe-coded the app? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Tag — v0.1",
     "The label put with git tag v0.1 on the release commit; git tag lists it. Day 3 starts from it."),
]

_ITEMS = [
    ('Two pages with navigation',),
    ('Add an expense — it survives a refresh',),
    ('4+ tests, each written ', (bs.keyword, 'before'), ' its code'),
    ('A review: triage, fixes, one reasoned refusal',),
    ('A README with ', (bs.keyword, 'your'), ' Why'),
    ('A tag: ', (bs.cmd, 'v0.1')),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'v0.1 — What You Just Built', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — v0.1 — What You Just Built", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # one row per item, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(_ITEMS), cols, filled=(2,))
        with st_zoom(113), st_grid(cols=cols, gap="3.5vh 0.5vw", cell_styles=cells) as g:
            for parts in _ITEMS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "4vh")
        with st_zoom(108):
            st_write(bs.foot, 'You drove, the agent typed. That is VibeEngineering.', tag=t.div)
