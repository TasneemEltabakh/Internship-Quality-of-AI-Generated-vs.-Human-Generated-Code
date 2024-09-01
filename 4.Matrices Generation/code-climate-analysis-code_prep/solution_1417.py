def combinations_list(colors):
    if len(colors) == 0:
        return [[]]
    result = []
    for el in combinations_list(colors[1:]):
        result += [el, el+[colors[0]]]
    return result
colors = ['orange', 'red', 'green', 'blue']
print("Original list:")
print(colors)
print("\nAll possible combinations of the said lists elements:")
print(combinations_list(colors))
