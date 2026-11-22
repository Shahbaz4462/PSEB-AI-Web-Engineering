# PSEB AI Web Engineering - Loops, Conditions & Collections
# Muhammad Shahbaz - IUB (SE 4M)
# Q3: Highest and lowest price (loop only, no max/min)

prices = [450, 1200, 300, 980, 75]

highest = prices[0]
lowest = prices[0]

for price in prices:
    if price > highest:
        highest = price
    if price < lowest:
        lowest = price

print("Highest:", highest)
print("Lowest:", lowest)
