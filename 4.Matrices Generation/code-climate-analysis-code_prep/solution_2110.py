# importing numpy as library
import numpy as np


# creating 1 D array with odd no of
# elements
x_odd = np.array([1, 2, 3, 4, 5, 6, 7])
print("\nPrinting the Original array:")
print(x_odd)

# calculating median
med_odd = np.median(x_odd)
print("\nMedian of the array that contains \
odd no of elements:")
print(med_odd)