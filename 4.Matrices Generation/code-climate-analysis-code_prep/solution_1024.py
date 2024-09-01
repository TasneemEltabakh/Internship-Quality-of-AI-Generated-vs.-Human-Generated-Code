import numpy as np
complex_num = [1 + 2j, 3 - 1j, 3 - 2j, 4 - 3j, 3 + 5j]
print("Original array:")
print(complex_num)
print("\nSorted a given complex array using the real part first, then the imaginary part.")
print(np.sort_complex(complex_num))
