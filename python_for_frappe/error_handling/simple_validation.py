def validate_trip_open(trip_name):
    status = frappe.db.get_value("Trip", trip_name, "trip_status")
    if status == "Closed":
        frappe.throw("Trip is closed. Insert, update or delete is not allowed.")
