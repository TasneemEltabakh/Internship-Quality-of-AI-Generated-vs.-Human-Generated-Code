def merge_lists(*args, fill_value = None):
  max_length = max([len(lst) for lst in args])
  result = []
  for i in range(max_length):
    result.append([
      args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
    ])
  return result
print("After merging lists into a list of lists:")
print(merge_lists(['a', 'b'], [1, 2], [True, False]))  
print(merge_lists(['a'], [1, 2], [True, False]))  
print(merge_lists(['a'], [1, 2], [True, False], fill_value = '_'))
