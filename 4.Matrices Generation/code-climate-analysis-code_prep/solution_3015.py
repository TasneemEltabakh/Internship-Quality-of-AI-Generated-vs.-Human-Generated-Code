
str=input("Enter the String:")
for i in range(len(str)):
  if str[i] == 'a' or str[i] == 'A' or str[i] == 'e' or str[i] == 'E' or str[i] == 'i'or str[i] == 'I' or str[i] == 'o' or str[i] == 'O' or str[i] == 'u' or str[i] == 'U':
    print(str[i],end=" ")