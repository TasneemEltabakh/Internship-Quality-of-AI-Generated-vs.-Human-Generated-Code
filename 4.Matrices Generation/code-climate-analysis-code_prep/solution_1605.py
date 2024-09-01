import itertools as it 

def group_similar_items(seq):
    result =  [list(el) for _, el in it.groupby(seq, lambda x: x.split('_')[0])]
    return result 

colors = ['red_1', 'red_2', 'green_1', 'green_2', 'green_3', 'orange_1', 'orange_2']
print("Original list:")
print(colors)
print("\nGroup similar items of the said list:")
print(group_similar_items(colors))

colors = ['red_1', 'green-1', 'green_2', 'green_3', 'orange-1', 'orange_2']
print("\nOriginal list:")
print(colors)
print("\nGroup similar items of the said list:")
print(group_similar_items(colors))
