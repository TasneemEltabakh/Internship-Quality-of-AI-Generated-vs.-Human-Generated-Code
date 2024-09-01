
print("Enter a range:")
range1=int(input())
range2=int(input())
print("Happy numbers between ",range1," and ",range2," are: ")
for i in range(range1,range2+1):
  num=i
  sum=0
  while sum != 1 and sum != 4:
    sum = 0
    while num != 0:
      rem = num % 10
      sum += (rem * rem)
      num //= 10
    num = sum

  if sum == 1:
    print(i,end=" ")