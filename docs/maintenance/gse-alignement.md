# Mission : alignement du support de formation AI4SE sur la version courante de GSE-One

## Paramètres de cette exécution (À REMPLIR avant d'envoyer)
RAPPORT(S) D'ALIGNEMENT — le ou les rapports générés à la fin du/des développement(s) GSE
depuis la dernière mise à jour du support sont accesibles par les chemins fournis à la fin.

## Contexte
Mon support de formation AI4SE, réalisé avec StreamTeX, enseigne la méthodologie GSE-One.
GSE-One a évolué depuis la dernière mise à jour du support ; cette mission réaligne le
support sur la version courante du plugin.

## Les deux corpus
- CIBLE (à modifier, avec mon accord uniquement) — le projet de formation StreamTeX :
  /Volumes/Mac_Data/Win_data/data/backups/Dropbox-nicolas.guelfi@laposte.net/messir Dropbox/Nicolas Guelfi/users/NG/Projets/AISE/ROS/trainings/AI4SE/githubs/AI4SE6D_STX/projects/ai4se6d
- RÉFÉRENCE (lecture seule, ne JAMAIS y écrire) — le dépôt gensem :
  /Volumes/Mac_Data/Win_data/data/backups/Dropbox-nicolas.guelfi@laposte.net/messir Dropbox/Nicolas Guelfi/users/NG/dev-dropbox/dvlpt/eclipse/git/github/gensem

## Détermination du périmètre de version (à faire en Phase 0)
1. VERSION COURANTE : lis le fichier VERSION à la racine de gensem — c'est la version cible.
2. DERNIÈRE VERSION ALIGNÉE : lis le fichier marqueur du projet de formation
   _LOCAL/gse-alignment-state.yaml (champs : last_aligned_version, reports_processed[],
   aligned_at). S'il n'existe pas, demande-moi sur quelle version le support est actuellement
   basé, puis crée le marqueur.
3. PÉRIMÈTRE : tous les changements entre ces deux versions. Sources : le(s) rapport(s)
   listé(s) en paramètre + toutes les entrées du CHANGELOG.md de gensem dans l'intervalle
   + tout autre rapport de docs/post-audit-reports/ couvrant l'intervalle et absent de
   reports_processed[]. Signale-moi tout trou de couverture (une version du CHANGELOG sans
   rapport correspondant) au lieu de le passer sous silence.

## Hiérarchie des sources de vérité (pour la référence GSE-One)
1. Le corpus gensem à son état courant : gse-one-spec.md, gse-one/src/activities/,
   gse-one/src/agents/, gse-one/src/principles/, gse-one/src/templates/, README.md,
   install.sh / install.py — c'est LUI qui fait foi.
2. Le(s) rapport(s) d'alignement listé(s) en paramètre — guides de lecture : leurs sections
   « changements de comportement » et « contenus enseignés » (chiffres, tables, vocabulaire)
   disent OÙ chercher, pas ce qui est vrai.
3. CHANGELOG.md pour le résumé par version.
Toute affirmation du support sur GSE-One doit être vérifiée contre la source 1 avant d'être
déclarée exacte ou périmée — jamais de mémoire, jamais par déduction du seul rapport.

## Outillage
- Le support est en StreamTeX : utilise sa suite de skills Claude (stx-*) — notamment la
  validation (stx-validate) et l'audit de cohérence (stx-coherence) après toute modification.
- Respecte les conventions du projet de formation (lis son CLAUDE.md/README s'il en a).

## Déroulé imposé
Phase 0 — Vérifications : périmètre de version (bloc ci-dessus) ; état git du projet de
  formation (propre ? branche ?). Si le projet est un dépôt git, crée une branche dédiée
  (ex. gse-align-v<version-courante>) avant toute modification.
Phase 1 — Inventaire (lecture seule) : cartographie les documents/slides du support et repère
  tout contenu qui mentionne GSE-One (commandes /gse:*, principes P1-P16, chiffres, tables,
  captures, exercices, chemins et modes d'installation, flux deploy/formation, numéros de
  version cités).
Phase 2 — Analyse d'écarts (lecture seule) : pour chaque contenu repéré, vérifie contre le
  corpus courant et classe : EXACT / PÉRIMÉ (avec la valeur actuelle et sa source) /
  À VÉRIFIER MANUELLEMENT (ex. captures d'écran, sorties d'outils). Produis un registre
  d'écarts dans un fichier de travail local au projet de formation (pas dans gensem), puis
  présente-moi la synthèse.
Phase 3 — Traitement : uniquement après mon accord, corrige les écarts par lots.
Phase 4 — Validation StreamTeX + relecture finale, commit(s) sur la branche, puis mise à jour
  du marqueur _LOCAL/gse-alignment-state.yaml (last_aligned_version = version courante,
  reports_processed += rapports traités, aligned_at = date) pour la prochaine mission.

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
  du support ET la source correspondante du corpus courant.
- Reste critique : si tu vois une meilleure approche pour l'objectif (un support cohérent avec
  la version courante et pédagogiquement bon), propose-la au lieu de suivre mécaniquement
  les rapports.
- Ne touche à RIEN (ni support, ni gensem) sans mon accord explicite. gensem est en lecture
  seule pour toute la mission.

Commence par les Phases 0-1 et présente-moi le périmètre de version puis l'inventaire.