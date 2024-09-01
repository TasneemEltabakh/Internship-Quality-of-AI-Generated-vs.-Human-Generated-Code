# importing popen from the os library
from os import popen


# Path to the file whose id we would
# be obtaining (relative / absolute)
file = r"C:\Users\Grandmaster\Desktop\testing.py"


# Running the command for obtaining the fileid,
# and saving the output of the command
output = popen(fr"fsutil file queryfileid {file}").read()


# printing the output of the previous command
print(output)