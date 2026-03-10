# Syndrome Pages Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build 4 static HTML syndrome pages (fièvre, diarrhée, dermatoses, éosinophilie) in the Tailwind design system, sourced from md-slides modules, deployed via GitHub Pages.

**Architecture:** Each page is a standalone HTML file that links to `../../dist/css/prototype.css` (already built) and defines page-specific component styles in an inline `<style>` block using CSS custom properties from the design tokens. No additional build step required. Assets (images, Plotly HTML, draw.io files) are copied from `md-slides` into `TropicalNotes/assets/`.

**Tech Stack:** HTML5, Tailwind CSS (via prototype.css), vanilla JS (scroll spy only), Plotly.js (chart HTML files), diagrams.net viewer (draw.io iframes), Google Fonts CDN, Python 3 + Plotly (chart export scripts, run once)

---

## File Map

### New files
| File | Responsibility |
|---|---|
| `pages/syndromes/fievre.html` | Fièvre au retour page |
| `pages/syndromes/diarrhee.html` | Diarrhée du voyageur page |
| `pages/syndromes/dermatoses.html` | Dermatoses du voyageur page |
| `pages/syndromes/eosinophilie.html` | Éosinophilie du voyageur page |
| `assets/charts/barres-etiologies.html` | Plotly bar chart (étiologies diarrhée) |
| `assets/charts/camembert-etiologies.html` | Plotly donut chart (étiologies diarrhée) |
| `assets/charts/carte-resistance-fq.html` | Plotly choropleth (résistance FQ) |
| `assets/diagrams/algo-dermatose.drawio.xml` | Draw.io algorithm (dermatoses) |
| `assets/diagrams/algo-diarrhee.drawio.xml` | Draw.io algorithm (diarrhée) |
| `assets/images/dermato/larva-migrans-iowa.jpg` | Clinical photo CLM |
| `assets/images/dermato/myiasis-cobuccio-1.jpg` | Clinical photo myiase J1 |
| `assets/images/dermato/myiasis-cobuccio-2.jpg` | Clinical photo myiase J4 |
| `assets/images/dermato/leishmaniasis-iowa.jpg` | Clinical photo leishmaniose |
| `assets/images/dermato/scabies-iowa.jpg` | Clinical photo gale |
| `assets/images/dermato/hansen-iowa.jpg` | Clinical photo Hansen |
| `assets/images/silhouette-femme.png` | Silhouette figure dermatoses |

### Modified files
| File | Change |
|---|---|
| `prototype.html` | Update 4 syndrome card `href` attributes to point to syndrome pages |
| `md-slides/scripts/barres_etiologies_diarrhee.py` | Add `fig.write_html()` export line |
| `md-slides/scripts/camembert_etiologies_diarrhee.py` | Add `fig.write_html()` export line |

---

## Shared HTML patterns

All 4 pages share the same structure. Reference the mockup at:
`.superpowers/brainstorm/408-1773117160/syndrome-page-design.html`

**Head boilerplate** (path prefix = `../../` for all syndrome pages):
```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="../../dist/css/prototype.css" rel="stylesheet">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Source+Sans+3:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
```

**Navbar** (copy verbatim from prototype.html, update `href="#"` links to `../../prototype.html#syndromes` etc.)

**Draw.io iframe pattern** (works after push to GitHub main branch):
```html
<iframe
  src="https://viewer.diagrams.net/?url=https://raw.githubusercontent.com/LEskargot/TropicalNotes/main/assets/diagrams/FILENAME.drawio.xml&embed=1&toolbar=0&layers=1"
  width="100%" height="520"
  style="border:none; border-radius:12px; background:#f0fafa;"
  loading="lazy"
  title="Algorithme diagnostique">
</iframe>
```

**Scroll spy JS** (add before `</body>` on each page):
```html
<script>
  const sections = document.querySelectorAll('.section[id]');
  const anchorLinks = document.querySelectorAll('.anchor-link');
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        anchorLinks.forEach(l => l.classList.remove('active'));
        const active = document.querySelector(`.anchor-link[href="#${entry.target.id}"]`);
        if (active) active.classList.add('active');
      }
    });
  }, { threshold: 0.3 });
  sections.forEach(s => observer.observe(s));
</script>
```

**Grain texture** (body::after, copy from prototype.html inline style)

---

## Chunk 1: Assets and chart generation

### Task 1: Create directory structure

**Files:**
- Create: `pages/syndromes/` (directory)
- Create: `assets/charts/` (directory)
- Create: `assets/diagrams/` (directory)
- Create: `assets/images/dermato/` (directory)

- [ ] **Step 1: Create directories**

```bash
mkdir -p pages/syndromes
mkdir -p assets/charts
mkdir -p assets/diagrams
mkdir -p "assets/images/dermato"
```

- [ ] **Step 2: Verify directories exist**

```bash
ls -d pages/syndromes assets/charts assets/diagrams assets/images/dermato
```

Expected: 4 lines, each directory listed without error.

- [ ] **Step 3: Commit skeleton**

```bash
git add pages/syndromes assets/charts assets/diagrams assets/images
git commit -m "feat: create syndrome pages and assets directory structure"
```

---

### Task 2: Copy static assets from md-slides

Source root: `C:/Users/ludov/Projects/md-slides/modules/urgences-infectio-voyage/`

**Files:**
- Create: `assets/diagrams/algo-dermatose.drawio.xml`
- Create: `assets/diagrams/algo-diarrhee.drawio.xml`
- Create: `assets/charts/carte-resistance-fq.html`
- Create: `assets/images/dermato/` (7 photos)
- Create: `assets/images/silhouette-femme.png`

- [ ] **Step 1: Copy draw.io algorithm files**

```bash
MDSRC="C:/Users/ludov/Projects/md-slides/modules/urgences-infectio-voyage"
cp "$MDSRC/algo-dermatose.drawio.xml" assets/diagrams/algo-dermatose.drawio.xml
cp "$MDSRC/algo-diarrhée.drawio.xml" assets/diagrams/algo-diarrhee.drawio.xml
```

Note: source filename has accent (`algo-diarrhée`), destination is ASCII (`algo-diarrhee`).

- [ ] **Step 2: Verify draw.io files**

```bash
ls -lh assets/diagrams/
```

Expected: 2 files, each >10KB (draw.io XML is typically 30–200KB).

- [ ] **Step 3: Copy Plotly carte-resistance HTML**

```bash
MDSRC="C:/Users/ludov/Projects/md-slides/modules/urgences-infectio-voyage"
cp "$MDSRC/carte-resistance-fq.html" assets/charts/carte-resistance-fq.html
```

- [ ] **Step 4: Copy clinical photos**

```bash
MDSRC="C:/Users/ludov/Projects/md-slides/modules/urgences-infectio-voyage"
cp "$MDSRC/photos-dermato/larva-migrans-iowa.jpg" assets/images/dermato/
cp "$MDSRC/photos-dermato/myiasis-cobuccio-1.jpg" assets/images/dermato/
cp "$MDSRC/photos-dermato/myiasis-cobuccio-2.jpg" assets/images/dermato/
cp "$MDSRC/photos-dermato/leishmaniasis-iowa.jpg" assets/images/dermato/
cp "$MDSRC/photos-dermato/scabies-iowa.jpg" assets/images/dermato/
cp "$MDSRC/photos-dermato/hansen-iowa.jpg" assets/images/dermato/
cp "$MDSRC/silhouette-femme.png" assets/images/silhouette-femme.png
```

- [ ] **Step 5: Verify photos**

```bash
ls assets/images/dermato/ | wc -l
```

Expected: `6`

- [ ] **Step 6: Commit assets**

```bash
git add assets/
git commit -m "feat: add syndrome page assets (draw.io, photos, Plotly carte)"
```

---

### Task 3: Generate interactive Plotly chart HTML files

Modify the two Python scripts to also export HTML, then run them locally.

**Files:**
- Modify: `C:/Users/ludov/Projects/md-slides/scripts/barres_etiologies_diarrhee.py`
- Modify: `C:/Users/ludov/Projects/md-slides/scripts/camembert_etiologies_diarrhee.py`
- Create: `assets/charts/barres-etiologies.html`
- Create: `assets/charts/camembert-etiologies.html`

- [ ] **Step 1: Edit barres_etiologies_diarrhee.py — replace export block**

In `C:/Users/ludov/Projects/md-slides/scripts/barres_etiologies_diarrhee.py`, replace the last 3 lines:

```python
# --- Export ---
output_path = "/home/ubuntu/md-slides/modules/urgences-infectio-voyage/barres-etiologies.png"
fig.write_image(output_path, width=750, height=750, scale=2, engine="kaleido")
print(f"Exporté: {output_path}")
```

With:

```python
# --- Export ---
import os
out_dir = os.path.join(os.path.dirname(__file__), "..", "..", "TropicalNotes", "assets", "charts")
os.makedirs(out_dir, exist_ok=True)
html_path = os.path.join(out_dir, "barres-etiologies.html")
fig.write_html(html_path, include_plotlyjs="cdn", full_html=True)
print(f"Exporté HTML: {html_path}")
```

