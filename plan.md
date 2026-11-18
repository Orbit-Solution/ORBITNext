# Implementation Plan: OrbitERPNext Rebrand and Dark Theme

**Date**: 2026-11-18 | **Spec**: User request to rebrand the current Frappe Docker deployment as OrbitERPNext

## Summary

Create a version-controlled branding layer for the existing Frappe/ERPNext Docker deployment. The solution will use a small custom Frappe app for OrbitERPNext naming, logo/favicon assets, and global dark-theme styling; the app will be included in the custom image through the existing `apps.json` and custom image build workflow. Site data will remain in the persistent `sites` volume. Basic site settings can be applied without rebuilding, while the permanent branded experience will be delivered through an immutable custom image.

## Technical Context

**Language/Version**: Frappe/ERPNext v16, Python and JavaScript/CSS assets, Docker Compose
**Primary Dependencies**: Frappe custom app, ERPNext, Docker BuildKit/Buildx, existing custom image Containerfile
**Storage**: Existing persistent `sites` volume; branding source and compiled assets belong in the image
**Testing**: Existing Compose validation plus browser/manual smoke checks against a disposable ERPNext site
**Target Platform**: Existing Docker Compose deployment using `compose.yaml` and the selected database/Redis overrides
**Performance Goals**: No additional runtime service; branding assets must be served by the existing frontend and remain cacheable
**Constraints**: Do not edit files inside running production containers; preserve site data; use the existing image lifecycle; do not replace ERPNext core files directly

## Constitution Check

- **Persistent data protection**: PASS — only the application image and site configuration are changed; the `sites` volume is retained.
- **Immutable production assets**: PASS — assets are built into a custom image and deployed by container recreation.
- **Configuration through existing deployment mechanisms**: PASS — the app is included through `apps.json`, and deployment continues to use the existing Compose workflow.
- **Backward compatibility**: PASS — the default Frappe/ERPNext image remains usable when the custom image variables are not selected.
- **Explicit validation**: PASS — build, Compose configuration, site migration, branding, theme, and asset-serving checks are included.

## Applied Guidelines

- Follow the repository's custom-app guidance in [docs/09-concepts/01-custom-app.md](docs/09-concepts/01-custom-app.md).
- Follow the image and asset lifecycle documented in [docs/13-explanation/03-asset-handling.md](docs/13-explanation/03-asset-handling.md).
- Follow the custom image and BuildKit secret workflow in [docs/02-setup/02-build-setup.md](docs/02-setup/02-build-setup.md).
- Keep branding changes in a custom app rather than modifying Frappe or ERPNext core assets.

## Implementation Steps

### Step 1: [Cross-cutting] Confirm branding inputs and deployment target
- **Requirements**: REQ-001, REQ-002, REQ-003
- **Design inputs**: Existing Frappe Docker image and persistent-site model
- **Description**: Confirm the OrbitERPNext display name, approved logo and favicon files, logo dimensions/formats, brand colors, dark-theme contrast requirements, target Frappe/ERPNext version, site hostname, and whether the dark theme applies to the desk, public website, or both. Default plan assumption: global desk dark theme plus a matching dark public Website Theme.

### Step 2: [Cross-cutting] Create the OrbitERPNext branding app
- **Requirements**: REQ-001, REQ-002, REQ-003
- **Design inputs**: Frappe custom app structure and current asset handling
- **Description**: Create a companion custom Frappe app named `orbiterpnext_branding` with app metadata, public logo/favicon assets, CSS variables, dark-theme styles, and hooks or fixtures for applying branding settings. Use supported Frappe extension points and avoid replacing core files. Include accessible color contrast, responsive logo variants, and a fallback when an asset is unavailable.

### Step 3: [Cross-cutting] Integrate the app into the custom image build
- **Requirements**: REQ-001, REQ-002, REQ-003, REQ-004
- **Design inputs**: [docs/02-setup/02-build-setup.md](docs/02-setup/02-build-setup.md), [images/custom/Containerfile](images/custom/Containerfile), [images/layered/Containerfile](images/layered/Containerfile)
- **Description**: Add the branding app repository and branch to the deployment `apps.json`, build a tagged custom image, verify assets are compiled, and ensure the image uses the existing startup entrypoint and immutable asset layout. Keep repository credentials in BuildKit secrets and never in image build arguments.

