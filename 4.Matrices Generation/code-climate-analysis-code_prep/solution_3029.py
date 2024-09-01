
n=int(input("Enter the n value:"))
fact=1
for i in range(1,n+1):
  fact*=i
result=1.0/fact
print("1/n!= ",result)
