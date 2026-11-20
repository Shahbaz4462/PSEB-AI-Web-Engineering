# PSEB AI Web Engineering - Task
# Shopping Cart: add items, show bill
# Muhammad Shahbaz - IUB (SE 4M)

cart = []

def add_item(name, price, qty):
    cart.append({"name": name, "price": price, "qty": qty})

add_item("Notebook", 250, 2)
add_item("Pen", 50, 5)
add_item("Bag", 1800, 1)

total = 0
print("------ Bill ------")
for item in cart:
    bill = item["price"] * item["qty"]
    total = total + bill
    print(item["name"], "x", item["qty"], "= Rs", bill)
print("------------------")
print("Total Bill = Rs", total)
