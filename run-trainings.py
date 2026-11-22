#!/usr/bin/env python3
"""Lanceur local des modules d'ai4se6d — copie adaptée de run-trainings.py.

Copie de streamtex-all-trainings/run-trainings.py (NG 2026-11-22 : « crée une
copie de ce script et rends-la opérationnelle dans ce projet ; on verra plus
tard pour une commande unifiée »). Mêmes gestes : chaque module sur son port
fixe, en arrière-plan, la page d'accueil reliée aux modules locaux, --fresh,
--kill, --list, --lang, et le Chrome de projection.

Usage (depuis la racine du dépôt) :
    uv run python run-trainings.py                    # tous les modules, accueil compris
    uv run python run-trainings.py --fresh --lang fr  # arrête, purge les caches, relance
    uv run python run-trainings.py ai4se6d            # pareil : l'acronyme est accepté
    uv run python run-trainings.py setup coding-agent         # ces modules seuls, par leur nom
    uv run python run-trainings.py --list             # les modules et leurs ports
    uv run python run-trainings.py --kill             # arrêter (ciblé par port)
    uv run python run-trainings.py --ports-offset 100 # une seconde série, à côté
    uv run python run-trainings.py --no-browser

CE QUI EST LANCÉ — les modules de modules/ qui ont un book.py, dans l'ORDRE FIGÉ
de la table MODULES ci-dessous. Le port se calcule sur le rang : un module
découvert en parcourant le disque s'insérerait au milieu et déplacerait les
ports des suivants. Un nouveau module s'AJOUTE À LA FIN de la table. Un
dossier de modules/ absent de la table est signalé à chaque lancement.

LES PORTS — 8600 à 8606 (pas de 1), mesurés libres le 2026-11-22 avec
`lsof -nP -iTCP -sTCP:LISTEN`. Hors des plages des autres lanceurs :
8501-8507 (run-manuals), 8510-8520 (run-postair), 8729-8817 et 8900+
(run-trainings de streamtex-all-trainings), 9000-9099. Les deux lanceurs
peuvent donc tourner ensemble.

LES LIENS ENTRE DOCUMENTS — chaque module lancé reçoit STX_URL_<CLÉ>=
http://localhost:<port> pour chacun des autres. <CLÉ> est la clé de sa carte
dans modules/ai4se6d_collection/collection.toml ([projects.<clé>]) : en local,
les boutons de la page d'accueil ouvrent les modules locaux ; un module non
lancé garde son adresse en ligne.

LA LANGUE VIT DANS L'ADRESSE — `--lang fr` ouvre …/?lang=fr. Les slides
d'ai4se6d sont en anglais : l'option est gardée pour l'identité avec le
lanceur d'origine, elle ne traduit rien.

NON REPRIS — `--html` (export et service des versions HTML locales) et
`--context` : ils dépendent de shared/i18n.py, shared/context.py et
shared/ports.py, propres à streamtex-all-trainings.
"""
from __future__ import annotations

import argparse
import os
import signal
import subprocess
import sys
import tempfile
import time
import webbrowser
from dataclasses import dataclass
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
MODULES_DIR = SCRIPT_DIR / "modules"
SHARED_DIR = MODULES_DIR / "shared-blocks"

ACRONYM = "AI4SE6D"
PORT_BASE = 8600


@dataclass(frozen=True)
class Module:
    """Un module : le nom qu'on tape, son dossier sous modules/, la clé de sa carte d'accueil."""
    name: str
    folder: str
    key: str

    @property
    def book(self) -> Path:
        return MODULES_DIR / self.folder / "book.py"

    @property
    def is_home(self) -> bool:
        return self.name == "home"

    @property
    def env_key(self) -> str:
        """Le suffixe des variables de liens, STX_URL_<…> : celui de streamtex/collection.py."""
        return self.key.upper().replace("-", "_")


#: ORDRE FIGÉ — un nouveau module s'ajoute À LA FIN (aucun port ne bouge).
MODULES: tuple[Module, ...] = (
    Module("home", "ai4se6d_collection", "home"),
    Module("genai-intro", "ai4se6d_genai_intro", "genai-intro"),
    Module("setup", "ai4se6d_setup", "setup"),
    Module("vibecoding", "ai4se6d_vibecoding", "vibecoding"),
    Module("coding-agent", "ai4se6d_coding_agent", "coding-agent"),
    Module("gensem", "ai4se6d_gensem", "gensem"),
    Module("various", "ai4se6d_various", "various"),
)

LOG_DIR = Path(tempfile.gettempdir()) / "streamtex-ai4se6d"

#: Le Chrome de projection — repris tel quel du lanceur d'origine, MÊME profil :
#: une seule instance de projection pour toutes les formations.
CHROME_FLAGS = ("--autoplay-policy=no-user-gesture-required", "--disk-cache-size=1", "--media-cache-size=1")
CHROME_PROFILE = Path.home() / ".trainings-chrome"
CHROME_CANDIDATES = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/usr/bin/google-chrome", "/usr/bin/google-chrome-stable", "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
)


