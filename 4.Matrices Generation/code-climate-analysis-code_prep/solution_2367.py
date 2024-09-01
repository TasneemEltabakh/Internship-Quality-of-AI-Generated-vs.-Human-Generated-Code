# import library
import numpy as np

# create 1d-array
x = np.arange(5)

print("Original array:",
x)

# apply true division
# on each array element
rslt = np.true_divide(x, 4)

print("After the element-wise division:",
rslt)