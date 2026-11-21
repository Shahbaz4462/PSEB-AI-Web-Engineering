# PSEB AI Web Engineering - Conditions Task 07
# Topic: Shopping discount using nested conditions
# Muhammad Shahbaz - IUB (SE 4M)

bill = float(input("Enter your total bill amount: Rs "))

if bill >= 5000:
    discount = bill * 20 / 100
    print("You got 20% discount")
elif bill >= 2000:
    discount = bill * 10 / 100
    print("You got 10% discount")
elif bill >= 1000:
    discount = bill * 5 / 100
    print("You got 5% discount")
else:
    discount = 0
    print("No discount - shop for Rs 1000 or more to get a discount")

print("Discount amount: Rs", discount)
print("Final bill: Rs", bill - discount)
