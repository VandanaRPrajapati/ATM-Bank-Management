# Import necessary functions and classes
from bank_operations import BankAccount, login
from menu import menu

# List of existing accounts
accounts = [
    BankAccount("123456", "1111", 8100),
    BankAccount("234567", "2024", 32000)
]

# Login Process
input_account = input("Enter account number: ")
input_pin = input("Enter PIN: ")

try:
    account = login(accounts, input_account, input_pin)
except ValueError as e:
    print(e)
    exit()

# Menu-driven program loop
while True:
    choice = menu()
    
    if choice == 1:
        print(account.check_balance())  # Check balance
    elif choice == 2:
        try:
            amount = float(input("Enter deposit amount: "))
            print(account.deposit(amount))  # Deposit money
        except ValueError as e:
            print(e)
    elif choice == 3:
        try:
            amount = float(input("Enter withdrawal amount: "))
            print(account.withdraw(amount))  # Withdraw money
        except ValueError as e:
            print(e)
    elif choice == 4:
        print("Thank you for using the Bank Management System!")
        break
    else:
        print("Invalid choice! Please try again...")
