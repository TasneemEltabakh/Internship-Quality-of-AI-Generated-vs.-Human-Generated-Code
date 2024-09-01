import arrow
a = arrow.utcnow()
print("Current datetime:")
print(a)
r = arrow.now('US/Mountain')
print("\nNaive datetime representation:")
print(r.naive)
