"""Basic tests for the checkout module."""

import unittest

from checkout import calculate_total, checkout


class TestCheckout(unittest.TestCase):
    def test_total_is_price_times_quantity(self):
        self.assertEqual(calculate_total(25.0, 4), 100.0)

    def test_checkout_returns_full_price(self):
        self.assertEqual(checkout(100, 1), 100.0)

    def test_negative_input_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_total(-1, 2)


if __name__ == "__main__":
    unittest.main()
