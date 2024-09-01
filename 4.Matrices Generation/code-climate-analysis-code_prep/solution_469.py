import numpy as np
a = np.array([[10],[20],[30]])
b = np.array([[40],[50],[60]])
c = np.dstack((a, b))
print(c)
