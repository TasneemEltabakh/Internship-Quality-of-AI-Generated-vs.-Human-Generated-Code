
print("Enter a range")
range1=int(input())
range2=int(input())
print("Abundant numbers between ",range1," and ",range2," are: ")
for j in range(range1,range2+1):
  sum=0
  for i in range(1,j):
    if(j%i==0):
      sum=sum+i
  if sum>j:
   print(j,end=" ")
