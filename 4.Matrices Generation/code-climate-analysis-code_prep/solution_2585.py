
arr=[]
cout=0
sum=0
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)
print("After reversing array is :");
for i in range(size-1,-1,-1):
  print(arr[i],end=" ")