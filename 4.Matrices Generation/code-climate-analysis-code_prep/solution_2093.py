# Python Program illustrating
# numpy.inner() method
import numpy as np

# Vectors
a = np.array([2, 6])
b = np.array([3, 10])
print("Vectors :")
print("a = ", a)
print("\nb = ", b)

# Inner Product of Vectors
print("\nInner product of vectors a and b =")
print(np.inner(a, b))

print("---------------------------------------")

# Matrices
x = np.array([[2, 3, 4], [3, 2, 9]])
y = np.array([[1, 5, 0], [5, 10, 3]])
print("\nMatrices :")
print("x =", x)
print("\ny =", y)

# Inner product of matrices
print("\nInner product of matrices x and y =")
print(np.inner(x, y))