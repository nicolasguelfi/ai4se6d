"""AI4SE 6D — Training Collection Hub."""

import streamlit as st
from custom.themes import dark

import streamtex as stx
import streamtex.styles as sts
from streamtex import TOCConfig, NumberingMode, st_book, ViewMode

import blocks

st.set_page_config(
    page_title="AI4SE 6D — Training Collection",
    layout="wide",
    initial_sidebar_state="expanded",
)
sts.theme = dark

st_book(
    [
        blocks.bck_home,
    ],
    toc_config=TOCConfig(
        numbering=NumberingMode.SIDEBAR_ONLY,
        toc_position=None,
        search=True,
        sidebar_max_level=2,
    ),
    paginate=False,
    view_modes=[ViewMode.CONTINUOUS],
)
