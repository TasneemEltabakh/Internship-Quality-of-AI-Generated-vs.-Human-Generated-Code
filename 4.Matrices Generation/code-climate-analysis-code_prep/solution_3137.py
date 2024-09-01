
import math
num=int(input("Enter a number:"))
flag=0
for i in range(0,num+1):
  if i*(i+1)==num:
    flag=1
    break
if flag==1:
  print("It is a Pronic Number.")
else:
 print("It is Not a Pronic Number.")