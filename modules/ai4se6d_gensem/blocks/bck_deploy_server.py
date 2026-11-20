"""Slide — The server and the address: port, domain, HTTPS, a deployment platform (CCSET16, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Server styles."""
    heading = s.project.titles.heading
    label = s.project.titles.label
    body = s.project.titles.body
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "deploy_server_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "deploy_server_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(66):
            st_write(bs.heading, "The Server and the Address", tag=t.div, toc_lvl="+1", label="Server, port, domain")
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, (bs.label, "Server"), ": a machine that runs your containers day and "
                                        "night — not your laptop")
                with l.item(): st_write(bs.body, (bs.label, "Port"), ": the container listens on one (CalcApp: ",
                                        (bs.cmd, "3000"), "); the server routes the address to it")
                with l.item(): st_write(bs.body, (bs.label, "Domain and HTTPS"), ": a name that points to the server, "
                                        "a certificate so the browser trusts it")
                with l.item(): st_write(bs.body, (bs.label, "Deployment platform"), ": does the chores — fetches your "
                                        "repository, builds the image, runs the container, routes the domain, "
                                        "restarts it when it crashes")
            with st_block(s.project.containers.callout):
                st_write(bs.body, "Your part: a Dockerfile that builds, an app that listens on the expected port, "
                         "and a configuration kept out of the code.", tag=t.div)
            st_write(bs.foot, "The course set-up comes after the GSE-One slide.", tag=t.div)
