
print("Enter the range of number(Limit):")
n=int(input())
a=10
b=5
i=1
while(i<=n):
  if(i%2==0):
    print(b,end=" ")
    b += 10
  else:
    print(a, end=" ")
    a += 50
  i+=1