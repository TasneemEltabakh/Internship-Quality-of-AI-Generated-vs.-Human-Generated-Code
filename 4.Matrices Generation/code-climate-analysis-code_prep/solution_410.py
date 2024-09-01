import numpy as np
arra_data = np.arange(0,16).reshape((4, 4))
print("Original array:")
print(arra_data)
print("\nExtracted data: First and third elements of the first and third rows ")
print(arra_data[::2, ::2])
