# define two methods


# second method that will be returned
# by first method
def B():
print("Inside the method B.")

# first method that return second method
def A():
print("Inside the method A.")

# return second method
return B


# form a object of first method
# i.e; second method
returned_function = A()


# call second method by first method
returned_function()