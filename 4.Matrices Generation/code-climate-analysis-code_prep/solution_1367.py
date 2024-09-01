import arrow
print("Current datetime:")
print(arrow.utcnow())
print("\nYYYY-MM-DD HH:mm:ss ZZ:")
print(arrow.utcnow().format('YYYY-MM-DD HH:mm:ss ZZ'))
print("\nDD-MM-YYYY HH:mm:ss ZZ:")
print(arrow.utcnow().format('DD-MM-YYYY HH:mm:ss ZZ'))
print(arrow.utcnow().format('\nMMMM DD, YYYY'))
print(arrow.utcnow().format())
