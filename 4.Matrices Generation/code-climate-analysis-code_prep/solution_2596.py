
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
most_oc=0
most_v=0
for i in range(0, size):
  if freq[arr[i]] > most_oc:
    most_oc = freq[arr[i]]
    most_v = arr[i]
print("The Most occurring Number ",most_v," occurs ",most_oc," times.")