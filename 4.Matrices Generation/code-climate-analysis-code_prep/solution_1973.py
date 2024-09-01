def print_diamond(size):

# print the first triangle
# (the upper half)
for i in range (size):

# print from first row till
# middle row
rownum = i + 1
num_alphabet = 2 * rownum - 1
space_in_between_alphabets = num_alphabet - 1

total_spots = (2 * size - 1) * 2 - 1
total_space = total_spots - num_alphabet

space_leading_trailing = total_space - space_in_between_alphabets
lead_space = int(space_leading_trailing / 2)
trail_space = int(space_leading_trailing / 2)

# print the leading spaces
for j in range(lead_space):
print('-', end ='')

# determine the middle character
mid_char = (1 + size - 1) - int(num_alphabet / 2)

# start with the last character
k = 1 + size - 1
is_alphabet_printed = False
mid_char_reached = False

# print the numbers alternated by '-'
for j in range(num_alphabet + space_in_between_alphabets):

if not is_alphabet_printed:
print(str(k), end ='')
is_alphabet_printed = True

if k == mid_char:
mid_char_reached = True

if mid_char_reached == True:
k += 1

else:
k -= 1

else:
print('-', end ='')
is_alphabet_printed = False

# print the trailing spaces
for j in range(trail_space):
print('-', end ='')

# go to the next line
print('')

# print the rows after middle row
# till last row (the second triangle
# which is inverted, i.e., the lower half)
for i in range(size + 1, 2 * size):

rownum = i
num_alphabet = 2 * (2 * size - rownum) - 1
space_in_between_alphabets = num_alphabet - 1

total_spots = (2 * size - 1) * 2 - 1
total_space = total_spots - num_alphabet

space_leading_trailing = total_space - space_in_between_alphabets
lead_space = int(space_leading_trailing / 2)
trail_space = int(space_leading_trailing / 2)

# print the leading spaces
for j in range(lead_space):
print('-', end ='')

mid_char = (1 + size - 1) - int(num_alphabet / 2)

# start with the last char
k = 1 + size - 1
is_alphabet_printed = False
mid_char_reached = False

# print the numbers alternated by '-'
for j in range(num_alphabet + space_in_between_alphabets):

if not is_alphabet_printed:
print(str(k), end ='')
is_alphabet_printed = True

if k == mid_char:
mid_char_reached = True

if mid_char_reached == True:
k += 1

else:
k -= 1

else:
print('-', end ='')
is_alphabet_printed = False

# print the trailing spaces
for j in range(trail_space):
print('-', end ='')

# go to the next line
print('')

# Driver Code
if __name__ == '__main__':

n = 5
print_diamond(n)