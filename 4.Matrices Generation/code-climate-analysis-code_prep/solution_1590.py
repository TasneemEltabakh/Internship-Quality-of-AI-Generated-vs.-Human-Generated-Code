import arrow
a = arrow.utcnow()
print("Current datetime:")
print(a)
print("\n3-tuple - ISO year, ISO week number, ISO weekday:")
print(arrow.utcnow().isocalendar())
print("\nISO 8601 formatted representation of the date and time:")
print(arrow.utcnow().isoformat())
