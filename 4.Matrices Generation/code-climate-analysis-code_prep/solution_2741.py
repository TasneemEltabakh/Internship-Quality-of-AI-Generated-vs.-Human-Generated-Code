
num=int(input("Enter a number:"))
flag=0
cube_power=num*num*num
while num!=0:
  if num%10!=cube_power%10:
    flag=1
    break
  num//=10
  cube_power//=10
if flag==0:
  print("It is a Trimorphic Number.")
else:
 print("It is Not a Trimorphic Number.")