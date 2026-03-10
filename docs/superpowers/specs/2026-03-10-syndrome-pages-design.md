# Design : Pages Syndrome — Tropical Notebook

**Date :** 2026-03-10
**Statut :** Approuvé

---

## Contexte

Tropical Notebook (tropicalnotebook.ch) est un référentiel de médecine tropicale et du voyage pour les médecins praticiens suisses. Le site utilise un nouveau design Tailwind CSS (`prototype.html`) avec un système de tokens personnalisés (teal/mint/gold/cream, polices DM Serif Display + Source Sans 3).

Quatre modules CME structurés en markdown (`md-slides/modules/urgences-infectio-voyage/`) constituent la source de contenu pour quatre pages syndrome à créer.

---

## Objectif

Créer 4 pages syndrome en HTML statique, dans le design système Tailwind existant, sourcées depuis les modules markdown, déployées via GitHub Pages.

**Fichiers à créer :**
- `pages/syndromes/fievre.html`
- `pages/syndromes/diarrhee.html`
- `pages/syndromes/dermatoses.html`
- `pages/syndromes/eosinophilie.html`

---

## Mise en page

**Défilement linéaire** (option A, approuvée) — pas d'onglets ni de sidebar. Tout le contenu est visible et scannable. Compatible Cmd+F. Facile à imprimer.

Une **barre d'ancres sticky** (sous la navbar) permet la navigation rapide entre sections.

---

## Structure de chaque page

```
1. Navbar (identique prototype.html)
2. Hero
   - Titre syndrome (DM Serif Display, fond teal-800→teal-700)
   - Breadcrumb : Syndromes > [Nom]
   - Sous-titre descriptif
   - Tags géographiques + badge source (ex: SSTTM 2025)
   - Badge urgence si applicable (⚡)
3. Barre d'ancres sticky (top: 56px)
   Diagnostic | Bilan | Pathogènes | Traitement | Points clés | Références
4. Section : Approche diagnostique
   - Tableau urgence : Pathogène × Délai d'action × Clé diagnostique
5. Section : Bilan initial
   - Tableau : Examen × Indication (chips) × Commentaire
6. Section : Pathogènes clés
   - Cards linkées vers pages pathogènes existantes (pages/viruses/, pages/bacteria/, pages/parasites/)
7. Section : Traitement
   - Cards color-coded par urgence (rouge = urgent, gold = secondaire, teal = standard)
   - Box Swiss TPH +41 61 284 81 44 si pertinent
8. Section : Points clés
   - Piège (fond orange, ⚠)
   - Perle (fond mint, ✦)
   - Retenir (grille 2 colonnes, fond teal-50)
9. Section : Références
   - Liste numérotée avec auteurs, journal, année, DOI
10. Footer
```

---

## Assets et intégration

### Algorithmes draw.io → `<iframe>` diagrams.net

Les fichiers `.drawio.xml` sont copiés vers `assets/diagrams/` et intégrés via :

```html
<iframe
  src="https://viewer.diagrams.net/?url=https://raw.githubusercontent.com/LEskargot/TropicalNotes/main/assets/diagrams/[fichier].drawio.xml&embed=1&toolbar=0"
  width="100%" height="500" style="border:none; border-radius:12px;">
</iframe>
```

| Fichier source | Destination | Page |
|---|---|---|
| `algo-dermatose.drawio.xml` | `assets/diagrams/algo-dermatose.drawio.xml` | dermatoses |
| `algo-diarrhée.drawio.xml` | `assets/diagrams/algo-diarrhee.drawio.xml` | diarrhee |

### Graphiques Plotly → HTML interactif → `<iframe>`

Modifier les scripts Python pour exporter en HTML (`fig.write_html(..., include_plotlyjs='cdn')`), puis copier vers `assets/charts/`.

| Script source | HTML généré | Page |
|---|---|---|
| `scripts/barres_etiologies_diarrhee.py` | `assets/charts/barres-etiologies.html` | diarrhee |
| `scripts/camembert_etiologies_diarrhee.py` | `assets/charts/camembert-etiologies.html` | diarrhee |
| `modules/.../carte-resistance-fq.html` | `assets/charts/carte-resistance-fq.html` | diarrhee |

