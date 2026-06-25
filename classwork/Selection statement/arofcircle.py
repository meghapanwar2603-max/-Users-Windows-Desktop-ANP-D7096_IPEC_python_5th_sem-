import math

# Input radius
radius = float(input("Enter the radius of the circle: "))

# Validation
if radius <= 0:
    print("Invalid radius! Radius must be greater than 0.")
else:
    area = 3.14* radius * radius
    print("Area of the circle =", area)
