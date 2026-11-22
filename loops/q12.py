# PSEB AI Web Engineering - Loops, Conditions & Collections
# Muhammad Shahbaz - IUB (SE 4M)
# Q12: Password checker (bonus)

while True:
    password = input("Enter a password: ")

    has_digit = False
    has_capital = False

    for ch in password:
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_capital = True

    if len(password) < 8:
        print("Weak: password is too short (at least 8 characters)")
    elif has_digit == False:
        print("Weak: password must have at least one digit")
    elif has_capital == False:
        print("Weak: password must have at least one capital letter")
    else:
        print("Password accepted")
        break
