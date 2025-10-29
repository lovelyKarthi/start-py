from frappe import ValidationError

def process_trip(trip_name):
    try:
        if not frappe.db.exists("Trip", trip_name):
            raise ValidationError("Trip not found")

        # Some risky DB operation
        frappe.db.sql("INVALID SQL")  # crash

    except ValidationError as e:
        # Business error → user message
        frappe.throw(str(e))

    except Exception:
        # Unexpected error → log + generic message
        frappe.log_error(frappe.get_traceback(), f"Trip Processing Failed: {trip_name}")
        frappe.throw("System error. Please contact support.")
