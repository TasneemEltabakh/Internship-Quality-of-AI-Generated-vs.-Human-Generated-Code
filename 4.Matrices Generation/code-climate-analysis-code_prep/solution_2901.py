
import math
PI=3.14
r=int(input("Enter the radius of the cylinder:"))
h=int(input("Enter the height of the cylinder:"))
surface_area=(2*PI*r*h)+(2*PI*math.pow(r,2))
volume=PI*math.pow(r,2)*h
print("Surface Area of the cylinder = ",surface_area)

print("Volume of the cylinder = ",volume)