import arrow
a = arrow.utcnow()
print("Current datetime:")
print(a)
print("\nProleptic Gregorian ordinal of the date:")
print(arrow.utcnow().toordinal())
