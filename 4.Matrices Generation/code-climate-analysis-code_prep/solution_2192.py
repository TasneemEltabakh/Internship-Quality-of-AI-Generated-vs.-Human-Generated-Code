# import numpy
import numpy as np

# using numpy.fill_diagonal() method
array = np.array([[1, 2], [2, 1]])
np.fill_diagonal(array, 5)

print(array)