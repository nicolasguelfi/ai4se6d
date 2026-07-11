# Registre d'écarts — alignement GSE-One v0.85.x → v0.89.0

Mission : ss12-bics-ai4se6d-alignement — 2026-07-11
Périmètre : gensem v0.85.0 (dernier alignement, effectif ~v0.85.2) → v0.89.0 (courante)
Rapport source : docs/post-audit-reports/2026-07-11-coding-agents-compatibility-train.md
Module concerné : modules/ai4se6d_gensem (170 blocs, ~14 400 lignes) + shared-blocks (glossaire)

Chaque écart a été vérifié en relisant (a) le fichier du support ET (b) la source du corpus
gensem courant citée. Statuts : PÉRIMÉ / NUANCE / ENRICHISSEMENT-OPTIONNEL / EXACT.

---

## PÉRIMÉ — lot mécanique proposé (modes d'installation v0.87.0)

### E1 — bck_gensem_plugin_architecture.py:90 — « auto-detects the 5 platforms »
- Support : `# One-liner (auto-detects the 5 platforms)` (commentaire du bloc de code curl).
- Corpus courant : README.md L78 + L101 — avec exactement UN agent sur le PATH il est
  choisi automatiquement ; avec PLUSIEURS, install.sh s'arrête avant tout téléchargement et
  exige `GSE_PLATFORM=…` ; `GSE_PLATFORM=all` pour tout installer.
- Correction : « auto-picks the single agent on PATH; several → set GSE_PLATFORM ».

### E2 — bck_gensem_plugin_architecture.py:95 — modes CLI périmés
- Support : `--mode plugin|no-plugin|local|sandbox`.
- Corpus courant : README.md L134 + L208 — modes = `project|machine|sandbox` ;
  anciens noms REJETÉS avec message de correspondance (plugin→machine ;
  no-plugin/local→project) ; `--scope`/`GSE_SCOPE` supprimés.
- Correction : `--mode project|machine|sandbox`.

### E3 — bck_gensem_plugin_architecture.py:102-103 — défaut curl et vocabulaire
- Support : « The curl default is a no-plugin install into the project (.claude/, .cursor/, …);
  set GSE_MODE=plugin for a user-scope plugin install. »
- Corpus courant : README.md L101/L134 — le défaut est le mode `project` : tout dans le
  dossier projet, registre à `<project>/.gse/registry`, RIEN dans `$HOME`, projet
  auto-portable (commit/sync) ; `GSE_MODE=machine` pour une installation machine entière.
- Correction : reformuler avec project/machine + auto-contenance.

### E4 — bck_gensem_t8_advanced.py:45 — tooltip « Installation » (mêmes deux erreurs)
- Support : « curl <repo>/install.sh | sh — auto-detects the 5 platforms. Or python3
  install.py --platform … --mode plugin|no-plugin|local|sandbox. »
- Corpus courant : idem E1 + E2.
- Correction : même reformulation (auto-pick single agent + project|machine|sandbox).

---

## NUANCE — à traiter individuellement

### E5 — bck_gensem_t2_cmd_hug.py:47 et :71 — « Only 4–5 explicit questions »
- Support : « Only 4–5 explicit questions needed » (tooltip) et « 4–5 questions only —
  the agent infers the rest from context » (accroche du slide).
- Corpus courant : gse-one-spec.md L1217 (v0.89.0) — 4-5 questions pour un projet typique
  AVEC code existant à inférer ; sur un projet greenfield (rien à inférer) : « up to a
  dozen quick single-tap questions » (aussi spec §0.2 L34).
- Impact pédagogique : l'exercice P1 du cours démarre sur un dossier CalcApp VIDE
  (greenfield) — les apprenants verront ~une douzaine de questions alors que le slide
  en promet 4-5. Risque de confusion en salle.
- Correction proposée : distinguer les deux cas (existant : 4-5 ; greenfield : jusqu'à
  une douzaine de questions rapides à un clic).

### E6 — bck_gensem_plugin_architecture.py:51-66 — arbre du plugin simplifié
- Support : arbre `plugin/` = agents/, rules/, skills/, hooks/, commands/, tools/.
- Corpus courant : `gse-one/plugin/` contient aussi `gse.json` (nouveau v0.86.0, résolution
  Axe 2 uniforme), `settings.json` (identité orchestrateur Claude), `templates/`,
  `references/`, dossiers plateformes codex/gemini/opencode.
