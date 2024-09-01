# Python program explaining
# numpy.diff() method



# importing numpy
import numpy as geek


# input array
arr = geek.array([1, 3, 4, 7, 9])

print("Input array : ", arr)
print("First order difference : ", geek.diff(arr))
print("Second order difference : ", geek.diff(arr, n = 2))
print("Third order difference : ", geek.diff(arr, n = 3))