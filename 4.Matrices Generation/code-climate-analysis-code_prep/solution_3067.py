


'num=int(input("Enter a number:"))
num2=num
sum=0
while(num!=0):
 rem=num%10
 num=int(num/10)
 sum=sum+rem*rem*rem
if sum==num2:
 print("It is an Armstrong Number")
else:
 print("It is not an Armstrong Number")



