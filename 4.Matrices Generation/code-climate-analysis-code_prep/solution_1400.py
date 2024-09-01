import numpy as np
x = np.zeros((3, 4))
y = np.expand_dims(x, axis=1).shape
print(y)
