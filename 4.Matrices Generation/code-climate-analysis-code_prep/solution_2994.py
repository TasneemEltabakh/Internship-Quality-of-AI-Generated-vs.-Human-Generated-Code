
rangenumber=int(input("Enter a Nth Number:"))
c = 0
letest = 0
num = 1
while c != rangenumber:
  sum = 0
  mult = 1
  num1=num
  while num1 != 0:
    rem = num1 % 10
    sum += rem
    mult *= rem
    num1 //= 10

  if sum == mult:
      c+=1
      letest = num

  num = num + 1
print(rangenumber,"th Spy number is ",letest)