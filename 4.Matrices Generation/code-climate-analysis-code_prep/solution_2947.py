
print("Enter the range of number(Limit):")
n=int(input())
i=1
a=0
b=6
k=10
p=11
while(i<=n):
  if (i % 2 == 0):
    print(b,end=" ")
    b += p
    p += 2
  else:
    print(a,end=" ")
    a += k
    k += 2
  i+=1