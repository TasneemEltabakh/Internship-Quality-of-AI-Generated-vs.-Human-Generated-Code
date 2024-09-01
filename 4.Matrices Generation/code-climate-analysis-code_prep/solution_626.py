def initialize_list_with_values(n, val = 0):
  return [val for x in range(n)] 
print(initialize_list_with_values(7))
print(initialize_list_with_values(8,3))
print(initialize_list_with_values(5,-2))
print(initialize_list_with_values(5, 3.2))
