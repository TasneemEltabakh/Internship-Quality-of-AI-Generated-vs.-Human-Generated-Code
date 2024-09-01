# importing the modules
import numpy as np

# creating the array
arr = np.array([23, 12, 1, 3, 4, 5, 6])
print("The Original Array Content")
print(arr)

# value of k
k = 4

# sorting the array
arr1 = np.sort(arr)

# k smallest number of array
print(k, "smallest elements of the array")
print(arr1[:k])