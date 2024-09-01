# Python program explaining
# loadtxt() function
import numpy as geek

# StringIO behaves like a file object
from io import StringIO

c = StringIO("0 1 2 \n3 4 5")
d = geek.loadtxt(c)

print(d)