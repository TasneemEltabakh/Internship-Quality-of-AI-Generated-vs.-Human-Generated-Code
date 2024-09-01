
import sys
arr=[]
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)
min=sys.maxsize
for j in range(0,size):
  if (arr[j] <= min):
    min = arr[j]

print("The smallest element of array: ",min)