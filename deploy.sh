#!/bin/bash

set -euo pipefail

cd /home/ubuntu/ORBITNext

echo "=== Pulling latest code ==="
git pull --ff-only origin main

echo "=== Updating submodules ==="
git submodule update --init --recursive

echo "=== Backing up database ==="
docker compose -f pwd.yml exec -T backend \
  bench --site frontend backup

echo "=== Building custom Docker image ==="
docker build \
  -f Dockerfile.orbitnext \
  -t orbitnext/custom:latest .

echo "=== Updating application containers ==="
docker compose -f pwd.yml up -d \
  --pull never --force-recreate \
  backend frontend websocket \
  queue-long queue-short scheduler

echo "=== Building branding assets ==="
docker compose -f pwd.yml exec -T backend \
  bench build --app orbiterpnext_branding

echo "=== Fixing frontend asset link ==="
docker compose -f pwd.yml exec -T frontend \
  ln -sfnT \
  /home/frappe/frappe-bench/apps/orbiterpnext_branding/orbiterpnext_branding/public \
  /home/frappe/frappe-bench/sites/assets/orbiterpnext_branding

echo "=== Running migrations ==="
docker compose -f pwd.yml exec -T backend \
  bench --site frontend migrate

echo "=== Clearing cache ==="
docker compose -f pwd.yml exec -T backend \
  bench --site frontend clear-cache

docker compose -f pwd.yml exec -T backend \
  bench --site frontend clear-website-cache

echo "=== Restarting services ==="
docker compose -f pwd.yml restart \
  backend frontend websocket \
  queue-long queue-short scheduler

echo "=== Deployment status ==="
docker compose -f pwd.yml ps

echo "=== Deployment completed successfully ==="
