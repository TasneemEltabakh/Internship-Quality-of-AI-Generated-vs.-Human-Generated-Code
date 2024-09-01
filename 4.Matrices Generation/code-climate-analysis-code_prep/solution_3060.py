
print("Enter a range:")
range1=int(input())
range2=int(input())
print("Evil numbers between ",range1," and ",range2," are: ")
for i in range(range1,range2+1):
  one_c = 0
  num=i
  while num != 0:
    if num % 2 == 1:
      one_c += 1
    num //= 2
  if one_c % 2 == 0:
    print(i,end=" ")