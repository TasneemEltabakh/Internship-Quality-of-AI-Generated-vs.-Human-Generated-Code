import collections
# declare an empty deque object
dq_object = collections.deque()
# Add elements to the deque - left to right
dq_object.append(2)
dq_object.append(4)
dq_object.append(6)
dq_object.append(8)
dq_object.append(10)
print("Deque before rotation:")
print(dq_object)
# Rotate once in negative direction
dq_object.rotate(-1)
print("\nDeque after 1 negative rotation:")
print(dq_object)
# Rotate twice in negative direction
dq_object.rotate(-2)
print("\nDeque after 2 negative rotations:")
print(dq_object)
