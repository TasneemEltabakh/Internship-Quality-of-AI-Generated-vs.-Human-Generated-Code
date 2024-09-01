def group_similar_items(seq,el):
    seq.append(seq.pop(seq.index(el)))
    return seq 

colors = ['red','green','white','black','orange']
print("Original list:")
print(colors)
el = "white"
print("Move",el,"at the end of the said list:")
print(group_similar_items(colors, el))

colors = ['red','green','white','black','orange']
print("\nOriginal list:")
print(colors)
el = "red"
print("Move",el,"at the end of the said list:")
print(group_similar_items(colors, el))

colors = ['red','green','white','black','orange']
print("\nOriginal list:")
print(colors)
el = "black"
print("Move",el,"at the end of the said list:")
print(group_similar_items(colors, el))
