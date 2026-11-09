"""Act IV — EU AI Act: what it means for you this week (risk levels + official timeline).

Timeline: Regulation (EU) 2024/1689, Art. 113 (entry into force 1 Aug 2024; 2 Feb 2025; 2 Aug 2025;
2 Aug 2026; 2 Aug 2027) as amended by the Digital Omnibus on AI (Commission proposal of
19 Nov 2025), adopted as Regulation (EU) 2026/1744: Council final approval 29 Jun 2026, act of
8 Jul 2026, OJ L of 24 Jul 2026, in force 27 Jul 2026. High-risk application moved to 2 Dec 2027
(stand-alone, Annex III) and 2 Aug 2028 (embedded in products, Annex I).
Status verified on 2026-11-09: https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng and
https://www.consilium.europa.eu/en/press/press-releases/2026/06/29/artificial-intelligence-council-gives-final-green-light-to-simplify-and-streamline-rules/
Do NOT reuse the dates of streamtex-all-trainings' bck_ethics_european_parliament_ai_act (stale).
"""
# Adapted from streamtex-all-trainings@7707c1c5:content/atoms/bck_ethics_risk_based_approach_three_levels.py
# @guideline: maximize-viewport
# @pattern: ptn_comparison_table
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """AI Act slides styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subheading = s.project.titles.section_title + s.center_txt
    tagline = Style.create(
        s.project.titles.subtitle + s.center_txt,
        "ide_ai_act_tagline",
    )
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    header_text = s.project.titles.table_header
    cell_text = s.project.titles.table_cell
    row_label = s.project.titles.table_label
    row_label_active = s.project.titles.table_label_active
    message = Style.create(
        s.project.titles.body + s.center_txt,
        "ide_ai_act_message",
    )
    status = Style.create(
        s.large + s.project.colors.muted + s.center_txt,
        "ide_ai_act_status",
    )
bs = BlockStyles


_RISK_COLS = "1fr 2.2fr 1.4fr"
_RISK_HEADERS = ("Risk level", "What it covers", "What the law asks")
# (level, description, measure, is_highlighted)
_RISKS = [
    ("Unacceptable", "Contrary to EU values (e.g. social scoring)", "Banned", False),
    ("High-risk", "Safety or fundamental rights (hiring, credit, exams…)", "Strict requirements + conformity assessment", True),
    ("Low or minimal", "All other AI systems", "None, or transparency", False),
]

_TIME_COLS = "1fr 2.6fr 1.2fr"
_TIME_HEADERS = ("Date", "What applies", "Status")
# (date, what applies, status, already applies on the course dates)
_MILESTONES = [
    ("1 Aug 2024", "Entry into force", "Done", True),
    ("2 Feb 2025", "Prohibited practices + AI literacy (Art. 4)", "Applies", True),
    ("2 Aug 2025", "General-purpose AI models (LLMs)", "Applies", True),
    ("2 Aug 2026", "Most other rules (transparency, penalties)", "Applies", True),
    ("2 Dec 2027", "High-risk, stand-alone (Annex III)", "Was 2 Aug 2026", False),
    ("2 Aug 2028", "High-risk in products (Annex I)", "Was 2 Aug 2027", False),
]


def _table(cols, headers, rows):
    """Header row + data rows; highlighted rows use the active cell style."""
    with st_grid(cols=cols, gap="8px", cell_styles=s.project.containers.table_header_cell) as g:
        for header in headers:
            with g.cell():
                st_write(bs.header_text, header)
    for first, second, third, active in rows:
        cell = s.project.containers.table_active_cell if active else s.project.containers.table_normal_cell
        label = bs.row_label_active if active else bs.row_label
        with st_grid(cols=cols, gap="8px", cell_styles=cell) as g:
            with g.cell():
                st_write(label, first)
            with g.cell():
                st_write(bs.cell_text, second)
            with g.cell():
                st_write(bs.cell_text, third)


def build():
    # Slide 1 — risk-based approach, and where your coding assistant sits
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "EU AI Act", tag=t.div, toc_lvl="1")
            st_write(bs.tagline, "What it means for you this week", tag=t.div)

            with st_zoom(85):
                _table(_RISK_COLS, _RISK_HEADERS, _RISKS)

            with st_block(s.project.containers.callout):
                st_write(
                    bs.message,
                    "Your coding assistant: generally ", (bs.keyword_accent, "not high-risk"),
                    ". What ", (bs.keyword_warn, "you build"), " with it may be.",
                    tag=t.div,
                )

    st_slide_break()

    # Slide 2 — official timeline + Digital Omnibus status
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.subheading, "AI Act Timeline", tag=t.div, toc_lvl="2")

            with st_zoom(85):
                _table(_TIME_COLS, _TIME_HEADERS, _MILESTONES)

            st_write(
                bs.body,
                (bs.keyword, "Digital Omnibus on AI"),
                " — ",
                (bs.keyword_warn, "now law"),
                ": Reg. (EU) 2026/1744, 27 Jul 2026",
                tag=t.div,
            )
            st_write(
                bs.status,
                "Proposed 19 Nov 2025 · checked on EUR-Lex, 9 Nov 2026",
                tag=t.div,
            )
