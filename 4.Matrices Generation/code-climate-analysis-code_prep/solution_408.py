import numpy as np
x = np.array([1., 2., 3., 4.], np.float32)
print("Original array: ")
print(x)
print("\n2^p for all the elements of the said array:")
r1 = np.exp2(x)
r2 = 2 ** x
assert np.allclose(r1, r2)
print(r1)
