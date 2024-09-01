# Python program explaining
# numpy.polygrid2d() method

# importing numpy as np

import numpy as np
from numpy.polynomial.polynomial import polygrid2d

# Input polynomial series coefficients
c = np.array([[1, 3, 5], [2, 4, 6]])

# using np.polygrid2d() method
ans = polygrid2d([7, 9], [8, 10], c)
print(ans)