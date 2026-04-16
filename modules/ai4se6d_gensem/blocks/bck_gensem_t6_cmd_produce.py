"""Slide — /gse:produce: create code in isolated worktrees."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t6cp_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t6cp_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t6cp_acc")
bs = BlockStyles


def build():
    st_marker("/gse:produce")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:produce \u2014 Build It Right", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:produce \u2014 Isolated Production",
                entries=[
                    ("Step 1", "Create a feature branch + worktree for the task. All work is isolated from main and other tasks."),
                    ("Step 2", "Execute the production plan in the isolated worktree. Code, tests, and docs are committed to the feature branch."),
                    ("Step 3", "Run the test suite after production. Results are attached as evidence (screenshots, coverage, campaign report)."),
                    ("Complexity tracking", "New dependencies detected during production are logged, their complexity cost checked against the sprint budget (P10)."),
                    ("Guardrails", "If the sprint goes over budget: Soft warning at 80%, Gate at 100%. The agent never silently exceeds the budget."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            with st_grid(cols="1fr 1fr 1fr", gap="12px") as g:
                with g.cell():
                    with st_block(_cell_acc):
                        st_write(bs.keyword + s.center_txt, "\U0001f333 Branch + Worktree")
                        st_space("v", 0.5)
                        st_write(bs.body, "Isolated from main")
                        st_write(bs.body, "One branch per task")
                with g.cell():
                    with st_block(_cell):
                        st_write(bs.keyword + s.center_txt, "\u2699\ufe0f Code + Commit")
                        st_space("v", 0.5)
                        st_write(bs.body, "Execute production plan")
                        st_write(bs.body, "Track dependencies")
                with g.cell():
                    with st_block(_cell_acc):
                        st_write(bs.keyword + s.center_txt, "\U0001f9ea Tests + Evidence")
                        st_space("v", 0.5)
                        st_write(bs.body, "Auto-run test suite")
                        st_write(bs.body, "Save campaign report")

            st_space("v", 1)
            st_write(bs.accent, "Every task in its own worktree \u2014 parallel work without interference.")
