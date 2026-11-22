"""Act IV — Where an IDE fits in this course: the editor reads, opencode writes (NG, 2026-11-22)."""
# Source: ai4se-kit/syllabus/ide-guide.md (kit 2026-11-22.3)
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """IDE role slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    lead = Style.create(s.project.titles.body + s.center_txt, "ide_editor_role_lead")
    column_title = Style.create(s.project.titles.subtitle + s.center_txt, "ide_editor_role_column_title")
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    keyword_critical = s.bold + s.project.colors.critical
    takeaway = Style.create(
        s.large + s.italic + s.project.colors.accent + s.center_txt,
        "ide_editor_role_takeaway",
    )
bs = BlockStyles

_LEAD_ZOOM = 90
_GRID_ZOOM = 65  # eight bullets in two columns: scaled to fit one screen like the neighbouring slides

_NOTES = [
    ("The message",
     "Two tools, two roles: opencode CHANGES the project, the editor is for READING it. No step of the course "
     "requires an editor."),
    ("Four uses",
     "Read the whole tree at a glance; see what the agent changed (Source Control, green/red diff); read the "
     "Markdown plans, requirements and reviews in preview; fix one line by hand — save, then tell opencode."),
    ("Why the editor's AI stays off",
     "Two agents overwrite each other; the editor's agent also reads AGENTS.md; completion writes your test for you "
     "(day 2); agent extensions such as Cline, Continue or Kilo bring a second agent back."),
    ("The trap",
     "Committing or syncing from the editor bypasses opencode and GSE-One: commits, branches and merges stay with "
     "them — no Commit or Sync button in the editor."),
    ("Source",
     "The course kit's IDE guide: ai4se-kit/syllabus/ide-guide.md."),
    ("Ask the room",
     "« Who already uses an editor with an AI assistant? What happens if it and opencode edit the same file? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(75):
                st_write(bs.heading, "Where an IDE Fits in This Course", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Where an IDE Fits in This Course", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        with st_block(s.center_txt):
            with st_zoom(_LEAD_ZOOM):
                st_write(
                    bs.lead,
                    (bs.keyword, "opencode"), " changes the project. The editor is for ",
                    (bs.keyword_accent, "reading"), " it. No step requires an editor.",
                    tag=t.div,
                )

            with st_zoom(_GRID_ZOOM), st_grid(
                cols="1fr 1fr",
                gap="32px",
                cell_styles=s.project.containers.callout,
            ) as g:
                with g.cell():
                    st_write(bs.column_title, "Four uses", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered, text_align="left",
                                 item_gap=0.6) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "Read the code"), " — the whole tree at a glance")
                        with l.item():
                            st_write(
                                bs.body, (bs.keyword_accent, "See what the agent changed"),
                                " — Source Control, green/red diff",
                            )
                        with l.item():
                            st_write(
                                bs.body, (bs.keyword_accent, "Read the Markdown"),
                                " — plans, reqs, reviews (preview)",
                            )
                        with l.item():
                            st_write(
                                bs.body, (bs.keyword_accent, "Fix one line by hand"),
                                " — save, then tell opencode",
                            )
                with g.cell():
                    st_write(bs.column_title, "Workshops: the editor's AI stays off", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered, text_align="left",
                                 item_gap=0.6) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword_critical, "Two agents"), " overwrite each other")
                        with l.item():
                            st_write(bs.body, (bs.keyword_warn, "The editor's agent"), " also reads AGENTS.md")
                        with l.item():
                            st_write(
                                bs.body, (bs.keyword_warn, "Completion"),
                                " writes your test for you (day 2)",
                            )
                        with l.item():
                            st_write(
                                bs.body, (bs.keyword_critical, "Agent extensions"),
                                " (Cline, Continue, Kilo) bring a second agent back",
                            )

            st_space("v", "3vh")
            st_write(
                bs.takeaway,
                "Commits, branches and merges stay with opencode and GSE-One: "
                "no Commit or Sync button in the editor.",
                tag=t.div,
            )
