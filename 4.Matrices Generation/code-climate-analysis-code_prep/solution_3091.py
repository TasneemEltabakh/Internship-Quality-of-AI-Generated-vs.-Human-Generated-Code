

'''Write a Python
programtofind out all Harshad numbers present within a given range.
orWrite a programtofind out all Harshad numbers present
within a given range using Python '''


print("Enter a range:")
range1=int(input())
range2=int(input())
print("Harshad numbers between ",range1," and ",range2," are: ")
for i in range(range1,range2+1):
  num2=i
  num=i
  sum=0
  while num!=0:
    rem=num%10
    num=int(num/10)
    sum=sum+rem
  if(num2%sum==0):
    print(i,end=" ")
