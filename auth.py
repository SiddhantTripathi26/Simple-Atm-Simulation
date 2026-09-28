#Encapsulates the authentication engine and attempt threshold logic.

Python
"""
Authentication Module
Handles credential verification and lockout thresholds.
"""

def verify_pin(actual_pin: str, max_attempts: int = 3) -> bool:
    """Prompts the user for their PIN and enforces an attempt counter.

    Args:
        actual_pin: The valid target PIN string.
        max_attempts: Maximum permitted consecutive failed entries.

    Returns:
        bool: True if authenticated successfully; False if attempts are exhausted.
    """
    attempts = max_attempts

    while attempts > 0:
        entered_pin = input("Enter your 4 digit pin: ").strip()

        if entered_pin == actual_pin:
            print("Logged in successfully!\n")
            return True

        attempts -= 1
        print(f"Incorrect Pin... you have {attempts} Attempts Remaining")

    print("Card Frezzed!")
    return False
