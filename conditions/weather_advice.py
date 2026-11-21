# PSEB AI Web Engineering - Conditions Task 10
# Topic: Weather advice from temperature
# Muhammad Shahbaz - IUB (SE 4M)

temp = float(input("Enter today's temperature in Celsius: "))

if temp >= 40:
    print("Very hot! Drink lots of water and avoid going out at noon")
elif temp >= 30:
    print("Hot day - wear light clothes")
elif temp >= 20:
    print("Pleasant weather - good day for outdoor work")
elif temp >= 10:
    print("Cool weather - take a jacket with you")
else:
    print("Very cold! Wear warm clothes")
