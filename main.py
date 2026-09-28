#Root CLI entry point that reads configuration, runs the authentication check, and drives the interactive menu loop.

Python
#!/usr/bin/env python3
"""
Project 26: Simple ATM Simulation
Course: CSE1021 - Problem Solving and Object-Oriented Programming

Entry point script that coordinates authentication and transaction loops.
"""

import json
import os
import sys
from src.auth import verify_pin
from src.transaction import collect_your_cash


def load_config(config_path: str = "config.json") -> dict:
    """Loads default configurations, falling back to built-in defaults if absent."""
    defaults = {
        "default_pin": "6969",
        "initial_balance": 500000.0,
        "currency": "Rs.",
        "withdrawal_multiple": 10,
        "max_auth_attempts": 3
    }
    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                defaults.update(loaded)
        except Exception:
            pass
    return defaults


def main():
    """Runs the primary lifecycle of the ATM simulation."""
    config = load_config()

    my_pin = config["default_pin"]
    balance = float(config["initial_balance"])
    currency = config["currency"]
    multiple = config["withdrawal_multiple"]
    max_attempts = config["max_auth_attempts"]

    print("<<< VIT ATM >>>")

    # Step 1: Authentication Gate
    if not verify_pin(my_pin, max_attempts=max_attempts):
        sys.exit(0)

    # Step 2: Main Menu Loop
    keep_going = True
    while keep_going:
        print("\n1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Exit")

        choice = input("Enter The choice: ").strip()

        if choice == "1":
            print(f"Your Account Balance is: {currency} {balance}")
        elif choice == "2":
            balance = collect_your_cash(balance, multiple=multiple, currency=currency)
        elif choice == "3":
            print("Thank you for using VIT ATM !")
            keep_going = False
        else:
            print("Incorrect choice, Please try again.")


if __name__ == "__main__":
    main()