### Step 4: [Cross-cutting] Apply site-level OrbitERPNext settings
- **Requirements**: REQ-001, REQ-002
- **Design inputs**: Existing site administration and persistent `sites` volume
- **Description**: Run the app installation/migration and configure the site name, app title, desk logo, website logo, favicon, and any allowed email/print branding settings. Ensure settings are applied idempotently and do not overwrite unrelated customer site configuration.

### Step 5: [Cross-cutting] Enable and verify dark theme behavior
- **Requirements**: REQ-003, REQ-005
- **Design inputs**: Frappe desk theme preferences and Website Theme behavior
- **Description**: Apply the global desk theme behavior supported by the selected Frappe version and configure the public Website Theme. Verify navigation, forms, dialogs, tables, reports, charts, notifications, login, print preview, and mobile layouts for contrast, readability, and missing asset references.

### Step 6: [Cross-cutting] Document deployment and rollback
- **Requirements**: REQ-004, REQ-005
- **Design inputs**: [docs/02-setup/02-build-setup.md](docs/02-setup/02-build-setup.md), [docs/13-explanation/03-asset-handling.md](docs/13-explanation/03-asset-handling.md)
- **Description**: Add an OrbitERPNext deployment guide covering required app repository inputs, image build, Compose generation, migration, rollout, cache invalidation, backup expectations, and rollback to the previous image tag. Document the distinction between runtime site settings and image-managed assets.

### Step 7: [Cross-cutting] Validate the branded deployment
- **Requirements**: REQ-001, REQ-002, REQ-003, REQ-004, REQ-005
- **Design inputs**: Existing repository tests and deployment commands
- **Description**: Validate Compose configuration, build the image, start a disposable environment, install/migrate the branding app, exercise login and desk/public-site flows, verify logo/favicon requests return successful responses, inspect browser console errors, confirm data survives recreation, and verify rollback to the prior image.

## Project Structure

```text
frappe_docker/
├── apps.json                              # Deployment input; references the branding app
├── docs/
│   └── 02-setup/
│       └── 08-orbiterpnext-branding.md    # Build, deploy, configure, rollback
├── images/
│   └── custom/Containerfile                # Existing custom image build path
├── compose.yaml                            # Existing stack, unchanged unless a deployment override is needed
└── overrides/                              # Existing deployment overrides

orbiterpnext_branding/                     # Companion custom Frappe app repository
├── orbiterpnext_branding/
│   ├── hooks.py
│   ├── fixtures/
│   └── public/
│       ├── images/
│       │   ├── orbiterpnext-logo.svg
│       │   └── orbiterpnext-favicon.svg
│       └── css/
│           └── orbiterpnext-dark.css
├── orbiterpnext_branding.egg-info/
└── pyproject.toml
```

## Testing Strategy

- **appType**: Mixed server-rendered HTML and single-page desk application
- **Critical user journeys**:
  1. Administrator logs in and sees OrbitERPNext branding.
  2. Administrator opens desk modules, forms, reports, dialogs, and notifications in dark mode.
  3. Anonymous visitor opens the public site/login page and sees the OrbitERPNext logo, favicon, and dark theme.
  4. Deployment recreates containers without losing site configuration or uploaded files.
  5. Rollback restores the previous image and remains operational.
- **primaryValidationStack**: Docker Compose, existing repository validation scripts, browser smoke testing with the available browser tooling, and direct HTTP asset checks.
- **fallbackMatrix**:
  - `infra-tier`: Docker Compose with disposable volumes → existing local/staging deployment. Prerequisite: Docker and Compose.
  - `browser-tier`: Browser smoke tests → HTTP checks plus manual verification. Prerequisite: running frontend and browser tooling.
