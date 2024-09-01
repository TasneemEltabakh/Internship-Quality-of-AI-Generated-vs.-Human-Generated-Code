
n=int(input("Enter the n Value:"))
x=int(input("Enter the x value:"))
fact=1
for i in range(1,n+1):
  fact*=i
result=pow(x,n)/fact
print("Result(x^n/n!)= ",result)
