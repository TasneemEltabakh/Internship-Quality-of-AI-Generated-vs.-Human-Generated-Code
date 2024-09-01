# import numpy
import numpy as np

# using numpy.isin() method
gfg1 = np.array([1, 2, 3, 4, 5])
lis = [1, 3, 5]
gfg = np.isin(gfg1, lis)

print(gfg)