# Python code to demonstrate the
# use of numpy.nanmean
import numpy as np

# create 2d array with nan value.
arr = np.array([[20, 15, 37], [47, 13, np.nan]])

print("Shape of array is", arr.shape)

print("Mean of array without using nanmean function:",
np.mean(arr))

print("Using nanmean function:", np.nanmean(arr))