import frappe

def after_install():
    # --- Website Branding ---
    frappe.db.set_single_value("Website Settings", "app_name", "IntraERP")
    frappe.db.set_single_value("Website Settings", "app_logo", "/assets/intra/images/logo.png")
    frappe.db.set_single_value("Website Settings", "favicon", "/assets/intra/images/favicon.png")
    
    # --- Navbar Settings ---
    navbar = frappe.get_doc("Navbar Settings")
    navbar.navbar_logo = "/assets/intra/images/logo.png"

    # 1. Hide specific items in settings_dropdown
    for item in navbar.settings_dropdown:
        if item.item_label in ["My Settings", "Session Defaults", "View Website", "Apps"]:
            item.hidden = 1

    # 2. Add "About" item before the last record
    new_item = {
        "item_label": "About",
        "item_type": "Route",
        "route": "https://intraerp.com",
        "hidden": 0
    }

    if len(navbar.settings_dropdown) > 0:
        navbar.settings_dropdown.insert(len(navbar.settings_dropdown) - 1, new_item)
    else:
        navbar.append("settings_dropdown", new_item)

    navbar.save(ignore_permissions=True)
    frappe.db.commit()
