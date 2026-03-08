# Fièvre au retour — Page syndrome Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build the first syndrome article page "Fièvre au retour de voyage" using the new Tailwind design system, with content from `research-fever-syndromes.md`.

**Architecture:** Static HTML page using Tailwind CSS CDN (same stack as prototype.html). Self-contained file with inline Tailwind config, navbar, floating TOC, two-part content (consultation rapide + pathogènes), and footer. No build system — serves directly via GitHub Pages.

**Tech Stack:** HTML5, Tailwind CSS CDN, vanilla JS (TOC scroll spy), DM Serif Display + Source Sans 3 fonts.

**Content source:** `/home/ubuntu/md-slides/docs/plans/research-fever-syndromes.md`

**Design doc:** `docs/plans/2026-03-08-syndrome-pages-design.md`

---

## Task 1: Create article page shell

**Files:**
- Create: `pages/syndromes/fievre-voyageur.html`

**Step 1: Create directory**

```bash
mkdir -p pages/syndromes
```

**Step 2: Create the HTML shell with shared components**

Copy from `prototype.html`:
- `<head>` block (Tailwind CDN, Google Fonts, Tailwind config, shared CSS)
- Navbar (identical, but update active state for "Syndromes")
- Footer (identical)

Add new article-specific structure:
- Breadcrumb: `Accueil > Par syndrome > Fièvre au retour de voyage`
- Two-column layout: main content (left/center) + floating TOC (right)
- Article header: title + "Dernière mise à jour" date + author

Layout structure:
```html
<body>
  <!-- Navbar from prototype.html -->
  <!-- Breadcrumb -->
  <main class="max-w-6xl mx-auto px-6 pt-24 pb-16">
    <div class="lg:grid lg:grid-cols-[1fr_240px] lg:gap-12">
      <article>
        <!-- Article header -->
        <!-- Part 1: Consultation rapide -->
        <!-- Part 2: Par pathogène -->
        <!-- Points clés -->
        <!-- Références -->
      </article>
      <aside>
        <!-- Floating TOC -->
      </aside>
    </div>
  </main>
  <!-- Footer from prototype.html -->
</body>
```

Article-specific CSS to add:
```css
/* Floating TOC */
.toc { position: sticky; top: 5rem; }
.toc a.active { color: var(--mint-500); border-left-color: var(--mint-500); }

/* Callout boxes */
.callout-piege { border-left: 4px solid #d4a01c; background: #fffceb; }
.callout-referer { border-left: 4px solid #12AD98; background: #edfcf8; }

/* Article typography */
.article-content h2 { font-family: 'DM Serif Display'; }
.article-content table { width: 100%; }

/* Responsive: hide TOC on mobile */
@media (max-width: 1023px) { aside.toc-sidebar { display: none; } }
```

**Step 3: Verify**

Open in browser: `pages/syndromes/fievre-voyageur.html`
Expected: navbar + breadcrumb + empty article area + empty TOC sidebar + footer. Responsive: TOC hidden on mobile.

**Step 4: Commit**

```bash
git add pages/syndromes/fievre-voyageur.html
git commit -m "feat: add article page shell for fièvre au retour syndrome"
```

---

## Task 2: Build Consultation Rapide section

**Files:**
- Modify: `pages/syndromes/fievre-voyageur.html`

**Content source:** `research-fever-syndromes.md` sections:
- "Cadre general" (incubation periods)
- Mandell Table 319.1 (exposure → signs → diagnosis)
- Mandell algorithm steps 1-5
- Declaration obligatoire table

**Step 1: Add Part 1 wrapper with distinct visual treatment**

```html
<section id="consultation-rapide" class="bg-cream-100 border border-teal-200/50 rounded-2xl p-8 mb-12">
  <div class="flex items-center gap-3 mb-6">
    <span class="section-label text-teal-600">Consultation rapide</span>
    <span class="text-xs text-teal-500/60 bg-teal-100 px-2 py-0.5 rounded-full">2 min</span>
  </div>
  <!-- 1.1 Diagramme placeholder -->
  <!-- 1.2 Bilan initial -->
  <!-- 1.3 Declaration obligatoire -->
</section>
```

