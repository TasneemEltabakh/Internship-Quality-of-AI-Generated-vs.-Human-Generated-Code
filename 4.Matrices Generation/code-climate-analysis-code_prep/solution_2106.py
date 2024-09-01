# Program to save a NumPy array to a text file


# Importing required libraries
import numpy


# Creating an array
List = [1, 2, 3, 4, 5]
Array = numpy.array(List)


# Displaying the array
print('Array:\n', Array)
file = open("file1.txt", "w+")


# Saving the array in a text file
content = str(Array)
file.write(content)
file.close()


# Displaying the contents of the text file
file = open("file1.txt", "r")
content = file.read()


print("\nContent in file1.txt:\n", content)
file.close()