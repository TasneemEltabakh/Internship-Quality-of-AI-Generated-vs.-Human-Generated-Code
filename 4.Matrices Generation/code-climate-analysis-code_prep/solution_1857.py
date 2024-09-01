import numpy as n

# create array
y = n.array([0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
print("Original array:", end=" ")
print(y)

# rount to nearest integer
y = n.rint(y)
print("After rounding off:", end=" ")
print(y)