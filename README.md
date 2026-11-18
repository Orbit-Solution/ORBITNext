<div align="center">
  <a href="https://www.orbitsolution.site/">
    <img src="https://www.orbitsolution.site/logo.png" alt="OrbitNext Logo" width="120" />
  </a>
  <h1>OrbitNext Docker</h1>
  <h3>Enterprise-Grade Container Orchestration for the OrbitNext Ecosystem</h3>
  <p>
    Deploy, scale, and manage your entire business suite—ERP, CRM, Helpdesk, and custom enterprise modules—in minutes with production-ready Docker configurations powered by <a href="https://www.orbitsolution.site/">Orbit Solution</a>.
  </p>
  <p>
    <a href="https://www.orbitsolution.site/">
      <img src="https://img.shields.io/badge/Official_Website-Orbit_Solution-0A7EA4?style=for-the-badge" alt="Orbit Solution Website" />
    </a>
    <a href="docs/">
      <img src="https://img.shields.io/badge/Documentation-Read_Docs-1E293B?style=for-the-badge" alt="Documentation" />
    </a>
    <a href="LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-10B981?style=for-the-badge" alt="MIT License" />
    </a>
  </p>
</div>

---

## Why OrbitNext Docker?

Modern enterprises need infrastructure that moves as fast as their operations. **OrbitNext Docker** eliminates complex server setups and dependency headaches, giving your team a standardized, cloud-native foundation from local evaluation to global production.

* **⚡ Zero-to-Live in Minutes:** Spin up a full-featured OrbitNext environment locally with a single command.
* **🏢 Built for Scale:** Production-hardened Docker Compose architectures designed for high availability, automated backups, and seamless updates.
* **🧩 All-in-One Business Suite:** Run OrbitNext ERP, CRM, Helpdesk, and custom vertical applications side-by-side in isolated, secure containers.
* **🛠️ Custom App Ready:** Easily package your proprietary OrbitNext extensions into immutable, version-controlled Docker images.

---

## Launch a Live Demo in 60 Seconds

Experience the full power of OrbitNext on your local machine using our quick-start evaluation setup (`pwd.yml`).

> **Note:** The demo configuration is built for rapid evaluation and testing. For persistent, high-traffic deployments, use our production setup in `compose.yaml`.

### Prerequisites
Ensure you have [Docker](https://docs.docker.com/get-docker/), [Docker Compose v2](https://docs.docker.com/compose/), and [Git](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git) installed.

### Quick Start

```bash
# 1. Clone the official repository
git clone [https://github.com/orbitsolution/orbitnext_docker](https://github.com/orbitsolution/orbitnext_docker)
cd orbitnext_docker

# 2. Launch the OrbitNext stack
docker compose -f pwd.yml up -d
