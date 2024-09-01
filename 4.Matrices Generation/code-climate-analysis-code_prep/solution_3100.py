


'''Write
a Python programto check whether a given number is an Abundant number
or not. orWrite a programtocheck whether
a given number is an Abundant number or not
using Python '''



num=int(input("Enter a number:"))
sum=0
for i in range(1,num):
 if(num%i==0):
   sum=sum+i
if sum>num:
 print("It is an Abundant Number")
else:

 print("It is not an Abundant Number")


