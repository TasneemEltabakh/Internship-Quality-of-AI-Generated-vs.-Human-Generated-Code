

'''Write
a Python programto find out all palindrome numbers present within a
given range. orWrite a programtofind out all
palindrome numbers present within a given range using Python '''


print("Enter a range in numbers(num1-num2):")
range1=int(input())
range2=int(input())
print(range1," to ",range2," palindrome numbers are ");
for i in range(range1,range2+1):
 num1=i
 num2=0
 while(num1!=0):
   rem=num1%10
   num1=int(num1/10)
   num2=num2*10+rem
 if(i==num2):
   print(i,end=" ")


