import frappe

def migrate_custom_fields():
    # Example migration: update all ToDo descriptions to uppercase
    todos = frappe.get_all('ToDo', fields=['name','description'])
    for t in todos:
        doc = frappe.get_doc('ToDo', t.name)
        doc.description = doc.description.upper()
        doc.save()
    frappe.db.commit()
