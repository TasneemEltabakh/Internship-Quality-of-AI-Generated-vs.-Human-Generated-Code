import numpy as np
from sys import getsizeof
x = [0] * 1024
y = np.array(x)
print(getsizeof(x))
