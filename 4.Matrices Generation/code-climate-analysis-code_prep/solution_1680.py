def unique_list(l):
    temp = []
    for x in l:
        if x not in temp:
            temp.append(x)
    return temp

text_str = ["Python", "Exercises", "Practice", "Solution", "Exercises"]
print("Original String:")
print(text_str)
print("\nAfter removing duplicate words from the said list of strings:")
print(unique_list(text_str))
