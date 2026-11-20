# PSEB AI Web Engineering
# Topic: Dictionary
# Muhammad Shahbaz - IUB (SE 4M)

# --- Creating a dictionary ---
student = {
    "name": "Muhammad Shahbaz",
    "roll_no": "F23BSEEN1M01186",
    "semester": 7,
    "department": "Software Engineering"
}
print(student)
print("Name:", student["name"])

# --- Adding and updating ---
student["city"] = "Bahawalpur"
student["semester"] = 8
print("Updated:", student)

# --- Loop on dictionary ---
for key, value in student.items():
    print(key, "->", value)

# --- Inventory task ---
inventory = {"pen": 50, "notebook": 30, "bag": 12}
item = "notebook"
print(item, "quantity is", inventory.get(item, 0))
inventory["pen"] = inventory["pen"] - 5   # 5 pens sold
print("After sale:", inventory)
