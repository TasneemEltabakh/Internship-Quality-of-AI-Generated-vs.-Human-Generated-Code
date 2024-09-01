
arr=[]
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)
arr.sort()
j=0
#Remove duplicate element
for i in range(0, size-1):
  if arr[i] != arr[i + 1]:
    arr[j]=arr[i]
    j+=1
arr[j] = arr[size - 1]
j+=1
print("After removing duplicate element array is")
for i in range(0, j):
  print(arr[i],end=" ")