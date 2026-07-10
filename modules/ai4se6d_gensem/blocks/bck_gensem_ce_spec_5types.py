"""Slide — 5 dimensions you can change when deriving your methodology."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Derivation dimensions slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    locator = s.project.colors.muted
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles


def build():
    st_marker("5 Derivation Dimensions")
    with st_block(s.project.containers.page_fill_top):
        with st_grid(
            cols="95% 5%",
            gap="0px",
            cell_styles=s.project.containers.grid_cell_centered,
        ) as g:
            with g.cell():
                with st_zoom(90):
                    st_write(bs.heading, "Deriving Your Methodology — 5 Dimensions You Can Change", tag=t.div, toc_lvl="+1")
            with g.cell():
                st_hover_tooltip(
                    title="Derivation Dimensions (Fork Level)",
                    entries=[
                        ("Why derive", "Different domains (medical, financial, safety-critical) need different phases, quality gates, and review criteria."),
                        ("Two levels", "Light specialization needs no fork (.gse/config.yaml). Deep specialization — new phases, new artifacts — means forking the methodology repo."),
                        ("Five dimensions", "Redefine phases, add/remove phases, redefine artifacts, strengthen gates, encode domain knowledge — each maps to a real location in the repo."),
                    ],
                    scale="2vw", width="70vw", position="left",
                )
        st_space("v", 1)

        with st_zoom(120):
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "Redefine phases"),
                        " (e.g., threat-model → design → implement → pentest → harden) — ",
                        (bs.locator, "src/activities/"),
                        " + the orchestrator's lifecycle sequences",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "Add or remove phases"),
                        ' (e.g., add "ethical review") — same, plus ',
                        (bs.locator, "config.yaml order"),
                        " for per-project reordering",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "Redefine artifacts"),
                        " (exact structure, content, format per phase) — ",
                        (bs.locator, "src/templates/"),
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "Strengthen quality gates"),
                        " (domain-specific verification criteria) — principles P7/P11 + review checklists (",
                        (bs.locator, "review.custom_checks"),
                        ")",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "Encode domain knowledge"),
                        " (medical, financial, safety-critical rules) — agent checklists + config custom checks",
                    )

            st_space("v", 2)

            with st_block(s.project.containers.callout):
                st_write(
                    bs.closing,
                    "Light specialization needs no fork (.gse/config.yaml). "
                    "Deep specialization — new phases, new artifacts — means forking the methodology repo; "
                    "GSE-One ships the tooling for it (generator, verify, meta-audit).",
                )
