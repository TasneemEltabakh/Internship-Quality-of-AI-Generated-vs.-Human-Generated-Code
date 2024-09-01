import arrow
print("Current datetime:")
print(arrow.utcnow())
earlier = arrow.utcnow().shift(hours=-4)
print(earlier.humanize())
later = earlier.shift(hours=3)
print(later.humanize(earlier))
