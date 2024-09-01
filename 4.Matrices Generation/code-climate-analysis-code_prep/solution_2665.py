
print("Enter the range of number:")
n=int(input())
print("Enter the value of x:")
x=int(input())
sum=1.0
i=1
while(i<=n):
  fact=1
  for j in range(1,i+1):
    fact*=j
    sum+=pow(x,i)/fact
  i+=1
print("The sum of the series = ",sum)