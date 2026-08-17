---
id: TASK-4
title: 'Retirer Bootstrap 4 / jQuery / laravel-mix, garder le pipeline Tailwind'
status: To Do
assignee: []
created_date: '2026-08-17 15:18'
labels:
  - cleanup
dependencies: []
priority: medium
ordinal: 4000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
package.json déclare encore bootstrap ^4.5.3, jquery, popper.js, laravel-mix ^5.0.9, sass ; webpack.mix.js et src/scss/ existent toujours. Attention : ce n'est PAS une suppression simple — index.html, prototype.html et 4 pages syndromes référencent encore dist/, et le script npm "tailwind" génère dist/css/prototype.css (toujours utilisé).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Inventaire des assets dist/ réellement utilisés
- [ ] #2 Dépendances Bootstrap/jQuery/laravel-mix retirées de package.json
- [ ] #3 webpack.mix.js et src/scss supprimés si inutilisés
- [ ] #4 Le rendu du site est inchangé
<!-- AC:END -->
