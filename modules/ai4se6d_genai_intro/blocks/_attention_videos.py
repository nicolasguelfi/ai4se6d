"""Shared layout of the two « mouse » attention videos (bck_llm_attention_mouse, bck_llm_attention_mouse_prediction).

Not a block (no bck_ prefix): a helper, like _context_charts.py. Copied from streamtex-all-trainings (NG, 2026-11-22:
"l'équivalent des deux blocs qui sont ici"): content/atoms/bck_deep_learning_attention_mouse*.py and the video player
of shared/media.py (`img`, start on view). English videos only (this module is in English), copied from
all-trainings assets/media/videos/attention/ to static/videos/attention/; they are drawn there by
_project/tools/animate_embedding.py (souris.toml, souris-prediction.toml).
"""
from pathlib import Path

import streamlit as st
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


VIDEOS = Path(__file__).resolve().parent.parent / "static" / "videos" / "attention"
_slide_top = Style("justify-content:flex-start;margin-top:0;", "attmouse_slide_top")
_heading = s.project.titles.slide_title + s.center_txt

# The video starts when its slide comes on screen, and starts again from the beginning each time it comes back
# (all-trainings shared/media.py `_START_ON_VIEW`, NG 2026-11-12). In continuous mode every slide is in the page at
# once and autoplay would start them all. The script runs in a one-line iframe placed right after the player (st.html
# drops <script>); it goes up to the block holding the video, pauses and rewinds it while it is off screen.
_START_ON_VIEW = """<script>(function () {
  var w = window.parent, d, f = window.frameElement;
  try { d = w.document; } catch (e) { return; }
  if (!f || !('IntersectionObserver' in w)) return;
  var cell = f.closest('[data-testid="stElementContainer"]');
  if (cell) cell.style.display = 'none';
  function find() {
    for (var n = f.parentElement; n && n !== d.body; n = n.parentElement) {
      var v = n.querySelector('video');
      if (v) return v;
    }
    return null;
  }
  function rewind(v) { v.pause(); try { v.currentTime = 0; } catch (e) {} }
  function wire(v) {
    if (v.__trainingsOnView) return;
    v.__trainingsOnView = true;
    v.autoplay = false;
    new w.IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) { rewind(v); return; }
        try { v.currentTime = 0; } catch (e) {}
        var p = v.play();
        if (p && p.catch) p.catch(function () {});
      });
    }, { threshold: 0.6 }).observe(v);
  }
  var tries = 0, t = w.setInterval(function () {
    var v = find();
    if (v) { wire(v); w.clearInterval(t); } else if (++tries > 40) w.clearInterval(t);
  }, 250);
})();</script>"""


def header(title, tip_title, notes):
    """Title (one line) with the « i » at the top right, in the 95% / 5% header grid."""
    with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
        with h.cell(), st_zoom(60):   # one line, leaves the screen to the video
            st_write(_heading, title, tag=t.div, toc_lvl="1")
        with h.cell():
            st_hover_tooltip(title=tip_title, entries=notes, position="left", width="50vw")
    st_space("v", "1vh")


def video(name, max_vh, muted=True):
    """One video of static/videos/attention, played once (no loop), started when its slide is on screen."""
    st_video(str(VIDEOS / name), autoplay=True, loop=False, muted=muted, max_vw=100, max_vh=max_vh)
    st.iframe(_START_ON_VIEW, height=1)


def slide():
    """The slide box: one screen, top-aligned."""
    return st_slide(style=_slide_top)
