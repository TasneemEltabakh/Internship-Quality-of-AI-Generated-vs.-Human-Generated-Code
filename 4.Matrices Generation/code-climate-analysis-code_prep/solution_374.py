import numpy as np
arra=np.ones((1,8,8))
print("Original array:")
print(arra)
result = np.triu(arra, k=1)
print("\nResult:")
print(result)
