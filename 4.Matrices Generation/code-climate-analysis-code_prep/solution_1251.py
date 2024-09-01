import textwrap
s = input("Input a string: ")
w = int(input("Input the width of the paragraph: ").strip())
print("Result:")
print(textwrap.fill(s,w))
