import frappe
from frappe.utils import now, get_url

print('Current time:', now())
print('Site URL:', get_url())
