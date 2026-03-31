"""Project-level environment flags for local vs deployed mode.

Variables:
    IS_EDITABLE:  Show image editing panels (default: True in local, False in deployed).
    IS_EXPORTABLE: Show export buttons in sidebar (default: True in local, False in deployed).

Set via environment variables in the Dockerfile or shell:
    ENV STX_EDITABLE=false
    ENV STX_EXPORT=false
"""
import os

IS_EDITABLE = os.environ.get("STX_EDITABLE", "true").lower() == "true"
IS_EXPORTABLE = os.environ.get("STX_EXPORT", "true").lower() == "true"
