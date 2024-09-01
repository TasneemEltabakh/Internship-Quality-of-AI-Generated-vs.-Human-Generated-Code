
arr=[]
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)
print("\nOdd numbers are:")
for i in range(0,size):
  if (arr[i] % 2 != 0):
    print(arr[i],end=" ")

print("\nEven numbers are:")
for i in range(0,size):
  if (arr[i] % 2 == 0):
    print(arr[i],end=" ")