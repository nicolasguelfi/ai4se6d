# Pureté de la méthodologie GSE-One — constats et propositions

- **Date** : 2026-07-10 · **Corpus analysé** : gensem @ v0.85.0 (lecture seule — aucun fichier modifié)
- **Question posée** : la méthodologie doit rester générique — ni technologie, ni étude de cas
  (calculatrice/CalcApp) câblée dedans. Le matériel de formation, lui, peut se spécialiser.
- **Méthode** : balayage exhaustif de `gse-one-spec.md` + `gse-one/src/**` (activities, agents,
  principles, templates, references) sur les termes cas-d'étude (calc, CalcApp, expense) et
  technologies (React, Vite, Next.js, Streamlit, Django, Flask, FastAPI, pytest, vitest,
  Playwright, TypeScript, Python, Node, Docker, Hetzner, Coolify, hcloud), puis lecture des
  contextes pour classer chaque occurrence.

## A0. Nommage du concept — RÉSOLU (gensem v0.85.1)

Le corpus s'auto-désignait « GSE-One — **Generic** Software Engineering One » depuis son commit
initial (2026-04-11, v0.8) — glissade de rédaction jamais remarquée. Le concept de l'auteur :
**GSE = Generative Software Engineering**, GSE-One = première instanciation de la méthodologie.
Corrigé le 2026-07-10 : 5 occurrences sources (spec l.1, §1.2, glossaire §16, identités
orchestrateur + lite), régénération 5 plateformes (`--verify`), 125 tests verts, release
**v0.85.1** taguée et poussée (commit `34c7a39`).

## A. Contamination par le cas d'étude de la formation — AVÉRÉE

### A1. Référence littérale « CalcApp » dans l'orchestrateur livré
- **Où** : `gse-one/src/agents/gse-orchestrator.md`, l.140 — *« Failure modes observed (v0.56
  pre-fix): … (b) on **CalcApp sprint 1** the agent silently skipped /gse:go Step 2.6 … »*
- **Nature** : note de modes de défaillance issue d'une session de formation, embarquée dans la
  source distribuée de l'orchestrateur. Seule occurrence littérale de « CalcApp » dans le corpus.
- **Correction proposée** : anonymiser — *« on a beginner training project »* — sans toucher au
  contenu technique de la note (les fixes Prop C restent valables).

### A2. L'exemple fil-rouge du corpus est l'app de la formation (expense tracker)
- **Où** (7 emplacements) :
  - `gse-one-spec.md` l.36 (Quick Start) : *« I want to build a personal expense tracker as a web app »*
  - `gse-one/src/activities/reqs.md` l.82 : thèmes *« Filter expenses by month », « Export to CSV »*
  - `gse-one/src/activities/tests.md` l.80-88 : scénarios Given/When/Then sur les expenses
  - `gse-one/src/activities/design.md` l.87 : table shared-state *Dashboard, Expenses, Budgets*
  - `gse-one/src/activities/produce.md` l.263 : table de réconciliation avec **`src/forms/Expense.tsx`**
  - `gse-one/src/activities/preview.md` l.341 : *« mock data with 3 sample expenses »*
  - `gse-one/src/agents/gse-orchestrator.md` l.259 : résumé débutant *« expenses are sorted by date »*
- **Nature** : exemples illustratifs (pas de comportement câblé) — mais l'identité totale entre
  l'exemple canonique de la méthode et le cas d'étude de la formation montre que la boucle de
  capitalisation formation→méthodologie a déposé l'étude de cas dans la méthode. Le `.tsx` de
  produce.md ajoute de surcroît un biais React/TypeScript à l'exemple.
- **Correction proposée** : politique d'exemples — (1) choisir un fil-rouge d'exemples **différent
  du cas d'étude de formation courant** (ou varier les domaines par activité : une app CLI dans
  reqs, une lib dans tests, un service API dans design…) ; (2) neutraliser les extensions de
  fichiers technologiquement marquées (`Expense.tsx` → `src/forms/expense_form.{ext}` ou un
  exemple non-web). Optionnel : une règle CLAUDE.md côté gensem « les exemples du corpus ne
  reprennent jamais le cas d'étude d'une formation en cours ».

