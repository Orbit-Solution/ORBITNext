# OrbitERPNext Branding & Dark Theme

Official branding companion app for OrbitERPNext, tailored to match the visual design system and typography of Orbit Solution ([https://www.orbitsolution.site/](https://www.orbitsolution.site/)).

## Brand Design Specification

### 1. Brand Identity

- **Application Title**: OrbitERPNext (or ORBITNext)
- **Publisher**: Orbit Solution ([info@orbitsolution.site](mailto:info@orbitsolution.site))
- **Brand Lockup**: Orbit Brandmark + Orbit ERPNext Wordmark

### 2. Typography

- **Headings & Titles (`font-heading`)**:
  - `Poppins, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`
  - Font weights: 600 (Semibold), 700 (Bold), 800 (Extrabold)
  - Applied to: Header titles, modal titles, page headers, navbar brand, stat numbers, card titles
- **Body & UI Controls (`font-sans`)**:
  - `Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`
  - Font weights: 400 (Regular), 500 (Medium), 600 (Semibold)
  - Applied to: Desk forms, tables, buttons, inputs, dropdowns, navigation items, tooltips

### 3. Theme Colors & Tokens

- **Backgrounds**:
  - Deep Space Canvas: `#05070f`
  - Elevation / Surfaces (Cards, Modals, Popovers, Dock): `#0d1017`
  - Hover / Active Surfaces: `#10141e`
  - Secondary Elevation: `#181c27`
- **Borders & Outlines**:
  - Subtle Border: `rgba(255, 255, 255, 0.08)`
  - Elevated Border: `rgba(255, 255, 255, 0.16)`
  - Focus Ring: `rgba(25, 85, 253, 0.5)`
- **Accent & Brand Colors**:
  - Primary Accent Blue: `#1955fd` (Hover: `#0052cc`, Active: `#003d99`)
  - Cyan Accent: `#00c3ff` / `#32d7fe`
  - Warm Highlight: `#fc9c4b`
  - Accent Gradient: `linear-gradient(135deg, #fc9c4b 0%, #32d7fe 50%, #1955fd 100%)`
  - Selection: `background: rgba(25, 85, 253, 0.25); color: #ffffff;`
- **Text & Ink**:
  - Heading White: `#ffffff`
  - Body Text: `#c4c4c4`
  - Muted Zinc: `#a1a1aa`
  - Subtle / Placeholder: `#71717a`

### 4. Assets & Icons

- `orbiterpnext-logo.svg`: Responsive vector logo lockup (Orbit icon + Orbit ERPNext text in Poppins)
- `orbiterpnext-logo.png`: 500x500 high-resolution brandmark
- `orbiterpnext-icon.png`: 36x36 / 64x64 rounded icon for navbar and app switcher
- `orbiterpnext-favicon.png`: 32x32 / 64x64 favicon
- `orbiterpnext-favicon.svg`: Vector favicon for crisp high-DPI browser tabs

### 5. Deployment Scope

- **Target Frappe Framework**: v16 (16.56.0+)
- **Target ERPNext**: v16 (16.55.0+)
- **Target Site**: `frontend` (`http://localhost:8080`)
- **Theme Scope**:
  - Desk Application: Global dark theme with Orbit Solution styling
  - Public Website & Login: Orbit Solution dark theme with branded login screen and favicon
