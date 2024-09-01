import numpy as np
x = np.array([10,-10,10,-10,-10,10])
y = np.array([.85,.45,.9,.8,.12,.6])
print("Original arrays:")
print(x)
print(y)
result = np.sum((x == 10) & (y > .5))
print("\nNumber of instances of a value occurring in one array on the condition of another array:")
print(result)
