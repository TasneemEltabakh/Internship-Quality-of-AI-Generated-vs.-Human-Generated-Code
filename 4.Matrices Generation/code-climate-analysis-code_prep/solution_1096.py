import arrow
a = arrow.utcnow()
print("Current datetime:")
print(a)
print("\nString representing the date, controlled by an explicit format string:")
print(arrow.utcnow().strftime('%d-%m-%Y %H:%M:%S'))
print(arrow.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
print(arrow.utcnow().strftime('%Y-%d-%m %H:%M:%S'))
