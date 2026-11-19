"""Checkout module for the online shopping application.

Handles order totals and the final checkout amount printed to the customer.
"""


def calculate_total(price, quantity):
    """Return the purchase total for a single line item."""
    if price < 0 or quantity < 0:
        raise ValueError("price and quantity must be non-negative")
    return price * quantity


def checkout(price, quantity):
    """Calculate and print the final amount the customer has to pay."""
    total = calculate_total(price, quantity)
    print(f"Total: GBP {total:.2f}")
    return total


if __name__ == "__main__":
    checkout(100, 1)
