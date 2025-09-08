import frappe

def before_uninstall():
    # --- Reset Website Settings ---
    frappe.db.set_single_value("Website Settings", "app_name", "Frappe")
    frappe.db.set_single_value("Website Settings", "app_logo", "/assets/frappe/images/frappe-framework-logo.svg")
    frappe.db.set_single_value("Website Settings", "favicon", "/assets/frappe/images/favicon.png")

    # --- Reset Navbar Settings ---
    navbar = frappe.get_doc("Navbar Settings")
    navbar.navbar_logo = "/assets/frappe/images/frappe-framework-logo.svg"

    # Unhide default items
    for item in navbar.settings_dropdown:
        if item.item_label in ["My Settings", "Session Defaults", "View Website", "Apps"]:
            item.hidden = 0

    # Remove our custom "About" item
    navbar.settings_dropdown = [
        i for i in navbar.settings_dropdown if i.item_label != "About"
    ]

    navbar.save(ignore_permissions=True)
    frappe.db.commit()
