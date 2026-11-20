"""Slide — Day 1 cycle CCSET03 applied to your own project: AI Act, licences, secrets, personal data (edition 2).

Day 1 source blocks (module ai4se6d_vibecoding): bck_ide_ai_act (risk levels, timeline), bck_ide_ai_rules
(rules for this week), bck_gse_solution_plugin (CCSET03). Syllabus: hd01-day1-am.md § EU AI Act and rules for this week.
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Ethics recall styles."""
    cycle = Style.create(s.project.titles.caption + s.center_txt, "ethics_recall_cycle")
    heading = s.project.titles.heading
    label = s.project.titles.label
    item = s.project.titles.table_cell
    card = Style.create(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md, "ethics_recall_card")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "ethics_recall_foot")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

CARDS = [
    ("AI Act", "Risk level: unacceptable, high, low or minimal. Transparency: people must know they deal "
               "with an AI, or with AI-made content."),
    ("Licences", "Your repository's licence, and your dependencies': may you use them this way?"),
    ("Secrets", "Never in git. A leaked key is revoked, not just deleted."),
    ("Personal data", "Keep the fewest, say why and for how long; demo with made-up data."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(64):
            st_write(bs.cycle, "CCSET03 applied — day 1, now on your project", tag=t.div)
            st_write(bs.heading, "Audit Your Own Project", tag=t.div, toc_lvl="1", label="Ethics and compliance, applied")
            with st_grid(cols="repeat(2, 1fr)", gap="18px", cell_styles=bs.card) as g:
                for title, text in CARDS:
                    with g.cell():
                        st_write(bs.label, title, tag=t.div)
                        st_write(bs.item, text, tag=t.div)
            st_write(bs.foot, "Recall: day 1 slides \"EU AI Act\" and \"Rules for This Week\" "
                     "(syllabus hd01 § EU AI Act and rules for this week).", tag=t.div)
            st_write(bs.source, cite("eu-aiact2024"), " · ", cite("eu-gdpr2016"), tag=t.div)
