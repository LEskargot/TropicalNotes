---
id: TASK-3
title: Sortir professionnels.html de la racine publiée
status: Done
assignee: []
created_date: '2026-08-17 15:18'
updated_date: '2026-08-18 14:55'
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
- [x] #1 Le fichier ne se trouve plus dans la racine servie
- [x] #2 L'URL publique /professionnels.html ne renvoie plus la page
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Résolution finale : fichier SUPPRIMÉ, pas seulement déplacé. Vérification faite contre la page en production : traveldoctor.ch/professionnels est bien du Divi (3673 classes et_pb_) mais son contenu a divergé de ce fichier — le titre principal « Avis spécialisé en infectiologie et médecine tropicale » n'y figure pas, et la page affiche « DTM&H Glasgow » que le fichier ne contient pas. L'auteur confirme n'avoir jamais collé ce fichier dans Divi. C'était donc un brouillon obsolète se faisant passer pour une source de vérité (493 caractères de texte visible contre ~156 000 sur la page réelle). Contenu conservé dans l'historique git : 5e4e02f, caa9f7d, 8192b3c, 6b2e372.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Fichier supprimé (et non simplement déplacé) après vérification que la page Divi en production a divergé de ce brouillon. Vérifié : /professionnels.html et /docs/traveldoctor-professionnels-divi.html renvoient tous deux 404.
<!-- SECTION:FINAL_SUMMARY:END -->
