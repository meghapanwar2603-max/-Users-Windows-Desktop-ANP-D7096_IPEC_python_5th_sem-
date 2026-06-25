import math

# Input radius
radius = float(input("Enter the radius of the circle: "))

# Validation
if radius <= 0:
    print("Invalid radius! Radius must be greater than 0.")
else:
    area = math.pi * radius * radius
    print("Area of the circle =", round(area, 2))