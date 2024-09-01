# importing Numpy package
import numpy as np

# creating a 3X3 Numpy matrix
n_array = np.array([[55, 25, 15],
[30, 44, 2],
[11, 45, 77]])

# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)

# calculating the Trace of a matrix
trace = np.trace(n_array)


print("\nTrace of given 3X3 matrix:")
print(trace)