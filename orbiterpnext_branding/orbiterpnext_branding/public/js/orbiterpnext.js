/**
 * OrbitERPNext Branding Script v2.0
 * Orbit Solution (https://www.orbitsolution.site/)
 *
 * Responsibilities:
 *  1. Apply dark theme token immediately (before first paint)
 *  2. Inject Orbit branded navbar logo / wordmark
 *  3. Add sidebar "Powered by Orbit" badge
 *  4. Patch document title
 *  5. Add CSS custom property overrides for feature flags
 *
 * Design principle: NO MutationObserver loops — all DOM work is
 * one-shot after DOMContentLoaded to prevent boot freeze.
 */
(function () {
  "use strict";

  /* ── 1. Immediate theme attribute (runs before first paint) ── */
  var html = document.documentElement;
  html.setAttribute("data-theme", "dark");
  html.classList.add("orbit-theme");

  /* ── 2. After DOM is ready ─────────────────────────────────── */
  function onReady() {
    if (document.body) {
      document.body.setAttribute("data-theme", "dark");
      document.body.classList.add("orbit-theme");
    }

    patchTitle();
    injectNavbarBrand();
    injectSidebarBadge();
    applyStatusBadgeIcons();
  }

  /* ── 3. Title patch ─────────────────────────────────────────── */
  function patchTitle() {
    if (
      document.title &&
      document.title.indexOf("ERPNext") !== -1 &&
      document.title.indexOf("Orbit") === -1
    ) {
      document.title = document.title.replace(/ERPNext/g, "OrbitERPNext");
    }
  }

  /* ── 4. Navbar brand injection ──────────────────────────────── */
  function injectNavbarBrand() {
    var brand = document.querySelector(
      ".navbar-brand, .navbar .brand, .desk-brand, .site-name",
    );
    if (!brand) return;

    /* Only inject if no Orbit branding already present */
    if (brand.querySelector(".orbit-wordmark")) return;

    var logoUrl = "/assets/orbiterpnext_branding/images/orbiterpnext-logo.svg";
    var existingImg = brand.querySelector("img");

    /* Replace or supplement with the Orbit SVG logo */
    if (existingImg) {
      existingImg.src = logoUrl;
      existingImg.alt = "OrbitERPNext";
      existingImg.style.height = "28px";
      existingImg.style.width = "auto";
    }

    /* Wordmark text span, hidden when logo is present */
    var wordmark = document.createElement("span");
    wordmark.className = "orbit-wordmark";
    wordmark.style.cssText = [
      "font-family: 'Poppins', system-ui, sans-serif",
      "font-weight: 700",
      "font-size: 15px",
      "letter-spacing: -0.025em",
      "color: #ffffff",
      "display: inline-flex",
      "align-items: center",
      "gap: 2px",
      existingImg ? "display:none" : "",
    ].join(";");
    wordmark.innerHTML =
      'Orbit<span style="color:#32d7fe;margin-left:2px">ERP</span>Next';

    brand.appendChild(wordmark);
  }

  /* ── 5. Sidebar Orbit badge ─────────────────────────────────── */
  function injectSidebarBadge() {
    var sidebar = document.querySelector(".desk-sidebar, .layout-side-section");
    if (!sidebar) return;
    if (sidebar.querySelector(".orbit-sidebar-badge")) return;

    var badge = document.createElement("div");
    badge.className = "orbit-sidebar-badge";
    badge.style.cssText = [
      "position: absolute",
      "bottom: 16px",
      "left: 50%",
      "transform: translateX(-50%)",
      "white-space: nowrap",
      "display: inline-flex",
      "align-items: center",
      "gap: 6px",
      "padding: 5px 12px 5px 10px",
      "border-radius: 99px",
      "background: rgba(25,85,253,0.10)",
      "border: 1px solid rgba(25,85,253,0.28)",
      "color: rgba(50,215,254,0.80)",
      "font-size: 10px",
      "font-weight: 700",
      "letter-spacing: 0.06em",
      "text-transform: uppercase",
      "font-family: 'Poppins', system-ui, sans-serif",
      "cursor: default",
      "user-select: none",
    ].join(";");
    badge.innerHTML =
      '<span style="width:6px;height:6px;border-radius:50%;' +
      "background:rgba(25,85,253,0.9);display:inline-block;" +
      'box-shadow:0 0 6px 2px rgba(25,85,253,0.5)"></span>' +
      "Orbit Solution";

    /* Make sidebar relative so badge absolute-positioning works */
    sidebar.style.position = "relative";
    sidebar.appendChild(badge);
  }

  /* ── 6. Status / indicator colour normalization ─────────────── */
  function applyStatusBadgeIcons() {
    /* Frappe uses inline dot-colours; ensure our CSS vars apply correctly.
       This is a no-op DOM pass — just lets CSS handle colouring. */
    var pills = document.querySelectorAll(".indicator-pill");
    for (var i = 0; i < pills.length; i++) {
      pills[i].setAttribute("data-orbit-styled", "1");
    }
  }

  /* ── Entry point ────────────────────────────────────────────── */
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", onReady);
  } else {
    onReady();
  }
})();
