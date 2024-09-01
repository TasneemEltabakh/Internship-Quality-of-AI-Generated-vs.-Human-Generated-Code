# importing package
import numpy

# define the polynomials
# p(x) = 5(x**2) + (-2)x +5
px = (5,-2,5)

# q(x) = 2(x**2) + (-5)x +2
qx = (2,-5,2)

# subtract the polynomials
rx = numpy.polynomial.polynomial.polysub(px,qx)

# print the resultant polynomial
print(rx)