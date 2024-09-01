import numpy as np
x = np.arange(12).reshape(3, 4)
for x in np.nditer(x):
    print(x,end=' ')
print()
