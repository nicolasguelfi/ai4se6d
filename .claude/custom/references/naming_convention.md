# Naming Convention — Hierarchical Category-First

> Complements `coding_standards.md` section 8. This rule takes precedence.

## Rule

All identifiers (block filenames, style IDs, image names) follow **category-first hierarchical naming**:

```
bck_<category>_<topic>.py
```

### Principles

1. **No numbers** — Never use ordinal numbers (b1_, p2_, 01_) in identifiers. Numbers prevent reordering and reuse.
2. **Category first** — The most general concept comes first for alphabetical grouping:
   - `bck_llm_capabilities.py`, `bck_llm_comparison.py`, `bck_llm_tokens.py` cluster together
3. **Topic second** — The most specific concept comes last:
   - `bck_llm_how_work.py` (not `bck_how_llms_work.py`)
4. **Self-sufficient names** — Each name must be understandable without external context:
   - `bck_llm_training` (not `bck_training` — training of what?)
   - `bck_genai_landscape` (not `bck_landscape` — landscape of what?)
5. **Short prefixes only when stable** — Use a category prefix only when the element is permanently tied to that category.

### Applies to

| Identifier type | Pattern | Example |
|---|---|---|
| Block files | `bck_<category>_<topic>.py` | `bck_llm_transformers.py` |
| Style IDs | `<category>_<role>` | `intro_title`, `llm_card_border` |
| Image names | `<category>_<subject>` | `genai_landscape.png` |

### Verification

After adding blocks, run `ls blocks/ | sort` to verify alphabetical clustering.
