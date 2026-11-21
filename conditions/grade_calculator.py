# PSEB AI Web Engineering - Conditions Task 03
# Topic: Grade calculator using elif ladder
# Muhammad Shahbaz - IUB (SE 4M)

percentage = float(input("Enter your percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid percentage!")
elif percentage >= 80:
    print("Grade: A+")
elif percentage >= 70:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: F (Fail)")
