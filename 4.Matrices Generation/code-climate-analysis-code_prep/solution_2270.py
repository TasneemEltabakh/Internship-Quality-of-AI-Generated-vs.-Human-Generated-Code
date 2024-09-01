# Import the numpy package
import numpy as np

# Create 3D-numpy array
# of 4 rows and 4 columns
arr = np.arange(3 * 4 * 4).reshape(3, 4, 4)

print("Original 3d array:\n",
arr)

# Create 2D diagonal array
diag_arr = np.diagonal(arr,
axis1 = 1,
axis2 = 2)

print("2d diagonal array:\n",
diag_arr)