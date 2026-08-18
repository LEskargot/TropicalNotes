---
id: TASK-33
title: Corriger la casse de l'image de la rage (404 en production)
status: Done
assignee: []
created_date: '2026-08-18 14:16'
updated_date: '2026-08-18 14:16'
labels:
  - consistency
dependencies: []
modified_files:
  - pages/viruses/rabies.html
priority: high
ordinal: 33000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
pages/viruses/rabies.html référençait dist/images/rage.jpg alors que le fichier s'appelle dist/images/Rage.jpg. GitHub Pages étant sensible à la casse, l'image renvoyait 404 en production — carte de distribution mondiale manquante sur une page clinique. Détecté lors du contrôle des liens internes pendant le nettoyage.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Référence corrigée en Rage.jpg
- [x] #2 Aucun autre lien interne cassé sur le site
<!-- AC:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Corrigé par sed dans pages/viruses/rabies.html. Contrôle complet : 487 liens internes vérifiés, 0 cassé. Seul cas de casse divergente du dépôt.
<!-- SECTION:FINAL_SUMMARY:END -->
