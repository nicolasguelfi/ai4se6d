"""Slides — 10% vs 25-30%, Fowler quote, Junior vs Senior."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: evidence-insight
# @reuse: bck_gensem_evidence_enterprise, _fowler, human_junior_senior (v01)
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_page_fill = s.project.containers.page_fill_top
_page_fill_center = s.project.containers.page_fill_center


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "ent_body")
    accent = Style.create(
        s.Large + s.bold + s.project.colors.accent + s.center_txt, "ent_acc",
    )
    stat_bad = Style.create(
        s.Huge + s.bold + s.project.colors.critical + s.center_txt, "ent_stat_bad",
    )
    stat_ok = Style.create(
        s.Huge + s.bold + s.project.colors.success + s.center_txt, "ent_stat_ok",
    )
    quote = Style.create(
        s.Large + s.project.colors.highlight + s.center_txt,
        "ent_quote",
    )
    source = s.project.citation + s.large + s.center_txt
    card_title = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.center_txt, "ent_card_t",
    )
    card_sub = Style.create(
        s.large + s.project.colors.muted + s.center_txt, "ent_card_sub",
    )
bs = BlockStyles


def build():
    st_slide_break(marker_label="Enterprise Evidence")

    # ── Slide: 10% vs 25-30% ───────────────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Why Process Matters", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="The Methodology Multiplier — Explained",
                        entries=[
                            ("What Bain found", "Companies that only deployed AI tools saw ~10% productivity gains. Those that also redesigned their processes around AI achieved 25-30%."),
                            ("What McKinsey adds", "It's not enough to save time coding — organizations must redirect that saved time to higher-value work like architecture and review."),
                            ("Why the gap", "Tools alone automate individual tasks. Process transformation restructures how the entire team works — that's where the multiplier comes from."),
                            ("GSE-One link", "GSE-One is exactly this: a structured process that wraps around AI tools to capture the full 25-30% instead of just 10%."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", "15vh")

            with st_grid(
                cols="repeat(auto-fit, minmax(300px, 1fr))",
                gap="32px",
            ) as g:
                with g.cell():
                    with st_block(s.project.containers.callout):
                        st_write(bs.stat_bad, "10%")
                        st_write(bs.body, "gains with tool alone")
                        st_write(bs.source, cite("bain2025"))

                with g.cell():
                    with st_block(s.project.containers.callout):
                        st_write(bs.stat_ok, "25-30%")
                        st_write(bs.body, "gains with tool + method")
                        st_write(bs.source, cite("bain2025"))

    st_slide_break(marker_label="Fowler's Warning")

    # ── Slide: Fowler quote ─────────────────────────────────────────
    with st_block(_page_fill_center):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Fowler's Warning", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Fowler & Booch — What the experts warn",
                        entries=[
                            ("Fowler's point", "Writing code is only a small part of software development. Understanding requirements, designing architecture, managing complexity — AI doesn't replace any of that."),
                            ("Booch's vision", "We are entering a 'third golden age' of SE where deep engineering foundations become MORE important, not less, because AI amplifies both good and bad practices."),
                            ("The warning", "Organizations that try to replace developers with AI will fail. Those that equip developers with AI + methodology will succeed."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 2)
            with st_block(s.project.containers.callout):
                st_write(
                    bs.quote,
                    '"Current enthusiasm for replacing developers with AI '
                    'fundamentally misunderstands what makes software '
                    'development valuable."',
                )
            st_space("v", 2)
            st_write(bs.accent, "Writing code \u2260 building software.")

    st_slide_break(marker_label="Junior vs Senior: The Contradictions")

    # ── Slide: Junior vs Senior ─────────────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Junior vs Senior: The Contradictions", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Junior vs Senior — Why they contradict",
                        entries=[
                            ("Cui (enterprise)", "In structured enterprise settings with mentoring and support, junior developers gained +27-39% productivity with AI."),
                            ("Daniotti (open-source)", "On GitHub without structured support, senior developers captured ALL gains while juniors showed ZERO improvement."),
                            ("METR (experts)", "Experienced developers on their own familiar code were 19% SLOWER with AI — the tool disrupted their existing workflows."),
                            ("The resolution", "Methodology determines who benefits. With structure, everyone gains. Without it, only experts do — and even they can lose."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)

            _studies = [
                ("Cui et al.", "4,867 devs, enterprise", "Juniors +27-39%, Seniors +8-13%",
                 s.project.containers.cell_primary_bg),
                ("METR", "16 devs, OSS", "Seniors -19% slower on familiar code",
                 s.project.containers.cell_accent_bg),
                ("Daniotti", "160K GitHub devs", "Seniors capture ALL gains, Juniors ZERO",
                 s.project.containers.cell_active_bg),
            ]

            with st_grid(
                cols="repeat(auto-fit, minmax(280px, 1fr))",
                gap="16px",
            ) as g:
                for name, scope, finding, bg in _studies:
                    with g.cell():
                        with st_block(bg + s.project.containers.cell_pad_md + s.center_txt):
                            st_write(bs.card_title, name)
                            st_write(bs.card_sub, scope)
                            st_space("v", 0.5)
                            st_write(bs.body, finding)

            st_space("v", 1)
            st_write(
                bs.accent,
                "The relationship is more nuanced than any single study suggests.",
            )
            st_space("v", "30vh")
