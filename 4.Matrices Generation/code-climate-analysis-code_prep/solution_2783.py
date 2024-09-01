
rangenumber=int(input("Enter a Nth Number:"))
c = 0
letest = 0
num = 1
while c != rangenumber:
  num2 = num
  num1 = num
  sum = 0
  while num1 != 0:
    rem = num1 % 10
    num1 = num1 // 10
    sum = sum + rem * rem * rem
  if sum == num2:
    c+=1
    letest = num

  num = num + 1
print(rangenumber,"th Armstrong Number is ",latest)