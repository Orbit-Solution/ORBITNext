app_name = "orbiterpnext_branding"
app_title = "OrbitERPNext Branding"
app_publisher = "Orbit Solution"
app_description = "OrbitERPNext official branding and dark theme"
app_email = "info@orbitsolution.site"
app_license = "MIT"

app_logo_url = "/assets/orbiterpnext_branding/images/orbiterpnext-logo.svg"

app_include_css = "/assets/orbiterpnext_branding/css/orbiterpnext-dark.css"
app_include_js = "/assets/orbiterpnext_branding/js/orbiterpnext.js"
web_include_css = "/assets/orbiterpnext_branding/css/orbiterpnext-dark.css"
web_include_js = "/assets/orbiterpnext_branding/js/orbiterpnext.js"

extend_bootinfo = "orbiterpnext_branding.boot.boot_session"

after_install = "orbiterpnext_branding.install.set_branding"
after_migrate = [
    "orbiterpnext_branding.install.set_branding"
]
