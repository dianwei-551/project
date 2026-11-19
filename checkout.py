"""Checkout module for the online shopping application.

Handles order totals, the student discount and the final amount printed
to the customer at checkout.
"""

STUDENT_DISCOUNT_RATE = 0.10


def calculate_total(price, quantity):
    """Return the purchase total for a single line item."""
    if price < 0 or quantity < 0:
        raise ValueError("price and quantity must be non-negative")
    return price * quantity


def apply_student_discount(total, is_student):
    """Return the amount to pay after the student discount is applied.

    Eligible students get 10% off; everyone else pays the original total.
    """
    if total < 0:
        raise ValueError("total must be non-negative")
    if is_student:
        return round(total * (1 - STUDENT_DISCOUNT_RATE), 2)
    return total


def checkout(price, quantity, is_student=False):
    """Calculate and print the final amount the customer has to pay."""
    total = calculate_total(price, quantity)
    discount = round(total * STUDENT_DISCOUNT_RATE, 2) if is_student else 0.0
    final_total = apply_student_discount(total, is_student)

    print(f"Subtotal        : GBP {total:.2f}")
    if is_student:
        print(f"Student discount: -GBP {discount:.2f} (10%)")
    print(f"Total to pay    : GBP {final_total:.2f}")
    return final_total


if __name__ == "__main__":
    checkout(100, 1, is_student=True)
