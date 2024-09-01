
print("Enter a range:")
range1=int(input())
range2=int(input())
print("Magic numbers between ",range1," and ",range2," are: ")
for i in range(range1,range2+1):
  num3 = i
  num1 = i
  sum=0
# Sum of digit
  while num1 != 0:
    rem = num1 % 10
    sum += rem
    num1 //= 10
# Reverse of sum
  rev = 0
  num2 = sum
  while num2 != 0:
    rem2 = num2 % 10
    rev = rev * 10 + rem2
    num2 //= 10
  if sum*rev==num3:
    print(i,end=" ")