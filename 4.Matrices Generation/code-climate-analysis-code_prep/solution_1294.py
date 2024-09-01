import arrow
utc = arrow.utcnow()
pacific=arrow.now('US/Pacific')
nyc=arrow.now('America/Chicago').tzinfo
print(pacific.astimezone(nyc))
