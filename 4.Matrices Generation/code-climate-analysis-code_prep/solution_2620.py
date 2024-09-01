

'''Write a Python
programtoadd find the Smallest digit in a number. orWrite a
programtoadd find the Smallest digit in a number using Python '''

print("Enter the Number :")
num=int(input())
smallest=num%10
while num > 0:
  reminder = num % 10
  if smallest > reminder:
    smallest = reminder
  num =int(num / 10)
print("The Smallest Digit is ", smallest)
