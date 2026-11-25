"""Slide — Installation step 3: connect your model key with opencode auth login."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Installation step slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    step = Style.create(s.project.titles.caption + s.center_txt, "setup_step_caption")
    body = s.project.titles.body
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    critical = Style.create(s.bold + s.project.colors.critical, "setup_critical")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_CODE_ZOOM = 170  # st_code font_size is not applied by Pygments: zoom instead

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Step 3 of the installation: everyone runs opencode auth login "
     "with the key the trainer sent them (Teams direct message or e-mail), type openrouter and choose OpenRouter; "
     "wait until opencode auth list shows it."),
    ("The message",
     "opencode needs a model to talk to: opencode auth login stores YOUR OpenRouter key. The trainer sends each "
     "learner's key by Teams direct message or e-mail (nicolas.guelfi@ros.lu) — never on paper."),
    ("How",
     "Run the command; in the provider list type openrouter to filter it and choose OpenRouter (the provider of "
     "the course key); paste the key the trainer sent you when asked."),
    ("The rule",
     "A key is a secret: never in a committed file, a prompt, a screenshot or an issue. Whoever has it spends "
     "your budget."),
    ("The trap",
     "« 401 » or « invalid API key » = wrong key or wrong provider: redo this step (see Common Errors)."),
    ("The check",
     "opencode auth list shows the provider you chose."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — opencode auth login",
     "opencode = the coding agent; auth = its credentials (logins) commands; login = add one. It shows a list of "
     "model providers (companies that run the AI models). Typing openrouter filters the list; Enter picks "
     "OpenRouter; then paste the key (Ctrl+Shift+V in the Ubuntu terminal, right-click or Ctrl+V in Windows "
     "Terminal for WSL, Cmd+V on macOS; the key may stay hidden). opencode stores it on your machine, outside every project folder."),
    ("Command — opencode auth list",
     "Lists the providers opencode has a credential for: names only, never the key itself. Done when OpenRouter "
     "is in the list. Inside the agent, /connect does the same as auth login."),
    ("Screen — Select variant (after choosing a model)",
     "A variant = the same model with another reasoning setting: none = no reasoning, low = a little, high = a lot,"
     " max = the most. More reasoning is slower and uses more tokens, so more of your OpenRouter credit. Default ="
     " the provider's own setting. For the course: keep Default (press Esc, or Enter on Default). Later, ctrl+t "
     "switches from one variant to the next."),
    ("Model list — « … Free » marked OpenCode",
     "The same model served by OpenCode Zen, not by OpenRouter: the course key is not used, it needs a Zen "
     "account. Free for a limited time, and the data sent may be used to improve the model. For the course: "
     "choose the line « DeepSeek V4.1 Flash · OpenRouter »."),
    ("Word — OpenRouter",
     "A service that gives access to many AI models (Claude, GPT, open models…) through one key. The trainer's key "
     "has a spending limit: whoever copies it spends that budget."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 3 of 8 · ~10 min", tag=t.div)
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "3 · Your Model Key", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — 3 · Your Model Key", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(100):
            st_write(bs.body, "Your key: sent by the trainer by ", (bs.label, "Teams direct message or e-mail"), ".",
                     tag=t.div)
        st_space("v", "1vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code="opencode auth login", language="bash", line_numbers=False)
        st_space("v", "2vh")
        with st_zoom(120):
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered,
                         text_align="left", item_gap=0.6) as l:
                with l.item():
                    st_write(bs.body, "Type ", (bs.cmd, "openrouter"), ", then choose ", (bs.label, "OpenRouter"))
                with l.item():
                    st_write(bs.body, "Paste your key when asked")
            st_space("v", "2vh")
            st_write(bs.body, (bs.critical, "Never"), " in a committed file, a prompt, a screenshot, an issue.")
            st_space("v", "2vh")
            with st_block(bs.done_box):
                st_write(bs.body, (bs.done_label, "Done when: "), (bs.cmd, "opencode auth list"), " shows it.")
