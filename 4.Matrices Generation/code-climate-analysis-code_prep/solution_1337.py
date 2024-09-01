import numpy as np    
a = np.array([[1,2,3],[4,3,1]])
print("Original array:")
print(a)
i,j = np.unravel_index(a.argmax(), a.shape)
print("Index of a maximum element in a numpy array along one axis:")
print(a[i,j])
