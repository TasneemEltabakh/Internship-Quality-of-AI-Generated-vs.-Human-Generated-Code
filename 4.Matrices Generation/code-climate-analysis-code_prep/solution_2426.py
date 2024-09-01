
arr=[]
temp=0
pos=0
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)
print("Enter the search element:")
ele=int(input())
print("Array elements are:")
for i in range(0,size):
  print(arr[i],end=" ")
for i in range(0,size):
  if arr[i] == ele:
      temp = 1
if temp==1:
  print("\nElement found....")
else:
  print("\nElement not found....")