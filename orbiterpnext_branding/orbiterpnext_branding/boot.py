import frappe

LOGO = "/assets/orbiterpnext_branding/images/orbiterpnext-logo.svg"


def boot_session(bootinfo):
    """Extend bootinfo with OrbitERPNext branding."""
    bootinfo.app_name = "OrbitERPNext"
    bootinfo.app_title = "OrbitERPNext"
    bootinfo.app_logo_url = LOGO
    bootinfo.desk_theme = "Dark"

    if hasattr(bootinfo, "apps_data") and isinstance(bootinfo.apps_data, dict):
        apps = bootinfo.apps_data.get("apps", [])
        for app in apps:
            if app.get("name") == "erpnext":
                app["title"] = "OrbitERPNext"
                app["logo"] = LOGO
