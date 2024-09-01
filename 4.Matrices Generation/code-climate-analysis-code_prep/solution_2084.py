# creating a variable and storing the text
# that we want to search
search_text = "dummy"

# creating a variable and storing the text
# that we want to add
replace_text = "replaced"

# Opening our text file in read only
# mode using the open() function
with open(r'SampleFile.txt', 'r') as file:

# Reading the content of the file
# using the read() function and storing
# them in a new variable
data = file.read()

# Searching and replacing the text
# using the replace() function
data = data.replace(search_text, replace_text)

# Opening our text file in write only
# mode to write the replaced content
with open(r'SampleFile.txt', 'w') as file:

# Writing the replaced data in our
# text file
file.write(data)

# Printing Text replaced
print("Text replaced")