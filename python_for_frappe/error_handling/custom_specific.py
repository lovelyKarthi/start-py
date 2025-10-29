class TripCancelError(frappe.ValidationError):
    """Custom error for trip cancellation rules."""

def cancel_trip(trip_name):
    try:
        if frappe.db.exists("Trip Payment", {"trip": trip_name, "paid_as": "Balance", "docstatus": 1}):
            raise TripCancelError("Balance payment exists, cannot cancel trip")

    except TripCancelError as e:
        frappe.throw(str(e))
