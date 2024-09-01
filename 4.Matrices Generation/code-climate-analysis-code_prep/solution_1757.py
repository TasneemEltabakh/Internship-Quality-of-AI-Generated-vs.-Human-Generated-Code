import numpy as np


array1 = np.array([0, 1, 1])
array2 = np.array([2, 2, 1])

# Original array1
print(array1)

# Original array2
print(array2)

# Covariance matrix
print("\nCovariance matrix of the said arrays:\n",
np.cov(array1, array2))