import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def my_custom_api_method(param1, param2=None):
    try:
        result = {'param1': param1, 'param2': param2}
        return result
    except Exception as e:
        frappe.throw(_("Error: {0}").format(str(e)))
