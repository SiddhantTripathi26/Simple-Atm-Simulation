# Project 26: Simple ATM Simulation

**Course:** CSE1021 - Problem Solving and Object-Oriented Programming  
**File:** statement.md  

---

## 1. Problem Statement

Manual banking operations require human tellers to handle basic transactions like cash dispensing, balance verifications, and user identification. This manual overhead creates service bottlenecks and limits transaction availability outside standard banking hours.

To address this, financial kiosks utilize Automated Teller Machines (ATMs). This project simulates the core logic of an ATM kiosk using Python. The system addresses critical functional challenges:
- **Authentication Security:** Implementing identity checks using a 4-digit PIN with a fixed retry threshold to mitigate brute-force attempts.
- **Transactional Integrity:** Enforcing strict arithmetic and business constraints on cash withdrawals (ensuring values are positive integers, denominations match supported multiples of 10, and transactions do not exceed the available balance).
- **Session Continuity:** Maintaining continuous state updates to the account balance across multiple sequential operations without unexpected program termination.

---

## 2. Scope of the Project

### 2.1 In-Scope
- **Command-Line Interface (CLI):** Lightweight terminal-driven menu allowing interactive user navigation.
- **PIN Verification Protocol:** Pre-session authentication allowing a maximum of three attempts before triggering a security lockout ("Card Frozen").
- **Account State Monitoring:** Real-time balance inquiry for an authenticated session.
- **Cash Withdrawal Engine:**
  - Input parsing and validation to reject non-numeric characters.
  - Multi-tier condition handling (negative check, zero check, denomination check, overdraft check).
  - Dynamic in-memory balance deduction.
- **Session Lifecycle:** Interactive loop facilitating consecutive actions until an explicit exit command is issued by the user.

### 2.2 Out-of-Scope
- **Persistent Storage:** Storage of accounts or logs in external files or databases (state resets on program termination).
- **Multi-Account / Concurrency:** Multi-tenant support, simultaneous account switching, or concurrent network transactions.
- **Hardware Integration:** Communication with physical card readers, keypad hardware, or mechanical cash dispensers.
- **Advanced Banking Features:** Deposit processing, fund transfers between accounts, account statement generation, or dynamic PIN alteration.

---

## 3. Target Users

- **Banking Customers / End Users:** Individuals requiring quick, self-service financial checks and cash withdrawals via terminal interfaces.
- **Academic Evaluators & Instructors:** Faculty assessing practical application of structured programming, modular functions, control loops, and edge-case validation.
- **Computer Science Students:** Learners studying procedural programming paradigms and terminal application state management in Python.

---

## 4. High-Level Features

- **Attempt-Limited PIN Authentication:** Checks user input against stored credentials (`6969`) with an automated lockout after 3 consecutive failures.
- **Real-Time Balance Display:** Immediate readout of available account funds upon request.
- **Defensive Cash Dispensing:**
  - Checks input format using `.isdigit()` to avoid program crashes.
  - Verifies currency denominations (multiples of 10).
  - Blocks overdraft attempts when requested amounts exceed available capital.
- **Continuous Multi-Transaction Loop:** Allows users to conduct multiple balance checks and withdrawals within a single login session.
