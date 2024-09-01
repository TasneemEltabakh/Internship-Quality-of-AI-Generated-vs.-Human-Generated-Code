
import math
print("Enter the range of number(Limit):")
n=int(input())
i=5
sum=0
while(i<=n):
  sum+=pow(i,2)
  i+=5
print("The sum of the series = ",sum)