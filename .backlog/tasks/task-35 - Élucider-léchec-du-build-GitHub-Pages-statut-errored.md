---
id: TASK-35
title: Élucider l'échec du build GitHub Pages (statut errored)
status: To Do
assignee: []
created_date: '2026-08-18 14:55'
updated_date: '2026-08-18 14:56'
labels:
  - cleanup
dependencies: []
priority: medium
ordinal: 35000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
L'API GitHub Pages renvoie status=errored / « Page build failed » pour les commits 8f40c675 et de2e0fcc (2026-08-18). IMPORTANT : le contenu est malgré tout déployé et correct — vérifié en production avec cache-busting (404 sur /admin/, /prototype.html, /professionnels.html ; la page fievre.html servie en ligne pointe vers ../../index.html ; rabies.html sert Rage.jpg). Écarté comme cause : .backlog/ (ses fichiers sont bien déployés, /.backlog/config.yml renvoie 200), symlinks (aucun), caractères problématiques dans les noms (aucun), .nojekyll (présent). Signal le plus fort : le dernier build réussi est 33ab858f du 2026-03-29, soit ~5 mois avant — et ce n'est pas un commit de cette session. L'intervalle est vide, donc rien n'indique que les changements d'aujourd'hui soient en cause. Piste principale : le dépôt utilise build_type=legacy (infrastructure dépréciée) ; migrer vers le déploiement Pages basé sur GitHub Actions (build_type=workflow). Impact réel inconnu : deux pushs ont été déployés correctement malgré le statut errored.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Cause identifiée
- [ ] #2 Build en statut 'built' à nouveau
- [ ] #3 Aucun e-mail d'échec récurrent
<!-- AC:END -->
