import numpy as np
x = np.array([[ 0.42436315, 0.48558583, 0.32924763], [ 0.7439979,0.58220701,0.38213418], [ 0.5097581,0.34528799,0.1563123 ]])
print("Original array:")
print(x)
print("Replace all elements of the said array with .5 which are greater than .5")
x[x > .5] = .5
print(x)
