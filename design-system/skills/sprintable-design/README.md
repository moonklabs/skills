# Sprintable Design System

A dark-mode-native, precision-engineered interface system for Sprintable. Inspired
by Linear's approach to darkness-as-medium, adapted for Sprintable's blue brand mark.

---

## Product context

Sprintable is a software product. The brand identity currently consists of:

- **Wordmark**: `sprintable` lowercase, set in a geometric, heavy sans with a diamond-tile mark to the left.
- **Mark**: a clustered diamond built from layered blue facets (dark `#0059a5`, mid `#3385f8`, light `#71aefe`), resembling a printing plate or pixel mosaic.
- **Tone**: technical, calm, precise — engineering-minded without being cold.

### Sources we were given

- `uploads/sprintable-logo-full.png` — primary horizontal logo lockup (copied to `assets/sprintable-logo-full.png`)
- `uploads/sprintable-logo-square.png` — square/app-icon mark (copied to `assets/sprintable-logo-square.png`)
- A written design brief (reproduced in this repo's history) describing a Linear-inspired
  dark system with Sprintable's blue as the chromatic accent.

No codebase, Figma, or product screenshots were provided. UI kits in this system are
**reference recreations** of the patterns described in the brief, using Sprintable's
blue in place of Linear's indigo — they are **not copies of any existing Sprintable
product screens**, because none were supplied.

---

## Content fundamentals

### Voice

Sprintable's voice is **technically fluent, quiet, and direct**. It does not
perform. It assumes you are smart and busy. The tone descends directly from the
engineering-tool lineage (Linear, Raycast, Arc) — utility framed as craft.

- **Person**: speaks to "you" (2nd person). First-person is "we" and used sparingly.
- **Register**: lowercase in the wordmark, sentence case in UI. Title Case in marketing H1s.
- **Length**: short. A headline is one clause. A button is one or two words.
- **Claims**: concrete, not aspirational. Verbs over adjectives.
- **Humor**: dry, observational, never meme-y or winking.
- **No emoji** in product UI. Emoji may appear in user-generated content only.

### Examples

**Good:**
- "Ship a sprint in an afternoon."
- "Plan, estimate, and ship — in one place."
- "Get started" / "Start a sprint" / "Open workspace"
- "Drafted 3 minutes ago by Aria"

**Avoid:**
- "Revolutionize your sprint velocity! 🚀"
- "We'll help you unlock incredible team potential."
- "Click here to begin your amazing journey ✨"

### Casing

- Sentence case in all UI and most headlines.
- The wordmark `sprintable` is always lowercase.
- Technical labels (env vars, code, CLI) use the exact casing of the thing they reference.
- Keyboard shortcuts in monospace with `⌘`, `⇧`, `⌥`, `⌃`, `↵`, `⎋` glyphs.

### Punctuation

- Em dash `—` for parenthetical beats.
- Sentence-final periods omitted in UI labels, buttons, chips, tooltips.
- Oxford comma.
- Code spans set in `Berkeley Mono` (fallback `JetBrains Mono`).

---

## Visual foundations

### Atmosphere

Sprintable is **dark-mode-native**, not dark-themed. The canvas is `#08090a` — a
near-black with a cool undertone. Content emerges from darkness through ultra-subtle
opacity steps, not through added color. Elevation is communicated by luminance
(slightly whiter surface) and by whisper-thin translucent white borders — almost
never by drop shadows, which are invisible on dark surfaces.

### Color

- **Grayscale dominates.** The entire chrome is achromatic.
- **One chromatic accent**, Sprintable blue (`#3385f8` primary, `#71aefe` light, `#0059a5` deep), reserved for primary CTAs, active states, links, and the brand mark. Never decorative.
- **Status green** (`#27a644`) for active/success indicators — status only, never decorative.
- **Text never pure white** — always `#f7f8f8` to prevent eye strain.

See `colors_and_type.css` for the full token set.

### Type

- **Inter Variable** (primary) with OpenType features `"cv01", "ss03"` applied globally. These are not optional — without them, it is generic Inter, not Sprintable's Inter.
- **Signature weight 510** (between regular and medium) as the default emphasis. Three-tier system: 400 / 510 / 590.
- **Aggressive negative letter-spacing at display sizes**: -1.584px at 72px, -1.056px at 48px, -0.704px at 32px. Relaxes to normal below 16px.
- **Berkeley Mono** for code (substituted with `JetBrains Mono` from Google Fonts — see "Font substitutions" below).

### Backgrounds

- **Flat, near-black canvas.** No gradients, no textures, no illustrations.
- **Full-bleed dark sections** with internal max-widths (~1200px) for containment.
- **No patterns, no noise, no grain.**
- Product screenshots sit on the same dark canvas, bordered with `rgba(255,255,255,0.08)`.

### Animation

- **Fast, short, functional.** Motion serves hierarchy — it does not decorate.
- Durations: 120ms (micro-state), 180ms (transition), 240ms (enter/exit). Never over 300ms for UI.
- **Easing**: `cubic-bezier(0.2, 0, 0, 1)` (standard ease-out) for most; `cubic-bezier(0.4, 0, 0.6, 1)` for emphasis.
- **No bounce**, no elastic, no spring overshoot. Never playful.
- Fades and subtle translate (4–8px) dominate; avoid scale beyond `0.97–1.03`.

### Hover states

- **Opacity step on background**: transparent buttons raise from `rgba(255,255,255,0.02)` to `rgba(255,255,255,0.05)`.
- **Text brightens**: `#d0d6e0` → `#f7f8f8` on hover for nav links.
- **Brand buttons shift**: `#3385f8` → `#5a9dff` on hover.
- **Cursor**: `pointer` only on actual clickable elements.

### Press states

- **Subtle scale down** (`scale(0.985)`) for primary buttons, 80ms.
- **Darker wash** on translucent surfaces (background opacity drops a half-step).
- No ripple effects.

### Borders

- **Always semi-transparent white** on dark surfaces — `rgba(255,255,255,0.05)` to `rgba(255,255,255,0.08)`. Never solid dark borders.
- **1px only.** No 2px or thicker borders anywhere.
- Solid borders (`#23252a`, `#34343a`) appear only on top of translucent surfaces when extra definition is needed.

### Shadows

See the elevation table in the brief. The short version:
- **Inner shadows** (`inset 0 0 12px rgba(0,0,0,0.2)`) create a "sunken" feel for recessed panels.
- **Ring shadows** (`0 0 0 1px rgba(0,0,0,0.2)`) act as borders-from-shadow.
- **Layered soft drops** for dialogs and popovers (5-stack).
- **Focus ring**: `0 0 0 3px rgba(51,133,248,0.35)`.

### Transparency & blur

Used **sparingly**. The primary uses:
- **Modal backdrop**: `rgba(0,0,0,0.85)` — no blur, just darkening.
- **Sticky header**: `backdrop-filter: blur(12px)` over `rgba(15,16,17,0.72)` when scrolled.
- **Never** on cards or inline surfaces — translucency there is achieved with white-alpha, not blur.

### Corner radii

- Micro (2px) — inline badges, subtle tags
- Comfortable (6px) — default for buttons, inputs
- Card (8px) — cards, dropdowns
- Panel (12px) — featured panels, command palettes
- Large (22px) — hero panels only
- Pill (9999px) — chips, filter pills, status tags
- Circle (50%) — avatars, status dots, icon buttons

### Cards

- Background: `rgba(255,255,255,0.02)` to `rgba(255,255,255,0.05)` (translucent, never solid).
- Border: `1px solid rgba(255,255,255,0.08)`.
- Radius: 8px default, 12px for featured.
- Shadow: none by default; ring shadow `0 0 0 1px rgba(0,0,0,0.2)` for extra definition.
- Hover: background opacity increases by ~0.02.

### Layout rules

- Max content width: **1200px**.
- Grid baseline: **8px**, with optical micro-adjustments at 7px and 11px for specific alignments.
- Vertical section rhythm: 80px+ desktop, 48px mobile.
- Fixed elements: only the sticky header and floating command palette trigger. No fixed side nav in marketing; product UI uses a static left sidebar on `#0f1011`.

### Imagery

- **Product screenshots**, not photography. Captured on the dark canvas.
- Any photography should be **cool, engineered, architectural** — Apple-product-launch quality. B&W or desaturated cool tones.
- **No stock photography of people looking at laptops.**

---

## Iconography

Sprintable's system leans on **stroke-based SVG icons** with a consistent 1.5px
stroke at 16px viewport, matching the Linear aesthetic this system is modeled on.

**The primary icon set is [Lucide](https://lucide.dev/)** (the community
successor to Feather), loaded from CDN. Stroke-weight and geometric character match
the dark, engineered feel of the system.

```html
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
```

Per-icon usage:

```html
<i data-lucide="search" style="width:16px;height:16px;stroke-width:1.5"></i>
<script>lucide.createIcons();</script>
```

**Substitution note**: Sprintable presumably has its own icon set in production.
None was provided to us. Lucide is used as the closest structural match to the
Linear-family aesthetic described in the brief. **Please flag or provide your
production icon font/sprite so we can replace Lucide with the real set.**

### Icon rules

- Default stroke: **1.5px** at 16px.
- Default color: `#8a8f98` (tertiary), brightening to `#f7f8f8` on hover/active.
- Never use filled icons mixed with stroke icons in the same surface.
- Status dots use solid color circles, not icons.
- **Emoji are not part of the UI vocabulary.** They may appear only in
  user-generated content (comments, names).
- **Unicode symbols** are acceptable for keyboard-shortcut notation (`⌘ ⇧ ⌥ ⌃ ↵ ⎋`)
  and arrows (`→`) in marketing copy.

### Logos

- `assets/sprintable-logo-full.png` — horizontal wordmark + mark (872×186). Use on light surfaces only (the wordmark portion is black).
- `assets/sprintable-logo-square.png` — mark only (176×179). Safe on any background.

For dark surfaces, use the mark alone with a white wordmark set in Inter Variable 590, letter-spacing -0.5px, sized proportional to the mark. See `ui_kits/web/Header.jsx` for the canonical treatment.

---

## Font substitutions

Source of truth in the brief calls for:

| Design intent | Substituted with | Why |
| --- | --- | --- |
| **Inter Variable** | Inter Variable (rsms.me/inter/inter.css) | Available, free, actual match |
| **Berkeley Mono** | **JetBrains Mono** (Google Fonts) | Berkeley Mono is a paid license and not redistributable; JetBrains Mono is the closest free technical monospace |

**Please provide the production Berkeley Mono WOFF2 files** if you want us to use
the real thing. Drop them in `fonts/` and update the `@font-face` in
`colors_and_type.css`.

---

## Index — what's in this folder

```
README.md                     — this file
SKILL.md                      — Agent Skills manifest (cross-compatible)
colors_and_type.css           — all color + type + spacing + shadow tokens
assets/
  sprintable-logo-full.png
  sprintable-logo-square.png
preview/                      — Design System cards (registered for review)
  type-*.html                 — typography specimens
  color-*.html                — color palettes
  spacing-*.html              — radii, shadows, spacing
  components-*.html           — buttons, inputs, cards, badges, menus
  brand-*.html                — logos, marks
ui_kits/
  web/                        — Sprintable marketing site kit
    index.html, *.jsx, README.md
  app/                        — Sprintable product UI kit (workspace)
    index.html, *.jsx, README.md
```

---

## Open questions & things we need from you

1. **Production icon set** — Lucide is a substitution. Share your real one.
2. **Berkeley Mono licensing** — want to ship with the real mono? Drop WOFF2s in `fonts/`.
3. **Real product screenshots / screens** — the UI kits are pattern references, not recreations of actual Sprintable surfaces. Share the real product (code, Figma, or screenshots) so we can make the kits pixel-faithful.
4. **Secondary brand colors** — is the palette truly the blue triad plus grayscale, or are there extended chromatic tokens for data viz, statuses, etc?
5. **Voice guide** — the tone section is inferred. Confirm or replace with your real copywriting guidelines.
