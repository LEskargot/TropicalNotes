# Design : Workflow de mise à jour des fiches pathogènes — Tropical Notebook

**Date :** 2026-03-10
**Statut :** Approuvé

---

## Contexte

Tropical Notebook dispose de 17 fiches pathogènes existantes dans le design Tailwind (DM Serif Display + Source Sans 3, tokens teal/mint/gold/cream). Ces fiches ont besoin d'être mises à jour avec du contenu basé sur la littérature récente et liées aux nouvelles pages syndrome.

**Fiches existantes :**
- `pages/parasites/` : malaria, leishmaniasis, schistosomiasis, african_trypanosomiasis, american_trypanosomiasis, giardiasis, intestinal_problems_parasites
- `pages/viruses/` : dengue, chikungunya, zika, yellow_fever, rabies, hepatitis_a, hepatitis_e
- `pages/bacteria/` : enteric_fever, rickettsiosis, leptospirosis

---

## Objectif

Pour chaque pathogène :
1. Recherche de littérature (PubMed + Scholar Gateway)
2. Fichier research markdown (source de vérité unique)
3. Mise à jour HTML (contenu actualisé, style textbook aligné design système)
4. Commit + push GitHub

---

## Workflow par pathogène

### Étape 1 — Recherche de littérature

Outils : PubMed MCP + Scholar Gateway MCP

Axes de recherche :
- Épidémiologie suisse (données OFSP/BAG, Senn/GeoSentinel, Swiss TPH)
- Présentation clinique (revues récentes, guidelines)
- Diagnostic (performances des tests, algorithmes)
- Traitement : **littérature internationale en priorité** (WHO, CDC, Mandell's, RCTs/méta-analyses récents) + SSTTM/SwissTPH comme référence suisse complémentaire quand disponible
- Points clés pratiques pour le médecin de premier recours suisse

### Étape 2 — Fichier research

**Destination :** `docs/research/[pathogene].md`

**Structure :**
```markdown
# Research : [Nom du pathogène]
_Date : YYYY-MM-DD | Sources : PubMed, Scholar Gateway, WHO, CDC, Mandell's_

## Contexte suisse / épidémiologie
## Présentation clinique
## Diagnostic
## Traitement
## Points clés
### Piège
### Perle
## Références
1. Auteur et al. Titre. Journal YYYY;vol:pages. DOI:...
```

### Étape 3 — Mise à jour HTML

**Style :** textbook (article avec sidebar TOC), même design Tailwind actuel.

**Contenu actualisé :**
- Épidémiologie avec données récentes et chiffres suisses
- Sections clinique/diagnostic/traitement mises à jour depuis le fichier research
- Callout boxes piège (gold) et perle (mint) consolidées
- Liens retour vers les pages syndrome qui citent ce pathogène
- Références numérotées en bas de page

**Ne pas changer :**
- Structure HTML générale (navbar, sidebar TOC, article layout)
- Design tokens et classes Tailwind
- Breadcrumb et navigation

### Étape 4 — Commit + push

```bash
git add docs/research/[pathogene].md pages/[categorie]/[pathogene].html
git commit -m "Update [pathogene]: research file + content refresh"
git push
```

---

## Ordre de traitement

Séquentiel, avec validation après chaque pathogène avant de passer au suivant.

1. **malaria** (priorité : lié à fievre.html, données suisses riches dans md-slides)
2. dengue
3. rickettsiosis
4. enteric_fever
5. schistosomiasis
6. leishmaniasis
7. chikungunya
8. zika
9. yellow_fever
10. rabies
11. hepatitis_a
12. hepatitis_e
13. leptospirosis
14. african_trypanosomiasis
15. american_trypanosomiasis
16. giardiasis
17. intestinal_problems_parasites

---

## Contraintes

- GitHub Pages statique : pas de build step supplémentaire
- Inline Tailwind CDN (pages existantes) — pas besoin de recompiler prototype.css
- Noms d'organismes en _italique_
- Contexte suisse : OFSP/BAG, SSTTM, Swiss TPH prioritaires pour les recommandations locales
- Langue : français tout au long
