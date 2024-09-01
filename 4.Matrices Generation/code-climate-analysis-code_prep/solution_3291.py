
import math
print("Enter a range:")
range1=int(input())
range2=int(input())
print("Sunny numbers between ",range1," and ",range2," are: ")
for i in range(range1,range2+1):
  root = math.sqrt(i+ 1)
  if int(root)==root:
    print(i,end=" ")