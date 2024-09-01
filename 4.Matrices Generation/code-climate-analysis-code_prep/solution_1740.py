# Python program to move
# files and directories


import shutil

# Source path
source = "D:\Pycharm projects\gfg\Test\B"

# Destination path
destination = "D:\Pycharm projects\gfg\Test\A"

# Move the content of
# source to destination
dest = shutil.move(source, destination)

# print(dest) prints the
# Destination of moved directory