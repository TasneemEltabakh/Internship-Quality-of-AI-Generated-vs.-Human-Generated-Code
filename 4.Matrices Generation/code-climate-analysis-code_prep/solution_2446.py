

'''Write
a Python programto count the number of digits in an integer. or

 Write a programtocount the
number of digits in an integer using
Python '''

n=int(input("Enter a number:"))
count=0
while n>0:
 n=int(n/10)
 count+=1
print("The number of digits in the number is", count)


