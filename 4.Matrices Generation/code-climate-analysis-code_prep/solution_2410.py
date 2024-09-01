# Python code to find mean of every numpy array in list

# Importing module
import numpy as np

# List Initialization
Input = [np.array([1, 2, 3]),
np.array([4, 5, 6]),
np.array([7, 8, 9])]

# Output list initialization
Output = []

# using np.mean()
for i in range(len(Input)):
Output.append(np.mean(Input[i]))

# Printing output
print(Output)