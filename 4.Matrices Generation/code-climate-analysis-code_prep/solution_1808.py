# importing library
import numpy

# create numpy array
arr = numpy.array([[1, 2, 3, 4, 5],
[10, -3, 30, 4, 5],
[3, 2, 5, -4, 5],
[9, 7, 3, 6, 5]
])

# declare specified value
X = 6

# view array
print("Given Array:\n", arr)

# finding out the row numbers
output = numpy.where(numpy.any(arr > X,
axis = 1))

# view output
print("Result:\n", output)