
str=input("Enter the String:")
count = 0
for i in range(len(str)):
  if str[i] == ' ':
    count+=1
print("Number of white space in a string are ",count)