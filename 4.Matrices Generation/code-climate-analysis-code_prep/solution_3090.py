
arr=[]
odd_type=0
even_type=0
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)
print("Array elements are:")
for i in range(0,size):
  print(arr[i],end=" ")
for i in range(0,size):
  if arr[i] % 2 == 0:
    even_type +=1
  else:
    odd_type +=1
if even_type==size:
    print("\nEven type array")
elif odd_type==size:
    print("\nodd type array")
else:
    print("\nMixed array")