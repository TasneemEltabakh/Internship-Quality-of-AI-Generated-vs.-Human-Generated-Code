
rangenumber=int(input("Enter a Nth Number:"))
c = 0
letest = 0
num = 1
while c != rangenumber:
  num1 = num
  sum = 0
  for i in range(1, num1):
    if num1 % i == 0:
      sum = sum + i
  if sum>num:
    c+=1
    letest = num

  num = num + 1
print(rangenumber,"th Abundant number is ",letest)