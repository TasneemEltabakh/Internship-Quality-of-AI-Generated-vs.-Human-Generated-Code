from collections import Counter
language = ['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python','PHP', 'Python']
print("Original list:")
print(language)
cnt = Counter(language)
print("\nMost common element of the said list:")
print(cnt.most_common(1)[0][0])
