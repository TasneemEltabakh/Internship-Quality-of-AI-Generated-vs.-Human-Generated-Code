# Python code explaining
# numpy.poly1d()

# importing libraries
import numpy as np

# Constructing polynomial
p1 = np.poly1d([1, 2])
p2 = np.poly1d([4, 9, 5, 4])

print ("P1 : ", p1)
print ("\n p2 : \n", p2)

# Solve for x = 2
print ("\n\np1 at x = 2 : ", p1(2))
print ("p2 at x = 2 : ", p2(2))

# Finding Roots
print ("\n\nRoots of P1 : ", p1.r)
print ("Roots of P2 : ", p2.r)

# Finding Coefficients
print ("\n\nCoefficients of P1 : ", p1.c)
print ("Coefficients of P2 : ", p2.coeffs)

# Finding Order
print ("\n\nOrder / Degree of P1 : ", p1.o)
print ("Order / Degree of P2 : ", p2.order)