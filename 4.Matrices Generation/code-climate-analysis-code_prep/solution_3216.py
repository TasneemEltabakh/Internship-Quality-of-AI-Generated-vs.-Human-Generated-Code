
print("Enter the range of number(Limit):")
n=int(input())
i=1
sum=0.0
while(i<=n):
  if(i%2==0):
    sum-=i/(i+1)
  else:
    sum+=i/(i+1)
  i+=1
print("The sum of the series = ",sum)