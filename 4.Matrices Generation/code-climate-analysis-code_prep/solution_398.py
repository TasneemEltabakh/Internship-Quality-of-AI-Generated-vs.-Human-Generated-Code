import numpy as np
x = np.ones((2,3,4,5))
print(np.rollaxis(x, 3, 1).shape)
