# PSEB AI Web Engineering - Conditions Task 08
# Topic: Type of triangle from its three sides
# Muhammad Shahbaz - IUB (SE 4M)

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# first check: can these sides make a triangle at all?
if a + b <= c or a + c <= b or b + c <= a:
    print("These sides cannot make a triangle")
elif a == b == c:
    print("It is an Equilateral triangle (all sides equal)")
elif a == b or b == c or a == c:
    print("It is an Isosceles triangle (two sides equal)")
else:
    print("It is a Scalene triangle (all sides different)")
