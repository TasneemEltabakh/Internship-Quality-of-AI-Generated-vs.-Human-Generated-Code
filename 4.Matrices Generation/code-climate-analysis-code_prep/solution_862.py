color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]

print(all(c == 'blue' for c in color1))
print(all(c == 'green' for c in color2))
