import math

r = float(input("Enter the radius of circle: "))
circumference = 2 * math.pi * r
area = math.pi * pow(r, 2)
print(f"The area is: {round(area, 2)} unit")
print(f"The circumference is: {round(circumference, 2)} sq. unit")

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The length of hypotenuse is: {round(hypotenuse, 2)} unit")
