
import math
rangenumber=int(input("Enter a Nth Number:"))
c = 0
letest = 0
num = 1
while c != rangenumber:
  num1 = num
  sqr = math.sqrt(num1)
  if sqr-math.floor(sqr)==0:
    c+=1
    letest = num

  num = num + 1
print(rangenumber,"th Perfect Square number is ",latest)