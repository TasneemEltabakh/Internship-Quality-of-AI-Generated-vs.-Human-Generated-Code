import numpy as np
x = np.arange(16).reshape((4, 4))
print("Original array:",x)
print("After splitting horizontally:")
print(np.hsplit(x, [2, 6]))
