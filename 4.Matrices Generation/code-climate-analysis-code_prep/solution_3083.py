


'''Write
a Python programto check whether a given number is a Harshad number or
not. orWrite a programtocheck whether
a given number is a Harshad number or not
using Python '''



num=int(input("Enter a number:"))
num2=num
sum=0
while num!=0:
 rem=num%10
 num=int(num/10)
 sum=sum+rem
if(num2%sum==0):
 print("It is a Harshad Number")
else:
print("It is not a Harshad Number")
