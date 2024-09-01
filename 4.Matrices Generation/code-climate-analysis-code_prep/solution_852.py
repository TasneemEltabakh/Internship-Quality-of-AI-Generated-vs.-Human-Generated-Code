import arrow
a = arrow.utcnow()
print("Datetime representation:")
print(a.datetime)
b = a.timestamp
print("\nTimestamp representation:")
print(b)
