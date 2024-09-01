
size=int(input("Enter the size of the array:"));
arr=[]
print("Enter the element of the array:");
for i in range(0,size):
  num = int(input())
  arr.append(num)

print("Before Sorting Array Element are: ",arr)

for out in range(size-1,0,-1):
  for inn in range(out):
    if arr[inn] > arr[inn +1]:
      temp=arr[inn]
      arr[inn]=arr[inn +1]
      arr[inn +1]=temp

print("\nAfter Sorting Array Element are: ",arr)