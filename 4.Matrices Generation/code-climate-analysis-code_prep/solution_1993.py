from inspect import signature


# declare a function gfg with some
# parameter
def gfg(x:str, y:int):
pass

# with the help of signature function
# store signature of the function in
# variable t
t = signature(gfg)

# print the signature of the function
print(t)

# print the annonation of the parameter
# of the function
print(t.parameters['x'])

# print the annonation of the parameter
# of the function
print(t.parameters['y'].annotation)