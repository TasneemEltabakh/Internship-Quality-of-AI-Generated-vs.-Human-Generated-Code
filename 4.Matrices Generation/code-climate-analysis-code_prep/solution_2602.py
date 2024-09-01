
import math
rangenumber=int(input("Enter a Nth Number:"))
c = 0
letest = 0
num = 1
while c != rangenumber:
  flag = 0
  for j in range(0, num + 1):
    if j * (j + 1) == num:
      flag = 1
      break
  if flag == 1:
      c+=1
      letest = num

  num = num + 1
print(rangenumber,"th Pronic number is ",letest)


