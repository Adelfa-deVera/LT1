# de Vera, Christen Iris C.
# 8 - Adelfa
# Lt1, Part 2 - Circular Garden
# September 19, 2026

import math

radius = float(input("Enter the radius of the garden: "))
A = math.pi * math.pow(radius, 2)
C = 2 * math.pi * radius
sqrt = math.sqrt(A)
lowsqrt = math.floor(A)
highsqrt = math.ceil(A)

print(f"Area of the garden: {A:.2f} square meters")
print(f"Circumference of the garden: {C:.2f} meters")
print(f"Square root of the area: {sqrt:.2f}")
print(f"Area rounded down: {lowsqrt} square meters")
print(f"Area rounded up: {highsqrt} square meters")