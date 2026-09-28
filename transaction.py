#Encapsulates financial validation rules and balance mutations.

Python
"""
Transaction Module
Processes cash withdrawals and balance updates with defensive validation.
"""

from typing import Tuple


def validate_and_withdraw(
    amount_str: str,
    current_balance: float,
    multiple: int = 10,
    currency: str = "Rs."
) -> Tuple[bool, float, str]:
    """Validates requested cash withdrawal against operational constraints.

    Args:
        amount_str: Raw input string from the user.
        current_balance: Current available funds.
        multiple: Required bill denomination multiple (default: 10).
        currency: Currency symbol prefix for messages.

    Returns:
        Tuple[bool, float, str]:
            - bool: True if withdrawal succeeded, False otherwise.
            - float: The updated balance.
            - str: Feedback message describing the outcome.
    """
    # Defensive Check 1: Numeric digits only
    if not amount_str.isdigit():
        return False, current_balance, "Enter Digits Only"

    amt = int(amount_str)

    # Defensive Check 2: Strictly positive amounts
    if amt <= 0:
        return False, current_balance, "Please Enter a Permissible amount"

    # Defensive Check 3: Overdraft prevention
    if amt > current_balance:
        return False, current_balance, "Low balance :("

    # Defensive Check 4: Denomination divisibility
    if amt % multiple != 0:
        return False, current_balance, f"Enter amount in multiples of {multiple} only!"

    # Success: Deduct funds
    new_balance = current_balance - float(amt)
    success_msg = f"Collect your Cash: {amt}\nNew balance is {currency} {new_balance}"
    return True, new_balance, success_msg


def collect_your_cash(
    current_balance: float,
    multiple: int = 10,
    currency: str = "Rs."
) -> float:
    """CLI wrapper that prompts user for cash and returns updated balance."""
    print(f"Note: You can withdraw in multiples of {multiple} only")
    amount_str = input(f"Enter Withdrawal amount: {currency} ").strip()

    _, updated_balance, message = validate_and_withdraw(
        amount_str, current_balance, multiple=multiple, currency=currency
    )
    print(message)
    return updated_balance
