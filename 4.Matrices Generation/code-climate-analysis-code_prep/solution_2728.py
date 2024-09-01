
size=int(input("Enter the size of the array:"));
arr=[]
print("Enter the element of the array:");
for i in range(0,size):
  num = int(input())
  arr.append(num)

print("Before Sorting Array Element are: ",arr)


for out in range(1,size-1):
  temp = arr[out]
  inn=out
  while inn > 0 and arr[inn -1] >= temp:
    arr[inn] = arr[inn -1]
    inn-=1
  arr[inn] = temp

print("\nAfter Sorting Array Element are: ",arr)

