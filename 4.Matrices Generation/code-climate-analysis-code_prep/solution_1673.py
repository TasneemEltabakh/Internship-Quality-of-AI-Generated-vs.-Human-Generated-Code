import numpy as np
x = np.eye(3)
print("3-D array:")
print(x)
f = np.ravel(x, order='F')
print("One dimension array:")
print(f)
