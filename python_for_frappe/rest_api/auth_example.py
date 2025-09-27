import frappe

@frappe.whitelist()
def token_auth_example(token=None):
    if token != 'my_secret_token':
        frappe.throw("Unauthorized")
    return {'status': 'success'}
