
num=int(input("Enter a number:"))
sum=0
mult=1
while num!=0:
  rem = num % 10
  sum += rem
  mult *= rem
  num //= 10

if sum==mult:
  print("It is a spy Number.")
else:
 print("It is not a spy Number.")