- Statut : simplification pédagogique assumée — PAS de contradiction frontale ; à décider
  si on ajoute une ligne (ex. gse.json + settings.json) ou si on laisse tel quel.

---

## ENRICHISSEMENT-OPTIONNEL — nouveautés 0.87-0.89 non enseignées (aucune contradiction)

### E7 — Portabilité du mode project (v0.87.0/v0.88.0)
Une installation Claude `project` voyage avec le dossier (trust dialog + /reload-plugins
sur une autre machine, guardrails actifs immédiatement via .claude/settings.json).
Pertinent en salle (clones, changements de poste). Candidat : tooltip t8 « GSE-One
Everywhere » ou slide plugin_architecture.

### E8 — Préparation de cours (v0.88.0/v0.89.0)
- Épinglage `GSE_VERSION` pour la cohorte (--training-init) — évite le rate limit GitHub
  derrière un NAT unique.
- Récupération en cours de session : app apprenant endommagée → re-lancer /gse:deploy
  (~5 min, depuis le repo GitHub de l'apprenant).
- Préconditions apprenant de /gse:deploy désormais vérifiées déterministiquement par
  l'agent (.env présent, DEPLOY_USER défini, remote origin) au lieu de questions y/n.
Candidat : tooltip du slide /gse:deploy (1-2 entrées).

---

## EXACT — vérifiés contre le corpus courant (aucune action)

- 24 commandes /gse:* = 24 skills (bck_gensem_plugin_architecture, t2_commands, glossaires) —
  activities/ = 24 fichiers ; plugin skills = 24 après copie sélective (rapport §2).
- 11 agents = 10 spécialistes + 1 orchestrateur (plugin/agents/ = 11 fichiers).
- 29 templates (find src/templates -type f = 29).
- ≈240 fichiers 5 plateformes (plugin/ = 244 fichiers).
- 16 principes (src/principles/ = 16 fichiers).
- 3 system hooks + 7 agent behaviors (principles/hooks.md items 2 et 3) — blocs
  plugin_architecture:81, plugin_cursor:72, t4_decisions:248-264, t2_commands:107.
- 13 dimensions HUG (activities/hug.md).
- Statuts plateformes : Claude/Cursor/opencode primaires, Codex/Gemini expérimentaux
  (README L4, spec L327) — t8_advanced cells + glossaire partagé.
- Orchestrateur : agents/gse-orchestrator.md sur Claude (référencé par settings.json,
  spec L312/L325), rules/gse-orchestrator.mdc sur Cursor — bck_gensem_plugin_cursor:34/53/68.
- Forme Cursor /gse-go (tiret) vs /gse:go (deux-points) — practice_p1:114-119 = README L57.
- /gse:deploy : 6 phases, rôles solo/instructor/learner, modes full/partial/app-only/training
  (activities/deploy.md L56-131) — bck_gensem_t7_cmd_deploy.
- /gse:audit cité 2× — activities/audit.md existe.
- Slides /ce-* (plugin_demo_*, plugin_sync, plugin_exercise) : méthode manuelle GenSEMOne
  du cours, hors périmètre GSE-One.
- Étude de cas CalcApp/expense du support : propre au cours — le changement d'exemple du
  corpus (0.85.2, reading tracker) ne s'applique pas au support ; aucune citation de
  l'exemple du corpus trouvée dans les slides.

## À VÉRIFIER MANUELLEMENT

- Néant : aucune capture d'écran de sortie d'outil GSE dans les blocs (images = logos).

---

## Trous de couverture signalés

- v0.85.1 et v0.85.2 (2026-07-10) : aucun rapport post-audit dédié. Contenu vérifié via
  CHANGELOG : 0.85.1 = correction du nom « Generative Software Engineering One » (déjà
  intégrée au support — commit 6eedcd6, Q16 de la mission précédente) ; 0.85.2 = pureté
  méthodologique du corpus (exemple neutre reading tracker, frontière core/DEPLOY §1.4) —
  vérifié sans impact sur les slides (voir EXACT, dernier point).
