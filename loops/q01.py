# PSEB AI Web Engineering - Loops, Conditions & Collections
# Muhammad Shahbaz - IUB (SE 4M)
# Q1: Pass or fail list

marks = [78, 45, 92, 33, 67, 88]
passed = 0

for mark in marks:
    if mark >= 40:
        print(mark, "Pass")
        passed = passed + 1
    else:
        print(mark, "Fail")

print("Passed:", passed)
