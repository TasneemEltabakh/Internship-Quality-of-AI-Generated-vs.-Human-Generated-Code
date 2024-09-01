import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])
y = np.reshape(x,(3,2))
print("Reshape 3x2:")
print(y)
z = np.reshape(x,(2,3))
print("Reshape 2x3:")
print(z)
