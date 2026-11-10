# Édition 2 — décisions de préparation

**Date** : 2026-11-09
**Édition** : DLH, 26-27/11, 03-04/12, 10-11/12/2026 — NG seul (Tiago Sousa ne fait plus partie de la formation et a transféré à NG la propriété de ses supports)
**Source** : planches de décision `ai4se1` et `gsel1` (session Claude `ss2-ul-gse`, 2026-11-08/09) ; rapport d'état des lieux (artefact « AI4SE — état des lieux », v3)
**Vue des six journées sur une page** : `2026-11-09-010-six-days-overview.md`.
**Déroulé des six journées en cycles (fait foi)** : `2026-11-10-012-six-days-cycles-plan.html`.
**Déroulés minutés des jours 3 à 6 (provisoires)** : `2026-11-10-011-days3-6-plan.md`. Remplacé par le fichier 012.
**Artefacts à produire pour les jours 3 à 6** : `2026-11-09-009-days3-6-specs.md` (contenu décidé et fichiers à reprendre, tiré de la planche `peda1`)
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

## 2quater. Tuteur et syllabus (planche `tut2`, 2026-11-09) — remplace la conception du tuteur de § 2ter

**But (NG).** Chaque participant possède un ensemble d'artefacts et un agent « training tutor », auquel il pose ses questions de compréhension et d'assistance pendant toute la formation.

- **Session.** Le tuteur a sa propre session opencode, ouverte dans le dossier du kit (`~/ai4se/ai4se-kit/tutor`). Elle est séparée de la session de travail : il n'y a plus de `@tutor` global.
- **Dépôts.** Un fichier de configuration personnel, `~/.config/ai4se/tutor-paths`, liste les dossiers qui font partie du contexte du tuteur.
  - Par défaut, il contient `~/ai4se`, un dossier simple et non un dépôt, qui contient des dépôts voisins sans aucune imbrication.
  - `tutor add <chemin>` ajoute un dossier situé ailleurs.
  - Les secrets sont interdits par des règles opencode qui ne peuvent pas être contournées (`.env*`, clés, `~/.ssh`, identifiants opencode, `.git/config`).
  - Vérifié le 9/11 avec opencode 2.2.6 : un dossier listé est lisible, `git -C` fonctionne, un `.env` est refusé, un dossier non listé est refusé.
- **GSE-One.** Clone de gensem à v0.90.0 dans `~/ai4se/gensem`, avec un guide « où trouver quoi ». Le tuteur cherche d'abord dans les documents, puis lit seulement la section utile.
- **Syllabus.** Rédigé, en anglais : vue d'ensemble des 12 demi-journées, une fiche par demi-journée, un glossaire, une FAQ et une procédure de reprise.
  - Maintenant : la vue d'ensemble et les fiches HD01-HD04. Fiches HD05-HD08 en phase 2, HD09-HD12 en phase 3.
  - Règle : une modification de diapositive met à jour la fiche de la même demi-journée, dans le même commit.
- **Hébergement.** Dans le kit public : le code sous MIT, le syllabus sous CC BY 4.0.
- **Mises à jour.** `tutor update` au début de chaque demi-journée.
- **Réponses.** Elles sont fondées sur le cours et citent leur source. Le tuteur dit quand le cours ne couvre pas la question.

## 2quinquies. Méthode de travail sur les supports StreamTeX (option A, NG, 2026-11-09)

But : aucune perte ni régression du travail de l'édition 1.

