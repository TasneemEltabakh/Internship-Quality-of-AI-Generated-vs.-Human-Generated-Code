import numpy as np
x1 = np.array(['Python', 'PHP', 'JS', 'examples', 'html'], dtype=np.str)
print("\nOriginal Array:")
print(x1)
print("Test if each element of the said array starts with 'P':")
r = np.char.startswith(x1, "P")
print(r)
