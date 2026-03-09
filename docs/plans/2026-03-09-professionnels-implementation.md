# /professionnels Landing Page — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a standalone HTML landing page for traveldoctor.ch/professionnels and revert TropicalNotes referral links to point to it.

**Architecture:** Single HTML file with inline styles (no external CSS), ready to paste into a Divi Code module. Responsive two-column layout using CSS grid. Separate task to revert `tel:` links in TropicalNotes.

**Tech Stack:** HTML, inline CSS, no JS framework. Matches traveldoctor.ch palette.

---

### Task 1: Create the landing page HTML

**Files:**
- Create: `professionnels.html` (at repo root, for easy copy-paste into Divi)

**Step 1: Write the complete HTML file**

The page body content (no `<html>`, `<head>`, or `<body>` tags — Divi provides those) with three sections:

```html
<!--
  traveldoctor.ch/professionnels — Page content for Divi Code module
  Paste this into: WordPress > Pages > Professionnels > Divi Builder > Code Module

  IMPORTANT: Replace +41 XX XXX XX XX with actual referral line number
-->

<div style="max-width: 800px; margin: 0 auto; padding: 40px 20px; font-family: 'Open Sans', Arial, sans-serif; color: #333;">

  <!-- SECTION 1: Hero -->
  <div style="text-align: center; margin-bottom: 48px;">
    <h1 style="font-size: 28px; font-weight: 700; color: #2d5e5b; margin-bottom: 12px;">
      Avis spécialisé en infectiologie tropicale
    </h1>
    <p style="font-size: 15px; color: #479793; margin-bottom: 16px;">
      Dr Ludovico Cobuccio — Spéc. FMH infectiologie · DTM&amp;H Glasgow · Médecine des voyages ISTM
    </p>
    <p style="font-size: 14px; color: #666;">
      Conseil téléphonique pour les cas urgents. Formulaire pour les demandes non urgentes.
    </p>
  </div>

  <!-- SECTION 2: Two columns -->
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; margin-bottom: 48px;">

    <!-- Left: Phone -->
    <div style="background: #f0faf9; border: 1px solid #b2dfdb; border-radius: 12px; padding: 32px; text-align: center;">
      <div style="font-size: 36px; margin-bottom: 12px;">&#9742;</div>
      <p style="font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; color: #479793; margin-bottom: 8px;">
        Urgent — Appel direct
      </p>
      <!-- TODO: Replace with actual referral line number -->
      <a href="tel:+41XXXXXXXXX" style="font-size: 24px; font-weight: 700; color: #2d5e5b; text-decoration: none;">
        +41 XX XXX XX XX
      </a>
      <p style="font-size: 13px; color: #888; margin-top: 12px;">
        Lun–Ven 08h30–18h00
      </p>
    </div>

    <!-- Right: Form -->
    <div style="background: #fff; border: 1px solid #e0e0e0; border-radius: 12px; padding: 32px;">
      <p style="font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; color: #479793; margin-bottom: 16px;">
        Non urgent — Formulaire
      </p>
      <form action="mailto:ludovico.cobuccio@traveldoctor.ch" method="POST" enctype="text/plain">
        <div style="margin-bottom: 12px;">
          <input type="text" name="Nom" placeholder="Votre nom" required
            style="width: 100%; padding: 10px 12px; border: 1px solid #ccc; border-radius: 8px; font-size: 14px; box-sizing: border-box;" />
        </div>
        <div style="margin-bottom: 12px;">
          <input type="email" name="Email" placeholder="Votre email" required
            style="width: 100%; padding: 10px 12px; border: 1px solid #ccc; border-radius: 8px; font-size: 14px; box-sizing: border-box;" />
        </div>
        <div style="margin-bottom: 16px;">
          <textarea name="Message" placeholder="Votre message" rows="4" required
            style="width: 100%; padding: 10px 12px; border: 1px solid #ccc; border-radius: 8px; font-size: 14px; resize: vertical; box-sizing: border-box;"></textarea>
        </div>
        <button type="submit"
          style="width: 100%; padding: 12px; background: #12AD98; color: #fff; font-size: 14px; font-weight: 600; border: none; border-radius: 8px; cursor: pointer;">
          Envoyer
        </button>
      </form>
      <p style="font-size: 12px; color: #888; margin-top: 12px; text-align: center;">
        Réponse sous 48h ouvrables
      </p>
    </div>
  </div>

  <!-- Responsive: stack on mobile -->
  <style>
    @media (max-width: 640px) {
      div[style*="grid-template-columns: 1fr 1fr"] {
        grid-template-columns: 1fr !important;
      }
    }
  </style>

  <!-- SECTION 3: Newsletter -->
  <div style="text-align: center; padding: 24px; background: #fdfaf3; border-radius: 12px; border: 1px solid #f0e6c8;">
    <p style="font-size: 14px; color: #666; margin-bottom: 12px;">
      Restez informé — actualités en médecine tropicale et des voyages
    </p>
    <a href="https://traveldoctor.ch/newsletter"
      style="display: inline-block; padding: 10px 24px; background: #d4a01c; color: #fff; font-size: 14px; font-weight: 600; border-radius: 8px; text-decoration: none;">
      S'inscrire à la newsletter
    </a>
  </div>

</div>
```