**Step 2: Add triage diagram placeholder**

Section 1.1 — placeholder for the SVG diagram (draw.io will be created later):

```html
<div id="triage" class="mb-8">
  <h3 class="font-serif text-xl text-teal-800 mb-4">Algorithme de triage</h3>
  <div class="bg-white border-2 border-dashed border-teal-200 rounded-xl p-12 text-center text-teal-400">
    <p class="text-sm">Diagramme de triage (SVG draw.io) — à intégrer</p>
    <p class="text-xs mt-2">Double axe : danger individuel + danger collectif</p>
  </div>
</div>
```

Add incubation periods table from research "Periodes d'incubation" section:

```html
<div class="mt-6 overflow-x-auto">
  <table>
    <thead><tr><th>Incubation</th><th>Pathogènes</th></tr></thead>
    <tbody>
      <tr><td>Courte (&lt;10j)</td><td>Arboviroses, rickettsioses, leptospirose, fièvre typhoïde</td></tr>
      <tr><td>Intermédiaire (10-21j)</td><td>Paludisme, FHV, Q fever, typhoïde, brucellose</td></tr>
      <tr><td>Prolongée (&gt;21j)</td><td>Hépatites virales, paludisme (P. vivax/ovale), TB, abcès amibien</td></tr>
    </tbody>
  </table>
</div>
```

**Step 3: Add bilan initial table**

Section 1.2 — from research + module content (merged):

