# Python Program illustrating
# numpy.var() method
import numpy as np

# 1D array
arr = [20, 2, 7, 1, 34]

print("arr : ", arr)
print("var of arr : ", np.var(arr))

print("\nvar of arr : ", np.var(arr, dtype = np.float32))
print("\nvar of arr : ", np.var(arr, dtype = np.float64))