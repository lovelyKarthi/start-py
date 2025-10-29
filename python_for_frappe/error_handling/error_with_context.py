# ----------------------------------------------------
# Error with User undestandable context
# Use when you want clear error messages with details.
# ----------------------------------------------------
def validate_payment(trip_name, amount):
    total_payable = 1000
    if amount > total_payable:
        frappe.throw(
            f"You cannot pay more than {total_payable}. "
            f"Attempted payment: {amount}."
        )
