
def partition(arr,first,last):
  i=first-1
  x=arr[last]
  for j in range(first,last):
    if(arr[j]<x):
      i+=1
      temp=arr[i]
      arr[i]=arr[j]
      arr[j]=temp
  i+=1
  temp=arr[i]
  arr[i]=arr[last]
  arr[last]=temp
  return i

def qsort(arr,first,last):
  if(first<last):
    mid=partition(arr,first,last)
    qsort(arr,first,mid-1)
    qsort(arr,mid+1,last)

size=int(input("Enter the size of the array:"))
arr=[]
print("Enter the element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)

print("Before Sorting Array Element are: ",arr)

qsort(arr,0,size-1)

print("\nAfter Sorting Array Element are: ",arr)