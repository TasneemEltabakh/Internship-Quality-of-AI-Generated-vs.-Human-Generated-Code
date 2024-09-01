# Python program explaining
# numpy.core.defchararray.join() method

# importing numpy
import numpy as geek

# input array
in_arr = geek.array(['Python', 'Numpy', 'Pandas'])
print ("Input original array : ", in_arr)

# creating the separator
sep = geek.array(['-', '+', '*'])


out_arr = geek.core.defchararray.join(sep, in_arr)
print ("Output joined array: ", out_arr)