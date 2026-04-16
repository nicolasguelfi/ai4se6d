"""P8 — Autonomous sprint on CalcApp — 3 scenarios by IT expertise."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: exercise-flow
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_pfc = s.project.containers.page_fill_center
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_act = s.project.containers.cell_active_bg + s.project.containers.cell_pad_md + s.center_txt
_hdr = s.project.containers.table_header_cell
_norm = s.project.containers.table_normal_cell


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.text.wrap.hyphens, "p8_body")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "p8_acc")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "p8_hl")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "p8_kw")
    timer = Style.create(s.Huge + s.bold + s.project.colors.highlight + s.center_txt, "p8_timer")
    table_hdr = s.project.titles.table_header
    table_txt = s.project.titles.table_cell
    table_lbl = s.project.titles.table_label
bs = BlockStyles

_left = Style("text-align: left;", "p8_left")

_FEATURES = [
    ("Dark/Light theme", "Low", "2-3 pts"),
    ("CSV export/import", "Low-Medium", "3-4 pts"),
    ("Date range filtering", "Low-Medium", "3-4 pts"),
    ("Data visualization", "Medium", "4-5 pts"),
    ("Recurring expenses", "Medium", "5-6 pts"),
    ("Multi-currency API", "High", "7-8 pts"),
]


def build():
    st_slide_break(marker_label="P8: Autonomous Sprint")

    # ── Slide 1: Feature table ──────────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "P8: Autonomous Sprint \u2014 Choose a Feature", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="Your Autonomous Sprint",
                entries=[
                    ("Goal", "Execute a complete GSE-One sprint on your own. No guidance from the trainer."),
                    ("Budget", "45 minutes \u2014 choose a feature that fits your IT expertise level."),
                    ("Success criteria", "Plan + requirements + code + tests + review + merge + compound.md."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

            with st_zoom(90):
                with st_grid(cols="40% 25% 15%", gap="6px", cell_styles=_hdr) as g:
                    for h in ("Feature", "Complexity", "Points"):
                        with g.cell():
                            st_write(bs.table_hdr + s.center_txt, h)

                for feat, comp, pts in _FEATURES:
                    with st_grid(cols="40% 25% 15%", gap="6px", cell_styles=_norm) as g:
                        with g.cell():
                            st_write(bs.table_lbl + s.center_txt, feat)
                        with g.cell():
                            st_write(bs.table_txt + s.center_txt, comp)
                        with g.cell():
                            st_write(bs.table_txt + s.center_txt, pts)

    st_slide_break(marker_label="P8: Beginner")

    # ── Beginner ────────────────────────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "P8: Autonomous Sprint \u2014 Beginner", tag=t.div, toc_lvl="+1")
            st_space("v", 1)

            with st_grid(
                cols="1fr 1fr",
                gap="16px",
                cell_styles=s.project.containers.cell_pad_sm,
            ) as g:
                with g.cell():
                    with st_block(_cell + _left):
                        with st_list(l_style=bs.body + _left, li_style=bs.body + _left, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body + _left, (bs.keyword, "1. "), (bs.keyword, "Recommended feature: "), "Dark/Light theme (2-3 pts)")
                            with l.item():
                                st_write(bs.body + _left, (bs.keyword, "2. "), (bs.keyword, "Use /gse:go exclusively "), "\u2014 let the agent guide the entire cycle")
                with g.cell():
                    with st_block(_cell + _left):
                        with st_list(l_style=bs.body + _left, li_style=bs.body + _left, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body + _left, (bs.keyword, "3. "), (bs.keyword, "Success: "), "sprint completed + compound.md written")
                            with l.item():
                                st_write(bs.body + _left, (bs.keyword, "4. "), (bs.keyword, "If stuck: "), "ask the agent \u201cwhat should I do next?\u201d")

            st_space("v", 1)
            st_write(bs.accent, "Goal: complete your first solo sprint from start to finish.")
            st_space("v", 1)
            st_write(bs.timer, "45 minutes")

    st_slide_break(marker_label="P8: Intermediate")

    # ── Intermediate ────────────────────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "P8: Autonomous Sprint \u2014 Intermediate", tag=t.div, toc_lvl="+1")
            st_space("v", 1)

            with st_grid(
                cols="1fr 1fr",
                gap="16px",
                cell_styles=s.project.containers.cell_pad_sm,
            ) as g:
                with g.cell():
                    with st_block(_cell_acc + _left):
                        with st_list(l_style=bs.body + _left, li_style=bs.body + _left, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body + _left, (bs.keyword, "1. "), (bs.keyword, "Recommended: "), "CSV export (3-4 pts) or Data visualization (4-5 pts)")
                            with l.item():
                                st_write(bs.body + _left, (bs.keyword, "2. "), (bs.keyword, "Use individual commands "), "\u2014 collect \u2192 assess \u2192 plan \u2192 reqs \u2192 design \u2192 preview \u2192 produce \u2192 tests \u2192 review \u2192 fix \u2192 deliver \u2192 compound")
                with g.cell():
                    with st_block(_cell_acc + _left):
                        with st_list(l_style=bs.body + _left, li_style=bs.body + _left, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body + _left, (bs.keyword, "3. "), (bs.keyword, "Success: "), "all 7 criteria met (plan, reqs, code, tests, review, merge, compound)")
                            with l.item():
                                st_write(bs.body + _left, (bs.keyword, "4. "), (bs.keyword, "Challenge: "), "stay within your complexity budget")

            st_space("v", 1)
            st_write(bs.accent, "Goal: demonstrate mastery of all individual commands in sequence.")
            st_space("v", 1)
            st_write(bs.timer, "45 minutes")

    st_slide_break(marker_label="P8: Advanced / Expert")

    # ── Advanced / Expert ───────────────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "P8: Autonomous Sprint \u2014 Advanced / Expert", tag=t.div, toc_lvl="+1")
            st_space("v", 1)

            with st_grid(
                cols="1fr 1fr",
                gap="16px",
                cell_styles=s.project.containers.cell_pad_sm,
            ) as g:
                with g.cell():
                    with st_block(_cell_act + _left):
                        with st_list(l_style=bs.body + _left, li_style=bs.body + _left, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body + _left, (bs.keyword, "1. "), (bs.keyword, "Recommended: "), "Multi-currency API (7-8 pts)")
                            with l.item():
                                st_write(bs.body + _left, (bs.keyword, "2. "), (bs.keyword, "Add a spike: "), "/gse:task --spike to evaluate the external currency API before committing")
                with g.cell():
                    with st_block(_cell_act + _left):
                        with st_list(l_style=bs.body + _left, li_style=bs.body + _left, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body + _left, (bs.keyword, "3. "), (bs.keyword, "Success: "), "all 7 criteria + health score >7 + compound.md with 3+ patterns")
                            with l.item():
                                st_write(bs.body + _left, (bs.keyword, "4. "), (bs.keyword, "Challenge: "), "write methodology feedback (Axe 2) in /gse:compound")

            st_space("v", 1)
            st_write(bs.accent, "Goal: push the methodology to its limits and provide feedback on GSE-One itself.")
            st_space("v", 1)
            st_write(bs.timer, "45 minutes")

    st_slide_break(marker_label="Go!")

    # ── Go! slide ───────────────────────────────────────────────────
    with st_block(_pfc):
        with st_block(s.center_txt):
            st_write(bs.highlight, "Complete sprint. No guidance. You drive.")
            st_space("v", 2)
            st_image(
                s.none, width="15%",
                uri="images/managed/GSE/images/logo-gse-geni-with-shield.webp",
            )
            st_space("v", 2)
            st_write(bs.timer, "45 minutes")
