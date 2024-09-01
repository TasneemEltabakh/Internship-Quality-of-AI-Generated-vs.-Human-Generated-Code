
import math
print("Enter a range to find all prime numbers within that range:")
range1=int(input())
range2=int(input())
print("Prime numbers between ",range1," and ",range2," are: ")
for j in range(range1,range2+1):
  count=0 for i in range(2,int(math.sqrt(j))+1):
  if j%i==0:
   count+=1
if count==0:
print(j,end=" ")
