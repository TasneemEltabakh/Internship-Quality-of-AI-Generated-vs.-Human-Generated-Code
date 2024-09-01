import numpy as np
iterable = (x for x in range(10))
print(np.fromiter(iterable, np.int))
