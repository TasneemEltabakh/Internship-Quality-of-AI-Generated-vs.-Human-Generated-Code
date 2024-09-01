
import sys
arr=[]
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)
max=-sys.maxsize-1
sec_max=-sys.maxsize-1
for j in range(0,size):
  if (arr[j] >= max):
    sec_max=max
    max = arr[j]
  elif(arr[i] >= sec_max):
    sec_max = arr[j]

print("The 2nd largest element of array: ",sec_max)