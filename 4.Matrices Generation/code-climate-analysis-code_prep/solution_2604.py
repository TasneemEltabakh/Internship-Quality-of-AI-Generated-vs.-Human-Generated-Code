
import math
print("Enter the range of number(Limit):")
n=int(input())
i=2
sum=1
while(i<=n):
  if(i%2==0):
    sum+=pow(i,2)
  else:
    sum-=pow(i,2)
  i+=1
print("The sum of the series = ",sum)