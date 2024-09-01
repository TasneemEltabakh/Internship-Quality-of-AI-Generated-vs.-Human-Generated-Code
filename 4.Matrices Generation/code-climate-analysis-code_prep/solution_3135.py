


'''Write
a Python programto check whether a given number is a perfect square
number or not. orWrite a programtocheck whether
a given number is a perfect square number or not using Python '''



import math
num=int(input("Enter a number:"))
sqr=math.sqrt(num)
if sqr-math.floor(sqr)==0:
 print("It is a Perfect Square")
else:
 print("It is not a Perfect Square")


