# PSEB AI Web Engineering - Conditions Task 05
# Topic: Check a letter - vowel or consonant
# Muhammad Shahbaz - IUB (SE 4M)

letter = input("Enter a single letter: ").lower()

if len(letter) != 1 or not letter.isalpha():
    print("Please enter only one alphabet letter")
elif letter in "aeiou":
    print(letter, "is a vowel")
else:
    print(letter, "is a consonant")
