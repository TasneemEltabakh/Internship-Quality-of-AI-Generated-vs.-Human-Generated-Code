import numpy as np
arra_data = np.arange(0,16).reshape((4, 4))
print("Original array:")
print(arra_data)
print("\nExtracted data: First element of the second row and fourth element of fourth row  ")
print(arra_data[[1,3], [0,3]])
