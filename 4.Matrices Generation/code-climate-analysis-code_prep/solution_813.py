def test(lst, char):
    result = [i for i in lst if i.startswith(char)]
    return result
text = ["abcd", "abc", "bcd", "bkie", "cder", "cdsw", "sdfsd", "dagfa", "acjd"]
print("\nOriginal list:")
print(text)
char = "a"
print("\nItems start with",char,"from the said list:")
print(test(text, char))
char = "d"
print("\nItems start with",char,"from the said list:")
print(test(text, char))
char = "w"
print("\nItems start with",char,"from the said list:")
print(test(text, char))
