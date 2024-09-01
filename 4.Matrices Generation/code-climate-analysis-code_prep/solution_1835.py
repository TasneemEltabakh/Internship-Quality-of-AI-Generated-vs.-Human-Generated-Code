# creating the array
arr = [4, 5, 5, 5, 3, 8]

# size of the list
size = len(arr)

# looping till length - 2
for i in range(size - 2):

# checking the conditions
if arr[i] == arr[i + 1] and arr[i + 1] == arr[i + 2]:

# printing the element as the
# conditions are satisfied
print(arr[i])