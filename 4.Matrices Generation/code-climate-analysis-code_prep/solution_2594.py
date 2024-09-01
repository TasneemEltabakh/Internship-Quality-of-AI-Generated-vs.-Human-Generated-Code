
arr=[]
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)
temp=size
while(temp>=0):
  for k in range(0,temp-1,1):
    temp2=arr[k]
    arr[k]=arr[k+1]
    arr[k+1]=temp2
  temp-=1
print("After reversing array is :")
for i in range(0, size):
  print(arr[i],end=" ")