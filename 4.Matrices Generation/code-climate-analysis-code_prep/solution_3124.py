
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
  if arr[i]>=max:
    max=arr[i]
for i in range(0,max+1):
  freq.append(0)
for i in range(0, size):
  freq[arr[i]]+=1
list_oc=9999
list_v=9999
for i in range(0, size):
  if freq[arr[i]] < list_oc:
    list_oc = freq[arr[i]]
    list_v = arr[i]
print("The List occurring Number ",list_v," occurs ",list_oc," times.")