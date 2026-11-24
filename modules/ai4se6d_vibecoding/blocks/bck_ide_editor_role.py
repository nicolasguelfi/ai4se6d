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
_GRID_ZOOM = 62  # two columns (right one rewritten 2026-11-23, longer): scaled so the slide fits one screen

_NOTES = [
    ("The message",
     "Two tools, two roles: opencode CHANGES the project, the editor is for READING it. The course editor is "
     "VSCodium (in the course VM: VS Code, already installed, its AI already off)."),
    ("Four uses",
     "Read the whole tree at a glance; see what the agent changed (Source Control, green/red diff); read the "
     "Markdown plans, requirements and reviews in preview; fix one line by hand — save, then tell opencode."),
    ("Problems with editors having AI support",
     "Editors such as VS Code or Cursor now ship their own AI: a chat agent that edits files, and completion "
     "(code suggested as you type, accepted with Tab). During the workshops only opencode writes to the project, "
     "so the editor's AI is switched off."),
    ("Why — two agents",
     "Two AI agents writing in the same folder overwrite each other's work, and you no longer know which one "
     "changed what."),
    ("Why — AGENTS.md",
     "The editor's agent also reads AGENTS.md and the GSE-One files, and may act on them: a second, uncontrolled "
     "executor of the same rules."),
    ("Why — completion",
     "Completion writes the code — or the test — in your place. On day 2 you write the test yourself first "
     "(test-first): accepting a suggestion defeats the exercise."),
    ("Why — extensions",
     "AI extensions such as Cline, Continue or Kilo Code put a second agent back into the editor: do not install "
     "them for the course."),
    ("How to switch it off",
     "VSCodium or VS Code: Settings (Cmd+, / Ctrl+,) → search « disable AI features » → tick it "
     "(settings.json: \"chat.disableAIFeatures\": true). VS Code: also sign out of Copilot. Cursor: do not use it "
     "during the workshops — its agent is the editor itself. Source: ai4se-kit/syllabus/ide-guide.md §1, §2, §7."),
    ("The trap",
     "Committing or syncing from the editor bypasses opencode and GSE-One: commits, branches and merges stay with "
     "them — no Commit or Sync button in the editor."),
    ("Source",
     "The course kit's IDE guide: ai4se-kit/syllabus/ide-guide.md; for opencode itself: syllabus/opencode-guide.md "
     "(cheat sheet)."),
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
        st_space("v", "1vh")
        with st_block(s.center_txt):
            with st_zoom(_LEAD_ZOOM):
                st_write(
                    bs.lead,
                    (bs.keyword, "opencode"), " changes the project. The editor is for ",
                    (bs.keyword_accent, "reading"), " it. The course editor: ",
                    (bs.keyword, "VSCodium"), " (in the VM: VS Code, AI already off).",
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
                    st_write(bs.column_title, "Problems with Editors having AI support", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered, text_align="left",
                                 item_gap=0.6) as l:
                        with l.item():
                            st_write(
                                bs.body, (bs.keyword_critical, "Two AI agents"),
                                " in one folder overwrite each other's work",
                            )
                        with l.item():
                            st_write(
                                bs.body, (bs.keyword_warn, "The editor's AI"),
                                " also reads AGENTS.md and acts on it",
                            )
                        with l.item():
                            st_write(
                                bs.body, (bs.keyword_warn, "AI completion"),
                                " writes your code, even the test you must write (day 2)",
                            )
                        with l.item():
                            st_write(
                                bs.body, (bs.keyword_critical, "AI extensions"),
                                " (Cline, Continue, Kilo Code) add a second agent",
                            )
                    st_space("v", "1vh")
                    st_write(
                        bs.body + "text-align:left;", (bs.keyword_accent, "So: "),
                        "Settings → « disable AI features » → tick it. No AI extensions.",
                        tag=t.div,
                    )

            st_space("v", "3vh")
            st_write(
                bs.takeaway,
                "Commits, branches and merges stay with opencode and GSE-One: "
                "no Commit or Sync button in the editor.",
                tag=t.div,
            )
