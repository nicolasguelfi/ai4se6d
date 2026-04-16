"""Slide — /gse:deliver: merge, tag, and ship."""
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
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t7cdl_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t7cdl_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t7cdl_acc")
bs = BlockStyles


def build():
    st_marker("/gse:deliver")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:deliver \u2014 Ship the Sprint", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:deliver \u2014 Merge, Tag, Deploy",
                entries=[
                    ("Merge", "Feature branches \u2192 sprint branch \u2192 main. Each merge is a Gate-tier decision (P12). Merge strategy adapted to user expertise (squash vs. merge vs. rebase)."),
                    ("Tag", "Semantic version tag on main after merge. Generates changelog."),
                    ("Optional deploy", "If git.post_tag_hook is configured, deployment runs automatically after tagging. If it fails, proposes rollback (Gate)."),
                    ("Health check", "Warns if health < 5 before delivering. You can proceed but must acknowledge the risk."),
                    ("Archive plan", "Step 9 reads .gse/plan.yaml and generates docs/sprints/sprint-NN/plan-summary.md. The PLN-NNN ID is inherited from plan.yaml.id to preserve P6 traceability. plan.yaml.status is then set to 'completed'."),
                    ("Cleanup", "Merged branches and worktrees are deleted to prevent sprawl (P12)."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            with st_grid(cols="1fr 1fr 1fr 1fr 1fr 1fr", gap="8px") as g:
                for icon, step in [
                    ("\U0001f500", "Merge features"),
                    ("\U0001f500", "Merge to main"),
                    ("\U0001f3f7\ufe0f", "Tag release"),
                    ("\U0001f4dd", "Changelog"),
                    ("\U0001f4e6", "Archive plan"),
                    ("\U0001f9f9", "Cleanup"),
                ]:
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.body, f"{icon} ", (bs.keyword, step))

            st_space("v", 1)

            with st_grid(cols="1fr 1fr", gap="16px") as g:
                with g.cell():
                    with st_block(_cell_acc):
                        st_write(bs.keyword + s.center_txt, "Merge = Gate Decision")
                        st_write(bs.body, "User validates every merge to main")
                with g.cell():
                    with st_block(_cell):
                        st_write(bs.keyword + s.center_txt, "Health < 5 = Warning")
                        st_write(bs.body, "Proceed only with acknowledged risk")
