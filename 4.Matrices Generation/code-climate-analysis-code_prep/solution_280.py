def bifurcate(colors, filter):
  return [
    [x for x, flag in zip(colors, filter) if flag],
    [x for x, flag in zip(colors, filter) if not flag]
  ]
print(bifurcate(['red', 'green', 'blue', 'pink'], [True, True, False, True]))
