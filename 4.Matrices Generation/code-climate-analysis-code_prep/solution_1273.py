import numpy as np
from numpy import linalg as LA
a = np.array([[1, 0, -1], [0, 1, 0], [1, 0, 1]])
print("Original matrix:")
print(a)
print("The condition number of the said matrix:")
print(LA.cond(a))