- [ ] **Step 2: Edit camembert_etiologies_diarrhee.py — replace export block**

In `C:/Users/ludov/Projects/md-slides/scripts/camembert_etiologies_diarrhee.py`, replace the last 3 lines:

```python
# --- Export ---
output_path = "/home/ubuntu/md-slides/modules/urgences-infectio-voyage/camembert-etiologies.png"
fig.write_image(output_path, width=1200, height=750, scale=2, engine="kaleido")
print(f"Exporté: {output_path}")
```

With:

```python
# --- Export ---
import os
out_dir = os.path.join(os.path.dirname(__file__), "..", "..", "TropicalNotes", "assets", "charts")
os.makedirs(out_dir, exist_ok=True)
html_path = os.path.join(out_dir, "camembert-etiologies.html")
fig.write_html(html_path, include_plotlyjs="cdn", full_html=True)
print(f"Exporté HTML: {html_path}")
```

- [ ] **Step 3: Run both scripts**

```bash
cd "C:/Users/ludov/Projects/md-slides"
python scripts/barres_etiologies_diarrhee.py
python scripts/camembert_etiologies_diarrhee.py
```

Expected output (each):
```
Exporté HTML: .../TropicalNotes/assets/charts/barres-etiologies.html
Exporté HTML: .../TropicalNotes/assets/charts/camembert-etiologies.html
```

If `plotly` is not installed: `pip install plotly`

- [ ] **Step 4: Verify HTML files exist and are non-empty**

```bash
ls -lh C:/Users/ludov/Projects/TropicalNotes/assets/charts/
```

Expected: 3 files (`barres-etiologies.html`, `camembert-etiologies.html`, `carte-resistance-fq.html`), each >100KB.

- [ ] **Step 5: Quick visual check — open in browser**

Open `assets/charts/barres-etiologies.html` in browser. Should show an interactive horizontal bar chart with coloured bars and range brackets. Hover should show tooltips.

- [ ] **Step 6: Commit charts**

```bash
cd "C:/Users/ludov/Projects/TropicalNotes"
git add assets/charts/barres-etiologies.html assets/charts/camembert-etiologies.html
git commit -m "feat: add interactive Plotly chart HTML files for diarrhee page"
```

---

## Chunk 2: Fièvre au retour page

### Task 4: Create pages/syndromes/fievre.html

**Files:**
- Create: `pages/syndromes/fievre.html`

Content sourced from: `C:/Users/ludov/Projects/md-slides/modules/urgences-infectio-voyage/module_fievre_voyageur.md`

Key slides to use: `rationale_q1` (urgency table), `cas_clinique_q2` (workup), `portrait_malaria`, `portrait_dengue`, `rationale_rickettsiose`, `rationale_typhoide`, `rationale_q3a` (treatment Riamet), `rationale_katayama`, `points_cles`, `evidence`

- [ ] **Step 1: Create fievre.html with full page structure**

