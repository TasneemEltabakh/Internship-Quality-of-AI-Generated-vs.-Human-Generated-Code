# Python program explaining
# numpy.moveaxis() function

# importing numpy as geek
import numpy as geek

arr = geek.zeros((1, 2, 3, 4))

gfg = geek.moveaxis(arr, 0, -1).shape

print (gfg)