import glob
import os
with open('a.txt', 'w') as f:
   f.write('Python program to create a symbolic link and read it to decide the original file pointed by the link.')
print('\nInitial file/dir name:', os.listdir())
with open('a.txt', 'r') as f:
   print('\nContents of a.txt:', repr(f.read()))   
os.rename('a.txt', 'b.txt')
print('\nAfter renaming initial file/dir name:', os.listdir())
with open('b.txt', 'r') as f:
   print('\nContents of b.txt:', repr(f.read()))
