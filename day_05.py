# PSEB AI Web Engineering - Day 05
# Topic: Numbers and String Operations
# Muhammad Shahbaz - IUB (SE 4M)

# --- Number operations ---
a = 20
b = 6
print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b)
print("Floor Divide:", a // b)
print("Remainder:", a % b)
print("Power:", a ** 2)

# --- String operations ---
course = "AI Web Engineering"
print(course.upper())
print(course.lower())
print(course.replace("AI", "Python"))
print("Length:", len(course))
print(course[0:2])        # slicing -> AI
print(course.split())     # ['AI', 'Web', 'Engineering']

# --- f-string ---
marks = 85
print(f"I got {marks} marks in {course}")

# --- Even or Odd check ---
num = 17
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
