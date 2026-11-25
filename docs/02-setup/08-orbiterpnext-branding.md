# OrbitERPNext Branding

A small Frappe custom app that applies OrbitERPNext branding and a dark theme.

It provides:

- OrbitERPNext logo and favicon assets
- Dark desk and public-website CSS
- A dark-theme preference bootstrap for supported Frappe desk clients
- Idempotent `after_migrate` site branding configuration

Branding values are applied only when the corresponding Frappe fields exist.

# OrbitERPNext Branding Deployment

The repository includes a local `orbiterpnext_branding` Frappe app. It adds:

- OrbitERPNext as the application name
- A generated OrbitERPNext logo and favicon
- Dark desk CSS and dark public-website CSS
- An `after_migrate` hook that updates supported System Settings and Website Settings fields

The app does not modify Frappe or ERPNext core source.

## Build

Create the custom image with BuildKit:

```bash
docker build \
  --no-cache \
  --build-arg=FRAPPE_PATH=https://github.com/frappe/frappe \
  --build-arg=FRAPPE_BRANCH=version-16 \
  --build-arg=CACHE_BUST="$(date +%s)" \
  --secret=id=apps_json,src=apps.json \
  --tag=orbiterpnext:16 \
  --file=images/custom/Containerfile .
```

The custom app is copied directly from `orbiterpnext_branding/`, so no private GitHub repository is required.

## Deploy

Set the custom image variables in `.env`:

```dotenv
CUSTOM_IMAGE=orbiterpnext
CUSTOM_TAG=16
PULL_POLICY=missing
DB_PASSWORD=change-this-password
ERPNEXT_VERSION=v16.55.0
```

Generate the Compose configuration with the overrides required by the target:

```bash
docker compose --env-file .env \
  -f compose.yaml \
  -f overrides/compose.mariadb.yaml \
  -f overrides/compose.redis.yaml \
  -f overrides/compose.noproxy.yaml \
  config > compose.orbiterpnext.yaml
```

Create or start the stack:

```bash
docker compose --project-name orbiterpnext \
  -f compose.orbiterpnext.yaml up -d
```

Create a site and install ERPNext, then install the branding app:

```bash
docker compose --project-name orbiterpnext \
  -f compose.orbiterpnext.yaml exec backend \
  bench new-site erp.example.com \
  --mariadb-root-password "$DB_PASSWORD" \
  --admin-password change-this-admin-password \
  --install-app erpnext

docker compose --project-name orbiterpnext \
  -f compose.orbiterpnext.yaml exec backend \
  bench --site erp.example.com install-app orbiterpnext_branding

docker compose --project-name orbiterpnext \
  -f compose.orbiterpnext.yaml exec backend \
  bench --site erp.example.com migrate
```

## Replacing the generated logo

Replace these files with approved production assets:

- `orbiterpnext_branding/orbiterpnext_branding/public/images/orbiterpnext-logo.svg`
- `orbiterpnext_branding/orbiterpnext_branding/public/images/orbiterpnext-favicon.svg`

SVG is preferred for the logo and favicon. Keep accessible contrast and test the logo at narrow viewport widths.

## Theme behavior

The app loads dark CSS for both desk and public website pages. Frappe user-level appearance settings may override or supplement the global CSS. The app also sets `data-theme="dark"` on the desk document for clients that support it.

Browser cache may retain the old assets after deployment. Rebuild with a new `CACHE_BUST` and recreate the frontend containers:

```bash
docker compose --project-name orbiterpnext \
  -f compose.orbiterpnext.yaml up -d --force-recreate backend frontend websocket
```

## Rollback

Keep the previous image tag and Compose file. To roll back:

```dotenv
CUSTOM_IMAGE=orbiterpnext
CUSTOM_TAG=15
PULL_POLICY=missing
```

Regenerate the Compose file and recreate the application containers. Do not delete the `sites` volume. Run migrations only with the ERPNext/Frappe versions supported by the existing backup.
