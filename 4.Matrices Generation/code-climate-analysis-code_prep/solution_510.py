def test(dictt):
    result = sum((len(values) for values in dictt.values()))
    return result
color = {'#FF0000':'Red', '#800000':'Maroon', '#FFFF00':'Yellow', '#808000':'Olive'}
print("\nOriginal dictionary:")
print(color)
print("\nTotal length of all values of the said dictionary with string values:")
print(test(color))
