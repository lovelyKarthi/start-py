import frappe

# Create a document
doc = frappe.get_doc({
    'doctype': 'ToDo',
    'description': 'Complete Python for Frappe snippets'
})
doc.insert()
frappe.db.commit()

# Read documents
todos = frappe.get_all('ToDo', filters={'status':'Open'}, fields=['name','description'])
print(todos)

# Update document
doc = frappe.get_doc('ToDo', 'TODO-ID')
doc.description = 'Updated description'
doc.save()
frappe.db.commit()

# Delete document
doc = frappe.get_doc('ToDo', 'TODO-ID')
doc.delete()
frappe.db.commit()
