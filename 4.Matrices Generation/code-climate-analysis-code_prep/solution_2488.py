
rangenumber=int(input("Enter a Nth Number:"))
c = 0
letest = 0
num = 1
while c != rangenumber:
  one_c = 0
  num1 = num
  while num1 != 0:
    if num1 % 2 == 1:
      one_c += 1
    num1 //= 2
  if one_c % 2 == 0:
      c+=1
      letest = num

  num = num + 1
print(rangenumber,"th Evil number is ",latest)