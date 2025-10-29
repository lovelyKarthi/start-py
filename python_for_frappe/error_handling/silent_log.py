def optional_check(trip_name):
    try:
        # non-critical check
        something = 1 / 0
    except Exception:
        frappe.log_error(frappe.get_traceback(), f"Optional check failed for Trip {trip_name}")
        # don’t throw, continue
