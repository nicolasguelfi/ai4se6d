FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_BROWSER_GATHERUSAGESTATS=false \
    UV_LINK_MODE=copy

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
        curl nginx-light \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Cache-bust: Coolify passes SOURCE_COMMIT automatically. Changing this ARG
# invalidates all subsequent layers.
ARG SOURCE_COMMIT=unknown

# Install dependencies
# .stx-version is copied first: changing the required version invalidates the cache.
# --no-sources ignores [tool.uv.sources] so uv resolves from PyPI instead of local path,
# keeping the streamtex version recorded in uv.lock — the version tested locally.
# (No --upgrade-package: it installed the latest PyPI release, untested here.)
# Then strip the sources section so "uv run" won't try to re-resolve the local path
COPY .stx-version pyproject.toml uv.lock ./
RUN uv sync --no-sources --no-dev && \
    sed -i '/^\[tool\.uv\.sources\]/,/^$/d' pyproject.toml && \
    uv pip install rich jinja2

# ─── OPTIONAL: enable PDF export in the container ───────────────────────
# By default PDF export is DISABLED here to keep the image light (~500 MB).
# The Python `playwright` package is already installed via streamtex[pdf],
# but the Chromium browser binary + its system libs are NOT.
# Without them, the UI shows: "PDF requires streamtex[pdf]" (misleading).
#
# To enable PDF export for all deployed modules, uncomment the line below.
# Cost: +170 MB (Chromium) + ~30 MB (system libs), +30-60s build time.
# The --with-deps flag auto-installs required apt packages (libnss3,
# libatk-bridge, libcups2, libdrm2, libxkbcommon, libxcomposite,
# libxdamage, libxfixes, libxrandr, libgbm, libpango, libcairo,
# libasound2, libatspi2, …) and downloads Chromium into
# /root/.cache/ms-playwright/ (auto-detected by Playwright at runtime —
# no env var needed).
#
# RUN uv run playwright install --with-deps chromium
# ────────────────────────────────────────────────────────────────────────

# Fail the build if the installed streamtex version is older than required.
# Uses importlib.metadata (package registry) — NOT streamtex.__version__
RUN REQUIRED=$(cat .stx-version | tr -d '[:space:]') && \
    INSTALLED=$(uv run python -c "from importlib.metadata import version; print(version('streamtex'))") && \
    echo "streamtex: required >= ${REQUIRED}, installed ${INSTALLED}" && \
    uv run python -c "import sys; \
r = tuple(int(x) for x in '${REQUIRED}'.split('.')); \
i = tuple(int(x) for x in '${INSTALLED}'.split('.')); \
sys.exit(1) if i < r else sys.exit(0)" || \
    { echo "ERROR: streamtex ${INSTALLED} < ${REQUIRED} — aborting build"; exit 1; }

# Copy all modules (shared-blocks included)
COPY modules/ ./modules/

# Nginx configuration for dual-mode (Streamlit + static HTML)
COPY nginx.conf /etc/nginx/nginx.conf

# Entrypoint script (supports dual / static-only / streamlit-only modes)
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# FOLDER is set at runtime by Coolify env var (default: collection hub)
ENV FOLDER="modules/ai4se6d_collection"

# Default nginx redirect snippet (entrypoint regenerates at runtime)
RUN mkdir -p /app/static-html && \
    echo 'return 302 /html/;' > /app/static-html/.nginx-redirect.conf

# Régime d'images (2026-09-11, décision d'auteur) : plus AUCUN réchauffage de
# cache ni export HTML à la construction. L'entrypoint efface et régénère les
# deux, pour le seul module servi (FOLDER), à CHAQUE démarrage — les couches
# de construction étaient jetées avant la première visite (mesuré : 2,6 Go par
# image, 87 Go sur le serveur pour rien). Le cache reste chaud dès la première
# visite : c'est le démarrage qui le garantit, pas l'image.


# STX_SERVE_MODE controls which services start (set at runtime by Coolify)
#   dual           = Nginx (:80) + Streamlit (:8501) — default
#   static-only    = Nginx (:80) only — no interactivity
#   streamlit-only = Streamlit (:8501) only — legacy
ENV STX_SERVE_MODE="dual"

EXPOSE 80 8501

# Health check: Streamlit first, then Nginx static
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health 2>/dev/null \
    || curl -fsL http://localhost:80/html/ -o /dev/null

# Entrypoint handles mode selection, cache refresh, and HTML re-generation
ENTRYPOINT ["/app/entrypoint.sh"]
