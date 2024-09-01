import numpy as np
arra_data = np.arange(0,16).reshape((4, 4))
print("Original array:")
print(arra_data)
print("\nExtracted data: First and second elements of the first and second rows ")
print(arra_data[0:2, 0:2])
