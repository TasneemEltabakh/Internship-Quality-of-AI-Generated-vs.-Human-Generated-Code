
print("Enter the range of number(Limit):")
n=int(input())
i=1
a=0
b=1
c=a+b
while(i<=n):
  print(c,end=" ")
  c = a + b
  a = b
  b = c
  i+=1