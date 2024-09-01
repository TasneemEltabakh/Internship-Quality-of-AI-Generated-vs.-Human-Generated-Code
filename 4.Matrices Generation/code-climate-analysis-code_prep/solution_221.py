import numpy as np
a = np.array([1, 3, 7, 9, 10, 13, 14, 17, 29])
print("Original array:")
print(a)
result = np.where(np.logical_and(a>=7, a<=20))
print("\nElements within range: index position")
print(result)
