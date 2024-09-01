
import sys
arr=[]
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)
max=-sys.maxsize-1
for j in range(0,size):
  if (arr[j] >= max):
    max = arr[j]
print("The largest element of array: ",max)