import numpy as np
x = np.array([0, 1, 3])
y = np.array([2, 4, 5])
print("\nOriginal array1:")
print(x)
print("\nOriginal array1:")
print(y)
print("\nPearson product-moment correlation coefficients of the said arrays:\n",np.corrcoef(x, y))
