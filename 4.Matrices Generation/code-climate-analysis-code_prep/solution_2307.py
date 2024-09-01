import numpy as np


# list
list1 = [3, 4, 5, 6]
print(type(list1))
print(list1)
print()

# conversion
array1 = np.asarray(list1)
print(type(array1))
print(array1)
print()

# tuple
tuple1 = ([8, 4, 6], [1, 2, 3])
print(type(tuple1))
print(tuple1)
print()

# conversion
array2 = np.asarray(tuple1)
print(type(array2))
print(array2)