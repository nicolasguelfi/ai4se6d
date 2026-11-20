"""Slide — When it breaks: roll back to the last version that worked (CCSET16, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Rollback styles."""
    heading = s.project.titles.heading
    label = s.project.titles.label
    body = s.project.titles.body
    lesson = Style.create(s.project.titles.body + s.bold + s.center_txt, "deploy_rollback_lesson")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(66):
            st_write(bs.heading, "When It Breaks: Roll Back", tag=t.div, toc_lvl="+1", label="Rollback")
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, (bs.label, "Roll back first, debug after"), ": redeploy the last "
                                        "version that worked")
                with l.item(): st_write(bs.body, "Only possible if you kept it: tagged releases, the previous image, "
                                        "one change per deployment")
                with l.item(): st_write(bs.body, "Data is the hard part: a changed database does not go back by itself")
                with l.item(): st_write(bs.body, "Measured by teams: how often a change fails, how long it takes "
                                        "to restore the service")
            with st_block(s.project.containers.callout):
                st_write(bs.lesson, "A deployment you cannot undo is a bet.", tag=t.div)
            st_write(bs.source, cite("humble-farley-cd2010"), " · ", cite("forsgren-accelerate2018"), tag=t.div)
