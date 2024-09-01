# Python code to count unique
# tuples in list of list

import collections
Output = collections.defaultdict(int)

# List initialization
Input = [[('hi', 'bye')], [('Geeks', 'forGeeks')],
[('a', 'b')], [('hi', 'bye')], [('a', 'b')]]

# Using iteration
for elem in Input:
Output[elem[0]] += 1

# Printing output
print(Output)