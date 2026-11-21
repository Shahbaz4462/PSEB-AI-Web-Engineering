# PSEB AI Web Engineering - Conditions Task 04
# Topic: Voting eligibility - age must be 18 or more
# Muhammad Shahbaz - IUB (SE 4M)

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age!")
elif age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote yet")
    print("You can vote after", 18 - age, "year(s)")
