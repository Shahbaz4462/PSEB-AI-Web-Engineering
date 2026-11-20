# PSEB AI Web Engineering - Day 04
# Topic: Variables and Data Types
# Muhammad Shahbaz - IUB (SE 4M)

# --- Variables ---
name = "Muhammad Shahbaz"
roll_no = "F23BSEEN1M01186"
semester = 7
cgpa = 3.42
is_student = True

print("Name:", name)
print("Roll No:", roll_no)
print("Semester:", semester)
print("CGPA:", cgpa)
print("Is Student:", is_student)

# --- Checking data types ---
print(type(name))        # str
print(type(semester))    # int
print(type(cgpa))        # float
print(type(is_student))  # bool

# --- Changing a variable value ---
city = "Bahawalpur"
print("City:", city)
city = "Lahore"
print("New City:", city)

# --- Taking input from user ---
user_name = input("Enter your name: ")
print("Welcome,", user_name)
