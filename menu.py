def menu():
    print("\n--- Welcome to Your Bank System ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    try:
        choice = int(input("Please select an option: "))
        return choice
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")
        return 0
