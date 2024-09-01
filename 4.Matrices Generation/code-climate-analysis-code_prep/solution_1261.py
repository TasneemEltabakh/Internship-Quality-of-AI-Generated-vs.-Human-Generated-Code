import numpy as np
x1 = np.array(['Python', 'PHP', 'JS', 'EXAMPLES', 'HTML'], dtype=np.str)
print("\nOriginal Array:")
print(x1)
print("count the lowest index of P:")
r = np.char.find(x1, "P")
print(r)
