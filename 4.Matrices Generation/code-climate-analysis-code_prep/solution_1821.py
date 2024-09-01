# Importing Numpy module
import numpy as np

# Creating a 1-D Numpy array
n_arr = np.array([75.42436315, 42.48558583, 60.32924763])
print("Given array:")
print(n_arr)

print("\nReplace all elements of array which are greater than 50. to 15.50")
n_arr[n_arr > 50.] = 15.50

print("New array :\n")
print(n_arr)