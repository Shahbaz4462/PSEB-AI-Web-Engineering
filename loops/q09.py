# PSEB AI Web Engineering - Loops, Conditions & Collections
# Muhammad Shahbaz - IUB (SE 4M)
# Q9: Student report card

students = [
    {"name": "Ali", "marks": [80, 75, 90]},
    {"name": "Sara", "marks": [95, 88, 92]},
    {"name": "Ahmed", "marks": [55, 62, 48]},
]

topper = ""
top_average = 0

for student in students:
    total = 0
    for mark in student["marks"]:
        total = total + mark
    average = total / len(student["marks"])

    if average >= 60:
        result = "Pass"
    else:
        result = "Fail"

    print(student["name"], format(average, ".2f"), result)

    if average > top_average:
        top_average = average
        topper = student["name"]

print("Topper:", topper)
