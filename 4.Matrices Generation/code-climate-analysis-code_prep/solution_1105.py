from itertools import groupby
def encode_str(input_str):
    return [(len(list(n)), m) for m,n in groupby(input_str)]
 
str1 = "AAASSSSKKIOOOORRRREEETTTTAAAABBBBBBDDDDD" 
print("Original string:")
print(str1)
print("Result:")
print(encode_str(str1))

str1 = "jjjjiiiiooooosssnssiiiiwwwweeeaaaabbbddddkkkklll" 
print("\nOriginal string:")
print(str1)
print("Result:")
print(encode_str(str1))
