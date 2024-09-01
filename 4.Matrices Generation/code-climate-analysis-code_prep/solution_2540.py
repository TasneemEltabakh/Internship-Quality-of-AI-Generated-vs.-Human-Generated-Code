
print("Enter two number to find G.C.D")
num1=int(input())
num2=int(input())
while(num1!=num2):
 if (num1 > num2):
   num1 = num1 - num2
 else:
   num2= num2 - num1

print("G.C.D is",num1)
