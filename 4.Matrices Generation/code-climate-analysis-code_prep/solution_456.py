import numpy as np
arra_data = np.arange(0,16).reshape((4, 4))
print("Original array:")
print(arra_data)
print("\nExtracted data: All the elements of the first and fourth columns ")
print(arra_data[:, [0,3]])
