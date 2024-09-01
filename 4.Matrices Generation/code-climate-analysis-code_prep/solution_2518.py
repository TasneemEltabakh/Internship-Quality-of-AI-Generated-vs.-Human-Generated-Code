
size=int(input("Enter the size of the array:"));
arr=[]
print("Enter the element of the array:");
for i in range(0,size):
  num = int(input())
  arr.append(num)

print("Before Sorting Array Elements are: ",arr)
for out in range(0,size-1):
  min = out
  for inn in range(out+1, size):
    if arr[inn] < arr[min]:
      min = inn
      temp=arr[out]
      arr[out]=arr[min]
      arr[min]=temp

print("\nAfter Sorting Array Elements are: ",arr)

