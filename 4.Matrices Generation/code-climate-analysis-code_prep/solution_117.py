import numpy as np
x = np.array([[10, 30], [20, 60]])
print("Original array:")
print(x)
print("Mean of each column:")
print(x.mean(axis=0))
print("Mean of each row:")
print(x.mean(axis=1))
