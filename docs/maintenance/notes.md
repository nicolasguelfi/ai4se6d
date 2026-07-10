# Mission : alignement du support de formation AI4SE sur GSE-One v0.85.0

## Contexte
Le plugin GSE-One vient de passer de v0.84.0 à v0.85.0 via un train de corrections issu d'un
audit complet de la méthodologie (126 findings corrigés). Mon support de formation AI4SE,
réalisé avec StreamTeX, enseigne GSE-One et doit être réaligné sur la version actuelle.

## Les deux corpus
- CIBLE (à modifier, avec mon accord uniquement) — le projet de formation StreamTeX :
  /Volumes/Mac_Data/Win_data/data/backups/Dropbox-nicolas.guelfi@laposte.net/messir Dropbox/Nicolas Guelfi/users/NG/Projets/AISE/ROS/trainings/AI4SE/githubs/AI4SE6D_STX/projects/ai4se6d
- RÉFÉRENCE (lecture seule, ne JAMAIS y écrire) — le dépôt gensem à l'état v0.85.0 :
  /Volumes/Mac_Data/Win_data/data/backups/Dropbox-nicolas.guelfi@laposte.net/messir Dropbox/Nicolas Guelfi/users/NG/dev-dropbox/dvlpt/eclipse/git/github/gensem

## Hiérarchie des sources de vérité (pour la référence GSE-One)
1. Le corpus v0.85.0 lui-même : gse-one-spec.md, gse-one/src/activities/, gse-one/src/agents/,
   gse-one/src/principles/, gse-one/src/templates/ — c'est LUI qui fait foi.
2. Le guide d'alignement : docs/post-audit-reports/2026-07-10-audit-v0.84.0-fix-train.md —
   ses sections 1 (changements de comportement) et 2 (contenus enseignés : chiffres, tables,
   vocabulaire) listent précisément ce qui a changé et ce qu'un support peut citer de périmé.
3. CHANGELOG.md (entrée 0.85.0) pour le résumé.
Toute affirmation du support sur GSE-One doit être vérifiée contre la source 1 avant d'être
déclarée exacte ou périmée — jamais de mémoire, jamais par déduction du seul rapport.

## Outillage
- Le support est en StreamTeX : utilise sa suite de skills Claude (stx-*) — notamment la
  validation (stx-validate) et l'audit de cohérence (stx-coherence) après toute modification.
- Respecte les conventions du projet de formation (lis son CLAUDE.md/README s'il en a).

## Déroulé imposé
Phase 0 — Vérifications : état git du projet de formation (propre ? branche ?). Si le projet
  est un dépôt git, crée une branche dédiée avant toute modification.
Phase 1 — Inventaire (lecture seule) : cartographie les documents/slides du support et repère
  tout contenu qui mentionne GSE-One (commandes /gse:*, principes P1-P16, chiffres, tables,
  captures, exercices, chemins d'installation, flux deploy/formation).
Phase 2 — Analyse d'écarts (lecture seule) : pour chaque contenu repéré, vérifie contre le
  corpus v0.85.0 et classe : EXACT / PÉRIMÉ (avec la valeur actuelle) / À VÉRIFIER MANUELLEMENT
  (ex. captures d'écran). Produis un registre d'écarts dans un fichier de travail local au
  projet de formation (pas dans gensem), puis présente-moi la synthèse.
Phase 3 — Traitement : uniquement après mon accord, corrige les écarts par lots.
Phase 4 — Validation StreamTeX + relecture finale, puis commit(s) sur la branche.

## Format d'interaction (obligatoire)
- Processus strictement séquentiel : les problèmes sont numérotés Problème 1, 2, 3…
  et chaque problème porte UNE question du même numéro (Q1, Q2…). Jamais de numérotation
  mixte lettres/chiffres.
- Tu peux grouper en un seul lot les corrections mécaniques sans alternative raisonnable
  (chiffres périmés, noms de commandes, chemins) ; tout le reste se traite un par un.
- Pour chaque problème : (a) résumé du problème expliqué simplement et pédagogiquement
  (introduis chaque terme interne par une parenthèse la première fois) ; (b) solutions
  possibles avec avantages ET inconvénients rédigés pédagogiquement ; (c) solution finale
  recommandée détaillée par fichier : nom du fichier, ancienne valeur → nouvelle valeur →
  effet escompté ; (d) une question au format : « QN : si tu dis ok alors j'appliquerai la
  réponse (x) de faire … » avec les réponses possibles et le défaut explicite.
- Vérification avant rapport : ne déclare jamais un contenu périmé sans avoir relu le fichier
  du support ET la source v0.85.0 correspondante.
- Reste critique : si tu vois une meilleure approche pour l'objectif (un support cohérent avec
  v0.85.0 et pédagogiquement bon), propose-la au lieu de suivre mécaniquement le rapport.
- Ne touche à RIEN (ni support, ni gensem) sans mon accord explicite. gensem est en lecture
  seule pour toute la mission.

Commence par les Phases 0-1 et présente-moi l'inventaire.