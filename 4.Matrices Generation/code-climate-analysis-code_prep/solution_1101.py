import arrow
a = arrow.utcnow()
print("Current datetime:")
print(a)
print("\nTime object with the same hour, minute, second, microsecond:")
print(arrow.utcnow().time())
print("\nTimestamp representation of the Arrow object, in UTC time:")
print(arrow.utcnow().timestamp)
