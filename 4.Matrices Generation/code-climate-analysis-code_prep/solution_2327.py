# Python program to demonstrate
# that keywords cant be used as
# identifiers


def calculate_sum(a, b):
return a + b


x = 2
y = 5
print(calculate_sum(x,y))


# def and if is a keyword, so
# this would give invalid
# syntax error
def = 12
if = 2


print(calculate_sum(def, if))