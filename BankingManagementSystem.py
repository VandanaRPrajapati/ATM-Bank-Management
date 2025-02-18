class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return f"Your current balance is: ₹{self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"₹{amount} deposited successfully!"
        else:
            raise ValueError("Deposit amount must be greater than 0")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        elif amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        else:
            self.balance -= amount
            return f"₹{amount} withdrawn successfully!"


def login(accounts, account_number, pin):
    for account in accounts:
        if account.account_number == account_number and account.pin == pin:
            return account
    raise ValueError("Invalid account number or PIN")


def menu():
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    return choice


# List to store all accounts
accounts = [
    BankAccount("123456", "1111", 5000),
    BankAccount("789012", "2222", 10000)
]

# Login
input_account = input("Enter account number: ")
input_pin = input("Enter PIN: ")

try:
    account = login(accounts, input_account, input_pin)
except ValueError as e:
    print(e)
    exit()

# Main menu loop
while True:
    choice = menu()
    if choice == 1:
        print(account.check_balance())
    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        print(account.deposit(amount))
    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        print(account.withdraw(amount))
    elif choice == 4:
        print("Thank you for using the Bank Management System!")
        break
    else:
        print("Invalid choice! Please try again.")
