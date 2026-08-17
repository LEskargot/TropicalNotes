---
id: TASK-1
title: Supprimer le dossier admin/ (Netlify CMS)
status: To Do
assignee: []
created_date: '2026-08-17 15:18'
labels:
  - cleanup
dependencies: []
priority: high
ordinal: 1000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
admin/ contient la config Netlify CMS (git-gateway, branch main). Le site est hébergé sur GitHub Pages, ce CMS n'est plus utilisé. Le dossier est servi publiquement : https://tropicalnotebook.ch/admin/ renvoie HTTP 200.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 admin/ supprimé du dépôt
- [ ] #2 https://tropicalnotebook.ch/admin/ renvoie 404 après déploiement
<!-- AC:END -->
