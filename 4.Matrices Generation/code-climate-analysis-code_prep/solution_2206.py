import numpy as np


# Original matrix
matrix1 = np.array([[1, 2, 3], [3, 4, 5]])
print(matrix1)

# Decomposition of the said matrix
q, r = np.linalg.qr(matrix1)
print('\nQ:\n', q)
print('\nR:\n', r)