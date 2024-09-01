
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

arr.sort()
arr2.sort()

flag=1
if size != size2:
  flag=0
else:
  for i in range(0, size):
    if arr[i] != arr2[i]:
      flag=0

if flag==0:
  print("Not same....")
else:
  print("same....")