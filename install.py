import frappe

def after_install():
    # Set website logo and favicon
    frappe.db.set_single_value("Website Settings", "app_name", "IntraERP")
    frappe.db.set_single_value("Website Settings", "app_logo", "/assets/intra/images/logo.png")
    frappe.db.set_single_value("Website Settings", "favicon", "/assets/intra/images/favicon.png")
    
    # Update Navbar Settings
    navbar = frappe.get_doc("Navbar Settings")
    navbar.update({
        "navbar_logo": "/assets/intra/images/logo.png"
    })
    navbar.save(ignore_permissions=True)

    frappe.db.commit()
