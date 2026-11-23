"""Slide — The Copilot Effect: what the largest RCT tells us."""
# @guideline: maximize-viewport
# @pattern: ptn_stat_hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Copilot RCT stat-hero styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = s.project.titles.stat_hero_primary
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    source = s.project.citation + s.large + s.center_txt
    transition = Style.create(
        s.Large + s.italic + s.center_txt + s.project.colors.muted,
        "ve_evidence_rct_transition",
    )
bs = BlockStyles

_NOTES = [
    ('The message',
     'The same tool can save half the time or cost time: it depends on the task.'),
    ('−55.8%',
     'Peng et al. (2023), a randomized controlled trial on GitHub Copilot: developers with Copilot finished a simple, well-defined lab task in 55.8% less time.'),
    ('+19%',
     'METR (2025): experienced developers on their own real repositories took 19% MORE time with AI tools (see « The METR Paradox »; the February 2026 update follows newer tools).'),
    ('The difference',
     'Complexity and discipline: a small, closed task suits generation; a large code base with its history and constraints needs context, review and tests — the VibeEngineering principles.'),
    ('Ask the room',
     '« Which of your tasks look like the lab task, and which like the real repo? »'),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            # title and « i » on the same line, title smaller (NG, 2026-11-23)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(100):
                    st_write(bs.heading, "The Copilot Effect", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — The Copilot Effect", entries=_NOTES,
                                     position="left", width="50vw")
            st_space("v", "2vh")

            with st_grid(
                cols="1fr 1fr",
                gap="32px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_write(bs.stat + s.project.colors.success + "zoom:0.7;", "\u221255.8%")   # green: a gain (NG, 2026-11-23)
                    st_space("v", 0.5)
                    st_write(
                        bs.body,
                        "time on a ",
                        (bs.keyword, "simple lab task"),
                    )
                    st_space("v", 0.5)
                    # REF: Peng et al. 2023, arXiv 2302.06590
                    st_write(bs.source, cite("peng-copilot2023"))

                with g.cell():
                    st_write(bs.stat + s.project.colors.critical + "zoom:0.7;", "+19%")   # crimson: a loss (NG, 2026-11-23)
                    st_space("v", 0.5)
                    st_write(
                        bs.body,
                        "time on ",
                        (bs.keyword_warn, "real repo issues"),
                    )
                    st_space("v", 0.5)
                    # REF: METR 2025 (arXiv 2507.09089) + Feb 2026 update
                    st_write(bs.source, cite("metr2025"), " · ", cite("metr-uplift2026"))

            st_space("v", 2)
            with st_zoom(150):
                st_write(
                    bs.body,
                    "The difference? ",
                    (bs.keyword_accent, "Complexity"),
                    " and ",
                    (bs.keyword_accent, "discipline"),
                    ".",
                )
            st_space("v", "2vh")
            st_write(bs.transition, "Who benefits the most? \u2192")