def port_of(m: Module, offset: int = 0) -> int:
    return PORT_BASE + MODULES.index(m) + offset


def all_ports(offset: int = 0) -> list[int]:
    return [port_of(m, offset) for m in MODULES]


def warn_unknown_folders() -> None:
    """Un dossier de modules/ avec un book.py mais absent de MODULES : on le dit, on ne l'invente pas."""
    known = {m.folder for m in MODULES}
    extra = sorted(p.parent.name for p in MODULES_DIR.glob("*/book.py") if p.parent.name not in known)
    if extra:
        print(f"ATTENTION : module(s) non déclaré(s) dans run-trainings.py, donc non lancé(s) : {', '.join(extra)}")
        print("            (l'ajouter À LA FIN de la table MODULES)")


def free_port(port: int, *, bavard: bool = True) -> None:
    """Libère le port (macOS/Linux : lsof ; Windows : netstat)."""
    if sys.platform == "win32":
        try:
            out = subprocess.run(["netstat", "-ano", "-p", "TCP"],
                                 capture_output=True, text=True, timeout=5).stdout
            for line in out.splitlines():
                if f":{port}" in line and "LISTENING" in line:
                    pid = line.strip().split()[-1]
                    if pid.isdigit():
                        subprocess.run(["taskkill", "/F", "/PID", pid], capture_output=True, timeout=5)
        except Exception:
            pass
        return
    try:
        pids = subprocess.run(["lsof", "-ti", f":{port}", "-sTCP:LISTEN"],
                              capture_output=True, text=True, timeout=5).stdout.split()
        if pids:
            if bavard:
                print(f"   port {port} occupé (PID {' '.join(pids)}) — arrêt…")
            for pid in pids:
                try:
                    os.kill(int(pid), signal.SIGTERM)
                except (ProcessLookupError, ValueError):
                    pass
            time.sleep(1.5)
    except FileNotFoundError:
        pass


def kill_all(offset: int = 0) -> None:
    """Arrête les modules d'ai4se6d — et RIEN d'autre : ciblé par PORT, jamais par nom de processus
    (un `pkill streamlit` tuerait aussi les autres lanceurs)."""
    ports = all_ports(offset)
    print(f"Arrêt des modules ai4se6d (ports {ports[0]}-{ports[-1]})…")
    for port in ports:
        free_port(port, bavard=False)
    print("Fait.")


def fresh(mods: list[Module], offset: int = 0) -> None:
    """Repartir d'un état propre pour les SEULS modules demandés : arrêt par port, purge de leur cache de pages
    (.stx_cache) et du bytecode (__pycache__) de leurs dossiers et de shared-blocks."""
    print(f"Arrêt des modules demandés : {', '.join(f'{m.name} ({port_of(m, offset)})' for m in mods)}")
    for m in mods:
        free_port(port_of(m, offset), bavard=False)
    removed = 0
    docs = [m.book.parent for m in mods]
    for racine in [SHARED_DIR] + docs:
        if not racine.exists():
            continue
        caches = list(racine.rglob("__pycache__"))
        if racine in docs:
            caches += list(racine.rglob(".stx_cache"))
        for cache in caches:
            for f in sorted(cache.rglob("*"), reverse=True):
                f.unlink(missing_ok=True) if f.is_file() else f.rmdir()
            cache.rmdir()
            removed += 1
    print(f"Caches purgés : {removed} dossier(s) (__pycache__, .stx_cache).")
    print("Restent à TA main, dans le navigateur :")
    print("  - recharger l'onglet (F5) ;")
    print("  - rechargement forcé (Cmd+Shift+R) — le navigateur cache les médias.")


