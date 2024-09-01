
print("Enter the range of number:")
n=int(input())
print("Enter the value of x:")
x=int(input())
sum=0
i=1
while(i<=n):
  for j in range(1,i+1):
    sum+=j
  i+=1
print("The sum of the series = ",sum)