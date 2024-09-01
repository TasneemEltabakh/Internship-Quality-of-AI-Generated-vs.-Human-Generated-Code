import arrow
print(arrow.utcnow())
print("Hour ceiling:")
print(arrow.utcnow().ceil('hour'))
print("\nMinute ceiling:")
print(arrow.utcnow().ceil('minute'))
print("\nSecond ceiling:")
print(arrow.utcnow().ceil('second')) 