- **Environment requirements**: Docker Buildx/BuildKit, a disposable Frappe site, database and Redis services, approved logo assets, and the target Frappe/ERPNext versions.
- **knownGaps**: User-specific theme preferences may override global desk defaults; print/PDF branding may require separate print-format configuration; public website pages supplied by other apps may need app-specific CSS review.
- **Test data strategy**: Use a disposable site and generated site name; seed only the minimum Administrator and sample records required for forms/reports; destroy disposable volumes after validation.
- **Acceptance criteria**: All required branding surfaces show OrbitERPNext, logo/favicon requests succeed, dark theme has no unreadable core controls, image recreation preserves site data, and the previous image can be restored.
- **Validation review expectations**: Confirm no Frappe/ERPNext core files were modified, no credentials are committed, all asset URLs resolve from the built image, and deployment documentation matches the tested commands.

## Phase 1: Setup

- [x] T001 [P] [Plan:1.1] Record generated default OrbitERPNext branding values and deployment scope in `docs/02-setup/08-orbiterpnext-branding.md`.
- [x] T002 [P] [Plan:1.1] Prepare optimized SVG logo and favicon files in `orbiterpnext_branding/orbiterpnext_branding/public/images/`.

## Phase 2: Foundational

- [x] T003 [Plan:2.1] Scaffold the `orbiterpnext_branding` Frappe app with package metadata, `hooks.py`, and install/migrate-safe initialization.
- [x] T004 [P] [Plan:2.1] Add OrbitERPNext CSS variables and dark-theme styles in `orbiterpnext_branding/orbiterpnext_branding/public/css/orbiterpnext-dark.css`.
- [x] T005 [P] [Plan:2.1] Add logo and favicon assets and reference them through supported Frappe app asset paths.

## Phase 3: Branding and Theme

- [x] T006 [US1] [Plan:3.2,3.4] Implement idempotent site branding configuration for app title, desk logo, website logo, favicon, and OrbitERPNext display name.
- [x] T007 [US1] [Plan:3.2,3.5] Register/load the dark-theme stylesheet through supported Frappe hooks and preserve user preference behavior where the platform requires it.
- [x] T008 [US1] [Plan:3.2,3.5] Configure supported public and desk branding fields through Frappe settings hooks.

## Phase 4: Image and Deployment

- [x] T009 [Plan:4.3] Include the local branding app in the custom image; retain ERPNext in `apps.json` and pass it as the existing BuildKit apps secret.
- [x] T010 [Plan:4.3] Integrate and build the branding app through `images/custom/Containerfile`.
- [x] T011 [Plan:4.4,4.6] Document Compose generation, migration, rollout, cache invalidation, backup, and rollback in `docs/02-setup/08-orbiterpnext-branding.md`.

## Phase 5: Validation and Polish

- [ ] T012 [P] [Plan:5.7] Validate generated Compose configuration and run the existing repository Compose/image checks.
- [ ] T013 [US1] [Plan:5.7] Start a disposable stack, create/migrate a site, install the branding app, and verify OrbitERPNext settings and asset URLs.
- [ ] T014 [US1] [Plan:5.7] Run browser smoke checks for dark-mode desk flows, public website/login, favicon, responsive layout, and browser console errors.
- [ ] T015 [Plan:5.7] Recreate frontend/backend containers, confirm site data and branding persist, and perform a rollback test with the previous image tag.

## Requirement Mapping

| REQ ID | Description | Plan Items | Implementation Evidence |
|--------|-------------|------------|------------------------|
| REQ-001 | Rebrand the application as OrbitERPNext | 2.1, 3.2, 3.4, 5.7 | Branding app metadata, idempotent site settings, admin/desk verification |
| REQ-002 | Replace the logo and favicon | 1.1, 2.1, 3.4, 5.7 | `public/images/` assets, configured logo fields, HTTP asset checks |
| REQ-003 | Provide a dark theme for the desk and public website | 1.1, 2.1, 3.5, 5.7 | Dark CSS, Website Theme, browser contrast and flow checks |
| REQ-004 | Deploy the changes using the current Docker setup | 4.3, 4.4, 4.6 | `apps.json`, custom image, Compose deployment and rollback guide |
| REQ-005 | Preserve behavior and verify the resulting deployment | 3.5, 4.6, 5.7 | Validation commands, smoke tests, persistence and rollback evidence |
