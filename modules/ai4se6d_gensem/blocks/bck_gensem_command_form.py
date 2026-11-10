"""Slide — Command form: the slides write /gse:…, in opencode you type /gse-… (decision P3, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Command form styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "command_form_body")
    big = Style.create(s.project.titles.stat_hero_primary, "command_form_big")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "command_form_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "command_form_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(72):
            st_write(bs.heading, "One Command Form", tag=t.div, toc_lvl="+1", label="Command form in opencode")
            st_write(bs.body, "Some slides show ", (bs.cmd, "/gse:plan"), " — the Claude Code form.", tag=t.div)
            st_write(bs.big, "/gse-plan", tag=t.div)
            st_write(bs.body, "In opencode, always type the dash form: ", (bs.cmd, "/gse-…"), tag=t.div)
            st_write(bs.foot, "Same command, same behaviour — only the separator changes.", tag=t.div)
