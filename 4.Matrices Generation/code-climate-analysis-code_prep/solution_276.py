import numpy as np
result  = np.triu([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], -1)
print("\nCopy of a matrix with the elements below the k-th diagonal zeroed:")
print(result)
