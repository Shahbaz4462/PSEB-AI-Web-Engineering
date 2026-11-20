# PSEB AI Web Engineering - Task
# Student Record: marks, percentage and grade
# Muhammad Shahbaz - IUB (SE 4M)

def get_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

record = {
    "name": "Muhammad Shahbaz",
    "roll_no": "F23BSEEN1M01186",
    "marks": [85, 78, 92, 88, 74]   # 5 subjects, each out of 100
}

total = sum(record["marks"])
percentage = total / len(record["marks"])

print("Name:", record["name"])
print("Roll No:", record["roll_no"])
print("Total Marks:", total, "/", len(record["marks"]) * 100)
print("Percentage:", percentage, "%")
print("Grade:", get_grade(percentage))
