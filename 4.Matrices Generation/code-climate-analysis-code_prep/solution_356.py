import numpy as np
arra_data = np.arange(0,36).reshape((6, 6))
print("Original array:")
print(arra_data)
print("\nExtracted data: First, third and fifth elements of the third and fifth rows")
print(arra_data[2::2, ::2]) 
