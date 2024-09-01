
num=int(input("Enter a number:"))
num2=0
while(num!=0):
 rem=num%10
 num=int(num/10)
 num2=num2*10+rem
print("The reverse of the number is",num2)
