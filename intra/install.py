import frappe

def after_install():
    # --- Website Branding ---
    frappe.db.set_single_value("Website Settings", "app_name", "IntraERP")
    frappe.db.set_single_value("Website Settings", "app_logo", "/assets/intra/images/logo.png")
    frappe.db.set_single_value("System Settings", "login_with_email_link", 0)
    
    frappe.db.set_single_value("Website Settings", "app_name", "IntraERP")
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
        # shift last item temporarily
        last_item = navbar.settings_dropdown[-1]
        navbar.settings_dropdown = navbar.settings_dropdown[:-1]

        # append new record properly
        navbar.append("settings_dropdown", new_item)

        # re-append the last item
        navbar.append("settings_dropdown", last_item.as_dict())
    else:
        navbar.append("settings_dropdown", new_item)

    navbar.save(ignore_permissions=True)
    frappe.db.commit()

    workspaces = frappe.get_all("Workspace", filters={"name": ["like", "ERPNext%"]}, fields=["name"])
    for ws in workspaces:
        new_name = ws.name.replace("ERPNext", "IntraERP", 1)
        try:
            frappe.rename_doc("Workspace", ws.name, new_name, force=True)
        except Exception as e:
            frappe.log_error(f"Rename failed for {ws.name}: {e}")

    # clear cache so sidebar picks up new names
    frappe.clear_cache()
    frappe.clear_website_cache()
