def remove_duplicate_dictionary(list_color):
    result = [dict(e) for e in {tuple(d.items()) for d in list_color}]
    return result

list_color = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
print ("Original list with duplicate dictionary:")
print(list_color)
print("\nAfter removing duplicate dictionary of the said list:")
print(remove_duplicate_dictionary(list_color))
