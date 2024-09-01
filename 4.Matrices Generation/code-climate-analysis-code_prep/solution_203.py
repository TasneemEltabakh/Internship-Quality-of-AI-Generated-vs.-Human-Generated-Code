from random import choice
def generate_random(start_range, end_range, nums):
    result = choice([i for i in range(start_range,end_range) if i not in nums])
    return result
   
start_range = 1
end_range = 10
nums = [2, 9, 10]
print("\nGenerate a number in a specified range (1, 10) except [2, 9, 10]")
print(generate_random(start_range,end_range,nums))

start_range = -5
end_range = 5
nums = [-5,0,4,3,2]

print("\nGenerate a number in a specified range (-5, 5) except [-5,0,4,3,2]")
print(generate_random(start_range,end_range,nums))
