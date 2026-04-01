#!/bin/bash
# StreamTeX container entrypoint — supports three serve modes:
#   dual           (default) Nginx + Streamlit — static fallback on error
#   static-only    Nginx only — no Streamlit, minimal resources
#   streamlit-only Streamlit only — legacy behaviour (no Nginx)
#
# Env vars:
#   FOLDER          module to serve (e.g. modules/ai4se6d_genai_intro)
#   STX_SERVE_MODE  dual | static-only | streamlit-only (default: dual)

set -e

FOLDER="${FOLDER:-modules/ai4se6d_collection}"
MODE="${STX_SERVE_MODE:-dual}"

cd /app/${FOLDER}

# --- Always: refresh cache and generate static HTML ---

echo "[entrypoint] Mode: ${MODE} | Folder: ${FOLDER}"

# Clear stale caches
rm -rf .stx_cache .streamlit/cache

# Re-warm the page cache (for Streamlit fast first load)
if [ "$MODE" != "static-only" ]; then
    echo "[entrypoint] Warming up page cache..."
    uv run stx cache warmup . 2>/dev/null || true
fi

# Generate static HTML export (only in dual/static-only modes)
if [ "$MODE" != "streamlit-only" ]; then
    echo "[entrypoint] Generating static HTML..."
    uv run stx export html --output /app/static-html/ . 2>/dev/null || true

    # Create a simple index.html redirect if the export didn't produce one
    if [ ! -f /app/static-html/index.html ]; then
        HTML_FILE=$(find /app/static-html/ -name "*.html" -maxdepth 2 | head -1)
        if [ -n "$HTML_FILE" ]; then
            REL_PATH="${HTML_FILE#/app/static-html/}"
            echo "<meta http-equiv=\"refresh\" content=\"0;url=${REL_PATH}\">" \
                > /app/static-html/index.html
        fi
    fi
fi

# --- Start services based on mode ---

case "$MODE" in
    static-only)
        echo "[entrypoint] Starting Nginx (static-only)..."
        exec nginx -g "daemon off;"
        ;;
    streamlit-only)
        echo "[entrypoint] Starting Streamlit (no Nginx)..."
        exec uv run streamlit run book.py \
            --server.port=8501 --server.address=0.0.0.0
        ;;
    dual|*)
        echo "[entrypoint] Starting Nginx + Streamlit (dual mode)..."
        nginx
        exec uv run streamlit run book.py \
            --server.port=8501 --server.address=0.0.0.0
        ;;
esac
