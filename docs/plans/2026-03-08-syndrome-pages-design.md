# Design: Pages syndrome — TropicalNotes

_Date: 2026-03-08 | Statut: v1, itération initiale_

---

## Architecture de contenu

### Source de vérité

```
research.md (dans md-slides repo, /home/ubuntu/md-slides/docs/plans/)
    ├── module.md  (cas cliniques + quiz → slides CME)
    └── page HTML  (algorithmes + tableaux → référentiel web TropicalNotes)
```

- Les fichiers `research-*.md` sont la source de vérité unique
- Le script de conversion lit le research et génère le HTML
- Pipeline: `node scripts/build-syndrome.js --research <path> --output <path>`
- Les research restent dans le repo md-slides, pas de couplage (pas de submodule)

### 4 pages syndrome à créer

| Research source | Page cible |
|---|---|
| `research-fever-syndromes.md` | `pages/syndromes/fievre-voyageur.html` |
| `research-diarrhee-voyageur.md` | `pages/syndromes/diarrhee-voyageur.html` |
| `research-dermatoses-voyageur.md` | `pages/syndromes/dermatoses-voyageur.html` |
| `research-eosinophilia-travelers.md` | `pages/syndromes/eosinophilie.html` |

---

## Structure de page (validée pour "Fièvre au retour")

### Vue d'ensemble

```
Navbar fixe
Breadcrumb: Accueil > Par syndrome > Fièvre au retour
En-tête (titre + date mise à jour) + Floating TOC (droite)
─────────────────────────────────────────
PARTIE 1 — CONSULTATION RAPIDE
  1.1 Diagramme de triage (SVG draw.io)
  1.2 Bilan initial systématique (tableau checklist)
  1.3 Déclaration obligatoire Suisse (tableau)
─────────────────────────────────────────
PARTIE 2 — PAR PATHOGÈNE
  2.1 Paludisme        → lien malaria.html
  2.2 Dengue/Arbo      → lien dengue.html
  2.3 Rickettsioses    → lien rickettsiosis.html
  2.4 Fièvre typhoïde  → lien enteric_fever.html
  2.5 FHV (Ebola etc.) → pas de fiche existante
  2.6 Katayama          → lien schistosomiasis.html
─────────────────────────────────────────
Points clés (3-5 bullets)
Références (tableau + DOIs)
Footer
```

### Partie 1 — Consultation rapide

Fond visuellement distinct (cream-200 ou bordure teal). Le GP scanne en 2 minutes.

**1.1 Diagramme de triage (SVG)**
- Algorithme draw.io avec double axe: danger individuel + danger collectif
- Format SVG inline ou img référencé
- À créer (pas encore de diagramme existant pour fièvre)

**1.2 Bilan initial systématique**
- Tableau: Test | Pourquoi | Piège
- TDR malaria, FSC, NS1 dengue, hémocultures, bilan hépatique/rénal

**1.3 Déclaration obligatoire**
- Tableau: Maladie | Délai | Modalité
- FHV = 2h téléphone, reste = 24h Infreport

### Partie 2 — Blocs pathogènes

Chaque bloc suit la même micro-structure:

```
En-tête: Nom pathogène + [→ Fiche détaillée] (lien)
├── Quand y penser (contexte, incubation, signes clés)
├── Diagnostic (tests, sensibilités, pièges)
├── Traitement (tableau: situation → ATB → dose → durée)
│   └── "référer" = lien CTA contextuel à chaque mention
└── ⚠ Piège à éviter (callout box, bordure gold)
```

Pathogènes couverts: Paludisme, Dengue/Arboviroses, Rickettsioses, Fièvre typhoïde, FHV, Katayama.

### Éléments transversaux

- **Floating TOC**: droite desktop, collapse mobile, highlight section active au scroll
- **Liens croisés**: chaque pathogène → fiche détaillée existante dans pages/
- **"Référer" contextuel**: le mot est un lien (couleur mint, discret) à chaque occurrence naturelle. CTA plus visibles aux points clés (critères sévérité, critères hospitalisation, points clés)
- **Callout boxes "Piège"**: encadrés avec bordure gold, icône warning
- **Posologies incluses**: dans chaque bloc traitement (le GP ne navigue pas ailleurs)
- **Pas de quiz** pour cette itération (format référentiel pur)

---

## Design system

Reprend le design system du prototype.html:
- Palette: teal dark (#1a3836), teal primary (#479793), mint (#12AD98), gold (#d4a01c), cream (#fefdfb)
- Typo: DM Serif Display (titres) + Source Sans 3 (corps)
- Tech: HTML statique + Tailwind CSS CDN, vanilla JS (TOC, scroll)
- Responsive: TOC disparaît sur mobile, tableaux scrollables horizontalement

---

## Décisions clés

1. **Research = source de vérité**, module et page web sont deux sorties différentes
2. **Page en deux parties**: consultation rapide (2 min) + approfondi par pathogène
3. **Par pathogène** (pas par étape clinique) avec liens croisés systématiques
4. **Posologies dans la page** (pas de renvoi pour les traitements)
5. **"Référer" organique** dans le texte + CTA aux moments clés
6. **Pas de quiz** dans cette itération
7. **Script simple** avec chemin en argument, pas de submodule
8. **Diagramme draw.io/SVG** pour chaque syndrome (à créer pour fièvre)
