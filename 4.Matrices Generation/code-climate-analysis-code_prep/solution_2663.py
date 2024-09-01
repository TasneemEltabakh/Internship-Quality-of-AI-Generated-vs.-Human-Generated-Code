

'''Write
a Python programto check whether a given number is a strong number or
not. or

Write a programtocheck whether
a given number is a strong number or not
using Python '''

num=int(input("Enter a number:"))
num2=num
sum=0
while(num!=0):
 fact=1
 rem=num%10
 num=int(num/10)
 for i in range(1,rem+1):
   fact=fact*i
 sum=sum+fact
if sum==num2:
 print("It is a Strong Number")
else:
 print("It is not a Strong Number")


