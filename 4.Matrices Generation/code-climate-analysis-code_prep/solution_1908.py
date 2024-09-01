# Open the file in write mode
f1 = open("output1.txt", "w")

# Open the input file and get
# the content into a variable data
with open("file.txt", "r") as myfile:
data = myfile.read()

# For Full Reversing we will store the
# value of data into new variable data_1
# in a reverse order using [start: end: step],
# where step when passed -1 will reverse
# the string
data_1 = data[::-1]

# Now we will write the fully reverse
# data in the output1 file using
# following command
f1.write(data_1)

f1.close()