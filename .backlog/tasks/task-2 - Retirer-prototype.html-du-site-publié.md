---
id: TASK-2
title: Retirer prototype.html du site publié
status: Done
assignee: []
created_date: '2026-08-17 15:18'
updated_date: '2026-08-18 14:55'
labels:
  - cleanup
dependencies: []
priority: high
ordinal: 2000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Artefact de développement servi publiquement (HTTP 200) sur un site dont l'objectif est la crédibilité professionnelle. Référence des assets dist/ — vérifier avant suppression.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 prototype.html n'est plus servi sur le domaine
- [x] #2 Aucun lien interne cassé
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Découverte : prototype.html n'était PAS un artefact orphelin — 16 liens depuis 4 pages syndromes (logo, #syndromes, #about) pointaient dessus. Pire, prototype.html a des menus déroulants morts (href="#") là où index.html a de vrais liens : les lecteurs arrivaient sur une page d'accueil à navigation cassée. Les 16 liens ont été repointés vers ../../index.html (ancres #syndromes et #about présentes dans index.html), le glob './prototype.html' retiré de tailwind.config.js, puis le fichier supprimé. Vérification : 487 liens internes contrôlés, 0 cassé. AC #1 (plus servi) à vérifier après push.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
16 liens repointés de prototype.html vers index.html dans 4 pages syndromes, glob retiré de tailwind.config.js, fichier supprimé. Vérifié en production : /prototype.html renvoie 404 et la page fievre.html servie en ligne pointe bien vers ../../index.html. Correction d'un vrai bug au passage : prototype.html avait des menus déroulants morts (href="#") là où index.html a de vrais liens. Contrôle global : 505 liens internes, 0 cassé.
<!-- SECTION:FINAL_SUMMARY:END -->
