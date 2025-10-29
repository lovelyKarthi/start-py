# Error handling playbook

## 🔹 1. Simple Validation Error (business rule)

👉 Use this when a condition should stop the user but it’s not a system bug.

```py
def validate_trip_open(trip_name):
    status = frappe.db.get_value("Trip", trip_name, "trip_status")
    if status == "Closed":
        frappe.throw("Trip is closed. Insert, update or delete is not allowed.")
```

Stops the action immediately.

No error log, because this is an expected business rule.

## 🔹 2. Validation vs System Error (mixed handling)

👉 Use this when you want to separate user mistakes from real bugs.

```py
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
```

Business errors → clear message to user.

System errors → logged & hidden behind a generic message.

## 🔹 3. Custom Domain-Specific Error

👉 Use this when you want your own error class for clarity.

```py
class TripCancelError(frappe.ValidationError):
    """Custom error for trip cancellation rules."""

def cancel_trip(trip_name):
    try:
        if frappe.db.exists("Trip Payment", {"trip": trip_name, "paid_as": "Balance", "docstatus": 1}):
            raise TripCancelError("Balance payment exists, cannot cancel trip")

    except TripCancelError as e:
        frappe.throw(str(e))
```

Makes your business logic more self-documenting.

You can catch only your domain-specific errors separately.

## 🔹 4. Full Transaction Safety

👉 Use this when you need to guarantee all-or-nothing.

```py
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
```

Ensures no partial updates on error.

Always rollback before logging.

## 🔹 5. Background Job (enqueue) Safe Error Handling

👉 Use this when logic runs asynchronously in RQ worker.

```py
def cancel_invoice(trip_name):
    try:
        # Business validation
        if frappe.db.exists("Trip Payment", {"trip": trip_name, "paid_as": "Balance", "docstatus": 1}):
            frappe.throw("Balance payments exist, cancel not allowed")

        # Expensive operations...
        # cancel invoices, reset fields, etc.

    except frappe.ValidationError as e:
        # Validation → visible to user in Job Dashboard
        frappe.throw(str(e))

    except Exception:
        # Unexpected crash → log + job marked failed
        frappe.log_error(frappe.get_traceback(), f"Trip Invoice Cancel Failed: {trip_name}")
        frappe.throw("System error in invoice cancel. Please contact support.")
```

User-facing errors → clear and visible in Job Dashboard.

Bugs → logged for developers.

## 🔹 6. Silent Logging (no throw)

👉 Use this when you don’t want to stop execution, but want debug info.

```py
def optional_check(trip_name):
    try:
        # non-critical check
        something = 1 / 0
    except Exception:
        frappe.log_error(frappe.get_traceback(), f"Optional check failed for Trip {trip_name}")
        # don’t throw, continue
```

Useful in hooks, schedulers, or background jobs where you don’t want to block everything.

## 🔹 7. User-Friendly Error with Context

👉 Use when you want clear error messages with details.

```py
def validate_payment(trip_name, amount):
    total_payable = 1000
    if amount > total_payable:
        frappe.throw(
            f"You cannot pay more than {total_payable}. "
            f"Attempted payment: {amount}."
        )
```

Users get a clear, actionable message.

Not just “Validation Failed”.