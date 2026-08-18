---
id: TASK-1
title: Supprimer le dossier admin/ (Netlify CMS)
status: Done
assignee: []
created_date: '2026-08-17 15:18'
updated_date: '2026-08-18 14:55'
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
- [x] #1 admin/ supprimé du dépôt
- [x] #2 https://tropicalnotebook.ch/admin/ renvoie 404 après déploiement
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
admin/index.html et admin/config.yml supprimés (git rm). Netlify CMS (git-gateway) inutilisé depuis le passage à GitHub Pages. Aucune référence interne ailleurs dans le dépôt. AC #2 (404 public) reste à vérifier après push.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
admin/index.html et admin/config.yml supprimés. Vérifié en production après déploiement : https://tropicalnotebook.ch/admin/ renvoie 404 (contrôle avec cache-busting).
<!-- SECTION:FINAL_SUMMARY:END -->
