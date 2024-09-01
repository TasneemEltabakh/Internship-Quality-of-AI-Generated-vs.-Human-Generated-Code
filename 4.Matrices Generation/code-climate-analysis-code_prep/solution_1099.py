from math import ceil
def chunk_list(lst, size):
  return list(
    map(lambda x: lst[x * size:x * size + size],
      list(range(ceil(len(lst) / size)))))
print(chunk_list([1, 2, 3, 4, 5, 6, 7, 8], 3))
