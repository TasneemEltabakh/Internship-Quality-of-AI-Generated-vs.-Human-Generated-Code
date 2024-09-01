# Python program explaining
# numpy.squeeze function

import numpy as geek

in_arr = geek.array([[[2, 2, 2], [2, 2, 2]]])

print ("Input array : ", in_arr)
print("Shape of input array : ", in_arr.shape)

out_arr = geek.squeeze(in_arr)

print ("output squeezed array : ", out_arr)
print("Shape of output array : ", out_arr.shape)