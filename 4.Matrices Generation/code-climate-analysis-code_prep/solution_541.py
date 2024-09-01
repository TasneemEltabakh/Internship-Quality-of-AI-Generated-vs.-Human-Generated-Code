import arrow
a = arrow.utcnow()
print("Current datetime:")
print(a)
cloned = a.clone()
print("\nCloned datetime:")
print(cloned)
