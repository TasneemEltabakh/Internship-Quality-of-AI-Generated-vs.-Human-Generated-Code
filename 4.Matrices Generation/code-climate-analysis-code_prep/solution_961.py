import arrow
a = arrow.utcnow()
print("Current datetime:")
print(a)
print("\nTime object with the same hour, minute, second, microsecond and timezone info.:")
print(arrow.utcnow().timetz())
