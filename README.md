<div align="center">
  <img src="docs/public/orbitnext-docker.png" alt="OrbitNext Docker" width="80" />
  <h1>OrbitNext Docker</h1>
  <p>Docker images and orchestration for <a href="https://www.orbitsolution.site/">OrbitNext</a> applications by Orbit Solution.</p>
  <p>
    <a href="https://github.com/orbitsolution/orbitnext_docker/actions/workflows/core-build-stable.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/orbitsolution/orbitnext_docker/core-build-stable.yml?branch=main&label=Build%20Stable" alt="Build Stable" />
    </a>
    <a href="https://github.com/orbitsolution/orbitnext_docker/actions/workflows/core-build-develop.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/orbitsolution/orbitnext_docker/core-build-develop.yml?branch=main&label=Build%20Develop" alt="Build Develop" />
    </a>
    <a href="https://www.orbitsolution.site/">
      <img src="https://img.shields.io/badge/Website-Orbit%20Solution-0A7EA4" alt="Orbit Solution" />
    </a>
    <a href="docs/">
      <img src="https://img.shields.io/badge/Docs-Open%20Docs-0A7EA4" alt="Docs" />
    </a>
  </p>
</div>

## What is this?

This repository is the official container setup for **OrbitNext**, developed and maintained by [Orbit Solution](https://www.orbitsolution.site/).

It provides Docker images, Compose configurations, and documentation for running OrbitNext applications—including OrbitNext ERP, CRM, Helpdesk, and custom enterprise modules—in containers.

Use it if you want to:

- run OrbitNext ERP, CRM, Helpdesk, or custom modules with Docker
- start from a quick local demo setup
- use production-ready Docker images and Compose configurations
- build custom OrbitNext application images
- deploy and operate OrbitNext in production

## Repository Structure

```bash
orbitnext_docker/
├── docs/                 # Complete deployment and operational documentation
├── overrides/            # Docker Compose configurations for different scenarios
├── compose.yaml          # Base Compose file for production setups
├── pwd.yml               # Single Compose file for quick disposable demo
├── images/               # Dockerfiles for building OrbitNext images
├── development/          # Development environment configurations
├── devcontainer-example/ # VS Code devcontainer setup
└── resources/            # Helper scripts and configuration templates
