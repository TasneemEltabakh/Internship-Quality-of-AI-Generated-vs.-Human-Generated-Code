import numpy as np
x = np.arange(12).reshape(3, 4)
print("Elements of the array in Fortan array:")
for x in np.nditer(x, order="F"):
    print(x,end=' ')
print("\n")
