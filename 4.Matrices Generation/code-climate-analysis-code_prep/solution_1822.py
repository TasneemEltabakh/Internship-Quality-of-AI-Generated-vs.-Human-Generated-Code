with open('example.txt', 'r', encoding='utf-8') as file:
data = file.readlines()

print(data)
data[1] = "Here is my modified Line 2\n"

with open('example.txt', 'w', encoding='utf-8') as file:
file.writelines(data)