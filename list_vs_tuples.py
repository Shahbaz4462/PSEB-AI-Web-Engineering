# PSEB AI Web Engineering
# Topic: List vs Tuple
# Muhammad Shahbaz - IUB (SE 4M)

# List -> changeable (mutable), written with [ ]
fruits_list = ["apple", "banana", "mango"]
fruits_list.append("orange")
fruits_list[0] = "green apple"
print("List:", fruits_list)

# Tuple -> not changeable (immutable), written with ( )
fruits_tuple = ("apple", "banana", "mango")
print("Tuple:", fruits_tuple)
print("Tuple first item:", fruits_tuple[0])
print("Banana count:", fruits_tuple.count("banana"))
print("Mango index:", fruits_tuple.index("mango"))

# fruits_tuple[0] = "orange"   # this line gives error, tuple cannot change

# --- List of tuples (student name + marks) ---
students = [("Ali", 85), ("Sara", 92), ("Usman", 74)]
for name, marks in students:
    print(name, "got", marks, "marks")

# --- Second highest number in a list ---
numbers = [12, 45, 23, 67, 34, 67]
unique_numbers = list(set(numbers))
unique_numbers.sort()
print("Second highest:", unique_numbers[-2])
