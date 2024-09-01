# Python program showing a use
# lambda function


# performing a addition of three number
x1 = (lambda x, y, z: (x + y) * z)(1, 2, 3)
print(x1)


# function using a lambda function
x2 = (lambda x, y, z: (x + y) if (z == 0) else (x * y))(1, 2, 3)
print(x2)