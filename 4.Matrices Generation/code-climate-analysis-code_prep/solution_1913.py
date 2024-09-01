# importing package
import numpy

# define the polynomials
# p(x) = 5(x**2) + (-2)x +5
px = (5, -2, 5)

# g(x) = x +2
gx = (2, 1, 0)

# divide the polynomials
qx, rx = numpy.polynomial.polynomial.polydiv(px, gx)

# print the result
# quotiient
print(qx)

# remainder
print(rx)