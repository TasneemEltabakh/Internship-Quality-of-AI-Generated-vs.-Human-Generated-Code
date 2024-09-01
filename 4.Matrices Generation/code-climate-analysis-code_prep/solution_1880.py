# import library
import numpy as np

# create numpy 1d-array
array1 = np.array([0, 1, 2])
array2 = np.array([3, 4, 5])

# pearson product-moment correlation
# coefficients of the arrays
rslt = np.corrcoef(array1, array2)

print(rslt)