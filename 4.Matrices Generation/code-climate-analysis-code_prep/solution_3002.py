


'''Write
a Python programto calculate the LCM of two numbers. or



 Write a programtocalculate the
LCM of two numbers using Python '''

print("Enter two number to find L.C.M:")
num1=int(input())
num2=int(input())
n1=num1
n2=num2
while(num1!=num2):
 if (num1 > num2):
   num1 = num1 - num2
 else:
   num2= num2 - num1
lcm=int((n1*n2)/num1)
print("L.C.M is",lcm)
