
str=input("Enter the String:")
ch=' '
for i in range(len(str)):
  if str[i] >= 'a' and str[i] <= 'z':
    ch = str[i]
    break
  else:
    continue
print("First small letter in a given String is: ", ch)