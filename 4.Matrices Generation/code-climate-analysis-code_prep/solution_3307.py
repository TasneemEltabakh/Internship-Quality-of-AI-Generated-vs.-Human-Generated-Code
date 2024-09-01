
print("Enter the range of number:")
n=int(input())
print("Enter the value of x:")
x=int(input())
sum=1.0
i=1
while(i<=n):
  sum+=pow(x,i)/i
  i+=1
print("The sum of the series = ",sum)