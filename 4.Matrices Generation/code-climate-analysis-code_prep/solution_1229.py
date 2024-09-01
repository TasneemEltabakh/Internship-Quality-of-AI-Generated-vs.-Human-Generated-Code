def unicode_to_str(lst):
    result = [str(x) for x in lst]
    return result
students =  [u'S001', u'S002', u'S003', u'S004']
print("Original lists:")
print(students)
print(" Convert the said unicode list to a list contains strings:")
print(unicode_to_str(students))
