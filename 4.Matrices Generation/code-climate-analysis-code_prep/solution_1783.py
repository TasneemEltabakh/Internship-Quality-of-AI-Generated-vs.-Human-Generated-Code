# Python code to demonstrate
# to replace nan values
# with an average of columns

import numpy as np

# Initialising numpy array
ini_array = np.array([[1.3, 2.5, 3.6, np.nan],
[2.6, 3.3, np.nan, 5.5],
[2.1, 3.2, 5.4, 6.5]])

# printing initial array
print ("initial array", ini_array)

# column mean
col_mean = np.nanmean(ini_array, axis = 0)

# printing column mean
print ("columns mean", str(col_mean))

# find indices where nan value is present
inds = np.where(np.isnan(ini_array))

# replace inds with avg of column
ini_array[inds] = np.take(col_mean, inds[1])

# printing final array
print ("final array", ini_array)