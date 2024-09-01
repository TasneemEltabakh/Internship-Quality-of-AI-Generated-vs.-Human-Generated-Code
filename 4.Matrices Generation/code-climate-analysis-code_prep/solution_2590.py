
str=input("Enter the String:")
str2 = []
i = 0
while i < len(str):
  ch = str[i]
  if (ch>='a' and ch <= 'z') or (ch >= 'A' and ch<= 'Z') or (ch >= '0' and ch <= '9') or (ch == '\0'):
    str2.append(ch)
  i += 1
Final_String = ''.join(str2)
print("After removing special character letter string is:",Final_String)