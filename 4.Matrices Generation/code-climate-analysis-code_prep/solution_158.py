import arrow
a = arrow.utcnow()
print("Current datetime:")
print(a)
print("\ntime.struct_time, in the current timezone:")
print(arrow.utcnow().timetuple())
