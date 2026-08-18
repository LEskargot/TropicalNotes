---
id: TASK-3
title: Sortir professionnels.html de la racine publiée
status: In Progress
assignee: []
created_date: '2026-08-17 15:18'
updated_date: '2026-08-18 14:16'
labels:
  - cleanup
dependencies: []
priority: high
ordinal: 3000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Ce fichier est la source à coller dans le module Code Divi de traveldoctor.ch/professionnels — ce n'est pas une page de tropicalnotebook.ch. Il est pourtant servi à https://tropicalnotebook.ch/professionnels.html (HTTP 200).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Déplacé hors de la racine servie (par ex. docs/)
- [ ] #2 L'URL publique ne renvoie plus la page
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Déplacé en docs/traveldoctor-professionnels-divi.html (git mv), nom explicite indiquant qu'il s'agit d'une source à coller dans Divi et non d'une page du site. Aucune référence interne. À noter : docs/ est lui aussi servi publiquement (GitHub Pages sert tout depuis main:/ — docs/research/*.md renvoie 200). Le déplacement libère l'URL /professionnels.html mais ne rend pas le fichier privé. AC #2 à vérifier après push.
<!-- SECTION:NOTES:END -->
