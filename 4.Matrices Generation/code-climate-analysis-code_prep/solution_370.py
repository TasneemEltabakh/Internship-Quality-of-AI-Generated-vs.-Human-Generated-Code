import numpy as np
x = np.random.uniform(1, 12, 5)
v = 4
n = x.flat[np.abs(x - v).argmin()]
print(n)
