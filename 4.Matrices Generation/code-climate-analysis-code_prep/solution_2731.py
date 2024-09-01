
print("Enter a range:")
range1=int(input())
range2=int(input())
print("Trimorphic numbers between ",range1," and ",range2," are: ")
for i in range(range1,range2+1):
  flag = 0
  num=i
  cube_power = num * num * num
  while num != 0:
    if num % 10 != cube_power % 10:
      flag = 1
      break
    num //= 10
    cube_power //= 10
  if flag == 0:
    print(i,end=" ")