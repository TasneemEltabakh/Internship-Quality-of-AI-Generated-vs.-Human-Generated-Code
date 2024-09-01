import numpy as np
x = np.array(['python exercises', 'PHP', 'java', 'C++'], dtype=np.str)
print("Original Array:")
print(x)
encoded_char = np.char.encode(x, 'cp500')
decoded_char = np.char.decode(encoded_char,'cp500')
print("\nencoded =", encoded_char)
print("decoded =", decoded_char)
