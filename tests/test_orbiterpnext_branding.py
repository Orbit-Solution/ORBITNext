from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "orbiterpnext_branding" / "orbiterpnext_branding"


def test_branding_app_assets_exist():
    assert (APP / "public" / "images" / "orbiterpnext-logo.svg").is_file()
    assert (APP / "public" / "images" / "orbiterpnext-favicon.svg").is_file()
    assert (APP / "public" / "css" / "orbiterpnext-dark.css").is_file()
    assert (APP / "public" / "js" / "orbiterpnext.js").is_file()


def test_branding_app_hooks():
    hooks = (APP / "hooks.py").read_text()
    assert 'app_title = "OrbitERPNext Branding"' in hooks
    assert "orbiterpnext-dark.css" in hooks
    assert "orbiterpnext.js" in hooks
    assert "after_migrate" in hooks


def test_branding_install_is_idempotent_and_field_guarded():
    install = (APP / "install.py").read_text()
    assert "OrbitERPNext" in install
    assert "meta.has_field(fieldname)" in install
    assert "ignore_permissions=True" in install


def test_custom_image_copies_branding_app():
    containerfile = (ROOT / "images" / "custom" / "Containerfile").read_text()
    assert "COPY --chown=frappe:0 orbiterpnext_branding" in containerfile
    assert "pip install -e apps/orbiterpnext_branding" in containerfile
