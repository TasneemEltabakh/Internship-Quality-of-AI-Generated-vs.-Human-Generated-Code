sem=1
octal=0
print("Enter the Decimal Number:")
number=int(input())
while(number !=0):
   octal=octal+(number%8)*sem
   number=number//8
   sem=int(sem*10)

print("Octal Number is ",octal)

