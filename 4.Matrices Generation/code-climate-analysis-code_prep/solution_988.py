def test(lst):
    result =[]
    for i in lst:
        j = i.replace(' ','')
        result.append(j)
    return result

text = ['abc ', '  ', ' ', 'sdfds ', ' ', '     ', 'sdfds ', 'huy']
print("\nOriginal list:")
print(text)
print("Remove additional spaces from the said list:")
print(test(text))
