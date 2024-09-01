
arr=[]
cout=0
sum=0
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)
for j in range(0, size):
  if ((j+1) % 2 == 1):
    sum += arr[j]
    cout+=1
avg = (sum / cout)
print("Average of Numbers in array at odd position is ", avg)