## B. Couplages technologiques comportementaux — décision d'architecture à prendre

### B1. L'activité DEPLOY est structurellement mono-pile (Hetzner + Coolify + Docker)
- **Ampleur** (occurrences dans `src/`) : Coolify **189** (deploy.md 85, deploy-operator.md 37,
  private-repo-github-app-setup.md 42, hetzner-infrastructure.md 14, ssh-operations.md 6…),
  Hetzner 42, Docker 69, hcloud 14 ; **4 templates** `Dockerfile.{streamlit,python,node,static}` ;
  healthcheck Streamlit `/_stcore/health` (Dockerfile.streamlit + deploy.md l.560 — déjà
  conditionné « for Streamlit, `/` for others », donc géré).
- **Nature** : choix assumé (« from zero to live » guidé, une seule pile supportée) — mais la spec
  ne déclare nulle part la **frontière** entre le cœur méthodologique générique (P1-P16,
  LC00-LC03, 23 activités) et ce module opérationnel opinioné (deploy + deploy-operator +
  références infra + templates Docker).
- **Dossier décision (à trancher côté gensem)** :
  1. **Déclarer la frontière dans la spec** (§1 ou §3.8) : « le cœur GSE-One est technologiquement
     neutre ; DEPLOY est un module opérationnel opinioné (pile Hetzner/Coolify/Docker), remplaçable
     sans affecter la méthodologie ». Coût quasi nul, honnêteté architecturale immédiate.
     *Recommandé comme premier pas.*
  2. **Extraire deploy en extension optionnelle** (installable à part). Cohérence maximale, coût
     d'outillage réel (installeur, registre, docs).
  3. **Abstraire le provider** (interface deploy multi-cloud). Coût élevé, bénéfice incertain pour
     un public formation.

### B2. Biais JS/TS dans la recommandation scaffold de PREVIEW
- **Où** : `gse-one/src/activities/preview.md` l.77 — la table de recommandation par domaine
  justifie scaffold pour `web` par *« Modern **JS/TS** scaffolds (Vite, Next.js) are fast »*
  (la liste des frameworks l.64-65 est marquée « etc. », donc illustrative — c'est la
  *justification* qui est marquée).
- **Correction proposée** : reformuler la justification de façon neutre (*« modern web scaffolds
  are fast to generate; setup cost recovered at PRODUCE »*), les exemples restant multi-tech
  (Vite+React, Streamlit, Next.js, React Native, etc.).

## C. Mentions légitimes — aucune action

- **Auto-détection des frameworks de test** (tests.md/spec §6.2, pytest/vitest…) : le mécanisme
  *détecte* l'existant, n'impose rien — c'est l'inverse d'une spécialisation.
- **Exemples multi-tech balancés** : design.md l.87 cite Streamlit *et* React *et* URL param
  (« e.g. ») ; l'exemple P15 (Python `match`, PEP 634) est un exemple d'apprentissage
  interchangeable.
- **Faux positifs** : 9/22 « React » dans src = « **React**ive Workflow », « **React** to alerts ».
- **Hors méthodologie** : INSTALL-OPENCODE.md (doc plateforme), outils mainteneur en Python
  (implémentation), manifests plugins.

## Synthèse

| # | Constat | Gravité | Correction | Coût |
|---|---|---|---|---|
| A1 | « CalcApp sprint 1 » dans gse-orchestrator.md l.140 | moyenne | anonymiser | 1 ligne |
| A2 | Fil-rouge d'exemples = cas d'étude de formation (+ `.tsx`) | moyenne | politique d'exemples + neutralisation | ~7 retouches |
| B1 | DEPLOY mono-pile sans frontière déclarée | décision | déclarer la frontière (option 1) | 1 § de spec |
| B2 | Justification JS/TS du scaffold web | basse | reformulation neutre | 1 ligne |

Le cœur méthodologique (16 principes, lifecycle, décisions, guardrails, traçabilité, tests,
review, compound) est **exempt de couplage technologique** : aucune règle, aucun seuil, aucun
guardrail ne dépend d'une technologie ou du cas d'étude. Les quatre points ci-dessus sont
périphériques (exemples, notes, et le module deploy) — traitables sans toucher à la méthode.
