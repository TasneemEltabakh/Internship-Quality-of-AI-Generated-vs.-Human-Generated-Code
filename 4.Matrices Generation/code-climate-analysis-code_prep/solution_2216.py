# importing numpy library
import numpy as np

# create numpy 2d-array
m = np.array([[1, 2],
[2, 3]])

print("Printing the Original square array:\n",
m)

# finding eigenvalues and eigenvectors
w, v = np.linalg.eig(m)

# printing eigen values
print("Printing the Eigen values of the given square array:\n",
w)

# printing eigen vectors
print("Printing Right eigenvectors of the given square array:\n"
v)