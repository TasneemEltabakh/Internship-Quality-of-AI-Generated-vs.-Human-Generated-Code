
arr=[]
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = float(input())
  arr.append(num)
sum=0.0
for j in range(0,size):
      sum+= arr[j]
print("sum of ",size," number : ",sum)