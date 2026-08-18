---
id: TASK-34
title: Regrouper les fichiers source hors de la racine servie
status: To Do
assignee: []
created_date: '2026-08-18 14:18'
labels:
  - cleanup
dependencies: []
priority: medium
ordinal: 34000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Même classe de problème que TASK-1/2/3 : la racine du dépôt contient des fichiers source servis publiquement qui ne sont pas des pages du site — research_dimorphic_fungi.md, research_link_audit.md, traveldoctor-full.jpeg. GitHub Pages sert tout depuis main:/, donc ils sont accessibles sur le domaine. Attention : research_dimorphic_fungi.md est référencé par TASK-24, mettre la référence à jour en cas de déplacement. À noter aussi que docs/ est lui-même servi (docs/research/*.md renvoie 200) — déplacer vers docs/ change l'URL mais ne rend rien privé.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Fichiers source déplacés hors de la racine
- [ ] #2 Références des tâches concernées mises à jour (TASK-24)
- [ ] #3 Aucun lien interne cassé
<!-- AC:END -->
