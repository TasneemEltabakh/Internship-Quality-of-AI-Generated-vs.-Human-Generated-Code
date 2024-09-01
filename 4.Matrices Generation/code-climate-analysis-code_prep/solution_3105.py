
import math
num=int(input("Enter a number:"))
num1 = num
c=0
while num1!=0:
  num1 //= 10
  c+=1
num1=num
sum=0
while num1!=0:
  rem = num1 % 10
  sum += math.pow(rem, c)
  num1 //= 10
  c-=1
if sum==num:
  print("It is a Disarium Number.")
else:
 print("It is Not a Disarium Number.")