"""Slide — Test Review: 3 tiers with agile thresholds (STRATEGY / TST-SPEC / IMPL)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_act = s.project.containers.cell_active_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "ttrt_body")
    body_left = Style.create(s.Large + s.text.wrap.hyphens, "ttrt_body_l")
    tier_name = Style.create(s.Large + s.bold + s.project.colors.primary + s.center_txt, "ttrt_name")
    tier_tag = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "ttrt_tag")
    label = Style.create(s.Large + s.bold + s.project.colors.primary, "ttrt_lbl")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "ttrt_acc")

bs = BlockStyles

_TIERS = [
    {
        "name": "STRATEGY",
        "tag": "[STRATEGY]",
        "when": "End of /gse:tests --strategy",
        "trigger": "security-sensitive domain OR complexity_budget > 15 OR --review-strategy",
        "blocks": "HIGH \u2192 blocks /gse:produce (Hard guardrail)",
        "cell": _cell_acc,
    },
    {
        "name": "TST-SPEC",
        "tag": "[TST-SPEC]",
        "when": "End of /gse:tests Step 3",
        "trigger": "\u22651 TST with quality_gap: true OR \u226520 TSTs OR --review-specs",
        "blocks": "HIGH \u2192 blocks /gse:produce (Hard guardrail)",
        "cell": _cell,
    },
    {
        "name": "IMPL",
        "tag": "[IMPL]",
        "when": "/gse:review Step 2e (always runs)",
        "trigger": "Unconditional \u2014 every sprint",
        "blocks": "HIGH \u2192 blocks /gse:deliver",
        "cell": _cell_act,
    },
]


def build():
    st_marker("Test Review \u2014 3 Tiers")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Test Review \u2014 3 Tiers with Agile Thresholds", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Test Review Layering \u2014 spec \u00a7D",
                        entries=[
                            ("Shift-left quality", "Strategy and spec defects caught before code is written against them. The old single post-production pass ran too late."),
                            ("Agile thresholds", "Tiers activate by condition, not by default. Small/low-risk sprints skip upstream tiers. No bureaucracy for simple work."),
                            ("Hard guardrail", "HIGH findings in STRATEGY or TST-SPEC block /gse:produce. MEDIUM/LOW are informational \u2014 they warn but don't stop."),
                            ("CLI flags", "Force a tier manually: --review-strategy, --review-specs, --deep-review (all three)."),
                            ("Light sprints", "Lightweight mode skips STRATEGY and TST-SPEC \u2014 straight to IMPL. Micro mode has no tier review at all."),
                            ("IMPL always runs", "The post-production IMPL tier is unconditional. It is the 5-agent review of /gse:review Step 2e, renamed and refocused on implementation quality."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 0.8)

            with st_zoom(95):
                with st_grid(cols="repeat(auto-fit, minmax(280px, 1fr))", gap="16px") as g:
                    for tier in _TIERS:
                        with g.cell():
                            with st_block(tier["cell"]):
                                st_write(bs.tier_name, tier["name"])
                                st_write(bs.tier_tag, tier["tag"])
                                st_space("v", 0.5)
                                st_write(bs.body_left, (bs.label, "When: "), tier["when"])
                                st_space("v", 0.3)
                                st_write(bs.body_left, (bs.label, "Trigger: "), tier["trigger"])
                                st_space("v", 0.3)
                                st_write(bs.body_left, (bs.label, "Blocks: "), tier["blocks"])

                st_space("v", 1)
                st_write(bs.accent, "Shift-left quality \u2014 strategy defects caught before code is written.")
