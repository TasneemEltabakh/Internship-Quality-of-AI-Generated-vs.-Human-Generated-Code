
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

if count>=1:
  print("Arrays are not disjoint.")
else:
  print("Arrays are disjoint.")