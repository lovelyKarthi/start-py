Python for Frappe - Quick Reference

- CRUD: frappe.get_doc(), frappe.get_all(), doc.insert(), doc.save(), doc.delete()
- API: frappe.whitelist(), frappe.form_dict, allow_guest
- Hooks: doc_events, scheduler_events
- Queue: frappe.enqueue(), queue='default', timeout
- Utilities: frappe.utils.now(), frappe.utils.get_url()
- Fixtures: defined in hooks.py, use fixtures list
- Migrations: use frappe.get_doc() loop, update fields, doc.save(), frappe.db.commit()
