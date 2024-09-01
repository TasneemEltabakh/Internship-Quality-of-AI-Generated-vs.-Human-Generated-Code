import itertools as it
print("Iterate over characters of a string and display\nconsecutive keys and groups from the iterable:")
str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'
data_groupby = it.groupby(str1)
for key, group in data_groupby:
    print('Key:', key)
    print('Group:', list(group))    
print("\nIterate over elements of a list and display\nconsecutive keys and groups from the iterable:")
str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'    
str1 = [1,2,2,3,4,4,5,5,5,6,6,7,7,7,8]
data_groupby = it.groupby(str1)
for key, group in data_groupby:
    print('Key:', key)
    print('Group:', list(group))
