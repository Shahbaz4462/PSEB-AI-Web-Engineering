# PSEB AI Web Engineering - Loops, Conditions & Collections
# Muhammad Shahbaz - IUB (SE 4M)
# Q2: Long city names (more than 6 letters)

cities = ["Lahore", "Multan", "Karachi", "Quetta", "Peshawar", "Bahawalpur"]

for city in cities:
    if len(city) > 6:
        print(city)
