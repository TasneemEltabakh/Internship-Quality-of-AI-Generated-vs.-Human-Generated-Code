# Python program to demonstrate
# nested lambda functions


f = lambda a = 2, b = 3:lambda c: a+b+c

o = f()
print(o(4))