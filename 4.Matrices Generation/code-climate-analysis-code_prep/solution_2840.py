
import sys
arr=[]
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)
min=sys.maxsize
sec_min=sys.maxsize
for j in range(0,size):
  if (arr[j] <= min):
    sec_min=min
    min = arr[j]
  elif(arr[i] <= sec_min):
    sec_min = arr[j]
print("The 2nd smallest element of array: ",sec_min)