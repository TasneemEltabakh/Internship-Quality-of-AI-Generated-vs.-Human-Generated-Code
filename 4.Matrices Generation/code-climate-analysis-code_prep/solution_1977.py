# Python program to replace text in a file
s = input("Enter text to replace the existing contents:")
f = open("file.txt", "r+")


# file.txt is an example here,
# it should be replaced with the file name
# r+ mode opens the file in read and write mode
f.truncate(0)
f.write(s)
f.close()
print("Text successfully replaced")