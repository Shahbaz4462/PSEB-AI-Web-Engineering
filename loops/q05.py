# PSEB AI Web Engineering - Loops, Conditions & Collections
# Muhammad Shahbaz - IUB (SE 4M)
# Q5: Grade report from a dictionary

students = {"Ali": 85, "Sara": 92, "Ahmed": 76, "Hina": 58, "Bilal": 64}

total = 0
count = 0

for name, marks in students.items():
    if marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "F"
    print(name, grade)
    total = total + marks
    count = count + 1

average = total / count
print("Average:", average)
