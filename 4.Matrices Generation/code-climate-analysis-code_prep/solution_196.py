import numpy as np    
x = np.arange(24).reshape((6,4))
print("Original arrays:")
print(x)
new_array = np.transpose(x)
print("After reverse the dimensions:")
print(new_array)
