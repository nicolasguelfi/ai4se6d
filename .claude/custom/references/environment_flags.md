# Environment Flags — IS_EDITABLE / IS_EXPORTABLE

> Complements `coding_standards.md`. This rule takes precedence for all AI4SE6D modules.

## Rule

Never hardcode `editable=True` or `editable=False` in a block file.
Always use the environment flag:

```python
from custom.config import IS_EDITABLE

st_ai_image(style, prompt, editable=IS_EDITABLE)
```

Same rule applies to export visibility — use `IS_EXPORTABLE` instead of hardcoded booleans.

## Why

`custom/config.py` reads two environment variables:

| Variable | Default | Local dev | Deployed (Coolify) |
|----------|---------|-----------|-------------------|
| `STX_EDITABLE` | `true` | Image editing panels visible | Set to `false` — panels hidden |
| `STX_EXPORT` | `true` | Export buttons visible | Set to `false` — buttons hidden |

Hardcoding `editable=True` bypasses this mechanism and exposes editing panels
to end users in production.

## Import pattern

Every block that uses `editable=` or checks exportability must import the flag:

```python
from custom.config import IS_EDITABLE
# or, if both are needed:
from custom.config import IS_EDITABLE, IS_EXPORTABLE
```

## Verification

After adding or modifying blocks, run from the module directory:

```bash
grep -r "editable=True" blocks/    # must return 0 results
grep -r "editable=False" blocks/   # must return 0 results
```

Both `True` and `False` literals are forbidden — the flag handles both cases.
