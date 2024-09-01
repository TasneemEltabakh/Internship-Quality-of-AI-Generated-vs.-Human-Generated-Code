
arr=[]
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)

search_elm=int(input("Enter the search element: "))
found=0

for i in range(size):
  if arr[i]==search_elm:
      found=1

if found==1:
    print("Search element is found.")
else:
    print("Search element is not found.")

