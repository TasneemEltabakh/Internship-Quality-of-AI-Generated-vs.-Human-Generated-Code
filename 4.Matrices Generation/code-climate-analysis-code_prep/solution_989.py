import numpy as np
x = np.arange(12).reshape((2, 6))
print("\nOriginal array:")
print(x)
r1 = np.percentile(x, 80, 1)
print("\n80th percentile for all elements of the said array along the second axis:")
print(r1)
