
def merge(arr,first,mid,last):

  n1 = (mid - first + 1)
  n2 = (last - mid)
  Left=[0]*n1
  Right=[0]*n2
  for i in range(n1):
    Left[i] = arr[i + first]
  for j in range(n2):
    Right[j] = arr[mid + j + 1];

  k = first
  i = 0
  j = 0

  while i < n1 and j < n2:
    if Left[i] <= Right[j]:
      arr[k]=Left[i]
      i+=1
    else:
      arr[k]=Right[j]
      j+=1
    k+=1

  while i < n1:
    arr[k] = Left[i]
    i +=1
    k +=1
  while j < n2 :
    arr[k] = Right[j]
    j +=1
    k +=1

def mergesort(arr,first,last):
  if(first<last):
    mid =first + (last - first)// 2
    mergesort(arr, first, mid)
    mergesort(arr, mid + 1, last)
    merge(arr, first, mid, last)

size=int(input("Enter the size of the array:"))
arr=[]
print("Enter the element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)

print("Before Sorting Array Element are: ",arr)

mergesort(arr,0,size-1)

print("\nAfter Sorting Array Element are: ",arr)