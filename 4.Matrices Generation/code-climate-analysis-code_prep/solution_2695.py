
arr=[]
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = int(input())
  arr.append(num)

search_elm=int(input("Enter the search element: "))
found=0

lowerBound = 0
upperBound = size-1

while lowerBound<=upperBound and not found:
  mid = (lowerBound + upperBound ) // 2
  if arr[mid]==search_elm:
    found=1
  else:
    if arr[mid] < search_elm:
      lowerBound = mid + 1
    else:
      upperBound = mid - 1
if found==1:
    print("Search element is found.")
else:
    print("Search element is not found.")


