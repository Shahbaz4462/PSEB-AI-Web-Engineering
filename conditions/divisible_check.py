# PSEB AI Web Engineering - Conditions Task 06
# Topic: Check if a number is divisible by 5 and 11 both
# Muhammad Shahbaz - IUB (SE 4M)

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print(num, "is divisible by both 5 and 11")
elif num % 5 == 0:
    print(num, "is divisible by 5 only")
elif num % 11 == 0:
    print(num, "is divisible by 11 only")
else:
    print(num, "is not divisible by 5 or 11")
