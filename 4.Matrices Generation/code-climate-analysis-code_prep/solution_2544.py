
size=int(input("Enter the size of the array:"));
arr=[]
print("Enter the element of the array:");
for i in range(0,size):
  num = int(input())
  arr.append(num)
print("Before Sorting Array Element are: ",arr)
low = 0
high= size-1
while low < high:
  for inn in range(low, high):
    if arr[inn] > arr[inn+1]:
      temp=arr[inn]
      arr[inn]=arr[inn+1]
      arr[inn+1]=temp
  high-=1
  for inn in range(high,low,-1):
    if arr[inn] < arr[inn-1]:
      temp=arr[inn]
      arr[inn]=arr[inn-1]
      arr[inn-1]=temp
low+=1
print("\nAfter Sorting Array Element are: ",arr)