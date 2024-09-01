
import math
print("Enter range:")
range1=int(input())
range2=int(input())
print("Perfect squares between ",range1," and ",range2," are: ")
for i in range(range1,range2+1):
  sqr=math.sqrt(i)
  if sqr-math.floor(sqr)==0:
    print(i,end=" ")
