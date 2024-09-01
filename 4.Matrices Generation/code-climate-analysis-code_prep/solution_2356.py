# opening both the files in reading modes
with open("file1.txt") as f1, open("file2.txt") as f2:

# reading f1 contents
line1 = f1.readline()

# reading f2 contents
line2 = f2.readline()

# printing contents of f1 followed by f2
print(line1, line2)