# Ensure connection.begin() work?
def safe_update(trip_name):
    connection = frappe.db
    try:
        connection.begin()

        # Perform multiple operations
        trip = frappe.get_doc("Trip", trip_name)
        trip.status = "Closed"
        trip.save()

        frappe.db.sql("UPDATE `tabTrip Payment` SET is_billed = 0 WHERE trip=%s", (trip_name,))

        connection.commit()

    except Exception:
        connection.rollback()
        frappe.log_error(frappe.get_traceback(), f"Trip Update Failed: {trip_name}")
        frappe.throw("Failed to update trip. Changes rolled back.")
