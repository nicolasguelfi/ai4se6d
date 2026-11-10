"""Slide — Install GSE-One v0.90.0 in your CalcApp folder (exercise E11, step 1, edition 2)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Install slide styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "install_calcapp_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "install_calcapp_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "install_calcapp_foot")
bs = BlockStyles

_GSE = (
    "cd ~/ai4se/calcapp && git switch mywork\n"
    "curl -fsSL https://raw.githubusercontent.com/nicolasguelfi/gensem/v0.90.0/install.sh \\\n"
    "  | GSE_PLATFORM=opencode GSE_VERSION=v0.90.0 sh"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "GSE-One in Your CalcApp", tag=t.div, toc_lvl="+1", label="Install GSE-One in CalcApp")
            st_write(bs.body, "The same command as on day 1, in your project folder this time.", tag=t.div)
            with st_zoom(140):
                st_code(s.none, code=_GSE, language="bash", line_numbers=False)
            st_write(bs.body, "Done when ", (bs.cmd, "cat .gse/registry"), " prints ", (bs.cmd, ".opencode"), tag=t.div)
            st_write(bs.foot, "Then commit the new files: they are part of your project.", tag=t.div)
