import arrow
print(arrow.utcnow())
print("Hour ceiling:")
print(arrow.utcnow().floor('hour'))
print("\nMinute ceiling:")
print(arrow.utcnow().floor('minute'))
print("\nSecond ceiling:")
print(arrow.utcnow().floor('second'))
