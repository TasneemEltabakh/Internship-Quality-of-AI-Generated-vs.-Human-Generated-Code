import numpy as np
a = np.array([[4, 12, -14], [12, 37, -53], [-14, -53, 98]], dtype=np.int32)
print("Original array:")
print(a)
q, r = np.linalg.qr(a)
print("qr factorization of the said array:")
print( "q=\n", q, "\nr=\n", r)
