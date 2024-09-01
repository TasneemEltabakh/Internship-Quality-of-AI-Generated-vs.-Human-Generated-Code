import numpy as np
x = np.array([[1,2,3], [4,5,np.nan], [7,8,9], [True, False, True]])
print("Original array:")
print(x)
print("Remove all non-numeric elements of the said array")
print(x[~np.isnan(x).any(axis=1)])
