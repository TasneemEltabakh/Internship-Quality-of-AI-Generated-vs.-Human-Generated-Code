def reverse_strings_list(string_list):
    result = [x[::-1] for x in string_list]
    return result

colors_list = ["Red", "Green", "Blue", "White", "Black"]
print("\nOriginal lists:")
print(colors_list)
print("\nReverse strings of the said given list:")
print(reverse_strings_list(colors_list))
