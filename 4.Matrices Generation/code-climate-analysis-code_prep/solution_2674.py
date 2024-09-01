
rangenumber=int(input("Enter a Nth Number:"))
c = 0
letest = 0
num = 1
while c != rangenumber:
  flag = 0
  num1=num
  cube_power = num * num * num
  while num1 != 0:
    if num1 % 10 != cube_power % 10:
      flag = 1
      break
    num1 //= 10
    cube_power //= 10
  if flag == 0:
      c+=1
      letest = num

  num = num + 1
print(rangenumber,"th Trimorphic number is ",latest)