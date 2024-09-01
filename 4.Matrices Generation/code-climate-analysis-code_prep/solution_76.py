import numpy as np
x = np.array([-180.,  -90.,   90.,  180.])
r1 = np.radians(x)
r2 = np.deg2rad(x)
assert np.array_equiv(r1, r2)
print(r1)
