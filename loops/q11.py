# PSEB AI Web Engineering - Loops, Conditions & Collections
# Muhammad Shahbaz - IUB (SE 4M)
# Q11: Simple ATM

balance = 10000
history = []

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        history.append("Deposited: " + str(amount))
        print("New balance:", balance)
    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance")
        else:
            balance = balance - amount
            history.append("Withdrew: " + str(amount))
            print("New balance:", balance)
    elif choice == "3":
        print("Balance:", balance)
    elif choice == "4":
        print("Transaction history:")
        for record in history:
            print(record)
        break
    else:
        print("Invalid choice")
