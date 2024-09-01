import numpy as np
x = np.array(['python exercises', 'PHP', 'java', 'C++'], dtype=np.str)
print("Original Array:")
print(x)
r = np.char.join(" ", x)
print(r)
