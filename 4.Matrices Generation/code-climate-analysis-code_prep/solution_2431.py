
i=0
octal=int(input("Enter Octal number:"))
Hex=['0']*50
decimal = 0
sem = 0
#Octal to decimal covert
while octal!=0:
  decimal=decimal+(octal%10)*pow(8,sem);
  sem+=1
  octal=octal// 10
#Decimal to Hexadecimal
while decimal!=0:
  rem=decimal%16
  #Convert Integer to char
  if rem<10:
    Hex[i]=chr(rem+48)#48 Ascii=0
    i+=1
  else:
    Hex[i]=chr(rem+55) #55 Ascii=7
    i+=1
  decimal//=16

print("Hexadecimal number is:")
for j in range(i-1,-1,-1):
  print(Hex[j],end="")