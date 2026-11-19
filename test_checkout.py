"""Tests for the checkout module, including the student discount."""

import unittest

from checkout import apply_student_discount, calculate_total, checkout


class TestCheckout(unittest.TestCase):
    def test_total_is_price_times_quantity(self):
        self.assertEqual(calculate_total(25.0, 4), 100.0)

    def test_checkout_returns_full_price_for_non_student(self):
        self.assertEqual(checkout(100, 1), 100.0)

    def test_negative_input_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_total(-1, 2)


class TestStudentDiscount(unittest.TestCase):
    def test_student_gets_ten_percent_off(self):
        self.assertEqual(apply_student_discount(100, True), 90.0)

    def test_non_student_pays_original_price(self):
        self.assertEqual(apply_student_discount(100, False), 100.0)

    def test_discount_is_rounded_to_two_decimals(self):
        self.assertEqual(apply_student_discount(9.99, True), 8.99)

    def test_checkout_applies_discount_for_student(self):
        self.assertEqual(checkout(100, 1, is_student=True), 90.0)

    def test_checkout_keeps_price_for_non_student(self):
        self.assertEqual(checkout(100, 1), 100.0)

    def test_zero_total_stays_zero(self):
        self.assertEqual(apply_student_discount(0, True), 0.0)


if __name__ == "__main__":
    unittest.main()
