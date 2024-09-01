
print("Enter a range:")
range1=int(input())
range2=int(input())
print("Strong numbers between ",range1," and ",range2," are: ")
for i in range(range1,range2+1):
  num2=i
  num1=i
  sum=0
  while(num1!=0):
    fact=1
    rem=num1%10
    num1=int(num1/10)
    for j in range(1,rem+1):
      fact=fact*j
    sum=sum+fact
  if sum==num2:
print(i,end=" ")
