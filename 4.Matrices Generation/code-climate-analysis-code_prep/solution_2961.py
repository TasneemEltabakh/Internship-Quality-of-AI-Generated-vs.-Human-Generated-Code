

'''Write a Python
programtofind out all Automorphic numbers present within a given
range. orWrite a programtofind out all Automorphic numbers
present within a given range using Python '''

print("Enter a range:")
range1=int(input())
range2=int(input())
print("Perfect numbers between ",range1," and ",range2," are: ")
for i in range(range1,range2+1):
  num=i
  sqr=num*num
  flag=0
  while num!=0:
    if(num%10 != sqr%10):
      flag=-1
      break
    num=int(num/10)
    sqr=int(sqr/10)
  if(flag==0):
print(i,end=" ")
