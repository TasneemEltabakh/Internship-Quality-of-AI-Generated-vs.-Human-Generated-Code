
import math
print("Enter a range:")
range1=int(input())
range2=int(input())
print("Pronic numbers between ",range1," and ",range2," are: ")
for i in range(range1,range2+1):
  flag = 0
  for j in range(0, i + 1):
    if j * (j + 1) == i:
      flag = 1
      break
  if flag == 1:
    print(i,end=" ")