**Step 2: Verify the file renders correctly**

Open `professionnels.html` in a browser and check:
- Hero text centered, credentials visible
- Two columns side by side on desktop, stacked on mobile (<640px)
- Phone number placeholder clearly marked
- Form fields functional (mailto opens email client)
- Newsletter button links to /newsletter
- Colors match traveldoctor.ch palette (teal #479793, mint #12AD98, gold #d4a01c)

**Step 3: Commit**

```bash
git add professionnels.html
git commit -m "Add /professionnels landing page HTML for Divi Code module"
```

---

### Task 2: Revert tel: links in fievre-voyageur.html

**Files:**
- Modify: `pages/syndromes/fievre-voyageur.html`

**Context:** The previous commit (`e6da40f`) replaced `https://traveldoctor.ch/professionnels` with `tel:+41779908914` in this file. Now that the /professionnels page exists, revert these to the URL. There are ~10 occurrences.

**Step 1: Replace all tel: links with URL links**

Two patterns to fix:

Pattern A — navbar/mobile menu links (keep gold styling, change href + text):
```
href="tel:+41779908914" → href="https://traveldoctor.ch/professionnels" target="_blank"
"&#9742; Referer un patient" → "Referer un patient"
```

Pattern B — inline ref-links in article body:
```
href="tel:+41779908914" class="ref-link">&#9742; Referer → href="https://traveldoctor.ch/professionnels" target="_blank" class="ref-link">Referer
```

Note: Remove the &#9742; (phone icon) from link text since it's no longer a phone link.

**Step 2: Verify no tel: links remain**

Run: `grep -n "tel:+41" pages/syndromes/fievre-voyageur.html`
Expected: no output

Run: `grep -c "traveldoctor.ch/professionnels" pages/syndromes/fievre-voyageur.html`
Expected: count matches the number of referral links (~10+)

**Step 3: Commit**

```bash
git add pages/syndromes/fievre-voyageur.html
git commit -m "Revert tel: links to traveldoctor.ch/professionnels in fievre-voyageur"
```

---

### Task 3: Final verification and push

**Step 1: Full grep for any remaining tel: links across the site**

Run: `grep -rn "tel:+41" pages/`
Expected: no output (all pages should use traveldoctor.ch/professionnels URLs)

**Step 2: Verify all professionnels links are consistent**

Run: `grep -c "traveldoctor.ch/professionnels" pages/**/*.html`
Expected: every article page has at least 2 hits (navbar + CTA)

**Step 3: Push**

```bash
git push
```
