# importing the library
import os

# giving directory name
dirname = 'D:\\AllData'

# giving file extension
ext = ('.exe', 'jpg')

# iterating over all files
for files in os.listdir(dirname):
if files.endswith(ext):
print(files) # printing file name of desired extension
else:
continue