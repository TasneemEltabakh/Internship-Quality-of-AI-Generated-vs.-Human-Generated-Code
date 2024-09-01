# Importing Numpy module
import numpy as np

# Creating a 3X3 2-D Numpy array
arr = np.array([[10, 20, 30],
[40, 5, 66],
[70, 88, 94]])

print("Given Array :")
print(arr)

# Access the First and Last rows of array
res_arr = arr[[0,2]]
print("\nAccessed Rows :")
print(res_arr)