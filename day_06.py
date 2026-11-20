# PSEB AI Web Engineering - Day 06
# Topic: Lists
# Muhammad Shahbaz - IUB (SE 4M)

# --- Creating a list ---
subjects = ["Python", "Web Engineering", "Database", "Operating System"]
print(subjects)
print("First subject:", subjects[0])
print("Last subject:", subjects[-1])

# --- Adding items ---
subjects.append("AI")
subjects.insert(1, "Data Structures")
print("After adding:", subjects)

# --- Removing items ---
subjects.remove("Database")
last = subjects.pop()
print("Removed last:", last)
print("After removing:", subjects)

# --- Slicing ---
print("First three:", subjects[0:3])

# --- Loop on list ---
for sub in subjects:
    print("Subject:", sub)

# --- Marks list task ---
marks = [78, 92, 64, 88, 71]
print("Total:", sum(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", sum(marks) / len(marks))
