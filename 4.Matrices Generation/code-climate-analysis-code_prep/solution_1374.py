import numpy as np
x = np.array([1, 3, 5, 7, 0])
print("Original array: ")
print(x)
print("Difference between neighboring elements, element-wise of the said array.")
print(np.diff(x))
