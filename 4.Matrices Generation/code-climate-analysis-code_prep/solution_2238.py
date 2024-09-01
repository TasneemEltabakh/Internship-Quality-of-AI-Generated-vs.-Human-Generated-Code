# importing the module
import numpy as np

# created array of strings
arr = np.array(['Akash', 'Rohit', 'Ayush',
'Dhruv', 'Radhika'], dtype = np.str)
print("Original Array :")
print(arr)

# with the help of np.char.multiply()
# repeating the characters 3 times
new_array = np.char.multiply(arr, 3)
print("\nNew array :")
print(new_array)