from collections import Counter, OrderedDict
class OrderedCounter(Counter,OrderedDict):
   pass
word_array = []
n = int(input("Input number of words: "))
print("Input the words: ")
for i in range(n):
   word_array.append(input().strip())
word_ctr = OrderedCounter(word_array)
print(len(word_ctr))
for word in word_ctr:
   print(word_ctr[word],end=' ')
