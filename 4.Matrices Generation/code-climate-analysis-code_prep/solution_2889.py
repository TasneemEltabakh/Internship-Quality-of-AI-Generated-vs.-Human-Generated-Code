num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
num3=int(input("Enter 3rd number:"))

num1=num1+num2+num3
num2=num1-num2-num3
num3=num1-num2-num3
num1=num1-num2-num3

print("***After swapping***")
print("Number 1: ",num1)
print("Number 2: ",num2)
print("Number 3: ",num3)