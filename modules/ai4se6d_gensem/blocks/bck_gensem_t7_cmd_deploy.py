"""Slide — /gse:deploy: from zero to live in one command."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_act = s.project.containers.cell_active_bg + s.project.containers.cell_pad_md + s.center_txt
_hdr_cell = s.project.containers.table_header_cell
_normal_cell = s.project.containers.table_normal_cell


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t7cd_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t7cd_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t7cd_acc")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "t7cd_hl")
    table_hdr = s.project.titles.table_header
    table_txt = s.project.titles.table_cell
    table_lbl = s.project.titles.table_label
bs = BlockStyles


def build():
    st_marker("/gse:deploy")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:deploy \u2014 From Zero to Live", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:deploy \u2014 Hetzner + Coolify",
                entries=[
                    ("Full pipeline", "Provision server \u2192 harden \u2192 install Coolify \u2192 configure DNS/SSL \u2192 deploy app. One guided flow."),
                    ("3 scenarios", "Zero infrastructure (solo): full provisioning. Pre-configured (training): connect + deploy. Existing: redeploy to current setup."),
                    ("--status", "Show current deployment state without changes."),
                    ("--redeploy", "Rebuild and redeploy the application. Does not provision new server."),
                    ("--destroy", "Tear down server. Gate-tier confirmation required \u2014 irreversible."),
                    ("Post-tag hook", "Can be triggered automatically after /gse:deliver via git.post_tag_hook. If deployment fails, proposes rollback (Gate)."),
                    ("Health check", "Warns if health < 5 before deploying. You can proceed but must acknowledge."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            with st_grid(cols="1fr 1fr 1fr 1fr 1fr", gap="8px") as g:
                for icon, step in [
                    ("\U0001f5a5\ufe0f", "Provision"),
                    ("\U0001f512", "Harden"),
                    ("\u2699\ufe0f", "Coolify"),
                    ("\U0001f310", "DNS/SSL"),
                    ("\U0001f680", "Deploy"),
                ]:
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.body, f"{icon} ", (bs.keyword, step))

            st_space("v", 1)

            with st_grid(cols="30% 70%", gap="8px", cell_styles=_hdr_cell) as g:
                with g.cell():
                    st_write(bs.table_hdr, "Option")
                with g.cell():
                    st_write(bs.table_hdr, "Description")

            for opt, desc in [
                ("/gse:deploy", "Full guided flow: provision \u2192 deploy"),
                ("--status", "Show deployment state (read-only)"),
                ("--redeploy", "Rebuild + redeploy (no new server)"),
                ("--destroy", "Tear down server (Gate \u2014 irreversible)"),
            ]:
                with st_grid(cols="30% 70%", gap="8px", cell_styles=_normal_cell) as g:
                    with g.cell():
                        st_write(bs.table_lbl, opt)
                    with g.cell():
                        st_write(bs.table_txt, desc)