### Photos cliniques → `assets/images/dermato/`

Copier depuis `md-slides/modules/urgences-infectio-voyage/photos-dermato/` :
- `larva-migrans-iowa.jpg`
- `myiasis-cobuccio-1.jpg`
- `myiasis-cobuccio-2.jpg`
- `leishmaniasis-iowa.jpg`
- `scabies-iowa.jpg`
- `hansen-iowa.jpg`

### Silhouette

`silhouette-femme.png` → `assets/images/silhouette-femme.png` (page dermatoses)

---

## CSS

Un fichier Tailwind partagé pour les pages syndrome : `dist/css/syndrome.css`

Entry point : `src/css/syndrome.css` (étend prototype.css ou identique)

Build : `npx tailwindcss -i src/css/syndrome.css -o dist/css/syndrome.css --minify`

Les styles inline spécifiques aux pages (tableaux, cards, points clés, hero) sont déclarés dans un `<style>` dans chaque page, en reprenant les tokens du design système.

---

## Contenu par page

### Fièvre au retour (`fievre.html`)
- **Urgence :** oui (badge ⚡)
- **Pathogènes liés :** malaria, dengue, rickettsiosis, enteric_fever, schistosomiasis
- **Traitement clé :** Riamet® 5j (SSTTM 2025), artésunate IV, doxycycline, azithromycine XDR
- **Piège :** TDR négatif ≠ paludisme exclu
- **Perle :** Swiss TPH 24/7, Riamet >65 kg → J28
- **Assets :** aucune image/iframe spécifique (pas de drawio pour fièvre)

### Diarrhée du voyageur (`diarrhee.html`)
- **Urgence :** non
- **Pathogènes liés :** (pas de pages dédiées existantes — lister sans lien)
- **Traitement clé :** azithromycine 1g dose unique, ESBL → culture avant ATB
- **Piège :** classification par nombre de selles (faux) vs impact fonctionnel
- **Perle :** Asie = 75% ESBL → culture avant tout ATB au retour
- **Assets :** `barres-etiologies.html`, `camembert-etiologies.html`, `carte-resistance-fq.html`, `algo-diarrhee.drawio.xml`

### Dermatoses du voyageur (`dermatoses.html`)
- **Urgence :** non
- **Pathogènes liés :** leishmaniasis (lien existant)
- **Traitement clé :** ivermectine dose unique (CLM, gale), occlusion (myiase), REFER (leishmaniose)
- **Piège :** CLM diagnostiquée comme mycose → antimycotiques inefficaces
- **Perle :** ivermectine = "couteau suisse" tropical (CLM, gale, strongyloïdose)
- **Assets :** photos cliniques (4 pathologies), `algo-dermatose.drawio.xml`, `silhouette-femme.png`

### Éosinophilie du voyageur (`eosinophilie.html`)
- **Urgence :** non (mais URGENCE si corticoïdes + _Strongyloides_ non exclu)
- **Pathogènes liés :** schistosomiasis (lien existant)
- **Traitement clé :** ivermectine (Subvectin® 3 mg), praziquantel 40 mg/kg
- **Piège :** coproparasitologie négative unique = rassurant (faux) — sensibilité 20-30%
- **Perle :** JAMAIS corticoïdes sans dépistage _Strongyloides_ (même corticothérapie courte) — mortalité hyperinfection 60-85%
- **Assets :** algorithme pratique = tableau HTML (pas de drawio)

---

## Liens retour

Après création des 4 pages, mettre à jour les cards syndrome dans `prototype.html` avec les vrais liens `href`.

---

## Contraintes techniques

- **GitHub Pages** (site statique) : pas de serveur, tout en HTML/CSS/JS vanilla
- Les iframes diagrams.net fonctionnent uniquement après push sur GitHub (URL raw GitHub)
- Node.js v22 : utiliser Tailwind CLI directement (pas Laravel Mix)
- Pas de framework JS : interactions (barre d'ancres active) en vanilla JS minimal
