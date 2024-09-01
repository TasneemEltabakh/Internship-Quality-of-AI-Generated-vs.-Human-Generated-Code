def test(list1):
    result =   [tuple(v for v in i if not isinstance(v, str)) for i in list1]
    return list(result)

marks = [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
print("\nOriginal list:")
print(marks)
print("\nRemove all strings from the said list of tuples:")
print(test(marks))
