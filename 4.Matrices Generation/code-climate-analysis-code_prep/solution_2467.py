
import math
print("Enter a range:")
range1=int(input())
range2=int(input())
print("Disarium numbers between ",range1," and ",range2," are: ")
for i in range(range1,range2+1):
  num =i
  c = 0
  while num != 0:
    num //= 10
    c += 1
  num = i
  sum = 0
  while num != 0:
    rem = num % 10
    sum += math.pow(rem, c)
    num //= 10
    c -= 1
  if sum == i:
    print(i,end=" ")