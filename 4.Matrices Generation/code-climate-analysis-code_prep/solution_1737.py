import numpy as np


# create array
x = np.array([1,2,3,4,5,1,2,1,1,1])
print("Original array:")
print(x)

print("Most frequent value in the above array:")
print(np.bincount(x).argmax())