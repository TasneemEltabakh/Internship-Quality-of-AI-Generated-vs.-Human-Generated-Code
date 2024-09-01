import numpy as np
x=np.array([1.6e-10, 1.6, 1200, .235]) 
print("Original array elements:")
print(x)
print("Print array values with precision 3:")
np.set_printoptions(suppress=True)
print(x)
