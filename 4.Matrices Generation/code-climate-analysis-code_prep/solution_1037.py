import numpy as np
x = np.array([1e-99, 1e-100])
print("Original array: ")
print(x)
print("\nNatural logarithm of one plus each element:")
print(np.log1p(x))
