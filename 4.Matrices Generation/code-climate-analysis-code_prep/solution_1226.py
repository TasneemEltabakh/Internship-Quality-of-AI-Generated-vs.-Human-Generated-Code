import numpy as np
x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
index = [0, 3, 4]
print("Original array:")
print(x)
print("Delete first, fourth and fifth elements:")
new_x = np.delete(x, index)
print(new_x)
