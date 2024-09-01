import numpy as np
m = np.array([[1,2],[3,4]])
print("Original matrix:")
print(m)
result =  np.linalg.qr(m)
print("Decomposition of the said matrix:")
print(result)
