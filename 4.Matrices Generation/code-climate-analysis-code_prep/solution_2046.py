# Python program explaining
# numpy.polygrid3d() method

# importing numpy as np

import numpy as np
from numpy.polynomial.polynomial import polygrid3d

# Input polynomial series coefficients
c = np.array([[1, 3, 5], [2, 4, 6], [10, 11, 12]])

# using np.polygrid3d() method
ans = polygrid3d([7, 9], [8, 10], [5, 6], c)
print(ans)