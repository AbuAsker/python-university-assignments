# Improting math library
import math

# Getting the value of two angles and a side length from the user
A,B = eval(input("Enter two angles(A B): "))
a = eval(input("Enter the value of a side length a: "))

# Calculating the third angle value using A & B
C = 180 - A - B

#Calculating the area
Area = ((a**2) * math.sin(math.radians(B)) * math.sin(math.radians(C))) / (2 * math.sin(math.radians(A)))

#Printing the result
print("The Area of the tringle is", Area)