Write `pages/syndromes/fievre.html` with the following complete content:

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Fièvre au retour de voyage — Tropical Notebook</title>
  <link href="../../dist/css/prototype.css" rel="stylesheet">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Source+Sans+3:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  <style>
    /* Grain texture */
    body::after { content:''; position:fixed; inset:0; pointer-events:none; z-index:9999; opacity:0.025; background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E"); }

    /* Design tokens */
    :root {
      --teal-50:#f0fafa; --teal-100:#d9f2f1; --teal-200:#b0e4e2;
      --teal-400:#479793; --teal-500:#2a9d8f; --teal-700:#2d5e5b;
      --teal-800:#1a3836; --teal-900:#0f2322;
      --mint-50:#edfcf8; --mint-200:#a6f0de; --mint-300:#66dfc2;
      --mint-400:#2dcaab; --mint-600:#1a8b7a;
      --gold-400:#d4a84b; --gold-100:#fef3cd;
      --cream-50:#fefdfb; --cream-100:#fdfaf4; --cream-200:#f8f2e4;
    }

    /* Navbar */
    .nav-fixed { backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px); }
    .dropdown-menu { opacity:0; visibility:hidden; transform:translateY(-4px); transition:all 0.2s ease; }
    .dropdown:hover .dropdown-menu { opacity:1; visibility:visible; transform:translateY(0); }

    /* Hero */
    .hero-pattern { position:absolute; inset:0; opacity:0.05; background-image:url("data:image/svg+xml,%3Csvg width='80' height='80' viewBox='0 0 80 80' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M40 0c2 12 8 20 20 24-12 2-18 8-20 16-2-8-8-14-20-16C32 20 38 12 40 0z' fill='%23ffffff' fill-opacity='0.4'/%3E%3C/svg%3E"); }

    /* Anchor nav */
    .anchor-nav { background:white; border-bottom:1px solid var(--teal-100); position:sticky; top:56px; z-index:40; }
    .anchor-nav-inner { max-width:900px; margin:0 auto; padding:0 1.5rem; display:flex; overflow-x:auto; scrollbar-width:none; }
    .anchor-nav-inner::-webkit-scrollbar { display:none; }
    .anchor-link { color:var(--teal-700); font-size:0.82rem; padding:0.75rem 1rem; border-bottom:2px solid transparent; text-decoration:none; white-space:nowrap; transition:color 0.2s,border-color 0.2s; font-weight:500; }
    .anchor-link:hover { color:var(--teal-500); border-bottom-color:var(--teal-200); }
    .anchor-link.active { color:var(--teal-500); border-bottom-color:var(--teal-500); }

    /* Sections */
    .section { margin-bottom:3.5rem; scroll-margin-top:112px; }
    .section-icon { width:38px; height:38px; border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:1.1rem; flex-shrink:0; }
    .section-label { font-size:0.72rem; text-transform:uppercase; letter-spacing:0.12em; font-weight:600; color:var(--teal-400); margin-bottom:0.15rem; }
    .section-title { font-family:"DM Serif Display",serif; font-size:1.45rem; color:var(--teal-800); }
    .divider { height:1px; background:linear-gradient(90deg,var(--teal-200),transparent); margin-bottom:1.25rem; }

    /* Urgency table */
    .urgency-table { border-radius:12px; overflow:hidden; border:1px solid var(--teal-100); }
    .urgency-row { display:grid; grid-template-columns:1fr 130px 1fr; align-items:center; padding:0.75rem 1rem; border-bottom:1px solid var(--teal-50); background:white; }
    .urgency-row:last-child { border-bottom:none; }
    .urgency-row:hover { background:var(--teal-50); }
    .urgency-row.header { background:var(--teal-800); color:white; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em; font-weight:600; }
    .badge { display:inline-flex; align-items:center; justify-content:center; border-radius:6px; padding:0.2rem 0.55rem; font-size:0.73rem; font-weight:700; }
    .badge-now { background:#fee2e2; color:#991b1b; }
    .badge-2h { background:#fef3c7; color:#92400e; }
    .badge-same { background:#dbeafe; color:#1e40af; }

    /* Workup table */
    .workup-table { width:100%; border-collapse:separate; border-spacing:0; border-radius:12px; overflow:hidden; border:1px solid var(--teal-100); }
    .workup-table th { background:var(--teal-800); color:white; padding:0.65rem 1rem; text-align:left; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em; }
    .workup-table td { padding:0.65rem 1rem; border-bottom:1px solid var(--teal-50); background:white; font-size:0.88rem; vertical-align:top; }
    .workup-table tr:last-child td { border-bottom:none; }
    .workup-table tr:hover td { background:var(--teal-50); }
    .test-name { font-weight:600; color:var(--teal-800); }
    .test-tip { font-size:0.77rem; color:var(--teal-400); margin-top:0.15rem; font-style:italic; }
    .chip { display:inline-block; border-radius:4px; padding:0.1rem 0.45rem; font-size:0.73rem; font-weight:600; margin-right:3px; }
    .chip-urgent { background:#fee2e2; color:#991b1b; }
    .chip-std { background:var(--mint-50); color:var(--mint-600); }
    .chip-opt { background:var(--cream-200); color:var(--teal-700); }

    /* Pathogen cards */
    .pathogen-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(195px,1fr)); gap:1rem; }
    .pathogen-card { background:white; border-radius:12px; border:1px solid var(--teal-100); padding:1.1rem; text-decoration:none; color:inherit; transition:transform 0.3s cubic-bezier(0.22,1,0.36,1),box-shadow 0.3s; position:relative; overflow:hidden; display:block; }
    .pathogen-card::before { content:''; position:absolute; bottom:0; left:0; right:0; height:3px; background:linear-gradient(90deg,var(--teal-700),var(--teal-400)); transform:scaleX(0); transform-origin:left; transition:transform 0.35s cubic-bezier(0.22,1,0.36,1); }
    .pathogen-card:hover { transform:translateY(-4px); box-shadow:0 16px 32px -8px rgba(26,56,54,0.12); }
    .pathogen-card:hover::before { transform:scaleX(1); }
    .patho-cat { font-size:0.68rem; text-transform:uppercase; letter-spacing:0.1em; color:var(--teal-400); font-weight:600; margin-bottom:0.3rem; }
    .patho-name { font-family:"DM Serif Display",serif; font-size:1.05rem; color:var(--teal-800); margin-bottom:0.2rem; }
    .patho-agent { font-size:0.8rem; color:var(--teal-700); font-style:italic; margin-bottom:0.5rem; }
    .patho-link { font-size:0.75rem; color:var(--teal-400); }

    /* Treatment cards */
    .treatment-card { background:white; border-radius:12px; border:1px solid var(--teal-100); border-left:4px solid var(--teal-400); padding:1.1rem 1.25rem; margin-bottom:1rem; }
    .treatment-card.urgent { border-left-color:#ef4444; }
    .treatment-card.secondary { border-left-color:var(--gold-400); }
    .treatment-condition { font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em; color:var(--teal-400); font-weight:600; margin-bottom:0.4rem; }
    .treatment-card.urgent .treatment-condition { color:#ef4444; }
    .treatment-card.secondary .treatment-condition { color:#b45309; }
    .treatment-drug { font-family:"DM Serif Display",serif; font-size:1.15rem; color:var(--teal-800); margin-bottom:0.3rem; }
    .treatment-detail { font-size:0.88rem; color:var(--teal-700); line-height:1.55; }
    .treatment-source { font-size:0.73rem; color:var(--teal-400); margin-top:0.5rem; border-top:1px solid var(--teal-50); padding-top:0.4rem; }
    .treatment-warning { background:#fff7ed; border:1px solid #fed7aa; border-radius:8px; padding:0.75rem 1rem; font-size:0.85rem; color:#9a3412; margin-top:0.75rem; display:flex; gap:0.5rem; line-height:1.5; }

    /* Swiss TPH */
    .swisstph-box { background:linear-gradient(135deg,var(--teal-800),var(--teal-700)); border-radius:12px; padding:1.25rem 1.5rem; color:white; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:1rem; margin-top:1.5rem; }
    .swisstph-label { font-size:0.72rem; text-transform:uppercase; letter-spacing:0.1em; color:var(--mint-300); font-weight:600; margin-bottom:0.25rem; }
    .swisstph-title { font-family:"DM Serif Display",serif; font-size:1.1rem; color:#fdfaf4; }
    .swisstph-contact { background:rgba(45,202,171,0.2); border:1px solid rgba(45,202,171,0.3); border-radius:8px; padding:0.5rem 1rem; color:var(--mint-300); font-size:0.9rem; font-weight:600; }

    /* Points clés */
    .points-grid { display:grid; grid-template-columns:1fr 1fr; gap:1rem; }
    .point-card { border-radius:12px; padding:1.1rem 1.25rem; }
    .point-piege { background:#fff7ed; border:1px solid #fed7aa; }
    .point-perle { background:var(--mint-50); border:1px solid rgba(45,202,171,0.2); }
    .point-retenir { background:var(--teal-50); border:1px solid var(--teal-100); grid-column:span 2; }
    .point-label { font-size:0.72rem; text-transform:uppercase; letter-spacing:0.12em; font-weight:700; margin-bottom:0.5rem; }
    .label-piege { color:#c2410c; }
    .label-perle { color:var(--mint-600); }
    .label-retenir { color:var(--teal-700); }
    .point-text { font-size:0.88rem; color:var(--teal-800); line-height:1.55; }
    .retenir-list { list-style:none; display:grid; grid-template-columns:1fr 1fr; gap:0.35rem 1.5rem; margin-top:0.5rem; }
    .retenir-list li { font-size:0.85rem; color:var(--teal-700); display:flex; gap:0.5rem; align-items:flex-start; line-height:1.4; }
    .retenir-list li::before { content:'→'; color:var(--teal-400); flex-shrink:0; font-weight:600; }

    /* Evidence */
    .evidence-list { display:grid; gap:0.5rem; }
    .evidence-item { background:white; border-radius:8px; border:1px solid var(--teal-100); padding:0.7rem 1rem; display:flex; gap:0.75rem; font-size:0.83rem; }
    .evidence-num { color:var(--teal-400); font-weight:700; font-size:0.75rem; flex-shrink:0; width:20px; padding-top:0.05rem; }
    .evidence-text { color:var(--teal-700); line-height:1.45; }

    html { scroll-behavior:smooth; }
  </style>
</head>
<body class="bg-cream-50 font-sans text-teal-900 antialiased">

<!-- NAVBAR -->
<nav class="nav-fixed fixed top-0 left-0 right-0 z-50 bg-teal-900/95 border-b border-teal-700/50">
  <div class="max-w-6xl mx-auto px-6">
    <div class="flex items-center justify-between h-14">
      <a href="../../prototype.html" class="flex items-center gap-3 group">
        <span class="text-mint-400 text-xl">
          <svg width="24" height="24" viewBox="0 0 28 28" fill="none"><path d="M14 2C14 2 8 8 8 14c0 4 2.5 7 6 8V8c0 0 4 3 4 8 0 3-1 5.5-3 7 4-1 7-5 7-9C22 8 14 2 14 2z" fill="currentColor" opacity="0.9"/><path d="M14 8v14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/></svg>
        </span>
        <span class="font-serif text-cream-100 text-lg tracking-wide group-hover:text-mint-300 transition-colors">Tropical Notebook</span>
      </a>
      <div class="hidden md:flex items-center gap-1">
        <a href="../../prototype.html#syndromes" class="px-4 py-2 text-sm text-mint-300 font-semibold">Syndromes</a>
        <div class="dropdown relative">
          <button class="px-4 py-2 text-sm text-cream-200 hover:text-mint-300 transition-colors flex items-center gap-1">
            Pathogènes <svg class="w-3.5 h-3.5 opacity-60" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="dropdown-menu absolute top-full right-0 mt-1 w-48 bg-teal-800 border border-teal-700/50 rounded-lg shadow-xl py-2">
            <a href="../bacteria.html" class="block px-4 py-2 text-sm text-cream-200 hover:bg-teal-700 hover:text-mint-300 transition-colors">Bactéries</a>
            <a href="../viruses.html" class="block px-4 py-2 text-sm text-cream-200 hover:bg-teal-700 hover:text-mint-300 transition-colors">Virus</a>
            <a href="../parasites.html" class="block px-4 py-2 text-sm text-cream-200 hover:bg-teal-700 hover:text-mint-300 transition-colors">Parasites</a>
          </div>
        </div>
        <a href="../../prototype.html#about" class="px-4 py-2 text-sm text-cream-200 hover:text-mint-300 transition-colors">À propos</a>
      </div>
    </div>
  </div>
</nav>

<!-- HERO -->
<div class="pt-14">
  <div style="background:linear-gradient(135deg,#1a3836 0%,#2d5e5b 100%); padding:3rem 1.5rem 2.5rem; position:relative; overflow:hidden;">
    <div class="hero-pattern"></div>
    <div style="max-width:900px; margin:0 auto; position:relative;">
      <div style="position:absolute; top:0; right:0; background:rgba(212,168,75,0.15); border:1px solid rgba(212,168,75,0.3); border-radius:8px; padding:0.5rem 0.9rem; color:#d4a84b; font-size:0.78rem; font-weight:600;">⚡ Urgence diagnostique</div>
      <div style="display:flex; align-items:center; gap:0.5rem; color:#66dfc2; font-size:0.78rem; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:1rem;">
        <a href="../../prototype.html#syndromes" style="color:inherit; text-decoration:none;">Syndromes</a>
        <span style="opacity:0.5">›</span>
        <span style="color:#fdfaf4;">Fièvre au retour</span>
      </div>
      <h1 style="font-family:'DM Serif Display',serif; color:#fdfaf4; font-size:2.4rem; line-height:1.15; margin-bottom:0.75rem;">Fièvre au retour<br>de voyage</h1>
      <p style="color:#d9f2f1; font-size:1rem; line-height:1.6; max-width:600px; margin-bottom:1.5rem;">Approche diagnostique structurée du patient fébrile au retour des tropiques. Priorité absolue au paludisme, dengue, rickettsiose et typhoïde.</p>
      <div style="display:flex; flex-wrap:wrap; gap:0.5rem;">
        <span style="background:rgba(255,255,255,0.1); color:#a6f0de; border:1px solid rgba(102,223,194,0.2); border-radius:20px; padding:0.2rem 0.75rem; font-size:0.78rem;">🌍 Afrique sub-saharienne</span>
        <span style="background:rgba(255,255,255,0.1); color:#a6f0de; border:1px solid rgba(102,223,194,0.2); border-radius:20px; padding:0.2rem 0.75rem; font-size:0.78rem;">🌏 Asie du Sud</span>
        <span style="background:rgba(255,255,255,0.1); color:#a6f0de; border:1px solid rgba(102,223,194,0.2); border-radius:20px; padding:0.2rem 0.75rem; font-size:0.78rem;">Amérique tropicale</span>
        <span style="background:rgba(255,255,255,0.1); color:#a6f0de; border:1px solid rgba(102,223,194,0.2); border-radius:20px; padding:0.2rem 0.75rem; font-size:0.78rem;">SSTTM 2025</span>
      </div>
    </div>
  </div>
</div>

<!-- ANCHOR NAV -->
<div class="anchor-nav">
  <div class="anchor-nav-inner">
    <a href="#diagnostic" class="anchor-link active">Diagnostic</a>
    <a href="#bilan" class="anchor-link">Bilan</a>
    <a href="#pathogenes" class="anchor-link">Pathogènes</a>
    <a href="#traitement" class="anchor-link">Traitement</a>
    <a href="#points-cles" class="anchor-link">Points clés</a>
    <a href="#references" class="anchor-link">Références</a>
  </div>
</div>

<!-- MAIN -->
<div style="max-width:900px; margin:0 auto; padding:2.5rem 1.5rem 4rem;">

  <!-- 1. APPROCHE DIAGNOSTIQUE -->
  <div class="section" id="diagnostic">
    <div style="display:flex; align-items:center; gap:0.75rem; margin-bottom:1.25rem;">
      <div class="section-icon" style="background:var(--mint-50);">🔍</div>
      <div>
        <div class="section-label">Étape 1</div>
        <h2 class="section-title">Approche diagnostique</h2>
      </div>
    </div>
    <div class="divider"></div>
    <p style="font-size:0.9rem; color:var(--teal-700); margin-bottom:1.25rem; line-height:1.6;">Fièvre + retour de voyage = exclure le paludisme en urgence. La temporalité de prise en charge guide l'ensemble du bilan.</p>
    <div class="urgency-table">
      <div class="urgency-row header">
        <span>Pathogène</span><span>Délai d'action</span><span>Clé diagnostique</span>
      </div>
      <div class="urgency-row">
        <span style="font-style:italic; font-weight:600; color:var(--teal-800);">Plasmodium falciparum</span>
        <span><span class="badge badge-now">MAINTENANT</span></span>
        <span style="color:var(--teal-700); font-size:0.88rem;">TDR + frottis — 77% des décès par maladie tropicale importée</span>
      </div>
      <div class="urgency-row">
        <span style="font-weight:600; color:var(--teal-800);">Fièvres hémorragiques virales</span>
        <span><span class="badge badge-2h">2 heures</span></span>
        <span style="color:var(--teal-700); font-size:0.88rem;">Isolement immédiat si retour zone endémique avec syndrome hémorragique</span>
      </div>
      <div class="urgency-row">
        <span style="font-style:italic; font-weight:600; color:var(--teal-800);">Dengue sévère</span>
        <span><span class="badge badge-same">Même jour</span></span>
        <span style="color:var(--teal-700); font-size:0.88rem;">Phase critique à la défervescence (J3–7) — NS1 + IgM/IgG</span>
      </div>
      <div class="urgency-row">
        <span style="font-style:italic; font-weight:600; color:var(--teal-800);">Salmonella typhi</span>
        <span><span class="badge badge-same">Même jour</span></span>
        <span style="color:var(--teal-700); font-size:0.88rem;">Hémocultures avant tout ATB — fièvre progressive &gt;7 jours</span>
      </div>
      <div class="urgency-row">
        <span style="font-style:italic; font-weight:600; color:var(--teal-800);">Rickettsia</span> spp.
        <span><span class="badge badge-same">Même jour</span></span>
        <span style="color:var(--teal-700); font-size:0.88rem;">Escarre présente → doxycycline sans attendre la confirmation sérologique</span>
      </div>
    </div>
  </div>

  <!-- 2. BILAN INITIAL -->
  <div class="section" id="bilan">
    <div style="display:flex; align-items:center; gap:0.75rem; margin-bottom:1.25rem;">
      <div class="section-icon" style="background:var(--gold-100);">🧪</div>
      <div>
        <div class="section-label">Étape 2</div>
        <h2 class="section-title">Bilan initial</h2>
      </div>
    </div>
    <div class="divider"></div>
    <table class="workup-table">
      <thead><tr><th>Examen</th><th>Indication</th><th>Commentaire</th></tr></thead>
      <tbody>
        <tr>
          <td><div class="test-name">TDR paludisme + frottis sanguin</div><div class="test-tip">Répéter à H12–24 si forte suspicion clinique</div></td>
          <td><span class="chip chip-urgent">Tous</span></td>
          <td style="font-size:0.88rem; color:var(--teal-700);">Ne pas exclure sur TDR seul — pfhrp2 deletion ~10% faux négatifs en Corne d'Afrique</td>
        </tr>
        <tr>
          <td><div class="test-name">FSC + CRP + bilan hépatique + créatinine</div></td>
          <td><span class="chip chip-urgent">Tous</span></td>
          <td style="font-size:0.88rem; color:var(--teal-700);">Thrombopénie → dengue ou malaria. Cytolyse → dengue, typhoïde, hépatite virale</td>
        </tr>
        <tr>
          <td><div class="test-name">NS1 dengue (ELISA) + IgM/IgG</div><div class="test-tip">NS1 si ≤J5 · IgM/IgG systématiques</div></td>
          <td><span class="chip chip-std">TDR −</span></td>
          <td style="font-size:0.88rem; color:var(--teal-700);">NS1 sensibilité 90% J0–J4 (Pillay Lancet Microbe 2025). NS1 seul insuffisant : toujours combiner IgM/IgG</td>
        </tr>
        <tr>
          <td><div class="test-name">Hémocultures × 2</div></td>
          <td><span class="chip chip-std">Fièvre prolongée</span></td>
          <td style="font-size:0.88rem; color:var(--teal-700);">Avant tout ATB. Rendement maximum pour typhoïde en phase bactériémique (&lt;14j)</td>
        </tr>
        <tr>
          <td><div class="test-name">PCR sur escarre (écouvillon)</div></td>
          <td><span class="chip chip-opt">Si escarre</span></td>
          <td style="font-size:0.88rem; color:var(--teal-700);">Sensibilité &gt;90%. Sérologie <em>Rickettsia</em> positive seulement après J10 — ne pas attendre</td>
        </tr>
        <tr>
          <td><div class="test-name">ECG</div></td>
          <td><span class="chip chip-opt">Avant Riamet®</span></td>
          <td style="font-size:0.88rem; color:var(--teal-700);">QTc baseline avant 1<sup>re</sup> dose, puis 4–6h après 3<sup>e</sup> dose (risque allongement QTc luméfantrine)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- 3. PATHOGÈNES CLÉS -->
  <div class="section" id="pathogenes">
    <div style="display:flex; align-items:center; gap:0.75rem; margin-bottom:1.25rem;">
      <div class="section-icon" style="background:var(--teal-50);">🦠</div>
      <div>
        <div class="section-label">Étape 3</div>
        <h2 class="section-title">Pathogènes clés</h2>
      </div>
    </div>
    <div class="divider"></div>
    <div class="pathogen-grid">
      <a href="../parasites/malaria.html" class="pathogen-card">
        <div class="patho-cat">Parasite</div>
        <div class="patho-name">Paludisme</div>
        <div class="patho-agent">Plasmodium falciparum</div>
        <div class="patho-link">Fiche complète →</div>
      </a>
      <a href="../viruses/dengue.html" class="pathogen-card">
        <div class="patho-cat">Virus</div>
        <div class="patho-name">Dengue</div>
        <div class="patho-agent">Flavivirus (sérotypes 1–4)</div>
        <div class="patho-link">Fiche complète →</div>
      </a>
      <a href="../bacteria/rickettsiosis.html" class="pathogen-card">
        <div class="patho-cat">Bactérie</div>
        <div class="patho-name">Rickettsiose</div>
        <div class="patho-agent">Rickettsia africae</div>
        <div class="patho-link">Fiche complète →</div>
      </a>
      <a href="../bacteria/enteric_fever.html" class="pathogen-card">
        <div class="patho-cat">Bactérie</div>
        <div class="patho-name">Fièvre typhoïde</div>
        <div class="patho-agent">Salmonella typhi XDR</div>
        <div class="patho-link">Fiche complète →</div>
      </a>
      <a href="../parasites/schistosomiasis.html" class="pathogen-card">
        <div class="patho-cat">Parasite</div>
        <div class="patho-name">Katayama / Schistosomiase</div>
        <div class="patho-agent">Schistosoma mansoni</div>
        <div class="patho-link">Fiche complète →</div>
      </a>
    </div>
  </div>

  <!-- 4. TRAITEMENT -->
  <div class="section" id="traitement">
    <div style="display:flex; align-items:center; gap:0.75rem; margin-bottom:1.25rem;">
      <div class="section-icon" style="background:#f0fdf4;">💊</div>
      <div>
        <div class="section-label">Étape 4</div>
        <h2 class="section-title">Traitement</h2>
      </div>
    </div>
    <div class="divider"></div>

    <div class="treatment-card">
      <div class="treatment-condition">Paludisme non compliqué — <em>P. falciparum</em></div>
      <div class="treatment-drug">Riamet® (artéméther / luméfantrine)</div>
      <div class="treatment-detail">
        4 cp 2×/j × <strong>5 jours</strong> (40 cp au total) — <strong>SSTTM 2025</strong><br>
        Schéma 5j recommandé pour tous (taux d'échec tardif ~9.6% à J28 avec schéma 3j si &gt;65 kg).<br>
        Si IMC ≥30 : préférer DHA-pipéraquine (Eurartesim®, à jeun strict).
      </div>
      <div class="treatment-source">Suivi obligatoire : frottis J3, J7, J28 · ECG avant 1<sup>re</sup> dose et à H4–6 après 3<sup>e</sup> dose · Déclaration OFSP 24h</div>
    </div>

    <div class="treatment-card urgent">
      <div class="treatment-condition">⚠ Paludisme grave (≥1 critère de gravité)</div>
      <div class="treatment-drug">Artésunate IV + hospitalisation urgente</div>
      <div class="treatment-detail">
        Critères SSTTM : parasitémie ≥2%, troubles de conscience, Hb &lt;7 g/dL, IRA, SDRA, choc, acidose, hypoglycémie.<br>
        Surveiller PADH (hémolyse retardée post-artésunate) entre J7 et J28.
      </div>
    </div>

    <div class="treatment-card secondary">
      <div class="treatment-condition">Rickettsiose — retour Afrique, escarre présente</div>
      <div class="treatment-drug">Doxycycline 200 mg/j × 7 jours</div>
      <div class="treatment-detail">
        Amélioration clinique typique en 48h. Ne pas attendre la confirmation sérologique (positive seulement &gt;J10).<br>
        Résistance intrinsèque aux bêta-lactamines — l'amoxicilline est inefficace.<br>
        Allergie tétracyclines : azithromycine 500 mg J1, puis 250 mg/j × 4j (données limitées).
      </div>
    </div>

    <div class="treatment-card secondary">
      <div class="treatment-condition">Typhoïde XDR — retour Pakistan / Inde / Bangladesh</div>
      <div class="treatment-drug">Azithromycine 1 g J1, puis 500 mg/j × 7–14j (PO)</div>
      <div class="treatment-detail">
        Résistance plasmidique blaCTX-M-15 : ampicilline + chloramphénicol + TMP-SMX + FQ + C3G (50% Pakistan 2019).<br>
        Forme grave : méropénème 1 g 3×/j IV ± azithromycine × 10–14j.<br>
        Défervescence lente (5–7j) même sous ATB efficace — ne pas changer prématurément.
      </div>
    </div>

    <div class="treatment-card">
      <div class="treatment-condition">Katayama (schistosomiase aiguë) — ≥6–8 semaines après exposition</div>
      <div class="treatment-drug">Praziquantel 40 mg/kg dose unique</div>
      <div class="treatment-detail">
        Attendre ≥6–8 semaines post-exposition (inefficace sur formes immatures).<br>
        Phase aiguë symptomatique : prednisone 0.5–1 mg/kg × 5–7j puis praziquantel différé.<br>
        <strong>Disponibilité en Suisse :</strong> praziquantel non inscrit au Compendium (Art. 49) — contacter Swiss TPH Basel.<br>
        Exclure <em>Strongyloides</em> AVANT tout corticoïde (mortalité hyperinfection 60–85%).
      </div>
    </div>

    <div class="treatment-warning">
      ⚠️ <span><strong>Dengue : AUCUN AINS</strong> (aspirine, ibuprofène, diclofénac, naproxène) — risque hémorragique majeur, y compris en automédication. Paracétamol uniquement. Hospitalisation si signes d'alarme à la défervescence (douleur abdominale, Ht ↑ + plaquettes ↓, saignement muqueux, léthargie).</span>
    </div>

    <div class="swisstph-box">
      <div>
        <div class="swisstph-label">Ressource 24/7 — Suisse</div>
        <div class="swisstph-title">Swiss TPH — Conseil diagnostique et thérapeutique</div>
        <div style="font-size:0.82rem; color:#d9f2f1; margin-top:0.25rem;">Import praziquantel (Art. 49) · Antibiogrammes XDR · Avis spécialisé toute heure</div>
      </div>
      <a href="tel:+41612848144" class="swisstph-contact">+41 61 284 81 44</a>
    </div>
  </div>

  <!-- 5. POINTS CLÉS -->
  <div class="section" id="points-cles">
    <div style="display:flex; align-items:center; gap:0.75rem; margin-bottom:1.25rem;">
      <div class="section-icon" style="background:#fff7ed;">⚡</div>
      <div>
        <div class="section-label">À retenir</div>
        <h2 class="section-title">Points clés</h2>
      </div>
    </div>
    <div class="divider"></div>
    <div class="points-grid">
      <div class="point-card point-piege">
        <div class="point-label label-piege">⚠ Piège</div>
        <div class="point-text">
          <strong>«TDR négatif = paludisme exclu»</strong><br><br>
          FAUX. Délétion pfhrp2 (Corne d'Afrique, ~10% faux négatifs) ou effet prozone en hyperparasitémie. TDR négatif possible même avec parasitémie élevée.<br><br>
          → Répéter TDR + frottis à H12–24 si suspicion clinique forte (retour Afrique, fièvre, pas de prophylaxie).
        </div>
      </div>
      <div class="point-card point-perle">
        <div class="point-label label-perle">✦ Perle</div>
        <div class="point-text">
          <strong>Swiss TPH 24/7 : +41 61 284 81 44</strong><br><br>
          Conseil diagnostic et thérapeutique disponible toute heure, y compris pour import praziquantel (Art. 49), antibiogrammes XDR typhoïde, et conseil malaria compliqué.<br><br>
          Riamet® &gt;65 kg : suivi frottis obligatoire à <strong>J28</strong> (taux d'échec tardif ~10%).
        </div>
      </div>
      <div class="point-card point-retenir">
        <div class="point-label label-retenir">→ Retenir</div>
        <ul class="retenir-list">
          <li>Fièvre + voyage → TDR + frottis IMMÉDIATEMENT — ne peut pas attendre le lendemain</li>
          <li>Riamet® : schéma <strong>5 jours / 40 cp</strong> (SSTTM 2025), surtout si &gt;65 kg</li>
          <li>Dengue : danger à la <strong>défervescence</strong> (J3–7), pas pendant la phase fébrile</li>
          <li>Fièvre + escarre en Afrique → <strong>doxycycline MAINTENANT</strong>, sans attendre séro</li>
          <li>Typhoïde Pakistan/Inde → suspecter XDR → <strong>azithromycine</strong>, pas fluoroquinolone</li>
          <li>Éosinophilie + bain eau douce Afrique = Katayama → <strong>jamais corticoïdes</strong> sans exclure <em>Strongyloides</em></li>
          <li>TDR malaria faux positif possible dans typhoïde (cross-réactivité) → confirmer par frottis + hémocultures</li>
          <li>Déclaration OFSP dans les 24h : paludisme, dengue, typhoïde, rickettsiose</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 6. RÉFÉRENCES -->
  <div class="section" id="references">
    <div style="display:flex; align-items:center; gap:0.75rem; margin-bottom:1.25rem;">
      <div class="section-icon" style="background:var(--cream-200);">📑</div>
      <div>
        <div class="section-label">Bibliographie sélective</div>
        <h2 class="section-title">Références</h2>
      </div>
    </div>
    <div class="divider"></div>
    <div class="evidence-list">
      <div class="evidence-item"><span class="evidence-num">1</span><span class="evidence-text"><strong>Giannone PJ et al.</strong> Swiss Trop Public Health 2022 — 52 décès par maladies tropicales importées en Suisse 1990–2019, paludisme 77%.</span></div>
      <div class="evidence-item"><span class="evidence-num">2</span><span class="evidence-text"><strong>Slack & Genton. 2024</strong> — Importance du dépistage systématique du paludisme au retour de voyage en Suisse.</span></div>
      <div class="evidence-item"><span class="evidence-num">3</span><span class="evidence-text"><strong>Rosenthal PJ. N Engl J Med 2024</strong> — Résistance partielle à l'artémisinine en Afrique de l'Est depuis 2020 ; implications cliniques.</span></div>
      <div class="evidence-item"><span class="evidence-num">4</span><span class="evidence-text"><strong>Jaureguiberry S et al. Am J Trop Med Hyg 2015</strong> — PADH (hémolyse retardée post-artésunate) : incidence, délai, prise en charge.</span></div>
      <div class="evidence-item"><span class="evidence-num">5</span><span class="evidence-text"><strong>Pillay S et al. Lancet Microbe 2025</strong> — NS1 ELISA : sensibilité 90% J0–J4 pour la dengue ; combinaison IgM/IgG indispensable.</span></div>
      <div class="evidence-item"><span class="evidence-num">6</span><span class="evidence-text"><strong>WHO. Global arboviral guidelines 2025</strong> — Prise en charge de la dengue sévère : critères d'alarme et conduite à tenir à la défervescence.</span></div>
      <div class="evidence-item"><span class="evidence-num">7</span><span class="evidence-text"><strong>Camprubí-Ferrer L et al. J Travel Med 2023</strong> — 30.5% des fièvres d'origine inconnue au retour de voyage sont sensibles à la doxycycline.</span></div>
      <div class="evidence-item"><span class="evidence-num">8</span><span class="evidence-text"><strong>Klemm EJ et al. Science 2018</strong> — Emergence XDR <em>Salmonella typhi</em> Pakistan : 87 isolats, résistance plasmidique blaCTX-M-15.</span></div>
      <div class="evidence-item"><span class="evidence-num">9</span><span class="evidence-text"><strong>Logan S et al. Clin Infect Dis 2013</strong> — Sérologie Katayama négative dans 14% des cas à la présentation ; répéter à 6–8 semaines.</span></div>
      <div class="evidence-item"><span class="evidence-num">10</span><span class="evidence-text"><strong>SSTTM / Swiss Society for Travel Medicine. Recommandations 2025</strong> — Schéma Riamet® 5 jours pour le paludisme à <em>P. falciparum</em> non compliqué.</span></div>
    </div>
  </div>

</div><!-- /main -->

<!-- FOOTER -->
<div style="background:var(--teal-800); color:var(--teal-100); padding:2rem 1.5rem; text-align:center; font-size:0.82rem; line-height:1.6;">
  <div style="font-family:'DM Serif Display',serif; color:#fdfaf4; font-size:1.1rem; margin-bottom:0.5rem;">Tropical Notebook</div>
  Médecine tropicale et du voyage pour praticiens — Suisse<br>
  <a href="mailto:ludovico.cobuccio@chuv.ch" style="color:var(--mint-300); text-decoration:none;">ludovico.cobuccio@chuv.ch</a> ·
  <a href="https://traveldoctor.ch" target="_blank" style="color:var(--mint-300); text-decoration:none;">traveldoctor.ch</a>
</div>

<script>
  // Dropdown toggle on mobile
  document.querySelectorAll('.dropdown button').forEach(btn => {
    btn.addEventListener('click', e => {
      e.currentTarget.closest('.dropdown').classList.toggle('active');
    });
  });
  // Scroll spy for anchor nav
  const sections = document.querySelectorAll('.section[id]');
  const anchorLinks = document.querySelectorAll('.anchor-link');
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        anchorLinks.forEach(l => l.classList.remove('active'));
        const active = document.querySelector(`.anchor-link[href="#${entry.target.id}"]`);
        if (active) active.classList.add('active');
      }
    });
  }, { rootMargin: '-56px 0px -60% 0px', threshold: 0 });
  sections.forEach(s => observer.observe(s));
</script>

</body>
</html>
```

- [ ] **Step 2: Verify the file was created and is valid HTML**

```bash
ls -lh pages/syndromes/fievre.html
```

Expected: file exists, size ~25–35KB.

Open `pages/syndromes/fievre.html` directly in a browser (file:// URL). Check:
- Navbar renders with teal background
- Hero with gradient background and urgency badge visible
- Anchor nav bar sticky below navbar
- All 6 sections render with correct icons, tables, and cards
- No JavaScript console errors
- Pathogen card links resolve to existing files (verify `../parasites/malaria.html` etc. exist)

- [ ] **Step 3: Verify pathogen page links exist**

```bash
ls pages/parasites/malaria.html pages/viruses/dengue.html pages/bacteria/rickettsiosis.html pages/bacteria/enteric_fever.html pages/parasites/schistosomiasis.html
```

Expected: 5 files listed without error.

- [ ] **Step 4: Commit fievre page**

```bash
git add pages/syndromes/fievre.html
git commit -m "feat: add fievre au retour syndrome page"
```

---

## Chunk 3: Diarrhée du voyageur page

### Task 5: Create pages/syndromes/diarrhee.html

**Files:**
- Create: `pages/syndromes/diarrhee.html`

Content sourced from: `module_diarrhee_voyageur.md`
Key slides: `epidemiologie`, `severite`, `algorithme`, `carte_resistance_fq`, `esbl_post_voyage`, `points_cles`, `evidence`

- [ ] **Step 1: Create diarrhee.html**

Write `pages/syndromes/diarrhee.html`. Use the same `<head>`, navbar, inline `<style>`, and JS as `fievre.html`. Adapt for diarrhée-specific content:

**Hero:**
- Title: `Diarrhée du voyageur`
- Subtitle: Approche diagnostique et thérapeutique. Sévérité par impact fonctionnel, pas par nombre de selles.
- Tags: 🌏 Asie du Sud, 🌍 Afrique, Amérique latine, ISTM 2017
- No urgency badge

**Section 1 — Approche diagnostique:** Severity classification table:

| Degré | Critère | Conduite |
|---|---|---|
| Légère | Tolérable, n'interfère pas | Hydratation + SRO |
| Modérée | Gênante, interfère avec les activités | ± Lopéramide, ± ATB si asie |
| **Sévère** | **Incapacitante OU dysenterie (selles sanglantes)** | **ATB empirique + investigations** |
| Persistante | ≥14 jours | Bilan parasitologique + coloproctologie |

Key rule box: `Sévérité = impact fonctionnel, pas nombre de selles (ISTM 2017)`

**Section 2 — Bilan initial:**

| Examen | Indication | Commentaire |
|---|---|---|
| Panel PCR bactérien multiplex | Sévère / dysenterie | Campylobacter, Shigella, ETEC, EAEC, EPEC, Salmonella |
| PCR *E. histolytica* | Dysenterie + tropiques | Distingue d'Entamoeba dispar (non pathogène) |
| PCR *C. difficile* | Si hospitalisation/ATB récents | Pas en routine — peu rentable sans facteur de risque |
| Coproparasitologie × 3 | Persistante ≥14j | Giardia, Cryptosporidium, helminthes |

**Section 3 — Graphiques étiologies:** Two Plotly iframes side by side:

```html
<div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:1.5rem;">
  <div>
    <p style="font-size:0.82rem; color:var(--teal-400); font-weight:600; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.5rem;">Proportion par pathogène</p>
    <iframe src="../../assets/charts/barres-etiologies.html" width="100%" height="420" style="border:none; border-radius:12px; background:#f0fafa;" loading="lazy" title="Étiologies diarrhée — fourchettes publiées"></iframe>
  </div>
  <div>
    <p style="font-size:0.82rem; color:var(--teal-400); font-weight:600; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.5rem;">Distribution relative</p>
    <iframe src="../../assets/charts/camembert-etiologies.html" width="100%" height="420" style="border:none; border-radius:12px; background:#f0fafa;" loading="lazy" title="Étiologies diarrhée — distribution"></iframe>
  </div>
</div>
```

**Section 4 — Pathogènes clés:** No dedicated pages exist — use non-linked info cards (same card style but `<div>` not `<a>`):
- ETEC (bactérie, *Escherichia coli* entérotoxinogène)
- *Campylobacter* spp. (bactérie, résistance FQ 75–89% Asie)
- *Shigella* spp. (bactérie, dysenterie)
- Norovirus (virus, ~18% par PCR multiplex)
- *Giardia lamblia* (parasite, diarrhée persistante)
- *Entamoeba histolytica* (parasite, dysenterie amibienne)

**Section 4b — Carte résistance FQ:**
```html
<div style="margin-top:1.5rem;">
  <p style="font-size:0.82rem; color:var(--teal-400); font-weight:600; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.5rem;">Résistance aux fluoroquinolones — <em>Campylobacter</em> spp.</p>
  <iframe src="../../assets/charts/carte-resistance-fq.html" width="100%" height="480" style="border:none; border-radius:12px; background:#f0fafa;" loading="lazy" title="Carte résistance fluoroquinolones"></iframe>
</div>
```

**Section 5 — Traitement:**

| Situation | Traitement |
|---|---|
| Diarrhée sévère / dysenterie, retour Asie | Azithromycine 1g dose unique PO |
| Diarrhée sévère / dysenterie, retour hors Asie | Azithromycine 1g dose unique (1ère ligne) |
| Dysenterie amibienne (*E. histolytica*) | Métronidazole 750 mg 3×/j × 5–10j + diloxanide furate |
| Dysenterie sans fièvre, viande hachée (EHEC) | PAS d'ATB — risque SHU (↑ production stx si ATB) |

Warning box: `Lopéramide CONTRE-INDIQUÉ si dysenterie (selles sanglantes, fièvre >38.3°C) — risque mégacôlon toxique`

**ESBL box** (teal card):
```
Retour Asie du Sud → 75% colonisation ESBL (87% si Inde — Kuenzli 2014)
ATB pendant voyage × diarrhée : OR 3.37 d'acquisition ESBL
→ TOUJOURS urine culture avant ATB si infection urinaire au retour
```

**Section 6 — Algorithme diarrhée:** Draw.io iframe:
```html
<iframe src="https://viewer.diagrams.net/?url=https://raw.githubusercontent.com/LEskargot/TropicalNotes/main/assets/diagrams/algo-diarrhee.drawio.xml&embed=1&toolbar=0&layers=1" width="100%" height="520" style="border:none; border-radius:12px; background:#f0fafa;" loading="lazy" title="Algorithme diarrhée du voyageur"></iframe>
<p style="font-size:0.75rem; color:var(--teal-400); margin-top:0.5rem; text-align:center; font-style:italic;">L'algorithme s'affiche après déploiement sur GitHub Pages</p>
```

**Points clés:**
- Piège: Classifier par nombre de selles → utiliser l'impact fonctionnel
- Perle: Asie du Sud = 75% ESBL → urine culture avant tout ATB au retour
- Retenir: 6 bullets (azithromycine 1ère ligne Asie, dysenterie = ATB, EHEC sans ATB, loperamide CI dysenterie, ESBL, déclaration OFSP)

**Références:** ISTM 2017 (Riddle), Künzli 2021, Jia 2025, Tribble 2007, COMBAT 2017 (Arcilla), Kuenzli 2014, Kantele 2015, Woerther 2017, Chappuis 2020 HUG

- [ ] **Step 2: Verify diarrhee.html renders correctly**

Open `pages/syndromes/diarrhee.html` in browser. Check:
- Iframes for bar chart and donut chart load (local file:// — Plotly charts should render since they use CDN JS)
- Draw.io iframe shows placeholder text (expected locally, will work after push)
- Pathogen cards display without broken links (info cards, no `href` needed)
- Warning boxes render in correct colors

- [ ] **Step 3: Commit diarrhee page**

```bash
git add pages/syndromes/diarrhee.html
git commit -m "feat: add diarrhee du voyageur syndrome page"
```

---

## Chunk 4: Dermatoses du voyageur page

### Task 6: Create pages/syndromes/dermatoses.html

**Files:**
- Create: `pages/syndromes/dermatoses.html`

Content sourced from: `module_dermatoses_voyageur.md`
Key slides: `epidemio`, `rationale_clm`, `rationale_myiase`, `rationale_leishmaniose`, `rationale_gale`, `algorithme`, `points_cles`, `evidence`

- [ ] **Step 1: Create dermatoses.html**

Write `pages/syndromes/dermatoses.html`. Same head/navbar/style/JS structure.

**Hero:**
- Title: `Dermatoses du voyageur`
- Subtitle: Approche morphologique — 4 patterns → 4 diagnostics. Pied + plage + trajet serpentant = CLM jusqu'à preuve du contraire.
- Tags: Caraïbes, Amérique centrale, Afrique sub-saharienne, Asie du Sud-Est

**Section 1 — Approche diagnostique:** Morphology table:

| Morphologie | Diagnostic principal | Agents | Traitement |
|---|---|---|---|
| Trajet serpentant / linéaire | **CLM (larva migrans cutanée)** | *Ancylostoma braziliense*, *A. caninum* | Ivermectine 200 µg/kg dose unique |
| Nodule + punctum central | **Myiase furonculaire** | *Dermatobia hominis*, *Cordylobia anthropophaga* | Occlusion → extraction 24–48h |
| Ulcère indolore + bords surélevés | **Leishmaniose cutanée** | *Leishmania* spp. | Biopsie + PCR espèce → RÉFÉRER |
| Papules prurigineuses diffuses | **Gale / piqûres arthropodes** | *Sarcoptes scabiei* | Perméthrine 5% + ivermectine PO |

**Section 2 — Photos cliniques:** 4 clinical case blocks, each with image + diagnosis + management:

**CLM block:**
```html
<div style="display:grid; grid-template-columns:280px 1fr; gap:1.5rem; align-items:start; background:white; border-radius:12px; border:1px solid var(--teal-100); padding:1.25rem; margin-bottom:1rem;">
  <img src="../../assets/images/dermato/larva-migrans-iowa.jpg" alt="Larva migrans cutanée — trajet serpentant" style="width:100%; border-radius:8px; object-fit:cover;">
  <div>
    <div style="font-size:0.72rem; text-transform:uppercase; letter-spacing:0.1em; color:var(--teal-400); font-weight:600; margin-bottom:0.3rem;">Cas clinique — CLM</div>
    <h3 style="font-family:'DM Serif Display',serif; font-size:1.15rem; color:var(--teal-800); margin-bottom:0.5rem;">Larva migrans cutanée</h3>
    <p style="font-size:0.88rem; color:var(--teal-700); line-height:1.55; margin-bottom:0.75rem;"><em>Ancylostoma braziliense / A. caninum</em> — larves d'ankylostomes animaux en impasse parasitaire chez l'homme. Pieds (39%), contact avec sable/plage. Avance de quelques mm/j.<br><br>Diagnostic clinique. Délai moyen au diagnostic : 41 jours (Sow 2017).</p>
    <div style="background:var(--mint-50); border:1px solid rgba(45,202,171,0.2); border-radius:8px; padding:0.65rem 0.9rem; font-size:0.85rem; color:var(--teal-800);">
      <strong>Traitement :</strong> Ivermectine 200 µg/kg PO dose unique (Subvectin® 3 mg, hors AMM). Guérison &gt;90%.<br>
      Alternative : albendazole 400 mg 2×/j × 3j.<br>
      <span style="color:#c2410c;"><strong>Inefficaces :</strong> mébendzole (0% guérison — López-Neila 2025), cryothérapie (larve survit &gt;5 min à −21°C).</span>
    </div>
  </div>
</div>
```

**Myiase block** (same grid layout):
- Photos: `myiasis-cobuccio-1.jpg` (J1) + `myiasis-cobuccio-2.jpg` (J4)
- Deux photos côte à côte dans la colonne image
- Note: photos Dr. Ludovico Cobuccio
- Content: nodule + punctum central + sensation de mouvement, *Dermatobia hominis* (Amériques) / *Cordylobia anthropophaga* (Afrique), traitement occlusion (vaseline 24–48h) + extraction complète, PAS d'ATB sauf surinfection secondaire

**Leishmaniose block:**
- Photo: `leishmaniasis-iowa.jpg`
- Content: ulcère indolore + bords surélevés, *Leishmania* spp., Amérique du Sud/Centrale/Afrique/Bassin méditerranéen, biopsie + PCR espèce (sensibilité 98% vs frottis 64%), risque mucocutanée (*L. braziliensis*), RÉFÉRER infectiologue/tropicaliste

**Gale block:**
- Photo: `scabies-iowa.jpg`
- Content: papules prurigineuses diffuses, aggravation nocturne, espaces interdigitaux/poignets/plis, *Sarcoptes scabiei*, traitement perméthrine 5% + ivermectine 200 µg/kg PO (OFSP 2024), répéter J7–10, traiter contacts simultanément

**Section 3 — Pathogènes liés:**
- *Leishmania* spp. → link to `../parasites/leishmaniasis.html` (exists)
- CLM, myiase, gale : info cards sans lien

**Section 4 — Algorithme diagnostique:** Draw.io iframe:
```html
<iframe src="https://viewer.diagrams.net/?url=https://raw.githubusercontent.com/LEskargot/TropicalNotes/main/assets/diagrams/algo-dermatose.drawio.xml&embed=1&toolbar=0&layers=1" width="100%" height="520" style="border:none; border-radius:12px; background:#f0fafa;" loading="lazy" title="Algorithme diagnostique dermatoses"></iframe>
<p style="font-size:0.75rem; color:var(--teal-400); margin-top:0.5rem; text-align:center; font-style:italic;">L'algorithme s'affiche après déploiement sur GitHub Pages</p>
```

**Points clés:**
- Piège: «Trajet serpentant = mycose → antimycotique» — FAUX. CLM ≠ mycose (pas de champignon qui progresse mm/j)
- Perle: Ivermectine = «couteau suisse» tropical (CLM, gale, strongyloïdose). Subvectin® 3 mg disponible en Suisse (Swissmedic mai 2023)
- Retenir: 6 bullets (pieds + sable + serpentant = CLM, nodule + punctum = myiase, ulcère indolore = leishmaniose RÉFÉRER, mébendzole inefficace, cryothérapie obsolète, gale perméthrine + ivermectine)

**Références:** Freedman NEJM 2006, Lederman IJID 2008, Bopp JDDG 2025, López-Neila 2025, Bouchaud 2000, Sow 2017, Wilder-Smith & Caumes 2024, Aronson CID 2016 IDSA/ASTMH, Mosimann 2013 Swiss TPH, Kofler OFSP 46/24, Lancet Infect Dis 2015 (myiase), Blaizot 2020

- [ ] **Step 2: Verify dermatoses.html**

Open in browser. Check:
- All 4 clinical photos render (local assets)
- Two-column layout for each case (image + text)
- Link to `../parasites/leishmaniasis.html` exists: `ls pages/parasites/leishmaniasis.html`
- No console errors

- [ ] **Step 3: Commit dermatoses page**

```bash
git add pages/syndromes/dermatoses.html
git commit -m "feat: add dermatoses du voyageur syndrome page"
```

---

## Chunk 5: Éosinophilie du voyageur page

### Task 7: Create pages/syndromes/eosinophilie.html

**Files:**
- Create: `pages/syndromes/eosinophilie.html`

Content sourced from: `module_eosinophilie_voyageur.md`
Key slides: `differentiel`, `diagnostic`, `traitement`, `algorithme_pratique`, `points_cles`, `evidence`

- [ ] **Step 1: Create eosinophilie.html**

Write `pages/syndromes/eosinophilie.html`. Same head/navbar/style/JS.

**Hero:**
- Title: `Éosinophilie du voyageur`
- Subtitle: Voyageur + éosinophilie &gt;0.5 G/L = helminthiase jusqu'à preuve du contraire. Jamais de corticoïdes sans dépistage *Strongyloides*.
- Tags: Afrique sub-saharienne, Asie du Sud-Est, Amérique tropicale, SSTTM · ISTM

**Section 1 — Approche diagnostique:**

**Differential table:**
| Cause | Prévalence | Argument |
|---|---|---|
| **Helminthiases (Schistosoma, Strongyloides, filaires)** | **19–80%** des éosinophilies voyageurs | Voyage tropical, eau douce, myalgies |
| Médicaments (ATB, AINS, anticonvulsants) | Fréquente (délai 2–8 semaines) | Temporalité d'introduction |
| Atopie / asthme | Rarement &gt;1.5 G/L | Éosinophilie modérée, pas de fièvre |
| HES idiopathique | Rare (&lt;5%) | Diagnostic d'exclusion |
| Protozoaires (malaria, Giardia) | **0%** | NE causent PAS d'éosinophilie |

Important box (red): `Protozoaires (malaria, Giardia, Cryptosporidium) = AUCUNE éosinophilie — piège classique`

**Section 2 — Bilan initial:**

Algorithme pratique as a numbered step list (from `algorithme_pratique` slide):

1. **Anamnèse médicamenteuse** — ATB, AINS, anticonvulsants (délai 2–8 semaines)
2. **Sérologie *Strongyloides* (ELISA)** — systématique, sensibilité 89–95%
3. **Sérologie *Schistosoma* (ELISA)** — si exposition eau douce Afrique/Amérique du Sud (sensibilité 71–96% ; répéter à 3 mois si phase aiguë)
4. **Sérologie *Toxocara*** — si HE ≥1.5 G/L (recommandations françaises 2023)
5. **Coproparasitologie × 3 + technique Baermann** — complémentaire ; ne pas se fier à un seul examen négatif (sensibilité *Strongyloides* 20–30%)
6. **Si HE ≥1.5 G/L persistante** → RÉFÉRER (Swiss TPH Basel, CHUV, HUG, Inselspital)

Table: Diagnostic performance:
| Examen | Sensibilité | Note |
|---|---|---|
| Coprologie directe × 1 | ~20–30% *Strongyloides* | Insuffisant seul |
| Baermann (selles) | ~72% | Demander spécifiquement |
| **Sérologie *Strongyloides* ELISA** | **89–95%** | **Référence — systématique** |
| **Sérologie *Schistosoma* ELISA** | **71–96%** | Systématique si eau douce |
| Sérologie *Toxocara* | 78% | Si HE ≥1.5 G/L |

**Section 3 — Pathogènes liés:**
- *Schistosoma mansoni/haematobium* → link to `../parasites/schistosomiasis.html`
- *Strongyloides stercoralis* → info card (no dedicated page)
- *Toxocara* spp. → info card
- Filaires → info card

**Section 4 — Traitement:**

Warning box (RED, prominent):
```
⛔ RÈGLE ABSOLUE
JAMAIS de corticoïdes (même courte durée) sans dépistage Strongyloides préalable
Syndrome d'hyperinfection : mortalité 60–85%
Si dépistage impossible : ivermectine empirique AVANT les corticoïdes
```

Treatment cards:
- *Strongyloides* : ivermectine 200 µg/kg PO dose unique à jeun (Subvectin® 3 mg — Swissmedic mai 2023). Répéter si hyperinfection quotidiennement jusqu'à selles négatives.
- *Schistosoma* phase chronique : praziquantel 40 mg/kg dose unique (ou 2 × 20 mg/kg à 4–6h)
- *Schistosoma* Katayama aiguë : prednisone 0.5–1 mg/kg × 5–7j puis praziquantel à 6–8 semaines
- Praziquantel Suisse : non inscrit Compendium → import Art. 49 via Swiss TPH

**Points clés:**
- Piège: Coproparasitologie négative unique = rassurant — FAUX. Sensibilité *Strongyloides* 20–30%. Référence = sérologie ELISA 89–95%.
- Perle: RÈGLE ABSOLUE — jamais de corticoïdes sans sérologie *Strongyloides* (même 40 ans après voyage, auto-infection indéfinie). Si urgent : ivermectine empirique D'ABORD.
- Retenir: 5 bullets (helminthiase 19–80%, protozoaires = pas d'éo, sérologies ELISA systématiques, JAMAIS corticoïdes, ivermectine Subvectin® + praziquantel via Swiss TPH)

**Références:** Thakker 2025 UK guidelines, Groh 2023 guidelines françaises, Checkley 2010, Logan 2013, Rochat 2015, Requena-Mendez 2017, Asundi 2019, O'Connell & Nutman 2015, Meltzer 2008, Subvectin Swissmedic 2023, Kamgno 2025 (*Loa loa* + ivermectine)

- [ ] **Step 2: Verify eosinophilie.html**

Open in browser. Check:
- Red warning box is prominent and visible
- Numbered algorithm steps render correctly
- Link to `../parasites/schistosomiasis.html` exists
- No console errors

- [ ] **Step 3: Commit eosinophilie page**

```bash
git add pages/syndromes/eosinophilie.html
git commit -m "feat: add eosinophilie du voyageur syndrome page"
```

---

## Chunk 6: Final integration and deployment

### Task 8: Update prototype.html syndrome card links

**Files:**
- Modify: `prototype.html`

- [ ] **Step 1: Find the syndrome card hrefs in prototype.html**

```bash
grep -n "href" prototype.html | grep -i "syndrome\|fievre\|diarrhee\|dermatose\|eosinophil"
```

If no existing syndrome-specific hrefs found, search for the syndrome section cards:

```bash
grep -n "Fièvre\|Diarrhée\|Dermatoses\|Éosinophilie" prototype.html
```

- [ ] **Step 2: Update the 4 syndrome card links**

For each syndrome card `<a>` tag in prototype.html, update the `href` attribute:
- Fièvre au retour → `href="pages/syndromes/fievre.html"`
- Diarrhée du voyageur → `href="pages/syndromes/diarrhee.html"`
- Dermatoses du voyageur → `href="pages/syndromes/dermatoses.html"`
- Éosinophilie du voyageur → `href="pages/syndromes/eosinophilie.html"`

- [ ] **Step 3: Verify links work from prototype.html**

Open `prototype.html` in browser. Click each syndrome card. Verify each respective page opens correctly.

- [ ] **Step 4: Commit prototype.html update**

```bash
git add prototype.html
git commit -m "feat: link syndrome cards in prototype.html to new syndrome pages"
```

---

### Task 9: Final verification and push

- [ ] **Step 1: Verify all files are present**

```bash
ls -lh pages/syndromes/
ls -lh assets/charts/
ls -lh assets/diagrams/
ls -lh assets/images/dermato/
```

Expected:
- `pages/syndromes/`: 4 HTML files
- `assets/charts/`: 3 HTML files (barres, camembert, carte)
- `assets/diagrams/`: 2 drawio.xml files
- `assets/images/dermato/`: 6 jpg files

- [ ] **Step 2: Check git status is clean**

```bash
git status
```

Expected: `nothing to commit, working tree clean`

- [ ] **Step 3: Update project memory**

Update `C:/Users/ludov/.claude/projects/C--Users-ludov-Projects-TropicalNotes/memory/MEMORY.md`:
- Mark syndrome pages as created in the "Next task" section
- Add note: draw.io iframes require push to GitHub to render (viewer.diagrams.net uses raw GitHub URL)
- Add note: Plotly charts in assets/charts/ are self-contained HTML, work locally

- [ ] **Step 4: Push to GitHub**

```bash
git push origin main
```

- [ ] **Step 5: Verify on GitHub Pages**

After push (wait ~1–2 minutes for GitHub Pages to rebuild):

1. Open `https://tropicalnotebook.ch/pages/syndromes/fievre.html` — verify full page renders
2. Open `https://tropicalnotebook.ch/pages/syndromes/diarrhee.html` — verify Plotly iframes load
3. Open `https://tropicalnotebook.ch/pages/syndromes/dermatoses.html` — verify photos load and draw.io iframe renders
4. Open `https://tropicalnotebook.ch/pages/syndromes/eosinophilie.html` — verify red warning box visible
5. Verify draw.io algorithm iframes render (requires GitHub Pages — not local)

- [ ] **Step 6: Final commit if any fixes needed**

If any issues found after live check, fix and commit:

```bash
git add .
git commit -m "fix: post-deployment corrections for syndrome pages"
git push origin main
```
