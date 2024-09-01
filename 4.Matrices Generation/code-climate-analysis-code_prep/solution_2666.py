
rangenumber=int(input("Enter an Nth Number:"))
c = 0
letest = 0
num = 1
while c != rangenumber:
  num1 = num
  sqr = num1 * num1
  flag = 0
  while num1>0:
    if num1%10 != sqr%10:
      flag = -1
      break
    num1 = num1 // 10
    sqr = sqr // 10

  if flag==0:
    c+=1
    letest = num

  num = num + 1
print(rangenumber,"th Automorphic number is ",letest)