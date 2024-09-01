# Importing required modules
import numpy


# Creating arrays
array1 = numpy.array([[1, 2], [3, 4]])
print('Array1:\n', array1)


array2 = numpy.array([[5, 6], [7, 8]])
print('\nArray2:\n', array2)


# Computing the Kronecker Product
kroneckerProduct = numpy.kron(array1, array2)
print('\nArray1  Array2:')
print(kroneckerProduct)