# Édition 2 — décisions de préparation

**Date** : 2026-11-09
**Édition** : DLH, 26-27/11, 03-04/12, 10-11/12/2026 — NG seul (Tiago Sousa ne fait plus partie de la formation et a transféré à NG la propriété de ses supports)
**Source** : planches de décision `ai4se1` et `gsel1` (session Claude `ss2-ul-gse`, 2026-11-08/09) ; rapport d'état des lieux (artefact « AI4SE — état des lieux », v3)
**Branche de travail** : `edition2` (un push sur `main` redéploie les 4 apps Coolify : on ne fusionne qu'une fois l'édition prête)

## 1. Décisions (planche `ai4se1`)

| # | Sujet | Décision | Remarque / résolution |
|---|---|---|---|
| 1 | Statut DLH | Message à DLH (inscrits, contrat, salle) **sans attendre** pour travailler | NG est sûr qu'il y aura une édition |
| 2 | Ambition | Rafraîchissement **ciblé** | ≈ 17-20 j au total |
| 3 | Organisation | Viser **tout avant le 26/11**, l'ordre des 3 vagues sert de priorité si le temps manque | |
| 4 | Agent apprenants | **opencode** principal ; Cursor gratuit comme simple éditeur si besoin | Pas de sièges Cursor Pro |
| 5 | Accès modèles | **Une clé plafonnée par apprenant** (type OpenRouter) | Modèles gratuits opencode Zen limités par IP : écartés |
| 6 | Machines | VM DLH de référence ; portables personnels acceptés ; installation en salle pour qui n'est pas prêt ; liste de contrôle à J-7 | Pas de session à distance |
| 7 | GSE-One | v0.89.1 retenue, puis **v0.90.0** (intégration de la PR #11 opencode 2, décidée par NG) — version épinglée pour la formation | Voir § 3 |
| 8 | Dépôts de Tiago | Nouveaux dépôts privés : `nicolasguelfi/ai4se6d-decks`, `nicolasguelfi/calcapp-course` (créés le 2026-11-09) | |
| 9 | Jour 2 | Import **condensé** du deck de Tiago en StreamTeX, dans ai4se6d | Cible ai4se6d choisie par NG (QCM) |
| 10 | CalcApp | **Starter épinglé** (Vite 7, Vitest 4, React Router 7, TS 5.9, package-lock) | |
| 11 | Outils jour 1 | **Acte IV** (bck_ide_*) réactivé + blocs opencode et LLM locaux repris de Tiago | |
| 12 | Encadrement | NG **seul**, sans dispositif particulier | Risque accepté |
| 13 | Démo jour 6 | **Supprimée** | Absente du programme publié |
| 14 | Traces de Tiago | **Retirer** sa fiche formateur et les mentions ; pas de crédit | |
| 15 | Mini-projet | Projet professionnel sous GSE-One, cadré par écrit | |
| 16 | Confidentialité | Pas de règle | Risque accepté |
| 17 | Évaluation | **Présence** seulement (certificat) | Écart connu avec le cahier des charges DLH (évaluation continue par tests) |
| 18 | Contenu GenAI | Rafraîchissement **ciblé** (LLM, outils, éthique/AI Act) | |
| 19 | gse-light | **Pas** présenté dans le cours | |
| 20 | Programme DLH | **Ne rien faire** | Une phrase de cadrage en ouverture du jour 1 (le programme annonce Cursor) |
| 21 | Secrets | Rotation **maintenant et après** la formation (par NG) | |
| 22 | StreamTeX | **Monter ai4se6d en 0.7.82** maintenant | Validation avant/après ; fait en premier pour découvrir les casses tôt |
| 23 | Lieu | Rester dans ai4se6d, **migrer après le 11/12** | |
| 24 | Langue | Slides en **anglais** | |

## 2. Décisions (planche `gsel1`, gse-light → GSE-One)

- Avant la formation : B2 (pas de livraison sur HIGH ouvert sans décision), B5 (deploy ne lit plus `.env` en entier), correction du README (installation épinglée), B6 (CI sur push) — **livrés en v0.89.1** ; B1 (script `check-learner.sh`) et B7 (vue formateur en lecture seule) **côté formation**.
- Après la formation : versions GSE-One de B1 et B7, puis B4, A2, A3, A1, B3, A5, A4, B8, B9, B10.
- Backlog : A7, B11, B15.
- Forme : les choix candidat par candidat sont respectés (pas de « tout livrer maintenant »).

## 2bis. Décisions pédagogiques (planche `peda1`, 2026-11-09)

Analyse qualitative du contenu et de la forme (dépôts des apprenants d'avril, revues de mars-avril, errata, rapport de retours). Ces choix **remplacent** les décisions 2, 3, 9 et 13 de la planche `ai4se1` et **complètent** la 12.

| # | Sujet | Décision NG | Conséquence retenue |
|---|---|---|---|
| P1 | Ampleur | **Refonte complète, en trois phases** : jours 1-2, puis jours 3-4, puis jours 5-6 (« on verra bien ce qu'on arrive à faire ») | Remplace les décisions 2-3. Calendrier en § 2ter |
| P2 | Jour 2 | **Plan B** : restructuré autour de CalcApp, git d'abord (35 min), pilotage d'opencode, le plan de l'apprenant pilote la construction, revue IA HIGH/MEDIUM/LOW, diapositive pont vers GSE-One | Remplace la décision 9. Starter avec étiquettes `j2-start`, `j2-part1`, `j2-v0.1` |
| P3 | opencode | **Passe complète** des supports (`/gse-…` dans les pratiques, bandeau dans la théorie, bloc « GSE-One dans opencode ») | |
| P4 | Rattrapage | **Starter public + étiquettes de reprise + répétition générale** | Diapositive « En retard de plus de 15 min ? » |
| P5 | Formateur seul | **Agent « tuteur » opencode** que les apprenants sollicitent quand ils sont perdus (idée de NG) | Complète la décision 12. Conception en § 2ter |
| P6 | Modèles | **Un modèle imposé** pendant les ateliers + un de secours + une heure de comparaison cadrée | Dépend du budget des clés (point ouvert) |
| P7 | Retours | **Questionnaire final** + **tickets GitHub sur le dépôt public de GSE-One** pendant la formation, pour corriger en cours de route | Comptes GitHub créés au jour 1 ; étiquette dédiée sur `nicolasguelfi/gensem` |
| P8 | Vérification | **Quiz à main levée** seulement | Cohérent avec la décision 17 |
| P9 | Chiffres | **Mise à jour à la source** + fiche des sources formateur | Captures de benchmarks le 23-24/11 |
| P10 | Notions jour 1 | **Quatre diapositives** (LLM → agent ; pas de mémoire ; paysage + coût ; AI Act + règles pratiques) — **en important d'abord les blocs existants de `streamtex-all-trainings`**, en attendant la migration de toute la formation vers all-trainings | Inventaire d'all-trainings fait avant d'écrire du neuf |
| P11 | Théorie GSE-One | **Allègement** : P1 en premier, liste de diapositives à sauter, cadres du jour 4 désactivés | |
| P12 | Orientation | **Une page imprimée** (recto : où suis-je ; verso : quand l'agent dérape) | Remplace la fiche de l'ancienne méthode |
| P13 | Gates | **Grille de 3 questions** + au moins une modification ou un refus par activité | |
| P14 | Exercices | **Fiche standard**, P1 à 60 min, P8 = lancement du mini-projet ; **allonger les pratiques si nécessaire** | |
| P15 | Dépôt des travaux | **GitHub dès le jour 3**, push chaque soir, étiquette `demo` | |
| P16 | Déploiement | **Dockerfile testé dans le starter** + mode opératoire + répétition | Avant le 10/12 |
| P17 | Mini-projet | **Une page** : portée, jalons, démo structurée | |
| P18 | Clôture | **Galerie en deux rotations** + éthique appliquée avant le déjeuner | **Remplace la décision 13** (les démos reviennent, en galerie) |
| P19 | Entre les blocs | **Rien** : NG ne peut pas contacter les apprenants ; tout se fait pendant la formation, aucun travail obligatoire à la maison | Voir ci-dessous |
| P20 | Objectifs | **Objectifs réels affichés au jour 1** + 30 min « mesurer la qualité » au jour 4 | Sans courriel J-7 (P19) |

**Conséquences de P19 (aucun contact avant ni entre les blocs).** Tout ce qui supposait un courriel J-7 passe en salle :
installation (opencode, GSE-One v0.90.0 épinglée, clé, tuteur), compte GitHub et `gh auth login` **au jour 1** (créneau d'installation, avec `check-learner.sh`) ;
objectifs réels sur une diapositive du jour 1 seulement ; niveau des apprenants relevé à main levée au jour 1 ; la « liste de contrôle à J-7 » de la décision 6 devient une liste de contrôle en salle.

## 2ter. Calendrier des trois phases et conception du tuteur

| Phase | Contenu | Rédaction | Vérification | Prêt pour |
|---|---|---|---|---|
| 1 | Jours 1-2 | 10/11 → **18/11** | 19-20/11 : répétition jours 1-2 (installation réelle, starter, étiquettes, modèle imposé) ; 23-24/11 : captures de benchmarks ; 25/11 : marge | 26/11 |
| 2 | Jours 3-4 | 19/11 → 02/12 (hors 26-27/11) | répétition P1 → P7 | 03/12 |
| 3 | Jours 5-6 | 04/12 → 09/12 | répétition du déploiement (3 comptes) | 10/12 |

**Tuteur (P5).** Agent opencode `tutor` (supports en anglais), installé dans la configuration globale de l'apprenant (`~/.config/opencode/agents/tutor.md`) par le kit public `nicolasguelfi/ai4se-kit` (`setup-learner.sh`) pour servir aussi dans le mini-projet ; appelé par `@tutor`.
Lecture seule (aucune écriture, commandes limitées à la lecture : `git status`, `git log`, lecture de `.gse/`) pour ne jamais interférer avec GSE-One.
Connaissances : programme, fiches d'exercice, page d'orientation, FAQ des erreurs fréquentes, procédure de reprise.
Présenté honnêtement comme une IA préparée par NG, pas comme NG ; renvoie au formateur pour tout ce qui touche la machine, la clé, le serveur ou une perte de travail.
Contenu hors corpus GSE-One (règle « pas de cas de formation dans le corpus distribué ») : il vit dans le kit. Retours : étiquette `ai4se-ed2` créée sur `nicolasguelfi/gensem` le 2026-11-09.

## 3. Fait depuis

- 2026-11-09 — gensem **v0.89.1** publiée (commit 1b4f70a, tag v0.89.1, CI et release au vert).
- 2026-11-09 — gensem **v0.90.0** publiée (commit 4c6f5be, tag v0.90.0, CI et release au vert) : adaptateur natif opencode 2, sélection par l'installateur, garde-fous git renforcés. Test réel opencode 2.2.6 (HOME isolé) : adaptateur V2 choisi, commit sur `main` bloqué en session réelle. Le V1 de v0.89.1 fonctionne aussi sur 2.2.6.
- 2026-11-09 — dépôts `ai4se6d-decks` (branches master, feat/tools-ecosystem-lecture-content, refactor/day2-split-image-slides) et `calcapp-course` (v0-plans … v5-production) créés en privé.

- 2026-11-09 — **Phase 1 rédigée** (branche `edition2`) :
  - jour 1 matin : objectifs réels, parcours 6 jours, « How we work », 3 notions adaptées d'all-trainings@7707c1c5 ;
  - Acte IV opencode + LLM locaux + AI Act (règlement (UE) 2026/1744 « Omnibus » : haut risque annexe III au 2/12/2027, annexe I au 2/08/2028) ;
  - chiffres revérifiés + `docs/trainer/sources-day1.md` ;
  - module `ai4se6d_setup` (installation en salle, FreeSelfApp, débrief) ;
  - module `ai4se6d_day2` (plan B, 104 blocs).
  - `stx validate --build` : 7 livres OK.
- 2026-11-09 — dépôts **publics** :
  - `nicolasguelfi/ai4se-kit` (tuteur `@tutor` en lecture seule, `setup-learner.sh`, `check-learner.sh`, testés dans un HOME isolé avec opencode 2.2.6) ;
  - `nicolasguelfi/calcapp-starter` (étiquette `j2-start`, plan d'exemple de secours, `npm start`, Dockerfile Node 22 → nginx testé, healthcheck sans curl).

**À sauter en direct au jour 1 (GenAI, pour tenir 50 min)** :
- `bck_ai_discriminative`, `bck_ai_generative`, `bck_ai_mccarthy` ;
- ères sauf `era_genai` ;
- une seule vue de `bck_llm_benchmarks` ;
- `bck_llm_transformer_demo`, `vocabulary`, `embeddings`, `semantic_space`, `attention`, `attention_viz`, `context_benchmark`, `pretraining`, `finetuning`, `alignment`.

## 4. Points ouverts

- ~~opencode 2~~ : réglé par v0.90.0 (voir § 3). Commande d'installation à utiliser en salle : `curl -fsSL https://raw.githubusercontent.com/nicolasguelfi/gensem/v0.90.0/install.sh | GSE_PLATFORM=opencode GSE_VERSION=v0.90.0 sh` (opencode installé AVANT, pour que l'installateur détecte la version 2).
- Budget et fournisseur des clés de modèle (≈ 20 clés plafonnées).
- Mode d'accès aux VM DLH (protocole, distribution des identifiants sur fiche papier).
