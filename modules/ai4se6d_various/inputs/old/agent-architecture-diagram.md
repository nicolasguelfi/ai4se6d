# Architecture d'un Agent IA Generative - Diagramme Combiné

## Vue d'ensemble

Un **agent IA** est composé de 3 éléments fondamentaux :
1. **Le Programme Orchestrateur** (processus local) - la boucle de contrôle
2. **Le LLM** (service distant stateless) - le moteur de décision
3. **Les Outils** (exécutés localement) - les effecteurs, incluant le spawn de sous-agents

## Diagramme d'architecture complet

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                        MACHINE LOCALE (poste utilisateur)                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  ┌─ PROCESSUS AGENT PRINCIPAL (PID 1000) ──────────────────────────────┐   ║
║  │                                                                     │   ║
║  │  ┌─ BOUCLE AGENT (event loop) ───────────────────────────────────┐  │   ║
║  │  │                                                               │  │   ║
║  │  │  ┌─────────┐    ┌──────────────────────┐    ┌─────────────┐  │  │   ║
║  │  │  │ CONTEXTE │───►│ APPEL LLM (HTTP POST)│───►│ RÉPONSE LLM │  │  │   ║
║  │  │  │         │    │ api.anthropic.com    │    │             │  │  │   ║
║  │  │  │• system │    │                      │    │ 3 cas:      │  │  │   ║
║  │  │  │• history│    │ Body:                │    │             │  │  │   ║
║  │  │  │• tools  │    │ { messages[],        │    │ A) texte ───────► FIN
║  │  │  │  schemas│    │   tools[],           │    │             │  │  │   ║
║  │  │  │• results│    │   model }            │    │ B) tool_call─────► ①
║  │  │  └─────────┘    └──────────────────────┘    │             │  │  │   ║
║  │  │       ▲                                     │ C) agent ───────► ②
║  │  │       │                                     └─────────────┘  │  │   ║
║  │  │       │  ┌──────────────────────────────────────────┐        │  │   ║
║  │  │       └──│ result injection (IPC: retour résultat)  │        │  │   ║
║  │  │          └──────────────────────────────────────────┘        │  │   ║
║  │  └───────────────────────────────────────────────────────────────┘  │   ║
║  │                                                                     │   ║
║  │  ① EXÉCUTION OUTIL LOCAL                                            │   ║
║  │  ┌──────────────────────────────────────────────────────────────┐   │   ║
║  │  │                                                              │   │   ║
║  │  │  tool_call reçu: {"tool":"X", "params":{...}}               │   │   ║
║  │  │                                                              │   │   ║
║  │  │  ┌─ Permission Gate ─┐                                      │   │   ║
║  │  │  │ Auto-allow ?      │── NON ──► Demande confirmation user  │   │   ║
║  │  │  │ User approve ?    │── OUI ──► Exécution ▼                │   │   ║
║  │  │  └───────────────────┘                                      │   │   ║
║  │  │                                                              │   │   ║
║  │  │  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌──────────┐ │   │   ║
║  │  │  │ read_file  │ │ bash       │ │ grep       │ │ edit     │ │   │   ║
║  │  │  │            │ │            │ │            │ │          │ │   │   ║
║  │  │  │ syscall:   │ │ fork/exec: │ │ fork/exec: │ │ syscall: │ │   │   ║
║  │  │  │ open+read  │ │ PID 1001   │ │ PID 1002   │ │ write    │ │   │   ║
║  │  │  └─────┬──────┘ └─────┬──────┘ └─────┬──────┘ └────┬─────┘ │   │   ║
║  │  │        │              │              │             │        │   │   ║
║  │  │        └──────────────┴──────────────┴─────────────┘        │   │   ║
║  │  │                        │                                    │   │   ║
║  │  │                   result (string)                           │   │   ║
║  │  │                        │                                    │   │   ║
║  │  │                        ▼                                    │   │   ║
║  │  │              ┌──────────────────┐                           │   │   ║
║  │  │              │ Réinjection dans │──────► retour boucle ▲   │   │   ║
║  │  │              │ le contexte      │                           │   │   ║
║  │  │              └──────────────────┘                           │   │   ║
║  │  └──────────────────────────────────────────────────────────────┘   │   ║
║  │                                                                     │   ║
║  │  ② SPAWN SOUS-AGENTS (l'outil "agent")                             │   ║
║  │  ┌──────────────────────────────────────────────────────────────┐   │   ║
║  │  │                                                              │   │   ║
║  │  │  tool_call: {"tool":"agent", "params":{"prompt":"...",       │   │   ║
║  │  │              "type":"Explore", "background": false}}         │   │   ║
║  │  │                                                              │   │   ║
║  │  │         fork/spawn              fork/spawn                   │   │   ║
║  │  │            │                       │                         │   │   ║
║  │  │  ┌─────────▼──────────┐  ┌────────▼───────────┐             │   │   ║
║  │  │  │ SOUS-AGENT A       │  │ SOUS-AGENT B       │             │   │   ║
║  │  │  │ PID 2000           │  │ PID 3000           │  parallèle  │   │   ║
║  │  │  │                    │  │                    │             │   │   ║
║  │  │  │ ┌──────────────┐   │  │ ┌──────────────┐   │             │   │   ║
║  │  │  │ │ SA PROPRE    │   │  │ │ SA PROPRE    │   │             │   │   ║
║  │  │  │ │ BOUCLE AGENT │   │  │ │ BOUCLE AGENT │   │             │   │   ║
║  │  │  │ │              │   │  │ │              │   │             │   │   ║
║  │  │  │ │ Son contexte │   │  │ │ Son contexte │   │             │   │   ║
║  │  │  │ │ Ses outils   │   │  │ │ Ses outils   │   │             │   │   ║
║  │  │  │ │ Ses appels   │   │  │ │ Ses appels   │   │             │   │   ║
║  │  │  │ │ LLM propres ─────────────► HTTP ──► LLM  │             │   │   ║
║  │  │  │ │ (N tours)    │   │  │ │ (M tours)    │   │             │   │   ║
║  │  │  │ └──────────────┘   │  │ └──────────────┘   │             │   │   ║
║  │  │  │                    │  │                    │             │   │   ║
║  │  │  │ Peut lui-même     │  │                    │             │   │   ║
║  │  │  │ spawner des       │  │                    │             │   │   ║
║  │  │  │ sous-sous-agents  │  │                    │             │   │   ║
║  │  │  │ (récursif)        │  │                    │             │   │   ║
║  │  │  └────────┬───────────┘  └────────┬───────────┘             │   │   ║
║  │  │           │ return result_A       │ return result_B         │   │   ║
║  │  │           └───────────┬───────────┘                         │   │   ║
║  │  │                       │ waitpid / join                      │   │   ║
║  │  │                       ▼                                     │   │   ║
║  │  │             ┌──────────────────┐                            │   │   ║
║  │  │             │ Réinjection dans │──────► retour boucle ▲    │   │   ║
║  │  │             │ contexte parent  │                            │   │   ║
║  │  │             └──────────────────┘                            │   │   ║
║  │  └──────────────────────────────────────────────────────────────┘   │   ║
║  └─────────────────────────────────────────────────────────────────────┘   ║
║                                                                            ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  RESSOURCES LOCALES ACCESSIBLES                                            ║
║  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────────────────┐   ║
║  │ Filesystem │ │ Processus  │ │ Réseau     │ │ Périphériques          │   ║
║  │ (fichiers) │ │ (terminal) │ │ (HTTP out) │ │ (clipboard, etc.)     │   ║
║  └────────────┘ └────────────┘ └────────────┘ └────────────────────────┘   ║
╚══════════════════════════════════════════════════════════════════════════════╝
              │
              │  HTTPS (réseau)
              │
╔═════════════▼════════════════════════════════════════════════════════════════╗
║                     SERVEUR(S) DISTANT(S)                                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  ┌─ SERVICE LLM (stateless) ───────────────────────────────────────────┐   ║
║  │                                                                     │   ║
║  │  Input:  { messages[], tools[], system_prompt, model }              │   ║
║  │                                                                     │   ║
║  │  ┌───────────────────────────────────────────────────────────┐      │   ║
║  │  │                    INFÉRENCE                              │      │   ║
║  │  │                                                           │      │   ║
║  │  │  Génération token par token (autorégressif)               │      │   ║
║  │  │  GPU cluster - calcul matriciel                           │      │   ║
║  │  │                                                           │      │   ║
║  │  │  ⚠ AUCUN état entre les appels                           │      │   ║
║  │  │  ⚠ AUCUN accès filesystem / réseau / processus           │      │   ║
║  │  │  ⚠ Ne fait QUE prédire la suite de tokens                │      │   ║
║  │  └───────────────────────────────────────────────────────────┘      │   ║
║  │                                                                     │   ║
║  │  Output: { text }  OU  { tool_call: name + params (JSON) }         │   ║
║  │                                                                     │   ║
║  └─────────────────────────────────────────────────────────────────────┘   ║
║                                                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Légende des mécanismes OS en jeu

| Mécanisme | Où dans le diagramme | Rôle |
|---|---|---|
| **Process (PID)** | Chaque agent = 1 processus avec son PID | Isolation, cycle de vie indépendant |
| **fork/spawn** | Lancement d'outils bash et de sous-agents | Création de processus enfants |
| **waitpid/join** | Parent attend résultats des sous-agents | Synchronisation inter-processus |
| **IPC (pipe/retour)** | Résultat outil/agent réinjecté dans le contexte | Communication inter-processus |
| **Concurrence** | Sous-agents A et B en parallèle | Exécution simultanée de processus |
| **Syscalls** | read_file (open/read), edit (write) | Accès aux ressources noyau |
| **Réseau (sockets)** | HTTP POST vers l'API LLM | Communication avec le service distant |
| **Permission gate** | Avant chaque exécution d'outil | Équivalent d'un contrôle d'accès (ACL) |
| **Event loop** | La boucle agent principale | Scheduler coopératif mono-thread |
| **Récursivité** | Un sous-agent peut spawner des sous-sous-agents | Arbre de processus (pstree) |

## Flux d'exécution temporel

```
Utilisateur
    │
    │  prompt: "Refactore le module auth"
    ▼
Agent Principal (PID 1000)
    │
    ├── LLM call #1 ──► "Je dois d'abord comprendre le code"
    │   Réponse: tool_call read_file("/src/auth.ts")
    │
    ├── Exécution locale: syscall open+read
    │   Résultat: contenu du fichier
    │
    ├── LLM call #2 ──► "C'est complexe, je lance 2 recherches en parallèle"
    │   Réponse: tool_call agent x2
    │
    ├── fork Sous-agent A (PID 2000): "Trouve tous les usages de auth"
    │   │── LLM call A.1 ──► tool_call grep
    │   │── LLM call A.2 ──► tool_call read_file
    │   └── return result_A
    │
    ├── fork Sous-agent B (PID 3000): "Vérifie les tests existants"  (parallèle)
    │   │── LLM call B.1 ──► tool_call glob
    │   │── LLM call B.2 ──► tool_call read_file
    │   └── return result_B
    │
    ├── join(A, B) - attend les deux résultats
    │
    ├── LLM call #3 ──► "Maintenant j'ai tout le contexte, j'édite"
    │   Réponse: tool_call edit("/src/auth.ts", ...)
    │
    ├── Permission gate ──► User approve? ──► OUI
    │
    ├── Exécution locale: syscall write
    │
    ├── LLM call #4 ──► "Terminé, voici le résumé"
    │   Réponse: texte
    │
    └── FIN ──► Affichage au user
```

## Points clés

1. **Le LLM est un service de calcul pur** sans effet de bord. Il ne fait que générer des tokens.
2. **Toute action** sur le monde (lire, écrire, exécuter, spawner) est effectuée par l'orchestrateur local.
3. **L'outil "agent"** n'est qu'un outil parmi d'autres qui, au lieu d'exécuter un syscall simple, instancie une nouvelle boucle agent complète avec son propre contexte et ses propres appels LLM.
4. **La récursivité** est possible : un sous-agent peut lui-même spawner des sous-sous-agents, formant un arbre de processus.
5. **Le contexte est reconstruit** à chaque appel API - le LLM n'a aucune mémoire persistante entre les requêtes.<!---->
