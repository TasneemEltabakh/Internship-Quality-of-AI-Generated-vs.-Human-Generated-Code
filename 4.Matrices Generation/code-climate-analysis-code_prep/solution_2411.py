# import numpy
import numpy as np

# using np.char.endswith() method
a = np.array(['geeks', 'for', 'geeks'])
gfg = np.char.endswith(a, 'ks')

print(gfg)