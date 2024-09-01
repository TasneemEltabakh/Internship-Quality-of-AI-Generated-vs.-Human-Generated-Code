# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using numpy.random.laplace() method
gfg = np.random.laplace(1.45, 15, 1000)

count, bins, ignored = plt.hist(gfg, 30, density = True)
plt.show()