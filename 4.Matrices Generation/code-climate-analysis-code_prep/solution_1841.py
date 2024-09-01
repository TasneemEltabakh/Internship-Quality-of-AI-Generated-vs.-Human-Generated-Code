# Python program to
# demonstrate queue implementation
# using collections.dequeue

from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')

# display the queue
print("Initial queue")
print(q,"\n")

# display the type
print(type(q))