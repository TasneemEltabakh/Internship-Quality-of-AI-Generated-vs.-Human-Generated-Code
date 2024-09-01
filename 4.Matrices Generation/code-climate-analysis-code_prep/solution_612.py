import numpy as np 

str1 = np.array([['Python-NumPy-Exercises'],
              ['-Python-']])
print("Original array of string values:") 
print(str1)
print("\nReplace '-' with '=' character in the said array of string values:")
print(np.char.strip(np.char.replace(str1, '-', '==')))
print("\nReplace '-' with ' ' character in the said array of string values:")
print(np.char.strip(np.char.replace(str1, '-', ' ')))
