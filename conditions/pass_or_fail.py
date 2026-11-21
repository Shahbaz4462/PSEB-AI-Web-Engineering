# PSEB AI Web Engineering - Conditions Task 02
# Topic: Pass or Fail - marks 40 and above is Pass
# Muhammad Shahbaz - IUB (SE 4M)

marks = int(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Marks must be between 0 and 100")
elif marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