| Test | Pourquoi | Piège |
|------|---------|-------|
| TDR malaria + frottis/GE | Exclure paludisme en 1er | TDR négatif ≠ exclu — répéter H12-24 si forte suspicion. pfHRP2 délétion (Corne d'Afrique ~10%) : utiliser TDR HRP2+pLDH |
| FSC + réticulocytes + LDH + haptoglobine | Hémolyse, thrombopénie, éosinophilie | Thrombopénie ≠ dengue seule (paludisme aussi) |
| NS1 dengue + IgM/IgG | Diagnostic dengue dès J1 | NS1 Se 90% J0-4, chute après J5 et en infection secondaire |
| Hémocultures × 2 | Typhoïde, sepsis bactérien | Prélever AVANT tout antibiotique |
| Bilan hépatique + créatinine | Sévérité, atteinte d'organe | Cytolyse ≠ hépatite — rickettsiose et dengue aussi |

**Step 4: Add declaration obligatoire table**

Section 1.3 — from research section 5 "Declaration obligatoire en Suisse":

| Maladie | Délai | Modalité |
|---------|-------|----------|
| FHV (Ebola, Marburg, Lassa, CCHF) | **2 heures** | Tél. OFSP 058 463 87 37 + médecin cantonal |
| Paludisme | 24 heures | Infreport / CH ELM |
| Fièvre typhoïde | 24 heures | Infreport / CH ELM |
| Dengue | 24 heures | Infreport / CH ELM |
| Chikungunya | 24 heures | Infreport / CH ELM |
| Zika | 24 heures | Infreport / CH ELM |

**Step 5: Verify**

Open in browser. Expected: cream-colored "Consultation rapide" box with triage placeholder, two tables, visually distinct from rest of page.

**Step 6: Commit**

```bash
git add pages/syndromes/fievre-voyageur.html
git commit -m "feat: add consultation rapide section with bilan and declaration tables"
```

---

## Task 3: Build pathogen blocks — Paludisme + Dengue

**Files:**
- Modify: `pages/syndromes/fievre-voyageur.html`

**Content source:** `research-fever-syndromes.md` sections 1 (Paludisme) and 2 (Dengue/Chikungunya/Zika)

**Step 1: Create the reusable pathogen block HTML pattern**

Each block follows this structure:
```html
<section id="paludisme" class="mb-12">
  <!-- Header with link to detailed page -->
  <div class="flex items-start justify-between mb-4">
    <h2 class="font-serif text-2xl text-teal-900">Paludisme</h2>
    <a href="../parasites/malaria.html" class="text-sm text-mint-600 hover:text-mint-500 flex items-center gap-1">
      Fiche détaillée →
    </a>
  </div>
  <p class="text-sm text-teal-700/70 mb-6 italic">1ère cause de fièvre mortelle chez le voyageur — 77% des décès tropicaux</p>

  <!-- Sub-sections -->
  <div class="space-y-6">
    <div>
      <h3>Quand y penser</h3>
      <!-- bullets -->
    </div>
    <div>
      <h3>Diagnostic</h3>
      <!-- content + piège callout -->
    </div>
    <div>
      <h3>Traitement</h3>
      <!-- table with posologies -->
    </div>
    <!-- Callout piège -->
    <div class="callout-piege">
      <strong>⚠ Piège à éviter</strong>
      <p>...</p>
    </div>
  </div>
</section>
```

**Step 2: Add Paludisme block**

Content from research section 1:

**Quand y penser:**
- Toute fièvre + voyage en zone d'endémie, incubation 10-21j
- Chimioprophylaxie absente ou mal prise
- 8 439 cas en Suisse 1990-2019, 52 décès (Giannone 2022)

**Diagnostic:**
- TDR + frottis/GE, répéter H12-24 si négatif + forte suspicion
- Seuil suisse de parasitémie ≥2% = hyperparasitémie (vs 5% OMS)
- Déclaration obligatoire OFSP

**Traitement — table:**
| Situation | Traitement | Posologie | Suivi |
|-----------|-----------|-----------|-------|
| P.f. non compliqué | Riamet® (A/L) | 5j / 40 cp (SSTTM 2025) | ECG pré-dose + post-3e dose. **Contrôle J3/J7/J28** (échec 9.6% si >65kg) |
| Alternative | Malarone® (A/P) | 4 cp/j × 3j | |
| P.f. sévère | Artésunate IV | 2.4 mg/kg H0, H12, H24 puis /24h | Relais PO si parasitémie ≤1%. Surveillance PADH 4 sem (Hb/LDH/hapto) |

Every mention of hospitalisation/sévère → "référer" as mint-colored link to traveldoctor.ch/professionnels.

**Piège callout:**
> Patient >65 kg traité par Riamet : 1 sur 10 récidive à J20-J28. Planifiez un frottis de contrôle à J28 (Sondén CID 2017, n=95).

**Step 3: Add Dengue/Arboviroses block**

Content from research section 2:

**Quand y penser:**
- Fièvre + thrombopénie + TDR malaria négatif, incubation 3-10j
- Record 2024: >14.6 millions de cas, 304 cas autochtones en Europe
- DDx critique avec paludisme: les deux causent fièvre + thrombopénie

**Diagnostic:**
- NS1 (J0-4) + IgM/IgG
- Differential table: Paludisme vs Dengue vs Chikungunya (from research)

**Traitement:**
- PAS d'AINS (recommandation forte OMS 2025)
- Réhydratation orale protocolisée
- Cristalloïdes IV si signes d'alarme
- Signes d'alarme WHO 2025 (list from research)

**Piège callout:**
> La phase critique survient à la DÉFERVESCENCE (J3-7), pas pendant la fièvre. Si l'hématocrite monte pendant que les plaquettes baissent → dengue sévère — [référer](traveldoctor.ch/professionnels) immédiatement.

Include Chikungunya and Zika specificities as brief sub-blocks.

**Step 4: Verify**

Open in browser. Expected: two pathogen blocks with consistent formatting, treatment tables, callout boxes.

**Step 5: Commit**

```bash
git add pages/syndromes/fievre-voyageur.html
git commit -m "feat: add paludisme and dengue pathogen blocks with clinical content"
```

---

## Task 4: Build pathogen blocks — Rickettsioses, Typhoïde, FHV, Katayama

**Files:**
- Modify: `pages/syndromes/fievre-voyageur.html`

**Content source:** `research-fever-syndromes.md` sections 3 (Rickettsioses), 4 (Typhoïde), 5 (FHV), and Katayama from `research-eosinophilia-travelers.md` section 3.

**Step 1: Add Rickettsioses block**

Content from research section 4:
- Quand y penser: fièvre + escarre(s) + retour Afrique australe, incubation 5-10j
- Diagnostic: clinique d'abord (triade), PCR écouvillon escarre Se >90%, sérologie tardive J10-14
- Traitement: **doxycycline 100 mg 2×/j × 7j — IMMÉDIATEMENT**, réponse 48h
- Differential des escarres (table from research: R. africae vs R. conorii vs R. rickettsii vs Orientia)
- Piège: bêta-lactamines INEFFICACES (résistance intrinsèque). MG prescrit amoxicilline → pas d'amélioration
- Link: `→ Fiche détaillée` → `../bacteria/rickettsiosis.html`

**Step 2: Add Fièvre typhoïde block**

Content from research section 3:
- Quand y penser: fièvre prolongée + retour Asie du Sud (Inde, Pakistan), VFR
- Diagnostic: hémocultures AVANT ATB (Se ~60%), TDR malaria faussement positif possible
- Traitement table:

| Situation | 1re ligne | Alternative | Durée |
|-----------|-----------|-------------|-------|
| Sensible | Ciprofloxacine 500 mg 2×/j PO | Ceftriaxone 2g/j IV ou azithromycine | 7-14j |
| Suspicion XDR | **Azithromycine** 1g J1 puis 500 mg/j | Méropénème 1g 3×/j IV | 7-14j |

- Piège: défervescence lente 5-7j même avec ATB efficace → ne pas changer trop vite. XDR au Pakistan (50% en 2019). TDR malaria faux positif.
- Link: → `../bacteria/enteric_fever.html`

**Step 3: Add FHV block**

Content from research section 5:
- Quand y penser: fièvre + retour <21j zone épidémique + contact sang/animaux
- Protocole IDENTIFIER — ISOLER — INFORMER
- Numéro OFSP: 058 463 87 37
- PAS de prélèvement avant avis spécialisé → [référer] immédiatement
- Piège: symptômes initiaux non spécifiques. Seuls les signes hémorragiques tardifs sont évidents — trop tard.
- Pas de fiche détaillée existante → pas de lien "Fiche détaillée"

**Step 4: Add Katayama block**

Content from `research-eosinophilia-travelers.md` section 3.2:
- Quand y penser: fièvre + éosinophilie + baignade eau douce Afrique, 4-8 sem post-expo
- Diagnostic: sérologie (négative les 6-8 premières semaines !), clinique. 53% infections au Lac Malawi (Logan 2013)
- Traitement: praziquantel 40 mg/kg (inefficace formes immatures → attendre 6-8 sem post-expo)
- **JAMAIS de corticoïdes sans exclure Strongyloides** (mortalité hyperinfection 60-85%) → [référer]
- Piège: sérologie négative au début (14% Logan 2013) ; corticoïdes donnés sans dépistage Strongyloides
- Link: → `../parasites/schistosomiasis.html`

**Step 5: Verify**

Open in browser. Expected: 6 pathogen blocks total, consistent formatting, all with callout boxes.

**Step 6: Commit**

```bash
git add pages/syndromes/fievre-voyageur.html
git commit -m "feat: add rickettsioses, typhoid, VHF and Katayama pathogen blocks"
```

---

## Task 5: Add Points clés + Références + TOC

**Files:**
- Modify: `pages/syndromes/fievre-voyageur.html`

**Step 1: Add Points clés section**

```html
<section id="points-cles" class="bg-teal-50 border border-teal-200/50 rounded-2xl p-8 mb-12">
  <h2 class="font-serif text-2xl text-teal-900 mb-6">Points clés</h2>
  <ul class="space-y-3">
    <li>Toute fièvre au retour de voyage = poser la question du voyage + TDR malaria sans délai</li>
    <li>Riamet® chez patient >65 kg = contrôle frottis J28 (échec tardif 1/10)</li>
    <li>Escarre + Afrique = doxycycline IMMÉDIATEMENT, pas d'amoxicilline, pas d'attente de sérologie</li>
    <li>Phase critique dengue = à la défervescence (J3-7), pas pendant la fièvre — surveiller Ht + plaquettes</li>
    <li>JAMAIS de corticoïdes sans exclure <i>Strongyloides</i> (mortalité hyperinfection 60-85%) — <a href="https://traveldoctor.ch/professionnels">référer</a></li>
  </ul>
</section>
```

Each bullet mentioning referral → mint-colored "référer" link.

**Step 2: Add Références section**

Table grouped by pathogen, from research "BIBLIOGRAPHIE COMPLETE" section.
22 references with authors, journal, year, key data point.
DOIs as clickable links where available.

```html
<section id="references" class="mb-12">
  <h2 class="font-serif text-2xl text-teal-900 mb-6">Références</h2>
  <div class="overflow-x-auto">
    <table class="text-sm">
      <thead><tr><th>Thème</th><th>Référence</th><th>Données clés</th></tr></thead>
      <tbody>
        <!-- 22 rows from research bibliography -->
      </tbody>
    </table>
  </div>
</section>
```

**Step 3: Populate the floating TOC**

List all section IDs with display names:
```html
<aside class="toc-sidebar hidden lg:block">
  <nav class="toc">
    <h4 class="text-xs font-semibold uppercase tracking-wider text-teal-500/60 mb-4">Sommaire</h4>
    <ul class="space-y-2 text-sm border-l-2 border-teal-100">
      <li><a href="#consultation-rapide" class="block pl-4 py-1 border-l-2 -ml-[2px] border-transparent hover:border-mint-400 text-teal-600 hover:text-mint-600 transition-colors">Consultation rapide</a></li>
      <li><a href="#paludisme" class="...">Paludisme</a></li>
      <li><a href="#dengue" class="...">Dengue / Arboviroses</a></li>
      <li><a href="#rickettsioses" class="...">Rickettsioses</a></li>
      <li><a href="#typhoide" class="...">Fièvre typhoïde</a></li>
      <li><a href="#fhv" class="...">Fièvres hémorragiques</a></li>
      <li><a href="#katayama" class="...">Katayama</a></li>
      <li><a href="#points-cles" class="...">Points clés</a></li>
      <li><a href="#references" class="...">Références</a></li>
    </ul>
  </nav>
</aside>
```

**Step 4: Add TOC scroll spy JavaScript**

```javascript
// Scroll spy for TOC
const tocLinks = document.querySelectorAll('.toc a');
const sections = document.querySelectorAll('section[id], div[id]');

const observerToc = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      tocLinks.forEach(link => {
        link.classList.remove('active', 'text-mint-600', 'border-mint-400');
        link.classList.add('border-transparent', 'text-teal-600');
      });
      const activeLink = document.querySelector(`.toc a[href="#${entry.target.id}"]`);
      if (activeLink) {
        activeLink.classList.add('active', 'text-mint-600', 'border-mint-400');
        activeLink.classList.remove('border-transparent', 'text-teal-600');
      }
    }
  });
}, { threshold: 0.2, rootMargin: '-80px 0px -60% 0px' });

sections.forEach(section => observerToc.observe(section));
```

**Step 5: Verify**

Open in browser. Expected: complete page with all sections, working TOC with scroll highlight, responsive layout (TOC hidden on mobile, tables scroll horizontally).

**Step 6: Commit**

```bash
git add pages/syndromes/fievre-voyageur.html
git commit -m "feat: add points clés, references, and floating TOC with scroll spy"
```

---

## Task 6: Polish — table styling, callout boxes, referral links, responsive

**Files:**
- Modify: `pages/syndromes/fievre-voyageur.html`

**Step 1: Style all tables consistently**

Tailwind classes for all article tables:
```
table: w-full text-sm text-left
thead: bg-teal-50 text-teal-700 uppercase text-xs tracking-wider
th: px-4 py-3 font-semibold
td: px-4 py-3 border-b border-teal-100
tr:hover: bg-cream-50
```

Wrap tables in `<div class="overflow-x-auto rounded-xl border border-teal-100">` for mobile scroll.

**Step 2: Style callout boxes**

Piège callout:
```html
<div class="border-l-4 border-gold-500 bg-gold-50 rounded-r-lg p-4 my-6">
  <div class="flex items-start gap-2">
    <span class="text-gold-600 font-bold text-sm">⚠ Piège</span>
  </div>
  <p class="text-sm text-teal-800 mt-1">...</p>
</div>
```

**Step 3: Style "référer" links**

All occurrences of "référer" in running text:
```html
<a href="https://traveldoctor.ch/professionnels" target="_blank"
   class="text-mint-600 hover:text-mint-500 font-medium border-b border-mint-300/50 hover:border-mint-400 transition-colors">
  référer
</a>
```

CTA-style at severity criteria / points clés:
```html
<a href="https://traveldoctor.ch/professionnels" target="_blank"
   class="inline-flex items-center gap-1.5 text-sm text-mint-600 hover:text-mint-500 font-semibold mt-2">
  Référer un patient →
</a>
```

**Step 4: Responsive final checks**

- Tables: horizontal scroll on mobile (already wrapped in overflow-x-auto)
- TOC: hidden on mobile (lg:block)
- Callout boxes: full width on mobile
- Navbar: mobile menu works (inherited from prototype)
- Font sizes: body text readable on mobile (base text-sm → text-base on mobile)

**Step 5: Add meta tags for SEO**

```html
<meta name="description" content="Fièvre au retour de voyage : algorithme de triage, bilan initial, paludisme, dengue, rickettsioses, typhoïde — guide pour le médecin de premier recours.">
<meta name="keywords" content="fièvre voyageur, paludisme, dengue, rickettsiose, médecine tropicale, Suisse">
```

**Step 6: Verify full page**

Open in browser at desktop and mobile width. Check:
- [ ] Navbar links work
- [ ] Breadcrumb links work
- [ ] TOC scroll spy highlights correct section
- [ ] All tables are readable and scroll on mobile
- [ ] Callout boxes are visually distinct
- [ ] "Référer" links all point to traveldoctor.ch/professionnels
- [ ] "Fiche détaillée" links point to correct pathogen pages
- [ ] Footer renders correctly
- [ ] No broken images or missing fonts

**Step 7: Commit**

```bash
git add pages/syndromes/fievre-voyageur.html
git commit -m "feat: polish table styling, callouts, referral links, and responsive layout"
```

---

## Task 7: Link from homepage

**Files:**
- Modify: `prototype.html`

**Step 1: Update syndrome card link**

In the "Par syndrome" section of prototype.html, find the "Fièvre au retour" card and update its link:

```html
<a href="pages/syndromes/fievre-voyageur.html" class="...">
```

Remove the "en construction" badge if present.

**Step 2: Verify**

Click the card on the homepage → navigates to the new syndrome page.

**Step 3: Commit**

```bash
git add prototype.html
git commit -m "feat: link fièvre au retour card to new syndrome page"
```

---

## Notes

- **SVG triage diagram**: placeholder for now. To be created in draw.io and exported as SVG. File: `dist/images/syndromes/triage-fievre.svg`. Will replace the dashed placeholder in section 1.1.
- **Build script**: deferred to after first page is validated. Once we're happy with the HTML structure, we can write `scripts/build-syndrome.js` to generate pages from research MD files.
- **Other 3 syndrome pages**: will reuse the same template structure. Task for a separate plan.
- **Existing pathogen pages** (malaria.html, etc.) are still old Bootstrap template. Migration to new template is a separate backlog item. Cross-links will work regardless.
