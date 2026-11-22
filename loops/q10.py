# PSEB AI Web Engineering - Loops, Conditions & Collections
# Muhammad Shahbaz - IUB (SE 4M)
# Q10: Shopping cart menu

cart = {}

while True:
    print("1. Add item")
    print("2. View cart")
    print("3. Checkout")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter item name: ")
        price = int(input("Enter price: "))
        cart[name] = price
        print(name, "added to cart")
    elif choice == "2":
        total = 0
        for name, price in cart.items():
            print(name, "-", price)
            total = total + price
        print("Total:", total)
    elif choice == "3":
        total = 0
        for price in cart.values():
            total = total + price
        if total > 5000:
            discount = total * 10 / 100
            total = total - discount
            print("10% discount applied")
        print("Total to pay:", total)
        break
    else:
        print("Invalid choice")
