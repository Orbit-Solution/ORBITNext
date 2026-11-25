import frappe

LOGO    = "/assets/orbiterpnext_branding/images/orbiterpnext-logo.svg"
FAVICON = "/assets/orbiterpnext_branding/images/orbiterpnext-favicon.svg"
BRAND_HTML = (
    '<span style="font-family:Poppins,system-ui,sans-serif;font-weight:700;'
    'letter-spacing:-0.025em;color:#ffffff;display:inline-flex;'
    'align-items:center;gap:4px">'
    'Orbit'
    '<span style="color:#32d7fe">ERP</span>'
    'Next'
    '</span>'
)
THEME_NAME = "Orbit Dark"


def set_branding():
    """Apply site-level OrbitERPNext branding — idempotent & safe."""

    _apply_website_theme()
    _apply_system_settings()
    _apply_website_settings()
    _apply_navbar_settings()
    _set_dark_theme_for_users()

    frappe.clear_cache()


# ── Helpers ──────────────────────────────────────────────────────────────

def _apply_website_theme():
    """Create or update the 'Orbit Dark' Website Theme."""
    try:
        custom_scss = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

body {
    font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background-color: #04060e !important;
    color: #c8c8d4 !important;
    -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4, h5, h6, .navbar-brand {
    font-family: 'Poppins', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    color: #ffffff !important;
    letter-spacing: -0.02em;
}
"""
        fields = {
            "primary_color":         "#1955fd",
            "background_color":      "#04060e",
            "text_color":            "#c8c8d4",
            "dark_color":            "#0b0e1a",
            "light_color":           "#0f1320",
            "google_font":           "Inter",
            "font_size":             "15px",
            "button_rounded_corners": 1,
            "button_shadows":        0,
            "custom_scss":           custom_scss,
        }

        if not frappe.db.exists("Website Theme", THEME_NAME):
            doc = frappe.get_doc({"doctype": "Website Theme", "theme": THEME_NAME, "custom": 1, **fields})
            doc.insert(ignore_permissions=True)
        else:
            doc = frappe.get_doc("Website Theme", THEME_NAME)
            for k, v in fields.items():
                setattr(doc, k, v)
            doc.save(ignore_permissions=True)

    except Exception as e:
        frappe.log_error(f"Website Theme error: {e}", "OrbitERPNext Branding")


def _apply_system_settings():
    """Rename the app in System Settings."""
    try:
        ss = frappe.get_single("System Settings")
        ss.app_name = "OrbitERPNext"
        ss.save(ignore_permissions=True)
    except Exception as e:
        frappe.log_error(f"System Settings error: {e}", "OrbitERPNext Branding")


def _apply_website_settings():
    """Set logo, favicon, theme, and footer branding."""
    try:
        ws = frappe.get_single("Website Settings")
        ws.app_name     = "OrbitERPNext"
        ws.app_logo     = LOGO
        ws.favicon      = FAVICON
        ws.splash_image = LOGO
        ws.brand_html   = BRAND_HTML
        ws.copyright    = "© Orbit Solution"
        ws.footer_items = []   # clear default footer links if any

        if frappe.db.exists("Website Theme", THEME_NAME):
            ws.website_theme = THEME_NAME

        ws.save(ignore_permissions=True)
    except Exception as e:
        frappe.log_error(f"Website Settings error: {e}", "OrbitERPNext Branding")


def _apply_navbar_settings():
    """Update navbar logo."""
    try:
        nav = frappe.get_single("Navbar Settings")
        nav.app_logo = LOGO
        nav.save(ignore_permissions=True)
    except Exception as e:
        frappe.log_error(f"Navbar Settings error: {e}", "OrbitERPNext Branding")


def _set_dark_theme_for_users():
    """Force 'Dark' desk theme for all enabled users who haven't set a preference."""
    try:
        frappe.db.sql("""
            UPDATE `tabUser`
               SET desk_theme = 'Dark'
             WHERE enabled = 1
               AND (desk_theme IS NULL OR desk_theme IN ('Light', ''))
        """)
        frappe.db.commit()
    except Exception as e:
        frappe.log_error(f"User desk_theme error: {e}", "OrbitERPNext Branding")
