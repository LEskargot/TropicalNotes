---
id: TASK-35
title: Élucider l'échec du build GitHub Pages (statut errored)
status: To Do
assignee: []
created_date: '2026-08-18 14:55'
labels:
  - cleanup
dependencies: []
priority: medium
ordinal: 35000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Depuis les commits du 2026-08-18, l'API GitHub Pages renvoie status=errored / « Page build failed » pour 8f40c675 et de2e0fcc, alors que le dernier build réussi est 33ab858f (2026-03-29). IMPORTANT : le contenu est malgré tout déployé et correct — vérifié en production (404 sur /admin/, /prototype.html, /professionnels.html ; fievre.html en ligne pointe vers ../../index.html ; .backlog/config.yml renvoie 200). Cause inconnue. Écarté : pas de symlink, pas de caractère problématique dans les noms de fichiers, .nojekyll présent. Piste : l'ajout de .backlog/ (34 fichiers, noms accentués, extensions .md.md) coïncide avec le début des erreurs. Conséquence pratique : GitHub envoie probablement des e-mails d'échec de build, et un futur push pourrait cesser de se déployer.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Cause identifiée
- [ ] #2 Build en statut 'built' à nouveau
- [ ] #3 Aucun e-mail d'échec récurrent
<!-- AC:END -->
