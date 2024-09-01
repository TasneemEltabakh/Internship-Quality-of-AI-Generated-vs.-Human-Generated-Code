# Python program to demonstrate
# opening a file


# Open function to open the file "myfile.txt"
# (same directory) in read mode and store
# it's reference in the variable file1

file1 = open("myfile.txt")

# Reading from file
print(file1.read())

file1.close()