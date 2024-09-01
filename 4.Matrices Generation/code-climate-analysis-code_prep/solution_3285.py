
import math
print("Enter the range of number:")
n=int(input())
sum=0.0
fact=1
for i in range(1,n+1):
  sum += pow(i, i) / i
print("The sum of the series = ",sum)