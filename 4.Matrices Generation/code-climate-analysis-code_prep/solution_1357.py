def remove_characters(str1,c):
    return ''.join([el for el in str1 if el == c])
text = "Python Exercises"
print("Original string")
print(text)
except_char = "P"
print("Remove all characters except",except_char,"in the said string:")
print(remove_characters(text,except_char))
text = "google"
print("\nOriginal string")
print(text)
except_char = "g"
print("Remove all characters except",except_char,"in the said string:")
print(remove_characters(text,except_char))
text = "exercises"
print("\nOriginal string")
print(text)
except_char = "e"
print("Remove all characters except",except_char,"in the said string:")
print(remove_characters(text,except_char))
