import os
path = r'g:\\testpath\\a.txt'
print("Original path:")
print(path)
print("\nDir and file name of the said path:")
print(os.path.split(path))
print("\nJoin one or more path components together:")
print(os.path.join(r'g:\\testpath\\','a.txt'))
