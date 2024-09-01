import numpy as np    
x = np.reshape(np.arange(16),(4,4))
print("Original arrays:")
print(x)
print("Sliced elements:")
result = x[[0,1,2],[0,1,3]]
print(result)
