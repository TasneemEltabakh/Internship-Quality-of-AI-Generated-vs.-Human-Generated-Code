

import math
PI=3.14
r=int(input("Enter the radius of the cone:"))
h=int(input("Enter the height of the cone:"))
surface_area=(PI*r)*(r+math.sqrt(math.pow(h,2)+math.pow(r,2)))
volume=PI*math.pow(r,2)*(h/3.0)
print("Surface Area of the cone= ",surface_area)
print("Volume of the cone = ",volume)