- **Repère fixe.** L'étiquette `edition1-final` (poussée sur GitHub) marque `main` à la fin de l'édition 1 (`05355ab`, 08/10/2026). Pour revoir l'édition 1 : `git checkout edition1-final`.
- **Branche.** Tout le travail se fait sur `edition2`. `main` n'est pas touchée avant la fusion, car un push sur `main` redéploie les 4 sites.
- **Désactiver au lieu de supprimer.** Un bloc retiré du cours est enlevé de la séquence du livre (`book.py`, `sequence_*.py`), mais son fichier reste. Aucun fichier de bloc ou d'image de l'édition 1 n'est supprimé.
- **Nouveau bloc quand le sens change.** On ne modifie un bloc existant que pour une petite correction (chiffre, nom d'outil, date). Une réécriture devient un nouveau bloc, et l'ancien est désactivé. Le nouveau bloc porte un nom fait de mots-clés, sans aucun chiffre (ni `_ed2`, ni numéro de jour ou de partie) : règle de NG du 10/11, `.claude/custom/references/naming_convention.md`.
- **Rapport avant fusion.** `uv run python scripts/edition_diff.py` liste, par module, les blocs ajoutés, désactivés et modifiés depuis `edition1-final`. Il échoue si un fichier de l'édition 1 a été supprimé. NG valide ce rapport et les captures des livres avant toute fusion dans `main`.
- **Hors git.** `_LOCAL/`, `docs/maintenance/gse-alignement.md` et `modules/ai4se6d_various/static/` ne sont pas suivis par git. Ils ne sont protégés que par l'historique de Dropbox, et on n'y touche pas.

## 2sexies. Déroulé en cycles (NG, 2026-11-10) — fait foi pour les six journées

Source : `2026-11-10-012-six-days-cycles-plan.html` (déroulé minuté, 25 fiches d'exercice, 16 points ouverts).

- **Cycle CCSET** (proposition de NG) : chaque concept suit quatre étapes : théorie (problème, solutions en théorie et en pratique), illustration conceptuelle de la solution retenue par GSE-One, exercice sur fiche, débrief. 16 cycles, CCSET01 à CCSET16 ; les jours 5-6 appliquent tous les cycles au mini-projet.
- **Jours 1-2 à la main** : vibe coding (jour 1) puis vibe engineering sur CalcApp (jour 2), avant GSE-One. Le plugin n'y apparaît que comme illustration (une diapositive « la solution retenue par GSE-One » par cycle) : **ni démonstration, ni exercice** avec le plugin.
- **Option A** : les quatre cours de génie logiciel du programme initial (concepts et GenSEM 60 min, élicitation des exigences 45, exigences non fonctionnelles 45, vérification et validation 30) occupent le **jour 3 matin** ; GSE-One est utilisé à partir du jour 3 après-midi. **Remplace P11** (« P1 avant toute théorie »).
- **Valeurs par défaut des 16 points ouverts validées** : déjeuner du jour 3 de 12:30 à 13:30 ; P2 et P4 fusionnés dans P1 ; 12 diapositives d'illustration (texte ou schéma, sans capture d'exécution) ; les trois cours écrits en phase 2 à partir des blocs du module gensem ; fiches d'exercice dans le syllabus du kit ; comparaison de modèles au jour 5 à 09:45 ; étiquette du starter avec couverture et `ci.yml` ; mini-projet redéployé au jour 6 seulement si le temps le permet ; galerie en deux rotations ; contrôle des dépôts à 13:45 ; pauses ajoutées aux jours 5-6 ; validation du jalon du jour 5 au fil de l'eau ; jour 3 sans marge ; dépôt privé autorisé pour le mini-projet. Reste à confirmer avec DLH : la taille du groupe (environ 20).
- **Production** des jours 1 à 4 lancée le 10/11 : suivi dans `2026-11-10-013-production-days1-4.md`.

## 2septies. Modèle de la formation (NG, 2026-11-10)

- **Modèle imposé** (décision P6) : `deepseek/deepseek-v4.1-flash` via OpenRouter, sur la clé de NG, pour tous les apprenants et pour **toute la préparation** des séances (répétitions comprises). **Secours** : `minimax/minimax-m3.1-flash`.
- **Pourquoi** : seul modèle observé sur une journée entière de la répétition à blanc du 10/11 (plan, TDD, revue qui trouve un vrai HIGH), coût estimé ≈ 12 $ par apprenant sur les jours 2 à 6 (≈ 250 $ pour 20), à confirmer par la répétition de référence. Prix OpenRouter du 10/11 : entrée 0,30 $, sortie 1,20 $, cache 0,006 $ par million de jetons.
- **Coût mesuré (répétition de référence du 10/11, un apprenant intensif, jours 1 à 4)** : 1,75 $ au total sur OpenRouter (dont 0,18 $ pour tout le jour 2) — le plafond de 20 $ par clé laisse une large marge.
- **Mesure** : 47,5 millions de jetons pour environ 2 h 45 d'agent pendant la répétition à blanc (surtout du contexte relu en cache).
- **À traiter en notion 4 (jour 1)** : l'origine du modèle et ce qu'on met dans un prompt (question de perception sur la confidentialité).
- **Écarté pour la préparation** : les modèles gratuits d'opencode (quota quotidien épuisé après environ 1 h 45 d'agent pendant la répétition à blanc ; confirme la décision 5).
- **Reste à faire** : identifiant exact vérifié après connexion de la clé, puis `opencode.base.json` du kit mis à jour ; répétition de référence des jours 2 à 4 refaite avec ce modèle.

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

- 2026-11-09 — **Tuteur v2 publié** (kit `2026-11-09.2`).
  - Contenu : session dédiée, dossiers de contexte configurables, règles anti-secrets, syllabus (programme des 12 demi-journées, HD01-HD04, guide GSE-One, glossaire, FAQ, reprise), clone de gensem v0.90.0.
  - Deux fuites trouvées et fermées par les tests :
    - l'outil grep lisait des `.env` : il est désactivé, remplacé par `git grep` ;
    - `git -C` et `ls` atteignaient des dossiers non listés : ils sont limités par une règle générée.
  - Test de bout en bout depuis GitHub (HOME isolé, modèle gratuit) : réponse en français qui cite le syllabus, `.env` refusé, `tutor update` OK.
- 2026-11-09 — Diapositives des jours 1-2 alignées sur le tuteur v2. Corrections de cohérence : `npm run test:run`, reprise dans `~/ai4se/calcapp-restart`, montants décimaux, syntaxe opencode 2. Ajout de `docs/trainer/sources-day2.md`.

**À sauter en direct au jour 1 (GenAI, pour tenir 50 min)** :
- `bck_ai_discriminative`, `bck_ai_generative`, `bck_ai_mccarthy` ;
- ères sauf `era_genai` ;
- une seule vue de `bck_llm_benchmarks` ;
- `bck_llm_transformer_demo`, `vocabulary`, `embeddings`, `semantic_space`, `attention`, `attention_viz`, `context_benchmark`, `pretraining`, `finetuning`, `alignment`.

## 4. Points ouverts

- ~~opencode 2~~ : réglé par v0.90.0 (voir § 3). Commande d'installation à utiliser en salle : `curl -fsSL https://raw.githubusercontent.com/nicolasguelfi/gensem/v0.90.0/install.sh | GSE_PLATFORM=opencode GSE_VERSION=v0.90.0 sh` (opencode installé AVANT, pour que l'installateur détecte la version 2).
- Budget et fournisseur des clés de modèle (≈ 20 clés plafonnées) : fournisseur OpenRouter et modèle fixés le 10/11 (§ 2septies) ; reste le plafond par clé.
- Mode d'accès aux VM DLH (protocole, distribution des identifiants sur fiche papier).
