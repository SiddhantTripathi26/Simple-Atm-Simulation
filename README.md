# Simple ATM Simulation

A beginner-friendly command-line interface (CLI) Python application simulating core automated teller machine (ATM) operations such as secure PIN authentication, balance inquiry, and cash withdrawal with input validations.

---

## Features

- **PIN Verification**:
  - Secure check with up to **3 attempts**.
  - Automatic card freeze notification upon exceeding the limit.
- **Balance Inquiry**:
  - View real-time available account balance.
- **Cash Withdrawal**:
  - Validation to ensure amounts are numeric and positive.
  - Multiples of 10 requirement check.
  - Insufficient funds (low balance) validation.
- **Interactive Menu**:
  - Loop-based terminal menu allowing multiple operations in one session until explicit exit.

---

## Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/) installed on your local machine.

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/simple-atm-simulation.git
   cd simple-atm-simulation
   ```

2. **Run the program:**
   ```bash
   python atm.py
   ```
   *(Replace `atm.py` with whatever name you gave your Python script file)*

---

## Default Credentials & Settings

| Parameter | Default Value | Description |
| :--- | :--- | :--- |
| **Default PIN** | `6969` | Initial PIN for login verification |
| **Max Attempts** | `3` | Number of allowed PIN entries before card is locked |
| **Initial Balance** | `Rs. 500,000.0` | Starting demo account balance |

---

## Usage Example

```text
<<< VIT ATM >>>
Enter your 4 digit pin: 6969
Logged in successfully!

1. Check Balance
2. Withdraw Cash
3. Exit
Enter The choice: 1
Your Account Balance is: $ 500000.0

1. Check Balance
2. Withdraw Cash
3. Exit
Enter The choice: 2
Note: You can withdraw in multiples of 10 only
Enter Wihdrawal amount: Rs. 500
Collect your Cash: 500
New balance is Rs. 499500.0

1. Check Balance
2. Withdraw Cash
3. Exit
Enter The choice: 3
Thank you for using VIT ATM !
```

---

## Future Enhancements

- [ ] Cash deposit feature (`deposit_cash`).
- [ ] PIN change functionality.
- [ ] Support for multiple accounts using a dictionary or SQLite database.
- [ ] Transaction history / mini-statement export.

---
