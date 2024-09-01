
import sys
arr=[]
freq=[]
max=-sys.maxsize-1
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)
for i in range(0, size):
  if(arr[i]>=max):
    max=arr[i]
for i in range(0,max+1):
  freq.append(0)

for i in range(0, size):
  freq[arr[i]]+=1
count=0
for i in range(0, max+1):
  if freq[i] == 1:
    count+=1
print("Numbers of distinct elements are ",count)