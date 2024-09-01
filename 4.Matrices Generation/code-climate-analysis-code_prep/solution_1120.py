import numpy as np
x = np.array([-4, -3, -2, -1, 0, 1, 2, 3, 4])
print("Original array: ")
print(x)
r1 = np.signbit(x)
r2 = x < 0
assert np.array_equiv(r1, r2)
print(r1)
