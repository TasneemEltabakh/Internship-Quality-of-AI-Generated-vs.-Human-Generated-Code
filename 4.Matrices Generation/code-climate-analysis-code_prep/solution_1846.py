# import library
import numpy as np

# create numpy 1d-array
arr = np.array([2, 0, 1, 5,
4, 1, 9])

print("Given array:", arr)

# sort an array in
# ascending order

# np.argsort() return
# array of indices for
# sorted array
sorted_index_array = np.argsort(arr)

# sorted array
sorted_array = arr[sorted_index_array]

print("Sorted array:", sorted_array)

# we want 1 largest value
n = 1

# we are using negative
# indexing concept

# take n largest value
rslt = sorted_array[-n : ]

# show the output
print("{} largest value:".format(n),
rslt[0])