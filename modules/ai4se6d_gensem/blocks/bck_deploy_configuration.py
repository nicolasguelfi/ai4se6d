"""Slide — Configuration in environment variables; secrets out of git (CCSET16, edition 2).

Sources: Twelve-Factor App, factor III Config; Meli et al., NDSS 2019 (abstract: secret leakage
"affecting over 100,000 repositories", "thousands of new, unique secrets are leaked every day").
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Configuration styles."""
    heading = s.project.titles.heading
    label = s.project.titles.label
    body = s.project.titles.body
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "deploy_config_cmd")
    stat = Style.create(s.project.titles.body + s.bold + s.center_txt, "deploy_config_stat")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(64):
            st_write(bs.heading, "Configuration and Secrets", tag=t.div, toc_lvl="+1",
                     label="Environment variables and secrets")
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, "Same image, different places: what changes is the ",
                                        (bs.label, "configuration"), ", read from ", (bs.label, "environment variables"),
                                        " (", (bs.cmd, "PORT"), ", a database address, an API key)")
                with l.item(): st_write(bs.body, (bs.label, "Secrets"), " (keys, passwords, tokens) never in the code: ",
                                        (bs.cmd, ".env"), " in ", (bs.cmd, ".gitignore"), ", and a committed ",
                                        (bs.cmd, ".env.example"), " with the names only")
                with l.item(): st_write(bs.body, "A pushed secret is public: deleting the commit is not enough — "
                                        "clones and forks keep it. ", (bs.label, "Revoke the key."))
            with st_block(s.project.containers.callout):
                st_write(bs.stat, "Secrets leaked in over 100,000 public GitHub repositories — "
                         "thousands of new ones every day", tag=t.div)
            st_write(bs.source, cite("wiggins-twelvefactor2011"), " · ", cite("meli-secrets2019"), tag=t.div)
