# Example hooks in hooks.py or custom app hooks
doc_events = {
    'ToDo': {
        'validate': 'my_app.todo.validate_todo',
        'on_update': 'my_app.todo.on_update_todo',
        'on_submit': 'my_app.todo.on_submit_todo',
        'on_cancel': 'my_app.todo.on_cancel_todo',
    }
}

# Example hook method
def validate_todo(doc, method):
    if not doc.description:
        frappe.throw("Description is required")
