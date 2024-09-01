
arr=[]
temp=0
pos=0
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)
print("Enter the element to be deleted:")
ele=int(input())
print("Before deleting array elements are:")
for i in range(0,size):
  print(arr[i],end=" ")
for i in range(0,size):
  if arr[i] == ele:
      pos = i
      temp = 1

if temp==1:
  arr.pop(pos)
print("\nAfter deleting array elements are:")
print(arr)