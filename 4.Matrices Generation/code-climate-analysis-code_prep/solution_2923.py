
arr=[]
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)
print("Enter the element:")
ele=int(input())
print("Enter the position:")
pos=int(input())
print("Before inserting array elements are:")
for i in range(0,size):
  print(arr[i],end=" ")
arr.insert(pos-1,ele)
print("\nAfter inserting array elements are:")
print(arr)