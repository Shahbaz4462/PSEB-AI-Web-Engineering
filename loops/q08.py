# PSEB AI Web Engineering - Loops, Conditions & Collections
# Muhammad Shahbaz - IUB (SE 4M)
# Q8: Unique values and the most frequent number

nums = [3, 5, 3, 8, 5, 3, 9]

counts = {}
for num in nums:
    if num in counts:
        counts[num] = counts[num] + 1
    else:
        counts[num] = 1

unique = []
for num in counts:
    unique.append(num)
print("Unique:", unique)

most_frequent = unique[0]
for num in counts:
    if counts[num] > counts[most_frequent]:
        most_frequent = num

print("Most frequent:", most_frequent, "(" + str(counts[most_frequent]) + " times)")
