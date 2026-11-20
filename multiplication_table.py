# PSEB AI Web Engineering - Task
# Multiplication Table of a Number
# Muhammad Shahbaz - IUB (SE 4M)

number = int(input("Enter a number for its table: "))

print(f"--- Table of {number} ---")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
