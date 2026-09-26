

# Project 26: Simple ATM Simulation
# Course: CSE1021 - Problem Solving and Object-Oriented Programming

def verify_pin(actual_pin):
    attempts = 3
    while attempts > 0:
        p = input("Enter your 4 digit pin: ")
        if p == actual_pin:
            print("Logged in successfully!\n")
            return True
        else:
            attempts = attempts - 1
            print("Incorrect Pin... you have", attempts, "Attempts Remaining")
            
    print("Card Frezzed!")
    return False

def collect_your_cash(current_balance):
    print("Note: You can withdraw in multiples of 10 only")
    
    amount_str = input("Enter Wihdrawal amount: Rs. ")
    
   
    if amount_str.isdigit():
        amt = int(amount_str)
        
        if amt <= 0:
            print("Please Enter a Permissible amount")
        elif amt > current_balance:
            print("Low balance :(")
        elif amt % 10 != 0:
            print("Enter amount in multiples of 10 only!")
        else:
            current_balance = current_balance - amt
            print("Collect your Cash:", amt)
            print("New balance is Rs.", current_balance)
    else:
        print(" Enter Digits Only")
        
    return current_balance


my_pin = "6969"
balance = 500000.0

print("<<< VIT ATM >>>")

is_logged_in = verify_pin(my_pin)

if is_logged_in == True:
    keep_going = True
    
    while keep_going:
        print("\n1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Exit")
        
        choice = input("Enter The choice: ")
        
        if choice == '1':
            print("Your Account Balance is: $", balance)
        elif choice == '2':
            balance = collect_your_cash(balance)
        elif choice == '3':
            print("Thank you for using VIT ATM !")
            keep_going = False
        else:
            print("Incorrect choice,Please try again.")