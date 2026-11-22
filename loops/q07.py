# PSEB AI Web Engineering - Loops, Conditions & Collections
# Muhammad Shahbaz - IUB (SE 4M)
# Q7: Stock check with tuples

products = [("Laptop", 150000, 3), ("Mouse", 2500, 0),
            ("Keyboard", 5000, 12), ("Monitor", 45000, 2)]

total_value = 0

for name, price, quantity in products:
    if quantity == 0:
        print("Out of stock:", name)
    elif quantity >= 1 and quantity <= 4:
        print("Low stock:", name)
    total_value = total_value + (price * quantity)

print("Total stock value:", total_value)
