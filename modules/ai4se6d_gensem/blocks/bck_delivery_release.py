"""Slide — A release: tag, version number, change log (semantic versioning) (CCSET14, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Release styles."""
    heading = s.project.titles.heading
    version = Style.create(s.project.titles.stat_hero_primary, "release_version")
    body = s.project.titles.body
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(66):
            st_write(bs.heading, "What a Release Is", tag=t.div, toc_lvl="+1", label="Release, version, change log")
            st_write(bs.version, "MAJOR . MINOR . PATCH", tag=t.div)
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, "MAJOR: breaks what users rely on · MINOR: adds · PATCH: fixes")
                with l.item(): st_write(bs.body, "A tag marks the exact commit that was delivered")
                with l.item(): st_write(bs.body, "A change log says what changed, for the people who use it")
            st_write(bs.source, cite("semver2013"), tag=t.div)
