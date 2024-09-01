
print("Enter the Nth value:")
rangenumber=int(input())
num = 1
c = 0
letest = 0
while (c != rangenumber):
   num2=num
   num1=num
   sum=0
   while(num1!=0):
    rem=num1%10
    num1=num1//10
    sum=sum+rem
   if(num2%sum==0):
     c+=1
     letest=num
   num = num + 1
print(rangenumber,"th Harshad number is ", letest);



