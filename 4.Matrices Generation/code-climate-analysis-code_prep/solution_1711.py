# Python code to demonstrate
# converting set into dictionary
# using fromkeys()


# initializing set
ini_set = {1, 2, 3, 4, 5}


# printing initialized set
print ("initial string", ini_set)
print (type(ini_set))


# Converting set to dictionary
res = dict.fromkeys(ini_set, 0)


# printing final result and its type
print ("final list", res)
print (type(res))