import arrow
print("Daylight savings time adjustment:")
a = arrow.utcnow().dst()
print(a)
