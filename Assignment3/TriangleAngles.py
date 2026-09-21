import math

# Get the three points of the triangle from the user
x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle (x1, y1, x2, y2, x3, y3): "))

# Compute the length of each side using the distance formula
a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Compute the angles using the Law of Cosines
A = math.acos((a * a - b * b - c * c) / (-2 * b * c))
B = math.acos((b * b - a * a - c * c) / (-2 * a * c))
C = math.acos((c * c - b * b - a * a) / (-2 * a * b))

# Convert the angles from radians to degrees
A = math.degrees(A)
B = math.degrees(B)
C = math.degrees(C)

# Display the results
print(f"The three angles are {A:.1f} {B:.1f} {C:.1f}")
