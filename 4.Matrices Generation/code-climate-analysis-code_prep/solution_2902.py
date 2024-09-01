
import math
rangenumber=int(input("Enter a Nth Number:"))
c = 0
letest = 0
num = 1
while c != rangenumber:
  num1=num
  root = math.sqrt(num1 + 1)
  if int(root) == root:
      c+=1
      letest = num

  num = num + 1
print(rangenumber,"th Sunny number is ",letest)