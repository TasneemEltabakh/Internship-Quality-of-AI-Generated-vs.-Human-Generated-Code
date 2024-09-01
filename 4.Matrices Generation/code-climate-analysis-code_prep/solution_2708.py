

'''Write
a Python programto check whether a given number is Friendly pair or
not. or

 Write a programtocheck whether
a given number is Friendly pair or not
using Python '''

print("Enter two numbers:")
num1=int(input())
num2=int(input())
sum1=0
sum2=0
for i in range(1,num1):
 if(num1%i==0):
   sum1=sum1+i
for i in range(1,num2):
 if(num2%i==0):
   sum2=sum2+i
if num1/num2==sum1/sum2:
 print("It is a Friendly Pair")
else:
 print("It is not a Friendly Pair")
