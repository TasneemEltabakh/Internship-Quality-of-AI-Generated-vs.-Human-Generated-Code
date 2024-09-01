import numpy as np
arra_data = np.arange(0,16).reshape((4, 4))
print("Original array:")
print(arra_data)
print("\nExtracted data: Second and fourth elements of the second and fourth rows ")
print(arra_data[1::2, 1::2])
