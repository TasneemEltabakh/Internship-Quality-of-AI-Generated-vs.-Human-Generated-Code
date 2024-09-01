import numpy as np
x = np.arange(1, 15)
print("Original array:",x)
print("After splitting:")
print(np.split(x, [2, 6]))
