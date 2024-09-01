import numpy as np


a = np.zeros(11)
print("Before any change ")
print(a)

a[1] = 2
print("Before after first change ")
print(a)

a.flags.writeable = False
print("After making array immutable on attempting second change ")
a[1] = 7