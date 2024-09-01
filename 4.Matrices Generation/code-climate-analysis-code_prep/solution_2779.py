

'''Write a Python
programtofind out all Perfect numbers present within a given range.
orWrite a programtofind out all Perfect numbers present
within a given range using Python '''


print("Enter a range:")
range1=int(input())
range2=int(input())
print("Perfect numbers between ",range1," and ",range2," are: ")

for j in range(range1,range2+1):
  sum=0
  num=j
  for i in range(1,j):
    if(j%i==0):
      sum=sum+i
  if sum==num:
   print(j,end=" ")
