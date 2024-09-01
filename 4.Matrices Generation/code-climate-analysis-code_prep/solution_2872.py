
print("Enter a range:")
range1=int(input())
range2=int(input())
print("Spy numbers between ",range1," and ",range2," are: ")
for i in range(range1,range2+1):
  num=i
  sum = 0
  mult = 1
  while num != 0:
    rem = num % 10
    sum += rem
    mult *= rem
    num //= 10

  if sum == mult:
    print(i,end=" ")