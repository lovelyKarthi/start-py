
# --------------------------------------------------
# Pattern for separating validation vs system errors
# --------------------------------------------------

import frappe
from frappe import ValidationError

def cancel(trip_name):
    try:
        # --- business rules ---
        if frappe.db.exists("Trip Payment", {"trip": trip_name, "paid_as": "Balance", "docstatus": 1}):
            # expected validation error
            raise ValidationError("Cancel balance payment(s) before cancelling invoice")

        # ... rest of cancel logic ...

    except ValidationError as e:
        # Expected error: just re-throw so user sees it in UI / job dashboard
        frappe.throw(str(e))

    except Exception as e:
        # Unexpected error: rollback + log full traceback
        frappe.db.rollback()
        frappe.log_error(
            message=frappe.get_traceback(),
            title=f"Trip Invoice Cancel Failed: {trip_name}"
        )
        frappe.throw(f"System error while cancelling invoices for Trip {trip_name}. Please contact support.")