def launch(m: Module, offset: int, links: dict[str, str]) -> int | None:
    port = port_of(m, offset)
    log_file = LOG_DIR / f"{m.name}.log"
    print(f"Lancement {m.name} (http://localhost:{port})…")
    free_port(port)
    # Rechargement à chaud : Streamlit ne surveille que le dossier du book et PYTHONPATH ;
    # shared-blocks y est posé pour que ses blocs rechargent aussi.
    env = dict(os.environ) | links
    env["PYTHONPATH"] = str(SHARED_DIR) + (os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
    with open(log_file, "w") as lf:
        proc = subprocess.Popen(
            ["uv", "run", "--project", str(SCRIPT_DIR), "streamlit", "run", "book.py",
             "--server.port", str(port), "--server.headless", "true", "--logger.level=warning"],
            # Le dossier du module, comme l'entrypoint Docker : son .streamlit/config.toml et son static/.
            stdout=lf, stderr=subprocess.STDOUT, cwd=str(m.book.parent), env=env,
            **({} if sys.platform != "win32" else {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP}),
        )
    time.sleep(2)
    if proc.poll() is None:
        return port
    print(f"   ÉCHEC — dernières lignes de {log_file} :")
    try:
        for line in log_file.read_text(encoding="utf-8").splitlines()[-15:]:
            print(f"   {line}")
    except OSError:
        pass
    return None


def open_projection_browser(url: str) -> None:
    """Ouvre ``url`` dans le Chrome de projection (instance dédiée, autoplay sonore, profil hors Dropbox).
    Repli : navigateur par défaut."""
    chrome = next((c for c in CHROME_CANDIDATES if Path(c).exists()), None)
    if chrome is None:
        print("Chrome introuvable — ouverture dans le navigateur par défaut "
              "(l'autoplay SONORE des vidéos n'y est pas garanti).")
        webbrowser.open(url)
        return
    CHROME_PROFILE.mkdir(parents=True, exist_ok=True)
    cmd = [chrome, f"--user-data-dir={CHROME_PROFILE}", *CHROME_FLAGS,
           "--no-first-run", "--no-default-browser-check", url]
    with open(LOG_DIR / "chrome-projection.log", "a") as lf:
        subprocess.Popen(cmd, stdout=lf, stderr=subprocess.STDOUT, start_new_session=True)
    print(f"Chrome de projection : {url}  (profil {CHROME_PROFILE})")


def ensure_pdf_export() -> None:
    """L'export PDF du panneau « Download as… » demande playwright ET son Chromium ; installé une fois si absent."""
    check = ("from streamtex.book import _chromium_installed_on_disk as c; "
             "import sys; sys.exit(0 if c() else 1)")
    if subprocess.run(["uv", "run", "python", "-c", check], cwd=str(SCRIPT_DIR),
                      capture_output=True).returncode == 0:
        return
    print("Export PDF : installation de Chromium pour playwright (une fois)…")
    r = subprocess.run(["uv", "run", "python", "-m", "playwright", "install", "chromium"], cwd=str(SCRIPT_DIR))
    if r.returncode != 0:
        print("   ÉCHEC — le PDF ne sera pas proposé ; à la main : uv run python -m playwright install chromium")


def print_list(off: int) -> None:
    print(f"{ACRONYM} — {len(MODULES)} modules (ordre de lancement ; le nom est celui qu'on tape)")
    for m in MODULES:
        absent = "" if m.book.is_file() else "   (book.py absent)"
        print(f"  └ {m.name:<14}{port_of(m, off):>6}   modules/{m.folder}{absent}")
    warn_unknown_folders()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("names", nargs="*", metavar="MODULE",
                    help=f"le nom d'un ou de plusieurs modules (voir --list ; défaut : tous). "
                         f"« {ACRONYM.lower()} » seul vaut « tous ».")
    ap.add_argument("--list", action="store_true", help="les modules et leurs ports")
    ap.add_argument("--kill", action="store_true", help="arrête les modules d'ai4se6d (ciblé par port)")
    ap.add_argument("--fresh", action="store_true",
                    help="arrête les SEULS modules demandés, purge leur .stx_cache (et le bytecode), puis les relance")
    ap.add_argument("--no-browser", action="store_true", help="n'ouvre pas le Chrome de projection")
    ap.add_argument("--lang", metavar="LANG", help="ouvre le document avec ?lang=LANG dans l'adresse")
    ap.add_argument("--ports-offset", type=int, default=0, metavar="N", help="décale tous les ports de N")
    a = ap.parse_args()
    off = a.ports_offset

    if a.list:
        print_list(off)
        return
    if a.kill:
        kill_all(off)
        return

    names = [n for n in a.names if n.upper() not in (ACRONYM, ".")]
    available = [m for m in MODULES if m.book.is_file()]
    if names:
        par_nom = {m.name.lower(): m for m in available}
        if inconnus := [n for n in names if n.lower() not in par_nom]:
            sys.exit(f"{ACRONYM} n'a pas de module {', '.join(inconnus)} — il a : {', '.join(par_nom)}")
        demandes = {n.lower() for n in names}
        mods = [m for m in available if m.name.lower() in demandes]
    else:
        mods = available
    print(f"{ACRONYM} — {len(mods)} module(s)")
    warn_unknown_folders()

    if a.fresh:
        fresh(mods, off)

    links = {f"STX_URL_{m.env_key}": f"http://localhost:{port_of(m, off)}" for m in mods}

    ensure_pdf_export()
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    lances: list[tuple[Module, int]] = []
    for m in mods:
        if port := launch(m, off, links):
            lances.append((m, port))
    if not lances:
        sys.exit("aucun module lancé")

    def url_of(port: int) -> str:
        return f"http://localhost:{port}" + (f"/?lang={a.lang}" if a.lang else "")

    print()
    print("===========================================================")
    print(f"{ACRONYM} — modules locaux")
    print("===========================================================")
    width = max(len(m.name) for m, _ in lances) + 2
    for m, port in lances:
        print(f"  {m.name:<{width}} {url_of(port)}")
    print()
    print("Page d'accueil : ses boutons mènent aux modules lancés ici, les autres à leur version en ligne.")
    print(f"Logs : {LOG_DIR}")
    print("Arrêt : uv run python run-trainings.py --kill")
    print("===========================================================")

    if not a.no_browser:
        open_projection_browser(url_of(next((p for m, p in lances if m.is_home), lances[0][1])))


if __name__ == "__main__":
    main()
