


'''Write
a Python programto check whether a given number is An Automorphic
number or not. orWrite a programtocheck whether
a given number is An Automorphic number or not using Python '''

num=int(input("Enter a number:"))
sqr=num*num
flag=0
while num!=0:
  if(num%10 != sqr%10):
   flag=-1
   break
  num=int(num/10)
  sqr=int(sqr/10)
if(flag==0):
 print("It is an Automorphic Number")
else:
 print("It is not an Automorphic Number")

