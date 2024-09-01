

'''Write a Python
programtoFind the 2nd largest digit in a given number. orWrite a
programtoFind 2nd largest digit in a given number using Python '''

print("Enter the Number :")
num=int(input())
Largest=0
Sec_Largest=0
while num > 0:
  reminder=num%10
  if Largest<reminder:
    Sec_Largest = Largest
    Largest = reminder
  elif reminder >= Sec_Largest:
    Sec_Largest = reminder
  num =num // 10

print("The Second Largest Digit is :", Sec_Largest)
