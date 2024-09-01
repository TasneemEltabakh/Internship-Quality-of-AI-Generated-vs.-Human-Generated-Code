import arrow
a = arrow.utcnow()
print("Current Datetime:")
print(a)
print("\nFloating-point representation of the said Arrow object:")
f = arrow.utcnow().float_timestamp
print(f) 
