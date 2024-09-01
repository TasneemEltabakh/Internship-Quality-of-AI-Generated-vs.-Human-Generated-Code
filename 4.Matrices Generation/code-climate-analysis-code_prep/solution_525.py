def test(str1):
    result = [int(str1) for str1 in str1.split() if str1.isdigit()]
    return result
str1 = "red 12 black 45 green" 
print("Original string:", str1) 
print("Extract numbers from the said string:")
print(test(str1))
