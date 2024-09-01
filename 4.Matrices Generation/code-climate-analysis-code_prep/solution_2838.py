
arr=[]
arr2=[]
size = int(input("Enter the size of the 1st array: "))
size2 = int(input("Enter the size of the 2nd array: "))

print("Enter the Element of the 1st array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)

print("Enter the Element of the 2nd array:")
for i in range(0,size2):
  num2 = int(input())
  arr2.append(num2)

count=0
for i in range(0, size):
  for j in range(0, size2):
    if arr[i] == arr2[j]:
      count+=1

if count==size2:
  print("Array two is a subset of array one.")
else:
  print("Array two is not a subset of array one.")