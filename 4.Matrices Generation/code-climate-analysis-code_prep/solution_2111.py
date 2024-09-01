# importing Numpy package
import numpy as np

# creating a Numpy array
n_array = np.array([[2, 3, 0],
[4, 1, 6]])

print("Given array:")
print(n_array)

# Checking whether specific values
# are present in "n_array" or not
print(2 in n_array)
print(0 in n_array)
print(6 in n_array)
print(50 in n_array)
print(10 in n_array)