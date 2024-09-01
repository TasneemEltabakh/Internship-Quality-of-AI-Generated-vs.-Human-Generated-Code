# Function to Check whether a given string is Heterogram or not

def heterogram(input):

# separate out list of alphabets using list comprehension
# ord function returns ascii value of character
alphabets = [ ch for ch in input if ( ord(ch) >= ord('a') and ord(ch) <= ord('z') )]

# convert list of alphabets into set and
# compare lengths
if len(set(alphabets))==len(alphabets):
print ('Yes')
else:
print ('No')

# Driver program
if __name__ == "__main__":
input = 'the big dwarf only jumps'
heterogram(input)