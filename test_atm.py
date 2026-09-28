#Automated unit tests using Python's built-in unittest runner to verify business logic and edge cases.

Python
"""
Unit tests for the ATM withdrawal engine.
Run via: python -m unittest discover tests
"""

import unittest
from src.transaction import validate_and_withdraw


class TestATMWithdrawal(unittest.TestCase):

    def setUp(self):
        self.initial_balance = 500000.0

    def test_valid_withdrawal(self):
        success, new_bal, msg = validate_and_withdraw("1500", self.initial_balance)
        self.assertTrue(success)
        self.assertEqual(new_bal, 498500.0)
        self.assertIn("Collect your Cash: 1500", msg)

    def test_non_digit_rejection(self):
        success, new_bal, msg = validate_and_withdraw("abc", self.initial_balance)
        self.assertFalse(success)
        self.assertEqual(new_bal, self.initial_balance)
        self.assertEqual(msg, "Enter Digits Only")

    def test_zero_amount_rejection(self):
        success, new_bal, msg = validate_and_withdraw("0", self.initial_balance)
        self.assertFalse(success)
        self.assertEqual(new_bal, self.initial_balance)
        self.assertEqual(msg, "Please Enter a Permissible amount")

    def test_negative_sign_rejection(self):
        # "-100".isdigit() returns False, protecting against negative input
        success, new_bal, msg = validate_and_withdraw("-100", self.initial_balance)
        self.assertFalse(success)
        self.assertEqual(new_bal, self.initial_balance)
        self.assertEqual(msg, "Enter Digits Only")

    def test_non_multiple_of_ten(self):
        success, new_bal, msg = validate_and_withdraw("45", self.initial_balance)
        self.assertFalse(success)
        self.assertEqual(new_bal, self.initial_balance)
        self.assertIn("multiples of 10 only", msg)

    def test_overdraft_prevention(self):
        success, new_bal, msg = validate_and_withdraw("600000", self.initial_balance)
        self.assertFalse(success)
        self.assertEqual(new_bal, self.initial_balance)
        self.assertEqual(msg, "Low balance :(")


if __name__ == "__main__":
    unittest.main()
